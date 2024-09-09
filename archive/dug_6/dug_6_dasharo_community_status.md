class: center, middle, intro

# &#x1F44B; Dasharo User Group #6 &#x1F389;

## Dasharo OSFV status

.center[<img src="/remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">]

???

<!--
SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>

SPDX-License-Identifier: CC-BY-SA-4.0
-->

Date of previous data snapshot: 11/03/2024
Date of data snapshot: 10/06/2024

---

# Agenda

- Dasharo Team Events Roadmap
- Dasharo Issues repo stats
- Dasharo coreboot and edk2 forks repos stats
- Dasharo Patchqueue Initiative
- Dasharo coreboot upstreaming
- Dasharo Matrix stats

---

# Dasharo Events Roadmap Q1-Q2'24

.center.image-100[![](img/dasharo_team_roadmap.png)]

---

# https://events.3mdeb.com

.center.image-70[![](img/3mdeb_events.png)]

- Link to all FOSSDEM 2024 3mdeb presentations and videos
- Link to DUG#5 and vPub 0xA (also on https://vpub.dasharo.com and YouTube)
- Link to FOSSASIA 2024 presentation and video
- Coming: Xen Summit presentation and video

---

# Dasharo Events Roadmap Q3-Q4'24

.center.image-100[![](img/dasharo_team_roadmap2.png)]

---

# LPC System Boot and Security MC CfP Open

.center.image-70[![](img/lpc2024_cfp.png)]

- Go to https://lpc.events
- Login
- Go to Call for Proposals
- Use Submit New Abstract

---

# Qubes OS Summit 2024 CfP

.center.image-60[![](/img/qubesos_summit_2024_cfp.png)]

- Go to: https://cfp.3mdeb.com
- Choose upcoming event CfP: `Qubes OS Summit 2024 (Sept. 20th – 22nd, 2024)`
- Use Submit Proposal

---

# Dasharo Events Roadmap Q1-Q2'25

.center.image-100[![](img/dasharo_team_roadmap3.png)]

---

# Dasharo Issues

.center.image-50[![](/img/dug_6_issues.png)]
.center.image-80[![](/img/dug_6_dasharo_issues.png)]

???

Modify and run:
./diagrams/dasharo_issues.py

---

# Dasharo Issues

### .center[Comments]

.center.image-50[![](/img/dug_6_dasharo_issues_comments.png)]

### .center[Top Contributors]

.center.image-60[![](/img/dug_6_dasharo_issues_comments_users.png)]

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

.center.image-70[![](/img/dug_6_coreboot_prs.png)]
.center.image-80[![](/img/dug_6_dasharo_coreboot.png)]

???

Modify and run:
./diagrams/dasharo_forks.py

---

# Dasharo Patchqueue Initiative

.center.image-80[![](/img/dasharo-pq.png)]

- The `dasharo-pq` repository was initiated to PoC new way of managing the
  downstream distribution of coreboot firmware, as highlighted in issue
  [#310](https://github.com/Dasharo/dasharo-issues/issues/310).

---

# Dasharo Patchqueue Initiative

### **Current Challenges:**

1. **Branching Model Complexity**: Difficulty in managing multiple
   platform-specific branches as the number of supported platforms increases.
2. **Synchronization Issues**: Effort-intensive and error-prone synchronization
   of features and fixes across branches.
3. **Mono-branch Problem**: The consolidation into a single branch (`dasharo`
   branch) for releases complicates rebasing with upstream, increasing the risk
   of errors and disrupting collaboration.
4. **Upstream Merging Difficulties**: The integration of upstream changes into
   downstream forks is complex and prone to missing crucial updates.

---

# Dasharo Patchqueue Initiative

### **Proposed Solution:**

- **Adopt Patch Management**: A shift towards a structured patch management
  system is proposed to address these issues, drawing inspiration from successful
  implementations in large and small projects (e.g., Debian, Linux, Qubes OS,
  XenServer, and TrenchBoot).

### **Hypothesized Benefits:**

- Enhanced systematic management of changes.
- Reduced complexity and error in merging upstream updates as well as
  upstreaming downstream changes.
- Improved consistency across multiple platform configurations.

---

# Dasharo/coreboot upstreaming

.center.image-70[![](/img/dug_6_coreboot_upstreaming.png)]
.center.image-80[![](/img/dug_6_dasharo_coreboot_upstraming.png)]

???

Top is total:
./contribution-stats list -r coreboot -s 01/01/2000 -e 06/10/2024 -o dug6.csv

Bottom:
./contribution-stats list -r coreboot -s 03/11/2000 -e 06/10/2024 -o dug6.csv

awk -F';' '{sum += $6} END {print sum}' dug6.csv #added lines
awk -F';' '{sum += $7} END {print sum}' dug6.csv #removed lines

---

# Dasharo/coreboot upstreaming

### .center[Delta `dasharo` branch vs upstream v24.02.01 tag]

#### .center[`527 files changed, 25401 insertions(+), 2111 deletions(-)`]

### .center[Top Upstreamers]

- **Michał Kopeć (mkc):** +1045
  - _ec/dasharo/ec: Add initial copy of ec/system76/ec_
- **Filip Lewiński (filipleple):** +587/-2
  - _util/inteltool: add Meteor Lake support_
- **Sergii Dmytruk (sergiid):** +572/-549
  - _security/vboot: extract secdata_tpm{1,2}.c_

???

---

# Dasharo/edk2 PRs

.center.image-60[![](/img/dug_6_edk2_prs.png)]
.center.image-80[![](/img/dug_6_dasharo_edk2.png)]

---

# Dasharo star history

.center.image-80[![](/img/dug_6_star-history.png)]

???

https://star-history.com/#Dasharo/coreboot&Dasharo/docs&Dasharo/dasharo-issues&2024-03-12

---

# Dasharo Matrix

### .center[Messages and Users]

.center.image-50[![](/img/dug_6_dasharo_general_matrix.png)]

### .center[Top contributors]

.center.image-50[![](/img/dug_6_dasharo_general_matrix_users.png)]

???

Getting number of messages for every user:
grep -E "\-.+:\s" matrix\ -\ Dasharo\ -\ General\ -\ Chat\ Export\ -\ 2024-03-12T11-16-54.063Z.txt |cut -d"-" -f2|cut -d":" -f1|grep -E "^ "|sort|uniq -c|grep -v "banned"|sort -h|grep -v import|grep -v "'"|grep -v "removed"|grep -v coreboot

To count messages add after pipe:
awk '{sum += $1} END {print sum}'

---

# Dasharo Matrix

.center.image-90[![](/img/dug_6_dasharo_users.png)]

---

# Dasharo Matrix

### .center[Most active Dasharo Community Matrix channels]

.center[Random (`#dasharo-random:matrix.org`)]
.center[Support (`#dasharo-support:matrix.org`)]
.center[Dasharo Developers vPub (`#dasharo-osf-vpub:matrix.org`)]

???

General: 31035
Random: 7815 (+604)
Support: 3859 (+537)
vPub: 3556 (+506)
OSFV: 1090 (+265)

---

class: center, middle, intro

# Q&A
