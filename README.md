# Dasharo User Group Presentations
<!--
SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>

SPDX-License-Identifier: CC-BY-SA-4.0
-->

This repository contains presentations from previous Dasharo User Group
meetings and scripts related to the creation of content in those presentations.

Historically we used [remarkjs](https://github.com/remarkjs/remark) with our
own [remark-remplates](https://github.com/3mdeb/remark-templates), but since
DUG#7 we switched to [slidev](https://sli.dev/).

## Usage

### slidev (>= DUG#7)

* Install npm manager e.g. [nvm](https://github.com/nvm-sh/nvm?tab=readme-ov-file#install--update-script)
* Use lts version of npm:

```bash
nvm install --lts
nvm use --lts
```

* Host presentations:

```bash
npm run dev -- -p 8000 --remote --force
```

- Open content in browser on http://0.0.0.0:8000

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
