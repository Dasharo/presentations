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
- Blog recent changes

---
clicks: 6
---

<center><img src="/img/dug_10/dasharo_team_roadmap.png" width="900"></center>

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
layout: two-cols
---

<center><img src="/img/dug_10/dug09.png" width="300"></center>

Link to DUG#9 and vPub 0xE [YouTube
playlist](https://www.youtube.com/watch?v=ZVgjzvRcnqU&list=PLuISieMwVBpKNjDQBK2MU78tbU1XWkiPD)
and [slides](https://cfp.3mdeb.com/developers-vpub-0xe-2025/schedule/).

::right::

<center><img src="/img/dug_10/zdm01.png" width="337"></center>

Link to ZDM#1 [YouTube playlist](https://www.youtube.com/live/RHuwtdhKxrc?feature=shared&t=1934) and [slides](https://cfp.3mdeb.com/zarhus-developers-meetup-0x1-2025/schedule/).

---

<center><img src="/img/dug_10/qoss25_poster.jpg" width="650"></center>

---

<center><img src="/img/dug_10/qoss25_cfs.png" width="550">

<br>

#### https://dl.3mdeb.com/dasharo/qoss/2025/qubes_os_summit_2025_prospectus.pdf

</center>

---

<center><img src="/img/dug_10/qoss25_tickets.png" width="900">

<br>

## https://events.dasharo.com/event/2/qubes-os-summit-2025

</center>

---
clicks: 4
---

<center><img src="/img/dug_10/dasharo_team_roadmap2.png" width="900"></center>

<!--

[click] Q4 we will start with Zarhus Developers Meetup.

[click] Right after it we plan to do HWIO NL training, we will see if we can
generate similar interest as last year.

[click] DUG#12 would be on second Thursday of December, it seem to be standard for DUG/vPub, 2nd Thu of last month of the quarter.

[click] We consider going to Tokyo for Linux Plumbers Conference as well as
applying for FOSDEM'26.

-->

---

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

<center><img src="/img/dug_10/issues.png" width="500"></center>
<center><img src="/img/dug_10/dasharo_issues.png" width="650"></center>

<!--

* Number of reported bugs was 20 smaller than last quarter. So we definitely
see some slowdown. Hopefully this is silent before storm and during vacation
period when we should have little bit more time to tinker we will get back on
track.
* We fixed 16 bugs less than in last quarter. Slowdown in adding bugs is bigger
than in fixing, at least in absolute terms. Percentage-wise things does not
look so shiny.

Modify and run:
./diagrams/dasharo_issues.py

-->

---

## <center>Dasharo Issues</center>

<br>

### <center>Comments</center>

<center><img src="/img/dug_10/issue_comments.png" width="500"></center>

### <center>Top Contributors</center>

<center><img src="/img/dug_10/issue_comments_users.png" width="550"></center>

<!--

Not much growth here. It is definitely one of the calmest quarters in Dasharo
history. We have to change that.

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

<center><img src="/img/dug_10/coreboot_prs.png" width="600"></center>
<center><img src="/img/dug_10/dasharo_coreboot.png" width="650"></center>

<!--

* Our average tempo of margining changes is 29.3PR/quarter, we are slightly above with 31PRs merged.
* Backlog of open PRs classically growing faster and faster. So if you want to help with review and validation feel free to join.
* We definitely hit record high in opening new PRs, where our average is 41.9PRs and we high 62PRs this quarter. And it is not yet end.

* Average margining tempo per quarter:
  - 26+39+31+21+37+29+29+21+31=264/9=29.3
* Average PRs creation:
  - 40+46+40+26+46+38+43+34+62=375/9=41.9

Modify and run:
./diagrams/dasharo_forks.py

-->

---

## <center>Dasharo/coreboot upstreaming</center>

<center><img src="/img/dug_10/coreboot_upstreaming.png" width="600"></center>
<center><img src="/img/dug_10/dasharo_coreboot_upstraming.png" width="600"></center>

<!--

On average we upstream ~2500SLOC every quarter. This quarter we are so far
already above the average. So maybe we don't work on issues much, but we definitely opened more PRs and upstreamed more code than average.

Average added:
- 2240+4203+173+2927+3819+3447+50+2751+3241=22851/9=2539

Top is total:

```shell
./contribution-stats list -r coreboot -s 01/01/2000 -e 06/10/2024 -o dug6.csv
```

```shell
awk -F';' '{sum += $6} END {print sum}' dug6.csv #added lines
awk -F';' '{sum += $7} END {print sum}' dug6.csv #removed lines
```

-->

---

### <center>Delta `dasharo` branch vs upstream v24.12 tag</center>

<br>

#### <center>`673 files changed, 2237 insertions(+), 40101 deletions(-)`</center>

<br>

### <center>Top Upstreamers</center>

- **Michał Kopeć (mkc):** +3121/-6
  - _mb/novacustom/mtl-h: Add discrete graphics variant_
  - _Documentation/mainboard/lenovo: Add ThinkCentre M700/M900 Tiny_
  - _ec/dasharo/ec: Add DTT power and battery participants_
- **Krystian Hebel (khebel):** +104/-1
  - _drivers/smmstore: allow full flash access for capsule updates_
- **Michał Żygowski (miczyg):** +16/-16
  - _soc/intel/elkhartlake/pmc,gpio: Fix PMC GPE GPIO routes_
  - _mainboard/protectli/vault_ehl/Kconfig: Configure TPM PIRQ_
  - _mb/protectli/vault_ehl/devicetree.cb: Fix assertion in soc/pmutil_

<!--

As said last time our statistics improved thanks to rebasing some platforms to
24.12 coreboot release. Still not all platforms received releases, but we
already working on 25.03 rebase. So it would be harder and harder to track
things.

Some platforms stay on older base and we will not change that unless there will
be new release coming.

We see that Michał Kopeć is definitely the leader of upstreaming with his work
around laptops being top contribution. We also would like to thank Krystian and
Michał Żygowski for their effort to upstream code.

Open file in LibreOffice and sort after lines added, you can limit file by:

```shell
./contribution-stats list -r coreboot -s 03/20/2025 -e 06/10/2025 -o dug10.csv
```

-->

---

<center><img src="/img/dug_10/dasharo_version.png" width="730">

<br>

### https://docs.dasharo.com/variants/versions/

</center>

<!--

You can find information about what branch which supported platform lives.

-->

---

## <center>Dasharo/edk2 PRs</center>

<center><img src="/img/dug_10/edk2_prs.png" width="650"></center>
<center><img src="/img/dug_10/dasharo_edk2.png" width="650"></center>

<!--

* Our average tempo of margining changes is 14.4PR/quarter, we are slightly
below with 11PRs merged.
* Backlog of open PRs classically growing faster and faster. So if you want to
help with review and validation feel free to join.
* This quarter was quite calm in edk2 Dasharo downstream, with roughly 18PRs
open, where average is 21.6PRs.

* Average margining tempo per quarter:
  - 9+22+19+8+18+20+10+13+11=130/9=14.4
* Average PRs creation:
  - 11+24+24+10+20+22+32+34+18=195/9=21.6

-->

---

## <center>Dasharo star history</center>

<center><img src="/img/dug_10/star-history.png" width="650"></center>

<!--

Take on 2025/06/10

https://star-history.com/#Dasharo/coreboot&Dasharo/docs&Dasharo/dasharo-issues

-->

---

## <center>Dasharo Matrix Community</center>

### <center>Messages and Users</center>

<center><img src="/img/dug_10/dasharo_general_matrix.png" width="500"></center>

### <center>Top contributors</center>

<center><img src="/img/dug_10/dasharo_general_matrix_users.png" width="500"></center>

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

# Top Contributors Benefits

* Unlimited access to the Dasharo Pro Package
* Up to 15% discount on hardware sold by 3mdeb (excluding dropshipping)
* How to claim?
  - Write an email to: contact@dasharo.com

<!--
Dasharo Matrix Community and Dasharo Issues Contributors benefits.
-->

---

<center><img src="/img/dug_10/dasharo_users.png" width="800"></center>

---

### <center>Most active Dasharo Community Matrix channels since last DUG</center>

<br>

#### <center>Random (`#dasharo-random:matrix.org`)</center>
<br>

#### <center>Support (`#dasharo-support:matrix.org`)</center>

<br>

#### <center>Laptops (`#dasharo-laptops:matrix.org`)</center>

<!--

* Random: 11006 (+1502)
* General: 36607 (+1411)
* Support: 6027 (+659)
* Laptops: 1408 (+217)
* OSFV: 1860 (+119)
* vPub: 4420 (+112)
* TrenchBoot: 2281 (+61)
* OST2: 348 (+12)
* Supermicro: 1667 (+8)
* OSF Bootstrapable Toolchain: 271

-->

---

<center><img src="/img/dug_10/bug_bounty.png" width="700">

<br>

### https://3mdeb.com/bug-bounty/

</center>

---

# <center>Blog recent changes: comments</center>
#### <center><https://blog.3mdeb.com></center>

<center><img src="/img/dug_10/comentario-example.png" width="700"></center>

<!--
We would also like to introduce you to some changes on our blog:
* Some time ago we've dropped the Disqus comments plugin, because of the ads.
* Recently, we've introduced open source project named Comentario, that seems to
  satisfy our needs
* The historical comments were successfully migrated, so you can now share your
  thoughts about recent and past articles
* Simple account creation is needed, but we will also enable login via popular
  external providers like GitHub, LinkedIn or Twitter/X
-->

---

<center><img src="/img/dug_10/blog-statistics-2025-06-11.png" width="750"></center>

<!--
* Additionally, Statistics page caught our attention:
  - at first, only Last 30 Days were visible - see the screenshot
  - after the contact with Comentario maintainer, dynamic range was introduced
    in recently released version v3.14.0, resolving our request
  - we are testing this feature and consider partially replacing the Google
    Analytics for this open-source alternative
* <describe statistics from ~20 days>

We are looking forward to the fruitful technical discussions on the blog and
more!
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
