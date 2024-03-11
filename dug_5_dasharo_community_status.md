class: center, middle, intro

# &#x1F44B; Dasharo User Group #5 &#x1F389;

## Dasharo Community Status

.center[<img src="/remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">]

???

<!--
SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>

SPDX-License-Identifier: CC-BY-SA-4.0
-->

---

# Community Heartbeat &#x1F493;

.image-100[![](/img/community_heartbeat_dug_4.png)]

???

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

# Dasharo/coreboot PRs

.center.image-80[![](/img/dug5_dasharo_coreboot.png)]

- Experiment v2 with data presentation.
- Since DUG#3 we merged 25 PRs, what is average results for Dasharo/coreboot.

---

# Dasharo/edk2 PRs

.center.image-80[![](/img/dug_5_dasharo_edk2.png)]

- EDK II fork activity is similar to coreboot fork.
- We merged 20 PRs.

---

# Dasharo Issues

.center.image-80[![](/img/dug_5_dasharo_issues.png)]

- `123 added / 90 resolved `

---

# Dasharo Matrix

.center.image-80[![](/img/dasharo_matrix_2023q4.png)]

- We more then double the size of our community over last 9 months.
- We would like to thank you for your contribution to growth of Dasharo.

---

class: center, middle, intro

# Q&A
