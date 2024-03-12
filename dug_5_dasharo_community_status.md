class: center, middle, intro

# &#x1F44B; Dasharo User Group #5 &#x1F389;

## Dasharo Community Status

.center[<img src="/remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">]

???

<!--
SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>

SPDX-License-Identifier: CC-BY-SA-4.0
-->

Date of previous data snapshot: 03/12/2023
Date of data snapshot: 11/03/2024

---

# Agenda

- DUG and vPub infrastructure transparency
- Events page updates
- Dasharo Team Events Roadmap
- Dasharo Issues repo stats
- Dasharo coreboot and edk2 forks repos stats
- Dasharo Matrix stats

---

# Openness and transparency paranoia

### .center[Presentations as a Code:<br>https://github.com/Dasharo/presentations]

.center.image-80[![](/img/dasharo_presentations_repo.png)]

---

# Openness and transparency paranoia

### .center[Presentations preparation is tracked in GitHub Milestones]

.center.image-70[![](/img/dug_milestones.png)]

---

# Openness and transparency paranoia

### .center[We are now FSFE REUSE complaint]

```bash
% reuse lint

# SUMMARY
* Bad licenses: 0

* Deprecated licenses: 0
* Licenses without file extension: 0
* Missing licenses: 0
* Unused licenses: 0
* Used licenses: CC0-1.0, CC-BY-SA-4.0, Apache-2.0
* Read errors: 0
* files with copyright information: 227 / 227
* files with license information: 227 / 227
```

---

# Open Collective donations enabled

.center.image-30[![](/img/oc_contrib2.png)]
.center.image-40[![](/img/oc_contrib.png)]

---

# Event page updates

### .center[Please let us know how much you don't like it]

.center.image-99[![](/img/dug_5_event_website_changes.png)]

---

# Event page updates

### .center[Pretalx widget (`cfp.3mdeb.com`) added to Attendize (`vpub.dasharo.com`)]

.center.image-90[![](/img/dug_5_event_website_changes2.png)]

---

# Event page plans

- migration to `events.dasharo.com`
  - `vpub.dasharo.com` seem to be to much focused on virtual events
- grand unification under MkDocs
  - `docs.dasharo.com + dasharo.com + events.dasharo.com ?`
- Git Cliff support
- Ideas and bug reports welcome:
  - https://github.com/dasharo/presentations/issues

---

# Dasharo Events Roadmap Q1-Q2'24

.center.image-100[![](img/dasharo_team_roadmap.png)]

---

# Dasharo Events Roadmap Q3-Q4'24

.center.image-100[![](img/dasharo_team_roadmap2.png)]

---

# Dasharo Issues

.center.image-50[![](/img/dug_5_issues.png)]
.center.image-80[![](/img/dug_5_dasharo_issues.png)]

???

Modify and run:
./diagrams/dasharo_issues.py

---

# Dasharo Issues

### .center[Comments]

.center.image-50[![](/img/dug_5_dasharo_issues_comments.png)]

### .center[Top Contributors]

.center.image-60[![](/img/dug_5_dasharo_issues_comments_users.png)]

???

Following should be run in dasharo-issues repo, gh command should be installed:

- number of unique users active in Dasharo community
  - PAGER="less -R" gh issue list -s all -L 5000 --json author,comments --jq '.[].author.login'|sort|uniq|wc -l
- count all comments
  - PAGER="less -R" gh issue list -s all -L 5000 --json comments --jq '.[].[].[].createdAt'|wc -l
- count how many comments each user posted
  - PAGER="less -R" gh issue list -s all -L 5000 --json comments --jq '.[].[].[].author.login'|sort|uniq -c|sort -h

---

# Dasharo/coreboot PRs

.center.image-50[![](/img/dug_5_coreboot_prs.png)]
.center.image-80[![](/img/dug_5_dasharo_coreboot.png)]

???

Modify and run:
./diagrams/dasharo_forks.py

---

# Dasharo/coreboot upstreaming

.center.image-50[![](/img/dug_5_coreboot_upstreaming.png)]
.center.image-80[![](/img/dug_5_dasharo_coreboot_upstraming.png)]

---

# Dasharo/coreboot upstreaming

### .center[Delta `dasharo` branch vs upstream v4.21 tag]

#### .center[`473 files changed, 22692 insertions(+), 2379 deletions(-)`]

### .center[Top Upstreamers]

- **Sergii Dmytruk (sergiid):** +1869/-42
  - _util: add smmstoretool for editing SMMSTORE_
- **Michał Kopeć (mkc):** +854
  - _mb/lenovo: Add ThinkCentre M700/M900 Tiny board (Skylake/Kaby Lake)_
- **Michał Żygowski (miczyg):** +183/-31
  - _device/pciexp_device.c: Fix setting Max Payload Size_

???

```
./contribution-stats list -r coreboot -s 12/03/2023 -o dug5.csv
./contribution-stats list -r coreboot -s 09/28/2023 -e 12/03/2023 -o dug4.csv
./contribution-stats list -r coreboot -s 07/06/2023 -e 09/28/2023 -o dug3.csv
./contribution-stats list -r coreboot -s 03/16/2023 -e 07/06/2023 -o dug2.csv
awk -F';' '{sum += $6} END {print sum}' dug4.csv #added lines
awk -F';' '{sum += $7} END {print sum}' dug4.csv #removed lines
```

---

# Dasharo/edk2 PRs

.center.image-50[![](/img/dug_5_edk2_prs.png)]
.center.image-80[![](/img/dug_5_dasharo_edk2.png)]

---

# Dasharo Matrix

### .center[Messages and Users]

.center.image-50[![](/img/dug_5_dasharo_general_matrix.png)]

### .center[Top contributors]

.center.image-50[![](/img/dug_5_dasharo_general_matrix_users.png)]

???

Getting number of messages for every user:
grep -E "\-.+:\s" matrix\ -\ Dasharo\ -\ General\ -\ Chat\ Export\ -\ 2024-03-12T11-16-54.063Z.txt |cut -d"-" -f2|cut -d":" -f1|grep -E "^ "|sort|uniq -c|grep -v "banned"|sort -h|grep -v import|grep -v "'"|grep -v "removed"|grep -v coreboot

To count messages add after pipe:
awk '{sum += $1} END {print sum}'

---

# Dasharo Matrix

.center.image-90[![](/img/dug_5_dasharo_users.png)]

---

# Dasharo Matrix

### .center[Most active Dasharo Community Matrix channels]

.center[Random (`#dasharo-random:matrix.org`)]
.center[Support (`#dasharo-support:matrix.org`)]
.center[Dasharo Developers vPub (`#dasharo-osf-vpub:matrix.org`)]

???

General: 29764
Random: 7211
Support: 3322
vPub: 3050
Supermicro: 1640
OSFV: 825
Announcements: 187
Laptops: 187

---

class: center, middle, intro

# Q&A
