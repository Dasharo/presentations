# Dasharo User Group Presentations
<!--
SPDX-FileCopyrightText: 2025 3mdeb <contact@3mdeb.com>

SPDX-License-Identifier: CC-BY-SA-4.0
-->

This repository contains presentations from previous Dasharo User Group
meetings and scripts related to the creation of content in those presentations.

Historically we used [remarkjs](https://github.com/remarkjs/remark) with our
own [remark-templates](https://github.com/3mdeb/remark-templates), but since
DUG#7 we switched to [slidev](https://sli.dev/).

## Usage

### slidev (>= DUG#10)

1. Initialize submodules:

```sh
git submodule update --init --checkout
```

1. Render slides

```sh
./slidev-template/scripts/render-slides.sh [slides_file]
```

Example:

```sh
./slidev-template/scripts/render-slides.sh pages/dug_10/x-dasharo-dbx-uc-ci.md
```

1. Open content in browser on <http://127.0.0.1:8000>

##### Export presentation

1. Export the desired presentation:

```sh
./slidev-template/scripts/ci/gen_slides.sh pages/dug_10/dug10.metadata
```

PDFs will be in `slidev-template/output`.

### slidev (>= DUG#7)

#### Installation

1. Install the `slidev-template` submodule:
    `git submodule update --init --remote slidev-template`

2. Go to the submodule directory:
    `cd slidev-template`

#### Usage

##### Start presentation

1. Start the desired presentation:
    `./scripts/local-preview.sh pages/dug_7/1-greetings-agenda.md`

2. Open content in browser on <http://127.0.0.1:8000>

##### Export presentation

1. Export the desired presentation:
    `./scripts/generate-pdf.sh ../pages/ram-wipe.md`

### remarkjs (< DUG#7)

- Clone repository
- Initialize submodules

  ```bash
  git submodule update --init --recursive --checkout
  ```

- Run local HTTP server e.g.

  ```bash
  python -m http.server
  ```

- Open content in browser on http://0.0.0.0:8000

## Contribution

- Please feel free to create issues for improvement ideas and bugs, as well as
  pull requests to fix any issues.
- Releases will occur quarterly, aligned with the DUG and vPubs schedule.
- If you intend to provide code improvements, please install all dependencies
  by running:

  ```bash
  pip install -r requirements.txt
  ```

- Before pushing code for review, ensure that `pre-commit run --all-files` does
  not return any issues.
