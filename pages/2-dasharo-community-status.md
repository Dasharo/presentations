---
layout: cover
background: /intro.png
class: text-center

---
## &#x1F44B; Dasharo User Group #7 &#x1F389;

### Dasharo Community Status

<center><img src="/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px"></center>

<!--

Date of previous data snapshot: 10/06/2024
Date of data snapshot: 09/09/2024

-->

---

# Agenda

- Dasharo Team Events Roadmap
- Dasharo Issues repo stats
- Dasharo coreboot and edk2 forks repos stats
- Dasharo Patchqueue Initiative
- Dasharo coreboot upstreaming
- Dasharo Matrix stats

---
clicks: 7
---

<center><img src="/dug_7/dasharo_team_roadmap.png" width="1000"></center>

<!--

[click] On OSFC Krystian explained challenges behind porting coreboot to POWER9 and running it on Talos II.

[click] DUG#7 - we are here

[click] Fifth time in last six years, together with Oracle we host System Boot
and Security Micro-conference on Linux Plumbers. This year with my own talk
which would discuss obstacles in ecosystem to build trustworthy solutions using
Linux.

[click] During Qubes OS Summit among many interesting talk which I would dive into details on later slides, 3mdeb Dasharo Team will deliver two:
- Miczyg's "Anti Evil Maid status and future plans"
- my "Implementing UEFI Secure Boot in Qubes OS: Challenges and Future Steps"

[click] During Yocto Dev Day Tymek will present talk about TEE and Secure
Storage, which is essential for security of any modern embedded application.

[click] During hardweare.io I will deliver first public and commercial training
giving hands-on experience on assessment and provisioning of Intel Root of
Trust and UEFI Chain of Trust (aka UEFI Secure Boot).

[click] We end this years events activity with DUG#8 and vPub 0xD

-->

---

## https://events.3mdeb.com

<br>
<center><img src="/dug_7/3mdeb_events.png" width="270"></center>
<br>

