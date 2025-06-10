---
theme: slidev-template/theme
layout: cover
background: /intro.png
class: text-center

---
## &#x1F44B; Dasharo User Group #10 &#x1F389;

### Dasharo Community Status

<center><img src="/img/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px"></center>

---

# Agenda

- Dasharo Team Events Roadmap
- Dasharo Issues repo stats
- Dasharo coreboot and edk2 forks repos stats
- Dasharo coreboot upstreaming
- Dasharo Matrix stats

---
clicks: 6
---

<center><img src="/img/dug_10/dasharo_team_roadmap.png" width="800px"></center>

<!--

[click] As I probably mentioned during last DUG, whole 3mdeb will focus more on
organizing our own events and improve those with hope to reach bigger audience.
We would like to minimize investment in external events.

[click] At the beginning of May we hosted first Zarhus Developers Meetup. Presentations and videos are already available.

[click] We decided to not go to Xen Summit to US, despite meeting everyone in
AMD was something very attractive, but we would like to focus on getting
customers who would like to deploy AMD based hardware with Dasharo.

[click] We closing second quarter of 2025 conference activity with DUG#10 and
vPub 0xF.

[click] In August we plan another Zarhus Developers Meetup.

[click] Our biggest event this year most likely would be Qubes OS summit for
which CfP is open. I will spent little bit more time on this event on further
slides.

Modify and run:
./diagrams/dasharo_team_events_roadmap.py

-->

---

## Published materials

- Link to DUG#9 and vPub 0xE [YouTube playlist]() and [slides]().
- Link to ZDM#1 [YouTube playlist](https://www.youtube.com/live/RHuwtdhKxrc?feature=shared&t=1934) and [slides](https://cfp.3mdeb.com/zarhus-developers-meetup-0x1-2025/schedule/).

---
layout: two-cols
---

<center><img src="/img/dug_8/hwio.jpg" width="600"></center>

::right::

<center><img src="/img/dug_7/ost2_logo2.png" width="250">
<br>
<img src="/img/dug_7/arch4221_qr.png" width="225">
Use QR code to get news about upcoming OST2 classes:
<br>
Arch4221: UEFI Secure Boot
<br>
TC3211: Intel Boot Guard
</center>

---
clicks: 4
---

<center><img src="/img/dug_10/dasharo_team_roadmap2.png" width="850"></center>

<!--

[click] Very rough plans for third and fourth quarter of 2025 start with
Hardwear.io USA in Santa Clara.

[click] Dates of DUG/vPub are roughly set until end of 2025.

[click] There is also a chance we will appear at Xen Summit in Silicon Valley.

[click] We consider going to Tokyo for Linux Plumbers Conference.

-->

---
layout: two-cols
---

<center><img src="/img/dug_8/hwio.jpg" width="600"></center>

::right::

<center><img src="/img/dug_7/ost2_logo2.png" width="250">
<br>
<img src="/img/dug_7/arch4221_qr.png" width="225">
Use QR code to get news about upcoming OST2 classes:
<br>
Arch4221: UEFI Secure Boot
<br>
TC3211: Intel Boot Guard
</center>

<!--

We are under second round of internal review. It still need a lot of work, but
we are on right track to publish Arch4221 this half of year.

In case of HWIO, please let us know if you need discount code.

-->

---

## <center>Dasharo Issues</center>

<center><img src="/img/dug_9/issues.png" width="500"></center>
<center><img src="/img/dug_9/dasharo_issues.png" width="650"></center>

<!--

* Number of reported bugs was almost the same as in last quarter. So we keep
  steady pace with rate around 110.
* We fixed 14 more bugs then in last quarter, what indicate some small
  progress, but we still have more bugs opened each quarter than we close.

Modify and run:
./diagrams/dasharo_issues.py

-->

---

## <center>Dasharo Issues</center>

<br>

### <center>Comments</center>

<center><img src="/img/dug_9/issue_comments.png" width="500"></center>

### <center>Top Contributors</center>

<center><img src="/img/dug_9/issue_comments_users.png" width="500"></center>

<!--

We decide to add Firminator at sixth position since he/she was very active over
last quarter. Other then that this is usual stead growth of comments and user
pool.

Following should be run in dasharo-issues repo, gh command should be installed:

- number of unique users active in Dasharo community

```shell
PAGER="less -R" gh issue list --repo "Dasharo/dasharo-issues" -s all -L 10000 --json author,comments --jq '.[].author.login'|sort|uniq|wc -l
```

- count all comments

```shell
PAGER="less -R" gh issue list --repo "Dasharo/dasharo-issues" -s all -L 10000 --json comments --jq '.[].[].[].createdAt'|wc -l
```

- count how many comments each user posted

```shell
PAGER="less -R" gh issue list --repo "Dasharo/dasharo-issues" -s all -L 10000 --json comments --jq '.[].[].[].author.login'|sort|uniq -c|sort -h
```

-->

---

## <center>Dasharo/coreboot PRs</center>

<center><img src="/img/dug_9/coreboot_prs.png" width="600"></center>
<center><img src="/img/dug_9/dasharo_coreboot.png" width="650"></center>

<!--

* Our average tempo of mergining changes dropped from 26PRs to less than 24PRs
  per quarter.
