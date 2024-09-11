---
layout: cover
background: /intro.png
class: text-center

---
## &#x1F44B; Dasharo User Group #7 &#x1F389;

### Dasharo Community Status

<center><img src="/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px"></center>

<!--

- consider what feature set is provided in roadmaps
  - define publicly visible deliverables of each phase
  - document frameworks and tools on which given release will be based on
- We need more focused slides, saying precisely what we plan for given release,
  what features what will be validated etc.
- Dasharo development unification
- Customer stories?
- Other 3mdeb roadmaps
  - Zarhus
  - UEFI Secure Boot focus - OSFV
- Features matrix concept
- Inform about our priorities
- Average Delay of Dasharo Community Release
- Average Time To Dasharo Community Release
- Explain Dasharo TrustRoot
- Dasharo Certification Lab

-->

---

<center><img src="/dug_7/community_roadmap_meme_new.png" width="450"></center>

_Please note that the roadmap for the Dasharo Community Support Program is
subject to change and may not represent final release candidates or end of
support dates. This roadmap is intended to provide guidance and direction for
the program's development, but is not a guarantee of specific timelines or
outcomes. For more information on release candidates or release dates, please
contact the Dasharo Team directly._

---

- For those watching this presentation first time we really encourage to look
  at past videos to get better context and understanding of the format.
  - [DUG#6](https://www.youtube.com/watch?v=Q8ILsTzoUjA&list=PLuISieMwVBpIQqHtHwYqypru50eg5nxoz),
    [DUG#5](https://www.youtube.com/watch?v=n7yv9T4VoFc&list=PLuISieMwVBpKBpfYlGZnDXOcqcQKXGXCX),
    [DUG#4](https://www.youtube.com/live/EN5rBAAOdOk?feature=shared&t=3973),
    [DUG#3](https://www.youtube.com/live/xHdlDmZVVkI?feature=shared&t=8700),
    [DUG#2](https://www.youtube.com/live/ZyctrnJNTPc?feature=shared&t=3395),
    [DUG#1](https://www.youtube.com/live/fUfjWyljKNs?feature=shared&t=795)
- We introduced statistics about our planning and execution effort.
- We decided to limit development stages we put on roadmap. Overall we are care
  about releases.
- All releases can be tracked as milestones in Dasharo Issues repo on Github

<center><img src="/dug_7/dasharo_gh_milestones.png" width="450"></center>

---

Let's recap new [Dasharo Naming
Convention](https://docs.dasharo.com/dasharo-naming-convention/) we introducing
since last DUG.

<center><img src="/dug_7/dasharo_naming_convention.png" width="1000"></center>

* Dasharo (coreboot+UEFI) Pro Package for Desktop
* Dasharo (coreboot+Heads) Pro Package for Laptops
* Dasharo (coreboot+SeaBIOS) Enterprise Package for Network Appliance

!!! notice
    Until EOQ4'24 we are in transition period. More information in [#762](https://github.com/Dasharo/dasharo-issues/issues/762).

---

<center><img src="/dug_7/dasharo_releases_kpis.png" width="800"></center>

<!--

There are at least 3 community releases coming:
- Odroid, Minnowobard and Dell OptiPlex 7010/9010
- Average: 6.00 releases/quarter
- 24 DCR / 44 DSPR = 0.54 DCR/DSPR
- Q1'24 DSPR:
- grep "^## v" docs/variants -r|grep -E "2024-0[1-3]"|grep -E "novacustom|protectli"
- Q1'24 DCR:
- All releases in Q1'24'`grep "^## v" docs/variants -r|grep -E "2024-0[1-3]"`
- DCR = All - DSPR
- Q2'24 DSPR:
- grep "^## v" docs/variants -r|grep 2024-0[4-6]|grep -E "novacustom|protectli"|grep -v"heads"
- Q2'24 DCR:
- grep "^## v" docs/variants -r|grep 2024-0[4-6]

-->

---

<center><img src="/dug_7/dasharo_per_segment.png" width="800"></center>

<!--

- we need historical and last quarter to see trends

-->

---

<center><img src="/dug_7/dasharo_roadmap_states.png" width="800"></center>

<!--

- we need historical and last quarter to see trends

-->
---

<center><img src="/dug_7/dcs_emu_roadmap_v0.7.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

* v0.2 was released according to plan,
  - more information on: https://docs.dasharo.com/variants/qemu_q35/releases/
* no further plans at this point for emulation path,

<!--

- DUG#7:
  - (RELEASED) QEMU Q35 v0.2.0 planned for Q2'24
- DUG#6:
  - (CHANGED) QEMU Q35 v0.2.0 planned for Q3'24
    - release scope changed: we will use coreboot+UEFI instead of pure UEFI
    - release date changed: to Q2'24
- DUG#5:
  - (NEW) QEMU Q35 v0.2.0 planned for Q3'24
- DUG#4:
  - (RELEASED) QEMU Q35 v0.1.0 release
- DUG#3:
  - (ON TRACK) QEMU Q35 v0.1.0 planned for Q4'23
- DUG#2:
  - (CHANGED) QEMU Q35 v0.1.0 planned for Q3'23
    - release date changed to Q4'23 (+1)
- DUG#1:
  - (NEW) QEMU Q35 v0.1.0 planned for Q3'23

-->

---

<center><img src="/dug_7/dcs_network_appliance_roadmap_v0.7_pt1.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

<!--

Small correction: 0.9.0 was released in Q2'24 not Q1 as it was on past
presentations.

- DUG#7
  - (RELEASED) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) v24.05.00.01 planned for Q2'24
  - (NEW) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) v24.08.00.01 planned for Q3'24
  - (CHANGED) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) legacy planned for Q3'24
    - release date changed to Q4'24
  - (CHANGED) PC Engines apu2/3/4/6 Dasharo (coreboot+UEFI) v0.9.1 planned for Q2'24
    - release date changed to Q4'24
- DUG#6
  - (RELEASED) PC Engines apu2/3/4/6 Dasharo (coreboot+UEFI) v0.9.0 planned for Q1'24
  - (CHANGED) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) mainline planned for Q2'24
    - release scope change: switched tag to 24.05.00.01
  - (CHANGED) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) legacy planned for Q3'24
    - release date changed to Q3'24
  - (NEW) PC Engines apu2/3/4/6 Dasharo (coreboot+UEFI) v0.9.1 planned for Q2'24
- DUG#5
  - (CHANGED) PC Engines apu2/3/4/6 Dasharo (coreboot+UEFI) planned for Q1'24
    - release scope changed: additional platform apu4
  - (NEW) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) mainline planned for Q2'24
  - (NEW) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) legacy planned for Q2'24
