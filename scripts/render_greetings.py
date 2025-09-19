#!/usr/bin/env python3
"""Render greetings agenda from pretalx schedule.xml into markdown.

Behavior:
- If `--schedule` is provided, use that path/URL.
- Else if `--dug-num` provided, compute pretalx URL:
  https://cfp.3mdeb.com/developers-vpub-0x{vpub_hex}-{year}/schedule/export/schedule.xml
  where vpub_hex = hex(dug_num + 5)[2:].
- Default time offset is +60 minutes to match existing repo pages.
- Default output is stdout; use `--output DIR` to write file into a directory.
- Will refuse to overwrite `pages/dug_<n>/1-greetings-agenda.md` unless `--force`.
"""
import argparse
import os
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import urllib.request

try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
except Exception:
    print(
        "Missing dependency: Jinja2. Install with: pip install Jinja2", file=sys.stderr
    )
    raise

EMOJI_MAP = {
    "greetings": "&#x1F44B;",
    "status": "&#x1F9ED;",
    "roadmap": "&#x1F9F0;",
    "talk": "&#x1F4BB;",
    "demo": "&#x1F9EA;",
    "closing": "&#x1F44F;",
}
SLIDES_RE = re.compile(r"\* \[slides\]\((https?://[^)]+)\)", re.IGNORECASE)


def schedule_url_for_dug(
    dug_num: int, year: int = None, base_url: str = "https://cfp.3mdeb.com"
) -> str:
    if year is None:
        year = datetime.now().year
    vpub_hex = format(dug_num + 5, "x")
    slug = f"developers-vpub-0x{vpub_hex}-{year}"
    return f"{base_url}/{slug}/schedule/export/schedule.xml"


def fetch_schedule(url: str) -> ET.Element:
    with urllib.request.urlopen(url) as r:
        data = r.read()
    return ET.fromstring(data)


def parse_schedule(path_or_url: str) -> ET.Element:
    if path_or_url.startswith(("http://", "https://")):
        return fetch_schedule(path_or_url)
    tree = ET.parse(path_or_url)
    return tree.getroot()


def normalize_time(
    start_raw: str, date_full: str = None, offset_minutes: int = 60
) -> str:
    dt = None
    if date_full:
        try:
            dt = datetime.fromisoformat(date_full)
        except Exception:
            dt = None
    if dt is None and start_raw:
        try:
            parts = start_raw.split(":")
            hour = int(parts[0])
            minute = int(parts[1]) if len(parts) > 1 else 0
            dt = datetime(2000, 1, 1, hour, minute)
        except Exception:
            return start_raw
    if dt is None:
        return start_raw
    if offset_minutes:
        dt = dt + timedelta(minutes=offset_minutes)
    try:
        return dt.strftime("%H:%M")
    except Exception:
        return start_raw


def pick_emoji(title_lower: str, evtype_lower: str) -> str:
    if "greet" in title_lower:
        return EMOJI_MAP["greetings"]
    if "closing" in title_lower or "closing" in evtype_lower:
        return EMOJI_MAP["closing"]
    if "roadmap" in title_lower or "roadmap" in evtype_lower:
        return EMOJI_MAP["roadmap"]
    if "status" in title_lower:
        return EMOJI_MAP["status"]
    if "demo" in title_lower:
        return EMOJI_MAP["demo"]
    if "talk" in evtype_lower:
        return EMOJI_MAP["talk"]
    return "&#x1F4CB;"


def extract_events(
    root: ET.Element,
    dug_num: int = None,
    slot_times: list | None = None,
    time_offset_minutes: int = 60,
):
    """Extract events from the 'Dasharo User Group' room.

    If `slot_times` is provided, assign start times from it in order. Otherwise,
    fall back to parsing and normalizing the schedule start times.
    """
    # Default fixed agenda slots (commonly used in repo pages)
    default_slots_17 = ["17:00", "17:05", "17:15", "17:55", "18:15", "18:35", "18:55"]
    default_slots_16 = ["16:00", "16:05", "16:15", "17:00", "17:15", "17:35", "17:55"]

    if slot_times is None:
        # Heuristic: DUG meetings from #8 onward use 17:00 anchor in repo pages
        try:
            use_17 = dug_num is not None and int(dug_num) >= 8
        except Exception:
            use_17 = True
        slot_times = default_slots_17 if use_17 else default_slots_16

    # Optional closing suffixes to match specific repository pages
    closing_suffix_by_dug = {
        10: " &#x27A1;&#xFE0F; &#x1F37A;&#x1F37B; vPub 0xD",
    }

    events = []
    for day in root.findall("day"):
        for room in day.findall("room"):
            name = room.get("name")
            if name and name.strip() == "Dasharo User Group":
                room_events = room.findall("event")
                for idx, ev in enumerate(room_events):
                    title = (ev.findtext("title") or "").strip()
                    start_raw = (ev.findtext("start") or "").strip()
                    date_full = ev.findtext("date") or None
                    # Prefer slot_times if available for consistent agenda formatting
                    if idx < len(slot_times):
                        start = slot_times[idx]
                    else:
                        start = normalize_time(
                            start_raw, date_full, time_offset_minutes
                        )
                    # extract other metadata but do not render speakers/slides by default
                    persons = [p.text for p in ev.findall("./persons/person") if p.text]
                    desc = ev.findtext("description") or ""
                    slides = None
                    m = SLIDES_RE.search(desc)
                    if m:
                        slides = m.group(1)
                    evtype = (ev.findtext("type") or "").lower()
                    emoji = pick_emoji(title.lower(), evtype)
                    # normalize closing title and apply suffix if defined
                    if "closing" in title.lower():
                        title = "Closing remarks"
                        if dug_num and dug_num in closing_suffix_by_dug:
                            title += closing_suffix_by_dug.get(dug_num, "")
                    events.append(
                        {
                            "title": title,
                            "start": start,
                            "speakers": persons,
                            "description": desc.strip(),
                            "slides": slides,
                            "emoji": emoji,
                        }
                    )
    return events


