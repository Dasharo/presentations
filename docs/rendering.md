# Rendering greetings agenda

Prerequisites

- Python 3.10+
- pip install -r requirements.txt (adds Jinja2 and pytest if not present)

Obtaining the pretalx export (example for dug_10):

```bash
# Ensure fixtures directory exists for the schedule export
mkdir -p fixtures

# Download and save the schedule XML into fixtures
curl -o fixtures/dug_10_schedule.xml "https://cfp.3mdeb.com/developers-vpub-0xf-2025/schedule/export/schedule.xml"
```

Render into a target output

- Render from a schedule XML to an output directory (won't overwrite existing
pages by default):

```bash
python3 scripts/render_greetings.py --schedule fixtures/dug_10_schedule.xml --dug-num 10 --output /tmp/outdir
```

- Render from a DUG number (pretalx URL inferred):

```bash
python3 scripts/render_greetings.py --dug-num 10 --output /tmp/outdir
```

- If you want to overwrite the repository page directly, provide --force (and
ensure the output path matches the repo file):

```bash
python3 scripts/render_greetings.py --dug-num 10 --output pages/dug_10/1-greetings-agenda.md --force
```

Compare generated vs repository

```bash
diff -u pages/dug_10/1-greetings-agenda.md /tmp/outdir/1-greetings-agenda.md
```

Preview locally

- The repository does not include a dedicated local-preview script. To preview,
view the generated Markdown in a Markdown viewer/editor, or render slides with
the Slidev-based template if you want slide previews:

```bash
git submodule update --init --checkout
slidev-template/scripts/render-slides.sh pages/dug_10/1-greetings-agenda.md
```

- Open the resulting slides in your browser as instructed by Slidev.

Troubleshooting

- If the generated file misses slides links, check that the Pretalx description
contains a bullet with a slides URL, and/or edit
`templates/1-greetings-agenda.j2` to render slides (ev.slides).
- If banner path differs, adjust `--banner-width` or edit the template path
accordingly.