- Link to DUG#6 and vPub 0xB [YouTube playlist and
slides](https://3mdeb.com/events/#_dasharo-user-group-0x6-developers-vpub-0xb)
added.
- Link to Xen Summit [presentation and
video](https://3mdeb.com/events/#_xen-project-summit): "Challenges and Status
of Enabling TrenchBoot in Xen Hypervisor" added.

---

<center><img src="/dug_7/dasharo_team_roadmap2.png" width="850"></center>

<!--

[click] Very rough plans for first half of 2025 start with FOSDEM 2025 and
"Open-source firmware devroom", of course call for devrooms is not yet
announced. We should know more on next DUG.

[click] Dates of DUG/vPub are roughly set until end of 2025. Most of the time
it is second Thursday of last month in quarter (March, June or December),
difference is with September, where it would be third Thursday.

[click] We will inform you as things will clarify.

-->

---

## LPC System Boot and Security MC Line Up

- [Schedule](https://lpc.events/event/18/sessions/201/)
- No more in person tickets, [virtual passes](https://cvent.me/g2ODDV) 50USD,
50% hobbyist discount possible
- Open [Matrix
channel](https://matrix.to/#/#system-boot-and-security-mc:lpc.events):
`#system-boot-and-security-mc:lpc.events`

<center><img src="/dug_7/lpc_sbs_sched.png" width="850"></center>

---

## LPC System Boot and Security MC Line Up

<center><img src="/dug_7/lpc_sbs_sched2.png" width="850"></center>

---
layout: two-cols
---

<center><img src="/dug_7/hwio.jpeg" width="600"></center>

::right::

<center><img src="/dug_7/ost2_logo2.png" width="250">
<br>
<img src="/dug_7/arch4221_qr.png" width="225">
Use QR code to get news about upcoming OST2 classes:
<br>
Arch4221: UEFI Secure Boot
<br>
TC3211: Intel Boot Guard
</center>

---

## Qubes OS Summit 2024 Line Up

- [Schedule](https://vpub.dasharo.com/e/16/qubes-os-summit-2024#schedule)
- No more in person tickets, [virtual passes](https://vpub.dasharo.com/e/16/qubes-os-summit-2024#tickets) free
- Open [Matrix
channel](https://matrix.to/#/#qubes-summit:matrix.org):
`#qubes-summit:matrix.org`

<center><img src="/dug_7/qoss_sched.png" width="500"></center>

---

## <center>Dasharo Issues</center>

<center><img src="/dug_7/issues.png" width="500"></center>
<center><img src="/dug_7/dasharo_issues.png" width="650"></center>

<!--

* We crossed 1k bugs reported.
* This quarter was quite active since we fixed over 100 bugs, as always such
big bucket like dasharo-issues need some cleanup, so big number partially means
we did cleanup.
* There still may be some inaccuracies related bugs in script generating the
diagram

Modify and run:
./diagrams/dasharo_issues.py

-->

---

## <center>Dasharo Issues</center>

<br>

### <center>Comments</center>

<center><img src="/dug_7/issues_comments.png" width="500"></center>

### <center>Top Contributors</center>

<center><img src="/dug_7/issues_comments_users.png" width="500"></center>

<!--

Following should be run in dasharo-issues repo, gh command should be installed:

- number of unique users active in Dasharo community

```shell
PAGER="less -R" gh issue list --repo "Dasharo/dasharo-issues" -s all -L 5000 --json author,comments --jq '.[].author.login'|sort|uniq|wc -l
```

- count all comments

```shell
PAGER="less -R" gh issue list --repo "Dasharo/dasharo-issues" -s all -L 5000 --json comments --jq '.[].[].[].createdAt'|wc -l
```

- count how many comments each user posted

```shell
PAGER="less -R" gh issue list --repo "Dasharo/dasharo-issues" -s all -L 5000 --json comments --jq '.[].[].[].author.login'|sort|uniq -c|sort -h
```

-->

---

## <center>Dasharo/coreboot PRs</center>

<center><img src="/dug_7/coreboot_prs.png" width="600"></center>
<center><img src="/dug_7/dasharo_coreboot.png" width="650"></center>

<!--

Modify and run:
./diagrams/dasharo_forks.py

-->

---
layout: two-cols
---

## Dasharo Beta Testing Group

Novacustom Beta Testing Group is in our opinion very efficient way to expose
potentially problematic binaries to small group of engaged community members.
Based on that experience we would like to build approach which would work for
all Dasharo market segments.

Benefit of beta testers would be free and early access to Dasharo binaries at
the price of potentially bricking your device. We believe number of those
benefits can grow in future, so beta testers could be proud and respected
members of community.

::right::

<center><img src="/dug_7/dasharo_beta_tester.png" width="350"></center>

---

## Dasharo Beta Testing Group

Rules are not written yet, but anyone interested can reach out. During initial
run we plan to accept maximum 3 people per market segment. Some basic
requirements have to be met like ability to recover.

<!-- markdownlint-disable-next-line MD018 -->
Process is tracked in [issue #76](https://github.com/Dasharo/presentations/issues/76). Feel free to provide
suggestions how things could work.

<center><img src="/dug_7/dasharo_beta_testing_group.png" width="600"></center>

---

## <center>Dasharo/coreboot upstreaming</center>

<center><img src="/dug_7/coreboot_upstreaming.png" width="600"></center>
<center><img src="/dug_7/dasharo_coreboot_upstraming.png" width="600"></center>

<!--

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

#### <center>`589 files changed, 30504 insertions(+), 2516 deletions(-)`</center>

<br>

### <center>Top Upstreamers</center>

- **Michał Żygowski (miczyg):** +1268
  - _mb/protectli/vault_adl_p: Add initial support for VP6630/VP6650/VP6670_
- **Sergii  Lewiński (sergiid):** +815
  - _drivers/efi/uefi_capsules.c: coalesce and store UEFI capsules_
- **Krystian Hebel (khebel):** +318
  - _mb/qemu-q35/smihandler.c: add support for SMIs on QEMU_

<!--

Open file in LibreOffice and sort after lines added, you can limit file by:

```shell
./contribution-stats list -r coreboot -s 06/11/2024 -e 09/09/2024 -o dug6-7.csv
```

-->

---

## <center>Dasharo/edk2 PRs</center>

<center><img src="/dug_7/edk2_prs.png" width="650"></center>
<center><img src="/dug_7/dasharo_edk2.png" width="650"></center>

---

## <center>Dasharo star history</center>

<center><img src="/dug_7/star-history.png" width="650"></center>

<!--

https://star-history.com/#Dasharo/coreboot&Dasharo/docs&Dasharo/dasharo-issues&2024-03-12

-->

---

## <center>Dasharo Matrix Community</center>

### <center>Messages and Users</center>

<center><img src="/dug_7/dasharo_general_matrix.png" width="500"></center>

### <center>Top contributors</center>

<center><img src="/dug_7/dasharo_general_matrix_users.png" width="500"></center>

<!--

* shall we count hanetzer, since he started cooperation with 3mdeb
* tlaurion advanced to top5, he is kind of on par with Demi

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

<center><img src="/dug_7/dasharo_users.png" width="800"></center>

---

### <center>Most active Dasharo Community Matrix channels since last DUG</center>

<br>

#### <center>Random (`#dasharo-random:matrix.org`)</center>
<br>

#### <center>Dasharo Developers vPub (`#dasharo-osf-vpub:matrix.org`)</center>
<br>

#### <center>Support (`#dasharo-support:matrix.org`)</center>
<!--

General: 32683 (+1648)
Random: 8416 (+601)
vPub: 3888 (+332)
Support: 4018 (+159)
Supermicro: 1659
OSFV: 1112 (+22)

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