* Backlog of open PRs growing.
* All that is result of lack of availability of the team as well as other
  priorities not always related to develop Dasharo. We would love to dedicate
  100% of our time to open-source firmware, but at this point it is not possible
  and we have to provide also additional services to break even.

Modify and run:
./diagrams/dasharo_forks.py

-->

---

## <center>Dasharo/coreboot upstreaming</center>

<center><img src="/img/dug_9/coreboot_upstreaming.png" width="600"></center>
<center><img src="/img/dug_9/dasharo_coreboot_upstraming.png" width="600"></center>

<!--

On average we upstream ~2500SLOC every quarter. It is not a lot, but this is
what we are comfortable with in current state of business.

Top is total:

```shell
./contribution-stats list -r coreboot -s 01/01/2000 -e 06/10/2024 -o dug6.csv
```

Bottom:

```shell
./contribution-stats list -r coreboot -s 03/11/2000 -e 06/10/2024 -o dug6.csv
```

```shell
awk -F';' '{sum += $6} END {print sum}' dug6.csv #added lines
awk -F';' '{sum += $7} END {print sum}' dug6.csv #removed lines
```

-->

---

### <center>Delta `dasharo` branch vs upstream v24.08 tag</center>

<br>

#### <center>`746 files changed, 45193 insertions(+), 102129 deletions(-)`</center>

<br>

### <center>Top Upstreamers</center>

- **Michał Kopeć (mkc):** +1540/-95
  - _mb/novacustom: add V5x0TU board (Meteor Lake)_
  - _mb/novacustom/mtl-h: Add iGPU variant_
  - _mb/novacustom/mtl-h/variants/igpu/hda_verb.c: Add all HDA verbs from stock FW_
- **Michał Żygowski (miczyg):** +35/-0
  - _soc/intel/cannonlake: Let coreboot lock MSR_IA32_DEBUG_INTERFACE_
  - _soc/intel/common/block/graphics: Add missing TWL GT SKUs_
- **Sergii Dmytruk (sergiid):** +23/-5
  - _drivers/efi/capsules: check for overflows of capsule sizes_
  - _drivers/efi/capsules.c: fix recording capsule size_

<!--

I'm not sure why we hit so many deletions, but this statistics should be
largely improved since we rebase on top of 24.12 where the diff is really
minimalistic. Hopefully I can present more information during next DUG.

Congratulations to Michał Kopeć for making most of upstreaming this quarter.

Open file in LibreOffice and sort after lines added, you can limit file by:

```shell
./contribution-stats list -r coreboot -s 06/11/2024 -e 09/09/2024 -o dug6-7.csv
```

-->

---

## <center>Dasharo/edk2 PRs</center>

<center><img src="/img/dug_9/edk2_prs.png" width="650"></center>
<center><img src="/img/dug_9/dasharo_edk2.png" width="650"></center>

<!--

On average we merge 15 PRs into our EDKII fork. We are in process of rebasing
to edk2-202502 release.

-->

---

## <center>Dasharo star history</center>

<center><img src="/img/dug_9/star-history.png" width="650"></center>

<!--

Take on 2025/03/17

https://star-history.com/#Dasharo/coreboot&Dasharo/docs&Dasharo/dasharo-issues

-->

---

## <center>Dasharo Matrix Community</center>

### <center>Messages and Users</center>

<center><img src="/img/dug_9/dasharo_general_matrix.png" width="500"></center>

### <center>Top contributors</center>

<center><img src="/img/dug_9/dasharo_general_matrix_users.png" width="500"></center>

<!--

* Not much activity recently, it is definitely part of our lack of time from
  our side to deliver new shiny stuff.
* tlaurion advanced to top4, so huge thanks to him for engaging in Dasharo Community

Getting number of messages for every user:

```shell
grep -E "\-.+:\s" matrix\ -\ Dasharo\ -\ General\ -\ Chat\ Export\ -\ 2024-03-12T11-16-54.063Z.txt |cut -d"-" -f2|cut -d":" -f1|grep -E "^ "|sort|uniq -c|grep -v "banned"|sort -h|grep -v import|grep -v "'"|grep -v "removed"|grep -v coreboot
```

To count messages add after pipe:

```shell
awk '{sum += $1} END {print sum}'
```

-->

---

<center><img src="/img/dug_9/dasharo_users.png" width="800"></center>

---

### <center>Most active Dasharo Community Matrix channels since last DUG</center>

<br>

#### <center>Support (`#dasharo-support:matrix.org`)</center>

<br>

#### <center>Random (`#dasharo-random:matrix.org`)</center>
<br>

#### <center>Dasharo OSFV (`#osfv:matrix.3mdeb.com`)</center>

<!--

* Support: 5368 (+1191)
* General: 32683 (+1648) 35196 (+865)
* Random: 9504 (+487)
* OSFV: 1741 (+607)
* vPub: 4308 (+88)
* TrenchBoot: 2220
* Supermicro: 1659
* Laptops: 1191
* OST2: 336
* OSF Bootstrapable Toolchain: 271

-->
---
layout: cover
background: /intro.png
class: text-center

---

# Questions?

<!--

Comment to satisfy pre-commit

-->