- DUG#4:
  - (CHANGED) PC Engines apu3 planned for Q4'23
    - release date changed to Q1'23 (+1)
    - add support for apu2 and apu6
- DUG#3:
  - (NEW) PC Engines apu3 planned for Q4'23

TODO: think how to improve presentation of all those combinations on roadmap
TODO: show what is new and what is old

-->

---

<center><img src="/dug_7/dcs_network_appliance_roadmap_v0.7_pt2.png" width="850" style="margin-left:-36px; margin-top:-40px"></center>

* We have to shift again, because of _external events_.
* As you already know the benefit of this release would be Intel TXT support backed by TrenchBoot Support.
* Here is Xen Summit 2024 [video](https://youtu.be/RVK52BCM-ZM) presenting status of the project.

<!--

* Initially in Qubes OS, but nothing would prevent support in regular Linux
distro, especially when DRTM patches will be merged upstream (we are at v11
already).
* There are two short term goals for Dasharo (coreboot+SeaBIOS) Tech
Preview:
  - Dasharo TrustRoot (aka Intel Root of Trust aka Intel Boot Guard) support
  - TrenchBoot as AEM for Qubes OS support

- DUG#7
  - (CHANGED) Protectli VP4670 planned for Q3'24
    - release date changed to Q4'24 (+1)
- DUG#6
  - (CHANGED) Protectli VP4670 planned for Q2'24
    - release date changed to Q3'24 (+1)
    - scope change to Dasharo (coreboot+SeaBIOS)
- DUG#5
  - (CHANGED) Protectli VP4670 planned for Q2'24
    - release date changed to Q2'24 (-1)
- DUG#4:
  - (CHANGED) Protectli VP4670 planned for Q2'24
    - release date changed to Q3'23 (+1)
- DUG#3:
  - (NEW) Protectli VP4670 planned for Q2'24

-->

---

<center><img src="/dug_7/dcs_network_appliance_roadmap_v0.7_pt3.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

* We still find some small issues in validation.
* It is very close to be published, but there is some change we will not fit it in Q3'24.
* Unfortunately platform is EOL, so we consider adding Dasharo Community Release by next DUG.

<!--

- DUG#7
  - (CHANGE) MinnowBoard Turbot Dasharo(coreboot+UEFI) planned for Q2'24
    - release date changed to Q3'24 (+1)
- DUG#6
  - (CHANGE) MinnowBoard Turbot Dasharo(coreboot+UEFI) planned for Q2'24
    - release scope changed it will base on 24.02.01
    - release date changed to: Q2'24
- DUG#5
  - (NEW) MinnowBoard Turbot Dasharo(coreboot+UEFI) planned for Q2'24

-->

---

<center><img src="/dug_7/dcs_network_appliance_roadmap_v0.7_pt4.png" width="850" style="margin-left:-36px; margin-top:-40px"></center>

* There is some possibility that release would be published earlier. Closer to beginning of Q4'24, or maybe even still in Q3'24
* Hopefully it would be interesting enough to professionals or enterprise users, so we could quickly release support for H4 and H4 Ultra (there is also option those would be supported out of the box, but we do not plan validation).

<!--

- DUG#7
  - (ON TRACK) Hardkernel Odroid-H4 Dasharo(coreboot+UEFI) planned for Q4'24
- DUG#6
  - (NEW) Hardkernel Odroid-H4 Dasharo(coreboot+UEFI) planned for Q4'24

-->

---

<center><img src="/dug_7/dcs_laptop_roadmap_v0.7.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

* There are two short term goals for Dasharo (coreboot+SeaBIOS) v1.7.2.x Tech
Preview:
  - Dasharo TrustRoot (aka Intel Root of Trust aka Intel Boot Guard) support
  - TrenchBoot as AEM for Qubes OS support

<!--

We planning to show some demo on Qubes OS Summit.

- DUG#7:
  - (RELEASED) Novacustom NV4x Dasharo (coreboot+Heads) v0.9.1 planned for Q3'24
  - (CHANGED) Novacustom NV4x Dasharo (coreboot+UEFI) v2.0.0 planned for Q3'24
    - release scope changed it will base on v2.0.0
    - release date changed to Q4'24 (+1)
- DUG#6:
  - (ON TRACK) Novacustom NV4x Dasharo (coreboot+Heads) v0.9.1 planned for Q3'24
  - (ON TRACK) Novacustom NV4x Dasharo (coreboot+UEFI) v1.8.0 planned for Q3'24
- DUG#5:
  - (RELEASED) Novacustom NV4x Dasharo (coreboot+Heads) v0.9.0 planned for Q4'23
  - (NEW) Novacustom NV4x Dasharo (coreboot+Heads) v0.9.1 planned for Q3'24
  - (NEW) Novacustom NV4x Dasharo (coreboot+UEFI) v1.8.0 planned for Q3'24
- DUG#4:
  - (CHANGED) Novacustom NV4x Dasharo (coreboot+Heads) v0.9.0 planned for Q4'23
    - release date changed to Q1'24 (+1)
- DUG#3:
  - (NEW) Novacustom NV4x Dasharo (coreboot+Heads) v0.9.0 planned for Q4'23

-->

---

<center><img src="/dug_7/dcs_desktop_lenovo_roadmap_v0.7.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

* It is second quarter we see no traction for this platform. It i very unlikely we can support it.
* For now we remove it from roadmap.

<!--

- DUG#7:
  - (REMOVED) Lenovo ThinkCentre M700/M900 Tiny planned for Q2'24
- DUG#6:
  - (ON TRACK) Lenovo ThinkCentre M700/M900 Tiny planned for Q2'24
- DUG#5:
  - (CHANGED) Lenovo M920Q planned for Q2'24
    - scope change/correction: ThinkCentre M700/M900 Tiny
- DUG#4:
  - (CHANGED) Lenovo M920Q planned for Q2'24
    - release date changed to Q3'24 (+1)
- DUG#3:
  - (NEW) Lenovo M920Q planned for Q2'24

-->

---

<center><img src="/dug_7/dcs_desktop_dell_roadmap_v0.7.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

* After almost two years on our roadmap it looks like Dell OptiPlex 7010/9010
is close to be released.
* The goal is to use this platform for TrenchBoot integration, what should render more releases.
* In v0.1.0 release we focus on UEFI compatibility.
* More about pre-order of this hardware in Shameless Plug

<!--

- DUG#7
  - (ON TRACK) Dell OptiPlex 7010/9010 v0.1.0 planned for Q3'24
- DUG#6
  - (CHANGED) Dell OptiPlex 7010/9010 v0.1.0 planned for Q2'24
    - release date changed to Q3'24 (+1)
- DUG#5
  - (CHANGED) Dell OptiPlex 7010/9010 v0.1.0 planned for Q4'23
    - release date changed to Q2'24 (+1)
  - (REMOVED) Dell T1650 v0.1.0 planned for Q1'24
- DUG#4
  - (CHANGED) Dell OptiPlex 7010/9010 v0.1.0 planned for Q4'23
    - release date changed to Q1'24 (+1)
  - (CHANGED) Dell T1650 v0.1.0 planned for Q1'24
    - release date changed to Q3'24 (+2)
- DUG#3
  - (CHANGED) Dell OptiPlex 7010/9010 v0.1.0 planned for Q4'23
    - release type changed to DES
  - (CHANGED) Dell T1650 v0.1.0 planned for Q1'24
    - release type changed to DES
- DUG#2
  - (CHANGED) Dell OptiPlex 7010/9010 v0.1.0 planned for Q2'23
    - release date changed to Q4'23 (+2)
  - (CHANGED) Dell T1650 v0.1.0 planned for Q3'23
    - release date changed to Q1'24 (+2)
- DUG#1
  - (NEW) Dell OptiPlex 7010/9010 v0.1.0 planned for Q2'23
  - (NEW) Dell T1650 v0.1.0 planned for Q3'23

-->

---

<center><img src="/dug_7/dcs_desktop_msi_z690_roadmap_v0.7.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

* Decision about merging Dasharo Pro/Enterprise Package release with Dasharo Community release was not made yet, but likelihood of that event rise.

<!--

- DUG#7
  - (CHANGED) MSI Z690-A v1.1.4 planned for Q3'24
    - release date changed to Q4'24 (+1)
  - (ON TRACK) MSI Z690-A v1.2.0 planned for Q4'24
- DUG#6
  - (ON TRACK) MSI Z690-A v1.1.4 planned for Q3'24
  - (ON TRACK) MSI Z690-A v1.2.0 planned for Q4'24
- DUG#5
  - (RELEASED) MSI Z690-A v1.1.3 planned for Q4'23
  - (NEW) MSI Z690-A v1.1.4 planned for Q3'24
  - (CHANGED) MSI Z690-A v1.2.0 planned for Q1'24
    - release date changed to Q2'24 (+2)
- DUG#4
  - (CHANGED) MSI Z690-A v1.1.3 planned for Q4'23
    - release date changed to Q1'24 (+1)
  - (CHANGED) MSI Z690-A v1.2.0 planned for Q1'24
    - release date changed to Q2'24 (+1)
- DUG#3
  - (RELEASED) MSI Z690-A v1.1.2 planned for Q3'23
  - (ON TRACK) MSI Z690-A v1.1.3 planned for Q4'23
  - (ON TRACK) MSI Z690-A v1.2.0 planned for Q1'24
- DUG#2
  - (ON TRACK) MSI Z690-A v1.1.2 planned for Q3'23
  - (NEW) MSI Z690-A v1.1.3 release planned for Q4'23
  - (CHANGED) MSI Z690-A v1.2.0 planned for Q4'23
    - release date changed to Q1'24 (+1)
- DUG#1
  - (NEW) MSI Z690-A v1.1.2 planned for Q3'23
  - (NEW) MSI Z690-A v1.2.0 planned for Q4'23

-->

---

<center><img src="/dug_7/dcs_desktop_msi_z790_roadmap_v0.7.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

* The same situation as with Z690-A.

<!--

- DUG#7
  - (CHANGED) MSI Z790-P v0.9.2 planned for Q3'24
    - release date changed to Q4'24 (+1)
  - (ON TRACK) MSI Z790-P v1.0.0 planned for Q4'24
- DUG#6
  - (ON TRACK) MSI Z790-P v0.9.2 planned for Q3'24
  - (ON TRACK) MSI Z790-P v1.0.0 planned for Q4'24
- DUG#5
  - (ON TRACK) MSI Z790-P v0.9.2 planned for Q3'24
  - (ON TRACK) MSI Z790-P v1.0.0 planned for Q4'24
- DUG#5
  - (RELEASED) MSI Z790-P v0.9.1 planned for Q4'23
  - (NEW) MSI Z790-P v0.9.2 planned for Q3'24
  - (CHANGED) MSI Z790-P v1.0.0 planned for Q1'24
    - release date changed to Q2'24 (+2)
- DUG#4
  - (CHANGED) MSI Z790-P v1.0.0 planned for Q1'24
    - release date changed to Q2'24 (+1)
  - (ON TRACK) MSI Z790-P v0.9.1 planned for Q4'23
- DUG#3
  - (RELEASED) MSI Z790-P v0.9.0 planned for Q3'23
  - (ON TRACK) MSI Z790-P v0.9.1 planned for Q4'23
  - (ON TRACK) MSI Z790-P v1.0.0 planned for Q1'24
- DUG#2
  - (NEW) MSI Z790-P v0.9.0 planned for Q3'23
  - (NEW) MSI Z790-P v0.9.1 planned for Q4'23
  - (ON TRACK) MSI Z790-P v1.0.0 planned for Q1'24
- DUG#1
  - (NEW) MSI Z790-P v1.0.0 planned for Q1'24

-->

---

<center><img src="/dug_7/dcs_desktop_msi_heads_roadmap_v0.7.png" width="800" style="margin-left:-36px; margin-top:-40px"></center>

* We will stick to one release for Dasharo (coreboot+Heads) per year on MSI
unless interest from community could justify change of that opinion.

<!--

- DUG#7
  - no new plans
- DUG#6
  - (RELEASED) MSI Z790-P Dasharo (coreboot+Heads) v0.9.0 planned for Q1'24
  - (RELEASED) MSI Z690-P Dasharo (coreboot+Heads) v0.9.0 planned for Q1'24
- DUG#5
  - (ON TRACK) MSI Z790-P Dasharo (coreboot+Heads) v0.9.0 planned for Q1'24
  - (NEW) MSI Z690-P Dasharo (coreboot+Heads) v0.9.0 planned for Q1'24
- DUG#4
  - (CHANGED) MSI Z790-P Dasharo (coreboot+Heads) v0.9.0 planned for Q1'24
    - release date changed to Q1'24 (-1)
    - version changed to v0.9.0
- DUG#3
  - (NEW) MSI Z790-P Dasharo (coreboot+Heads) v1.0.1 planned for Q2'24

-->

---

<center><img src="/dug_7/dcs_workstation_roadmap_v0.7.png" width="800" style="margin-left:-36px; margin-top:-40px"></center>

* For now we have remove Talos II release from our roadmap because of lack of interest.

<!--

- DUG#7:
  - (REMOVED) RCS Talos II v0.8.0 planned for Q3'24
- DUG#6:
  - (CHANGED) RCS Talos II v0.8.0 planned for Q2'24
    - release date changed to Q3'24 (+1)
- DUG#5:
  - (REMOVED) ASUS KGPE-D16 v0.5.0 planned for Q2'24
  - (CHANGED) RCS Talos II v0.8.0 planned for Q1'24
    - release date changed to Q2'24 (+1)
- DUG#4:
  - (CHANGED) ASUS KGPE-D16 v0.5.0 planned for Q2'24
    - release date changed to Q3'24 (+1)
    - no response from Immunefi
    - we have to cancel KGPE-D16 from roadmap at some point
  - (NEW) RCS Talos II v0.8.0 planned for Q1'24
    - depends on agreeing on Heads commit on which we should integrate things,
      we already one month blocked because lack of decision
- DUG#3
  - (CHANGED) ASUS KGPE-D16 v0.5.0 planned for Q1'24
    - release type changed to DES
    - release date changed to Q2'24 (+1)
  - (RELEASED) RCS Talos II v0.7.0 planned for Q3'23
- DUG#2
  - (CHANGED) ASUS KGPE-D16 v0.5.0 planned for Q3'23
    - release date changed to Q1'24 (+2)
  - (ON TRACK) RCS Talos II v0.7.0 planned for Q3'23
- DUG#1
  - (NEW) ASUS KGPE-D16 v0.5.0 planned for Q3'23
  - (NEW) RCS Talos II v0.7.0 planned for Q3'23

-->
---
layout: cover
background: /intro.png
class: text-center

---
# Q&A

---
layout: cover
background: /intro.png
class: text-center

---
# CHANGELOG

---

# Changelog DUG#7

- (RELEASED) QEMU Q35 v0.2.0 planned for Q2'24
- (RELEASED) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) v24.05.00.01 planned for Q2'24
- (NEW) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) v24.08.00.01 planned for Q3'24
- (CHANGED) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) legacy planned for Q3'24
  - release date changed to Q4'24
