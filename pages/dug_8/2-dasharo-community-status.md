---
theme: ../../slidev-template/theme
layout: cover
background: /intro.png
class: text-center

---
## &#x1F44B; Dasharo User Group #8 &#x1F389;

### Dasharo Community Status

<center><img src="/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px"></center>

<!--

Date of previous data snapshot: 09/09/2024
Date of data snapshot: 10/12/2024

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
clicks: 6
---

<center><img src="/dug_8/dasharo_team_roadmap.png" width="1000"></center>

<!--

[click] During Yocto Dev Day Tymek and Danil presented a talk about TEE and
Secure Storage, which is essential for security of any modern embedded
application.

[click] During hardweare.io in Amsterdam I delivered first public and
commercial training giving hands-on experience on assessment and provisioning
of Intel Root of Trust and UEFI Chain of Trust (aka UEFI Secure Boot). We plan
to continue delivering commercial public and private training in 2025.

[click] We end this years events activity with DUG#8 and vPub 0xD

[click] First event of 2025 would be Xen Winter Meetup in Grenoble at the end
of January, from that event we going directly to FOSDEM. In Grenoble I will
present: "Enabling UEFI Secure Boot in XCP-ng: Establishing a Robust Chain of
Trust".

[click] Our FOSDEM devroom discussing Open-source firmware
was approved. This is fifth edition of the event.

[click] First quarter conference activity we end up with DUG#9 and vPub 0xE.

-->

---

## Published materials

- Link to DUG#7 and vPub 0xC [YouTube playlist](https://www.youtube.com/playlist?list=PLuISieMwVBpIJQpso6QICMUqqW5z8L1S2) and [slides](https://dl.3mdeb.com/dasharo/dug/7/).
- Linux to Qubes OS Summit 2024 [YouTube playlist day1](https://www.youtube.com/watch?v=lJFxtdan9qY&list=PLuISieMwVBpJmIaHgyv7yKDwrHpqym9Qh) and [day2](https://www.youtube.com/watch?v=9AkBeBwxdA0&list=PLuISieMwVBpL5S7kPUHKenoFj_YJ8Y0_d).
- Link to Yocto Summit [video](https://youtu.be/W78AKeWh57g?feature=shared) and [slides](https://pretalx.com/media/ypdd-oss-elce-2024/submissions/9VBPNF/resources/Practical_Security_for_Embedded_Systems__p7PFTGm.pdf).

---

<center><img src="/dug_8/fosdem25.png" width="700"></center>

<!--

* Not all talks are visible, we still wait for confirmation.
* We plan pPub party on Sunday 2nd February, so if you will be around feel free
to join.
* We will also join party at Delirium Cafe on Saturday.

-->

---
clicks: 2
---

<center><img src="/dug_8/dasharo_team_roadmap2.png" width="850"></center>

<!--

[click] Very rough plans for second and third quarter of 2025 start with Hardwear.io USA in Santa Clara.

[click] Dates of DUG/vPub are roughly set until end of 2025. June edition will
be 12th June, precise date of September edition is not known yet because we
still working on Qubes OS Summit organization.

-->

---
layout: two-cols
---

<center><img src="/dug_8/hwio.jpg" width="600"></center>

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

## <center>Dasharo Issues</center>

<center><img src="/dug_8/issues.png" width="500"></center>
<center><img src="/dug_8/dasharo_issues.png" width="650"></center>

<!--

* Number of reported bugs was slightly smaller, but we keep the rate of 100+
bugs added every quarter.
* It is important to note that number of bugs in OSS projects is not quality indicator, it is rather community and development activity indicator.
* Number of fixed bugs can be treated as development KPI.

Modify and run:
./diagrams/dasharo_issues.py

-->

---

## <center>Dasharo Issues</center>

<br>

### <center>Comments</center>

<center><img src="/dug_8/issue_comments.png" width="500"></center>

### <center>Top Contributors</center>

<center><img src="/dug_8/issue_comments_users.png" width="500"></center>

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

<center><img src="/dug_8/coreboot_prs.png" width="600"></center>
<center><img src="/dug_8/dasharo_coreboot.png" width="650"></center>

<!--

* We keep tempo of around 30 PRs merged per quarter.
* Number of open PRs keep growing at bigger and bigger scale, we trying to
extend our team to support customer requirements.

Modify and run:
./diagrams/dasharo_forks.py

-->

---
layout: two-cols
---

## Dasharo Beta Testing Group

There is not much interest in joining Beta Testing group, so we will hold on
with this effort for some time.

**Tech Preview** - we still plan to introduce some experimental releases, which
would be available to Beta Tester and as paid option to everyone else. Those
will cover some advanced security features like: TrenchBoot, SMI Transfer
Monitor, Intel Boot Guard or similar. This more likely will happen in 2025.

::right::

<center><img src="/dug_7/dasharo_beta_tester.png" width="350"></center>

---

## Free (as free &#x1F37A;&#x1F37B;)

For all those brave souls who are not afraid of bricking their systems we
provide free untested binaries, which are artifacts of our CI/CD.

<center><img src="/dug_8/dasharo_cicd1.png" width="900"></center>

---

## Free (as free &#x1F37A;&#x1F37B;)

<center><img src="/dug_8/dasharo_cicd2.png" width="900"></center>

---

## <center>Dasharo/coreboot upstreaming</center>

<center><img src="/dug_8/coreboot_upstreaming.png" width="600"></center>
<center><img src="/dug_8/dasharo_coreboot_upstraming.png" width="600"></center>

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

#### <center>`700 files changed, 40702 insertions(+), 2653 deletions(-)`</center>

<br>

### <center>Top Upstreamers</center>

- **Michał Żygowski (miczyg):** +48
  - _soc/intel/cannonlake,skylake: Fix locking SMRAM_
  - _util/superiotool/ite: Add extra dumps for IT8613E EC_
- **Sergii Dmytruk (sergiid):** +2
  - _payloads/edk2/Makefile: detect invalid commit hash on checkout_

<!--

Open file in LibreOffice and sort after lines added, you can limit file by:

```shell
./contribution-stats list -r coreboot -s 06/11/2024 -e 09/09/2024 -o dug6-7.csv
```

-->

---

## <center>Dasharo/edk2 PRs</center>

<center><img src="/dug_8/edk2_prs.png" width="650"></center>
<center><img src="/dug_8/dasharo_edk2.png" width="650"></center>

---

## <center>Dasharo star history</center>

<center><img src="/dug_8/star-history.png" width="650"></center>

<!--

https://star-history.com/#Dasharo/coreboot&Dasharo/docs&Dasharo/dasharo-issues&2024-03-12

-->

---

## <center>Dasharo Matrix Community</center>

### <center>Messages and Users</center>

<center><img src="/dug_8/dasharo_general_matrix.png" width="500"></center>

### <center>Top contributors</center>

<center><img src="/dug_8/dasharo_general_matrix_users.png" width="500"></center>

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

<center><img src="/dug_8/dasharo_users.png" width="800"></center>

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
