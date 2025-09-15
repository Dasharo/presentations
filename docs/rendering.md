# Rendering greetings agenda

Prerequisites

- Python 3
- pip install -r requirements.txt (adds Jinja2 and pytest if not present)

Obtaining the pretalx export (example for dug_10):

```bash
curl -o fixtures/dug_10_schedule.xml "https://cfp.3mdeb.com/developers-vpub-0xf-2025/schedule/export/schedule.xml"
```

Render into a temporary directory (won't overwrite existing pages by default):

```bash
python3 scripts/render_greetings.py --schedule fixtures/dug_10_schedule.xml --dug-num 10 --output /tmp/outdir
```

Compare generated file with authoritative repository file:

```bash
diff -u pages/dug_10/1-greetings-agenda.md /tmp/outdir/1-greetings-agenda.md
```

Preview locally (project helper):

```bash
./scripts/local-preview.sh pages/dug_10/1-greetings-agenda.md
```

Troubleshooting

- If the generated file misses slides links, check that the pretalx description contains a bullet with `[slides](https://...)`.
- If banner path differs, adjust `--banner-width` or edit `templates/1-greetings-agenda.j2` to change the image path.