- (CHANGED) PC Engines apu2/3/4/6 Dasharo (coreboot+UEFI) v0.9.1 planned for Q2'24
  - release date changed to Q4'24
- (CHANGED) Protectli VP4670 planned for Q3'24
  - release date changed to Q4'24 (+1)
- (CHANGED) MinnowBoard Turbot Dasharo(coreboot+UEFI) planned for Q2'24
  - release date changed to Q3'24 (+1)
- (ON TRACK) Hardkernel Odroid-H4 Dasharo(coreboot+UEFI) planned for Q4'24
- (RELEASED) Novacustom NV4x Dasharo (coreboot+Heads) v0.9.1 planned for Q3'24

---

# Changelog DUG#7

- (CHANGED) Novacustom NV4x Dasharo (coreboot+UEFI) v2.0.0 planned for Q3'24
  - release scope changed it will base on v2.0.0
  - release date changed to Q4'24 (+1)
- (REMOVED) Lenovo ThinkCentre M700/M900 Tiny planned for Q2'24
- (ON TRACK) Dell OptiPlex 7010/9010 v0.1.0 planned for Q3'24
- (CHANGED) MSI Z690-A v1.1.4 planned for Q3'24
  - release date changed to Q4'24 (+1)
- (ON TRACK) MSI Z690-A v1.2.0 planned for Q4'24
- (CHANGED) MSI Z790-P v0.9.2 planned for Q3'24
  - release date changed to Q4'24 (+1)
- (ON TRACK) MSI Z790-P v1.0.0 planned for Q4'24
- (REMOVED) RCS Talos II v0.8.0 planned for Q3'24