def render_template(
    template_path: str, dug_num: int, events, banner_width: str = "650px"
) -> str:
    template_dir = os.path.dirname(template_path) or "."
    template_name = os.path.basename(template_path)
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape([]),
        keep_trailing_newline=True,
    )
    tpl = env.get_template(template_name)
    return tpl.render(dug_num=dug_num, events=events, banner_width=banner_width)


def ensure_output_path(output: str, dug_num: int) -> str:
    if output is None:
        return None
    if os.path.isdir(output):
        return os.path.join(output, "1-greetings-agenda.md")
    if output.endswith(".md"):
        d = os.path.dirname(output)
        if d and not os.path.exists(d):
            os.makedirs(d, exist_ok=True)
        return output
    os.makedirs(output, exist_ok=True)
    return os.path.join(output, "1-greetings-agenda.md")


def main(argv=None):
    p = argparse.ArgumentParser()
    mutex = p.add_mutually_exclusive_group(required=False)
    mutex.add_argument(
        "--schedule", help="Path or URL to schedule.xml (overrides --dug-num)"
    )
    mutex.add_argument("--dug-num", type=int, help="DUG number (e.g. 10)")
    p.add_argument(
        "--year",
        type=int,
        help="Year used to build the vPub slug (default: current year)",
    )
    p.add_argument(
        "--template",
        default="templates/1-greetings-agenda.j2",
        help="Jinja2 template path",
    )
    p.add_argument(
        "--output", default=None, help="Output file or directory (default: stdout)"
    )
    p.add_argument("--banner-width", default="650px", help="Banner width, e.g. 650px")
    p.add_argument(
        "--force",
        action="store_true",
        help="Allow overwriting pages/dug_<n>/1-greetings-agenda.md",
    )
    p.add_argument(
        "--time-offset-minutes",
        type=int,
        default=60,
        help="Apply offset to times (minutes)",
    )
    p.add_argument(
        "--base-url",
        default="https://cfp.3mdeb.com",
        help="Base URL for pretalx instance",
    )
    args = p.parse_args(argv)

    if not args.schedule and args.dug_num is None:
        p.error("Provide either --schedule or --dug-num")

    schedule_source = args.schedule
    if schedule_source is None:
        schedule_source = schedule_url_for_dug(args.dug_num, args.year, args.base_url)

    try:
        root = parse_schedule(schedule_source)
    except Exception as e:
        print(f"Failed to load schedule from {schedule_source}: {e}", file=sys.stderr)
        sys.exit(2)

    events = extract_events(
        root, dug_num=args.dug_num, time_offset_minutes=args.time_offset_minutes
    )
    rendered = render_template(
        args.template, args.dug_num or 0, events, banner_width=args.banner_width
    )

    outpath = ensure_output_path(args.output, args.dug_num or 0)
    if outpath:
        repo_expected = None
        if args.dug_num:
            repo_expected = os.path.abspath(
                os.path.join("pages", f"dug_{args.dug_num}", "1-greetings-agenda.md")
            )
        if (
            repo_expected
            and os.path.abspath(outpath) == repo_expected
            and os.path.exists(outpath)
            and not args.force
        ):
            print(
                f"Refusing to overwrite repository page {repo_expected}. Pass --force to overwrite.",
                file=sys.stderr,
            )
            sys.exit(2)
        with open(outpath, "w", encoding="utf-8") as f:
            f.write(rendered)
        print(f"Wrote {outpath}")
    else:
        sys.stdout.write(rendered)


if __name__ == "__main__":
    main()
