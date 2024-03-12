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

- Considerations of lowlighter/metrics followup plugin
  - it can be easily selfhosted
  - gives a lot of inspiration as well as data
  - of course those data points are little bit different and key question is
    what to do with those, it essentially provide new data which may be but
    doesn't have to be relevant
- Commands cheat sheet

  - issues: `./diagrams/dasharo_issues.py`
  - PRs: `./diagrams/dasharo_forks.py`
  - number of unique users active in Dasharo community
    - PAGER="less -R" gh issue list -s all -L 5000 --json author,comments --jq '.[].author.login'|sort|uniq|wc -l
  - count all comments
    - PAGER="less -R" gh issue list -s all -L 5000 --json comments --jq '.[].[].[].createdAt'|wc -l
  - count how many comments each user posted
    - PAGER="less -R" gh issue list -s all -L 5000 --json comments --jq '.[].[].[].author.login'|sort|uniq -c|sort -h
  - matrix activity
    - fetching all communication may be not the most effective way to get data (general: 00:11-TBD),
      there seem to be need for differential download, but it looks like matrix
      does not support that
    - number of messages for DUG#4 snapshot:
    - matrix comments per user:
    - grep -E "\-.+: " matrix\ -\ Dasharo\ -\ General\ -\ Chat\ Export\ -\ 2023-07-02T22-37-07.435Z.txt |cut -d"-" -f2|cut -d":" -f1|grep -E "^ "|sort|uniq -c|grep -v "banned"|sort -h|grep -v import|grep -v "'"|grep -v "removed"|grep -v coreboot

- TBD: look at community status of other projects, news?
  - consider news presentation with Dasharo status about the OpenSIL
  - maybe announcements section
- Documentation releases?
  - in long run everything should be a release, it would be easier to track
    ideas related to improvements of given area of development

---

# Dasharo Issues

.center.image-50[![](/img/dug_5_issues.png)]
.center.image-80[![](/img/dug_5_dasharo_issues.png)]

---

# Dasharo/coreboot PRs

.center.image-50[![](/img/dug_5_coreboot_prs.png)]
.center.image-80[![](/img/dug_5_dasharo_coreboot.png)]

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

# Dasharo Issues

### .center[Comments]

.center.image-50[![](/img/dug_5_dasharo_issues_comments.png)]

### .center[Top Contributors]

.center.image-60[![](/img/dug_5_dasharo_issues_comments_users.png)]

---

# Dasharo Matrix

.center.image-90[![](/img/dug_5_dasharo_users.png)]

---

# Dasharo Matrix

## .center[Messages]

## .center[Top contributors]

---

class: center, middle, intro

# Q&A
