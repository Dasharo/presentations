class: center, middle, intro

# Dasharo Roadmap

### &#x1F44B; Dasharo User Group #6 &#x1F389;

.center[<img src="/remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">]

???

<!--
SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>

SPDX-License-Identifier: CC-BY-SA-4.0
-->

???

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

---

# Dasharo Roadmap Disclaimer

.center.image-65[![](/img/goal_without_plan.png)]

_Please note that the roadmap for the Dasharo Community Support Program is
subject to change and may not represent final release candidates or end of
support dates. This roadmap is intended to provide guidance and direction for
the program's development, but is not a guarantee of specific timelines or
outcomes. For more information on release candidates or release dates, please
contact the Dasharo Team directly._

---

# Dasharo Roadmap History

- For those watching this presentation first time we really encourage to look
  at past videos to get better context and understanding of the format.
  - [DUG#5](https://www.youtube.com/watch?v=n7yv9T4VoFc&list=PLuISieMwVBpKBpfYlGZnDXOcqcQKXGXCX),
    [DUG#4](https://www.youtube.com/live/EN5rBAAOdOk?feature=shared&t=3973),
    [DUG#3](https://www.youtube.com/live/xHdlDmZVVkI?feature=shared&t=8700),
    [DUG#2](https://www.youtube.com/live/ZyctrnJNTPc?feature=shared&t=3395),
    [DUG#1](https://www.youtube.com/live/fUfjWyljKNs?feature=shared&t=795)
- We introduced statistics about our planning and execution effort.
- We decided to limit development stages we put on roadmap. Overall we are care
  about releases.
- All releases can be tracked as milestones in Dasharo Issues repo on Github
  .center.image-60[![](/img/dasharo_gh_milestones.png)]

---

# Dasharo Naming Convention

.center.image-100[![](/img/dasharo_naming_convention.png)]

- [[RFC] Dasharo Entry Subscription naming scheme #762](https://github.com/Dasharo/dasharo-issues/issues/762) issue
- [[RFC] Initial documentation of Dasharo Product Naming Convention #820](https://github.com/Dasharo/docs/pull/820) PR

---

# Dasharo Naming Convention

### Examples

```plain
Dasharo (coreboot+Heads) Pro Package for Laptop
```

A package aimed at professional retail customers with laptops, incorporating
coreboot with the Heads payload.

```plain
Dasharo (UEFI) Enterprise Package for Desktop
```

A package for enterprise business customers for desktops, employing UEFI with
no additional payload specified.

### Plan

- Q2'24 Announcement - happen right now
- Q3-Q4'24 Transition Period - we use both naming schemes
- EOQ4'24 Switch - we switching to new naming scheme

---

# Dasharo Releases in time

.center.image-95[![](/img/dug_6_dasharo_releases_kpis.png)]

???

- Average: 6.09 releases/quarter
- 24 DCR / 44 DSPR = 0.54 DCR/DSPR
- Q1'24 DSPR:
- grep "^## v" docs/variants -r|grep 2024-0[1-3]|grep -E "novacustom|protectli"
- Q1'24 DCR:
- grep "^## v" docs/variants -r|grep 2024-0[1-3]
- Q2'24 DSPR:
- grep "^## v" docs/variants -r|grep 2024-0[4-6]|grep -E "novacustom|protectli"
- Q2'24 DCR:
- grep "^## v" docs/variants -r|grep 2024-0[4-6]

---

# Dasharo Releases per segment

.center.image-95[![](/img/dug_6_dasharo_per_segment.png)]

???

- we need historical and last quarter to see trends

---

# Dasharo Roadmap States

.center.image-95[![](/img/dug_6_dasharo_roadmap_states.png)]

---

# Dasharo Emulation Roadmap

.center[
<img src="/img/dcs_emu_roadmap_v0.6.png" width="900px" style="margin-left:-36px; margin-top:-40px">
]

- [v0.2.0 milestone](https://github.com/Dasharo/dasharo-issues/milestone/26) is
  planned for Q2'24, instead of Q3'24
- This release will be based on coreboot+UEFI, instead of pure UEFI as before.
- The goal is to provide platform for testing [UEFI Capsule Updates in coreboot](https://docs.dasharo.com/projects/capsule-updates/).

???

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

---

# Dasharo Network Appliance Roadmap

.center[
<img src="/img/dcs_network_appliance_roadmap_v0.6_pt1.png" width="700px" style="margin-left:36px; margin-top:-40px">
]

- Dasharo(coreboot+UEFI) v0.9.0 was released according to plan.
- v0.9.1 was added for Q2'24.
- Dasharo(coreboot+SeaBIOS) version changed to v24.05.00.01.
- v4.0.34 was delayed by one quarter.

???

TODO: think how to improve presentation of all those combinations on roadmap

- DUG#6
  - (RELEASED) PC Engines apu2/3/4/6 Dasharo (coreboot+UEFI) v0.9.0 planned for Q1'24
  - (CHANGED) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) mainline planned for Q2'24
    - release scope change: switched tag to 24.05.00.01
  - (CHANGED) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) legacy planned for Q3'24
    - release date changed to Q3'24
  - (NEW) PC Engines apu2/3/4/6 Dasharo (coreboot+UEFI) v0.9.1 planned for Q1'24
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

---

# Dasharo for PC Engines

.center.image-40[![](/img/dcsppfna.png)]

- Personal use (<= 5 devices):
  - Dasharo (coreboot+SeaBIOS): https://dasharo.com/pcengines/buy/seabios
- Business inquiries, volume sales, OSS support:
  .center[https://www.dasharo.com/pages/contact]

---

# Dasharo Network Appliance Roadmap

.center[
<img src="/img/dcs_network_appliance_roadmap_v0.6_pt2.png" width="850px" style="margin-left:-16px; margin-top:-40px">
]

- Miczyg presented demo on [Xen Summit 2024](https://github.com/3mdeb/conferences/blob/master/2024/XenSummit/Challenges_and_Status_of_Enabling_TrenchBoot_in_Xen_Hypervisor.md), video coming
- DES Release had to be delayed by one quarter because of other projects.
- Release will be based on coreboot+SeaBIOS as UEFI support needs more time.

???

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

---

# Dasharo Network Appliance Roadmap

.center[
<img src="/img/dcs_network_appliance_roadmap_v0.6_pt3.png" width="850px" style="margin-left:-16px; margin-top:-40px">
]

- Because of the issues we faced with FSP while enabling TXE we decided to
  switch to upstream version.
- Release will be based on coreboot 24.02.01
- Commercial support for Dasharo TrustRoot:
  .center[https://www.dasharo.com/pages/contact]

???

- DUG#6
  - (CHANGE) MinnowBoard Turbot Dasharo(coreboot+UEFI) planned for Q2'24
    - release scope changed it will base on 24.02.01
    - release date changed to: Q2'24
- DUG#5
  - (NEW) MinnowBoard Turbot Dasharo(coreboot+UEFI) planned for Q2'24

---

# Dasharo Network Appliance Roadmap

.center[
<img src="/img/dcs_network_appliance_roadmap_v0.6_pt4.png" width="850px" style="margin-left:-16px; margin-top:-40px">
]

- As part of our activity on hardwear.io in OST2 conference we would like to
  made this port with goal of gaining modern and relatively cheap training
  platform.
- Depending on CPU and hardware issues we may port other H4 models.
- We reached out to Hardkernel asking for cooperation.

???

- DUG#6
  - (NEW) Hardkernel Odroid-H4 Dasharo(coreboot+UEFI) planned for Q4'24

---

# Dasharo Laptops Roadmap

.center[
<img src="/img/dcs_laptop_roadmap_v0.6.png" width="900px" style="margin-left:-36px; margin-top:-40px">
]

- Commercial support for Dasharo TrustRoot using Dasharo or Customer Keys

???

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

---

# Dasharo Desktop Lenovo Roadmap

.center[
<img src="/img/dcs_desktop_lenovo_roadmap_v0.6.png" width="900px" style="margin-left:-36px; margin-top:-40px">
]

- No traction here so far, so we treat it as on track until it will fall from
  track.
-

???

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

---

# Dasharo Desktop Dell Roadmap

.center[
<img src="/img/dcs_desktop_dell_roadmap_v0.6.png" width="900px" style="margin-left:-36px;margin-top:-40px">
]

- Unfortunately we didn't demoed Dasharo(coreboot+SeaBIOS) TrenchBoot
- There is still some traction about bringing back operational hardware in
  Dasharo Certification Lab, so I'm leaving this target on our roadmap, but
  shifting release date to next quarter.

???

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

---

# Dasharo Desktop MSI Z690-A Roadmap

.center[
<img src="/img/dcs_desktop_msi_z690_roadmap_v0.6.png" width="800px" style="margin-left:6px;margin-top:-40px">
]

- We consider shifting Dasharo Community Release to Q3'24 instead of doing
  v1.1.4, but no decision was made so far.

???

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

---

# Dasharo Desktop MSI Z790-P Roadmap

.center[
<img src="/img/dcs_desktop_msi_z790_roadmap_v0.6.png" width="850px" style="margin-left:-16px;margin-top:-40px">
]

- No changes to this roadmap.

???

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

---

# Dasharo Desktop MSI Heads Roadmap

.center[
<img src="/img/dcs_desktop_msi_heads_roadmap_v0.6.png" width="800" style="margin-left:6px;margin-top:-40px">
]

- Both releases were delivered on-time. No plans for new releases.

???

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

---

# Dasharo Desktop ASRock Roadmap

.center[
<img src="/img/dcs_desktop_asrock_roadmap_v0.6.png" width="900px" style="margin-left:-36px;margin-top:-40px">
]

- This target is stalled and it seem like hanetzer don't have time to push that
  forward in OpenSIL direction.
- Recent news about [Framework 13
  AMD](https://www.phoronix.com/news/Framework-13-AMD-Coreboot-WIP) show
  potential for porting coreboot to modern AMD, but we have not time for it so far.

???

---

# Dasharo Workstation Roadmap

.center[
<img src="/img/dcs_workstation_roadmap_v0.6.png" width="900px" style="margin-left:-36px;margin-top:-40px">
]

- KGPE-D16 removed from Dasharo roadmap.
  - We have call scheduled with FSF regarding RYF, we will see if it can bring
    some fresh air to this roadmap.
- Dasharo (coreboot+Heads) v0.8.0 for Talos II moved to Q3'24.
  - At this point there are no resources for this release.

???

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

---

# Dasharo Server Roadmap

.center[
<img src="/img/dcs_server_roadmap_v0.6.png" width="900px" style="margin-left:-36px;margin-top:-40px">
]

- There were some inquiries on various channels, but essentially we have zero
  serious traction in server area, so we remove X11SSH-TF from our roadmap.
- Unless something will change I will also stop tracking Dasharo Server Roadmap.

???

- DUG#6
  - (REMOVED) Supermicro X11SSH-TF v0.1.0 planned for Q2'24
- DUG#5
  - (ON TRACK) Supermicro X11SSH-TF v0.1.0 planned for Q2'24
- DUG#4
  - (CHANGED) Supermicro X11SSH-TF v0.1.0 planned for Q2'24
    - release type changed to DES
- DUG#3
  - (CHANGED) Supermicro X11SSH-TF v0.1.0 planned for Q1'24
    - release date changed to Q2'24 (+1)
- DUG#2
  - (CHANGED) Supermicro X11SSH-TF v0.1.0 planned for Q4'23
    - release date changed to Q1'24 (+1)
- DUG#1
  - (NEW) Supermicro X11SSH-TF v0.1.0 planned for Q4'23

---

class: center, middle, intro

# Q&A

---

class: center, middle, intro

# CHANGELOG

---

# Changelog DUG#6

- (CHANGED) QEMU Q35 v0.2.0 planned for Q3'24
  - release scope changed to: Dasharo (coreboot+UEFI)
  - release date changed to: Q2'24 (-1)
- (RELEASED) PC Engines apu2/3/4/6 Dasharo (coreboot+UEFI) v0.9.0 planned for Q1'24
- (CHANGED) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) mainline planned for Q2'24
  - release scope change: switched tag to 24.05.00.01
- (CHANGED) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) legacy planned for Q3'24
  - release date changed to: Q3'24 (+1)
- (NEW) PC Engines apu2/3/4/6 Dasharo (coreboot+UEFI) v0.9.1 planned for Q1'24
- (CHANGED) Protectli VP4670 planned for Q2'24
  - release date changed to: Q3'24 (+1)
  - release scope change to: Dasharo (coreboot+SeaBIOS)
- (CHANGE) MinnowBoard Turbot Dasharo(coreboot+UEFI) planned for Q2'24
  - release scope changed to: 24.02.01

---

# Changelog DUG#6

- (NEW) Hardkernel Odroid-H4 Dasharo(coreboot+UEFI) planned for Q4'24
- (ON TRACK) Novacustom NV4x Dasharo (coreboot+Heads) v0.9.1 planned for Q3'24
- (ON TRACK) Novacustom NV4x Dasharo (coreboot+UEFI) v1.8.0 planned for Q3'24
- (ON TRACK) Lenovo ThinkCentre M700/M900 Tiny planned for Q2'24
- (CHANGED) Dell OptiPlex 7010/9010 v0.1.0 planned for Q2'24
  - release date changed to Q3'24 (+1)
- (ON TRACK) MSI Z690-A v1.1.4 planned for Q3'24
- (ON TRACK) MSI Z690-A v1.2.0 planned for Q4'24
- (RELEASED) MSI Z790-P Dasharo (coreboot+Heads) v0.9.0 planned for Q1'24
- (RELEASED) MSI Z690-P Dasharo (coreboot+Heads) v0.9.0 planned for Q1'24
- (CHANGED) RCS Talos II v0.8.0 planned for Q2'24
  - release date changed to Q3'24 (+1)
- (REMOVED) Supermicro X11SSH-TF v0.1.0 planned for Q2'24

---

# Changelog DUG#5

- (NEW) QEMU Q35 v0.2.0 planned for Q3'24
- (CHANGED) PC Engines apu2/3/4/6 Dasharo (coreboot+UEFI) planned for Q1'24
  - release scope changed: additional platform apu4
- (NEW) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) mainline planned for Q2'24
- (NEW) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) legacy planned for Q2'24
- (CHANGED) Protectli VP4670 planned for Q2'24
  - release date changed to Q2'24 (-1)
- (NEW) MinnowBoard Turbot Dasharo(coreboot+UEFI) planned for Q2'24
- (RELEASED) Novacustom NV4x Dasharo (coreboot+Heads) v0.9.0 planned for Q4'23
- (NEW) Novacustom NV4x Dasharo (coreboot+Heads) v0.9.1 planned for Q3'24
- (NEW) Novacustom NV4x Dasharo (coreboot+UEFI) v1.8.0 planned for Q3'24
- (CHANGED) Lenovo M920Q planned for Q2'24
  - scope change/correction: ThinkCentre M700/M900 Tiny
- (CHANGED) Dell OptiPlex 7010/9010 v0.1.0 planned for Q4'23
  - release date changed to Q2'24 (+1)
- (REMOVED) Dell T1650 v0.1.0 planned for Q1'24

---

# Changelog DUG#5

- (RELEASED) MSI Z690-A v1.1.3 planned for Q4'23
- (NEW) MSI Z690-A v1.1.4 planned for Q3'24
- (CHANGED) MSI Z690-A v1.2.0 planned for Q1'24
  - release date changed to Q2'24 (+2)
- (RELEASED) MSI Z790-P v0.9.1 planned for Q4'23
- (NEW) MSI Z790-P v0.9.2 planned for Q3'24
- (CHANGED) MSI Z790-P v1.0.0 planned for Q1'24
  - release date changed to Q2'24 (+2)
- (ON TRACK) MSI Z790-P Dasharo (coreboot+Heads) v0.9.0 planned for Q1'24
- (NEW) MSI Z690-P Dasharo (coreboot+Heads) v0.9.0 planned for Q1'24
- (REMOVED) ASUS KGPE-D16 v0.5.0 planned for Q2'24
- (CHANGED) RCS Talos II v0.8.0 planned for Q1'24
  - release date changed to Q2'24 (+1)
- (ON TRACK) Supermicro X11SSH-TF v0.1.0 planned for Q2'24
- Summary: 9 new, 7 changed, 2 on track, 3 released, 2 removed (total: 23)

---

# Changelog DUG#4

- (RELEASED) QEMU Q35 v0.1.0 release
- (CHANGED) PC Engines apu3 planned for Q4'23
  - release date changed to Q1'23 (+1)
  - add support for apu2 and apu6
- (CHANGED) Protectli VP4670 planned for Q2'24
  - release date changed to Q3'23 (+1)
- (CHANGED) Novacustom NV4x Dasharo (coreboot+Heads) v0.9.0 planned for Q4'23
  - release date changed to Q1'24 (+1)
- (CHANGED) Lenovo M920Q planned for Q2'24
  - release date changed to Q3'24 (+1)
- (CHANGED) Dell OptiPlex 7010/9010 v0.1.0 planned for Q4'23
  - release date changed to Q1'24 (+1)
- (CHANGED) Dell T1650 v0.1.0 planned for Q1'24
  - release date changed to Q3'24 (+2)
- (CHANGED) MSI Z690-A v1.1.3 planned for Q4'23
  - release date changed to Q1'24 (+1)

---

# Changelog DUG#4

- (CHANGED) MSI Z690-A v1.2.0 planned for Q1'24
  - release date changed to Q2'24 (+1)
- (CHANGED) MSI Z790-P v1.0.0 planned for Q1'24
  - release date changed to Q2'24 (+1)
- (ON TRACK) MSI Z790-P v0.9.1 planned for Q4'23
- (CHANGED) MSI Z790-P Dasharo (coreboot+Heads) v0.9.0 planned for Q1'24
  - release date changed to Q1'24 (-1)
  - version changed to v0.9.0
- (CHANGED) ASUS KGPE-D16 v0.5.0 planned for Q2'24
  - release date changed to Q3'24 (+1)
- (NEW) RCS Talos II v0.8.0 planned for Q1'24
  - depends on agreeing on Heads commit on which we should integrate things,
    we already one month blocked because lack of decision
- Summary: 1 new, 11 changed, 1 on track, 1 released, 0 removed (total: 15)

---

# Changelog DUG#3

- (ON TRACK) QEMU Q35 v0.1.0 planned for Q4'23
- (NEW) PC Engines apu3 v0.9.0 planned for Q4'23
- (NEW) Protectli VP4670 v0.9.0 planned for Q2'24
- (NEW) Novacustom NV4x Dasharo (coreboot+Heads) v0.9.0 planned for Q2'24
- (NEW) Lenovo M920Q v0.9.0 planned for Q2'24
- (CHANGED) Dell OptiPlex 7010/9010 v0.1.0 planned for Q4'23
  - release type changed to DES
- (CHANGED) Dell T1650 v0.1.0 planned for Q1'24
  - release type changed to DES
- (RELEASED) MSI Z690-A v1.1.2 planned for Q3'23
- (ON TRACK) MSI Z690-A v1.1.3 release planned for Q4'23
- (ON TRACK) MSI Z690-A v1.2.0 planned for Q1'24
- (RELEASED) MSI Z790-P v0.9.0 planned for Q3'23

---

# Changelog DUG#3

- (ON TRACK) MSI Z790-P v0.9.1 planned for Q4'23
- (ON TRACK) MSI Z790-P v1.0.0 planned for Q1'24
- (NEW) MSI Z790-P Dasharo (coreboot+Heads) v1.0.1 planned for Q2'24
- (CHANGED) ASUS KGPE-D16 v0.5.0 planned for Q1'24
  - release type changed to DES
  - release date changed to Q2'24 (+1)
- (RELEASED) RCS Talos II v0.7.0 planned for Q3'23
- (CHANGED) Supermicro X11SSH-TF v0.1.0 planned for Q1'24
  - release date changed to Q2'24 (+1)
- Summary: 5 new, 4 changed, 5 on track, 3 released, 0 removed (total: 17)

---

# Changelog DUG#2

- (CHANGED) QEMU Q35 v0.1.0 planned for Q3'23
  - release date changed to Q4'23 (+1)
- (CHANGED) Dell OptiPlex 7010/9010 v0.1.0 planned for Q2'23
  - release date changed to Q4'23 (+2)
- (CHANGED) Dell T1650 v0.1.0 planned for Q3'23
  - release date changed to Q1'24 (+2)
- (ON TRACK) MSI Z690-A v1.1.2 planned for Q3'23
- (NEW) MSI Z690-A v1.1.3 release planned for Q4'23
- (CHANGED) MSI Z690-A v1.2.0 planned for Q4'23
  - release date changed to Q1'24 (+1)
- (NEW) MSI Z790-P v0.9.0 planned for Q3'23
- (NEW) MSI Z790-P v0.9.1 planned for Q4'23
- (ON TRACK) MSI Z790-P v1.0.0 planned for Q1'24
- (CHANGED) ASUS KGPE-D16 v0.5.0 planned for Q3'23
  - release date changed to Q1'24 (+2)

---

# Changelog DUG#2

- (ON TRACK) RCS Talos II v0.7.0 planned for Q3'23
- (CHANGED) Supermicro X11SSH-TF v0.1.0 planned for Q4'23
  - release date changed to Q1'24 (+1)
- Summary: 3 new, 6 changed, 3 on track, 0 released, 0 removed (total: 12)

---

# Changelog DUG#1

- (NEW) QEMU Q35 v0.1.0 planned for Q3'23
- (NEW) Dell OptiPlex 7010/9010 v0.1.0 planned for Q2'23
- (NEW) Dell T1650 v0.1.0 planned for Q3'23
- (NEW) MSI Z690-A v1.1.2 planned for Q3'23
- (NEW) MSI Z690-A v1.2.0 planned for Q4'23
- (NEW) MSI Z790-P v1.0.0 planned for Q1'24
- (NEW) ASUS KGPE-D16 v0.5.0 planned for Q3'23
- (NEW) RCS Talos II v0.7.0 planned for Q3'23
- (NEW) Supermicro X11SSH-TF v0.1.0 planned for Q4'23
- Summary: 9 new, 0 changed, 0 on track, 0 released, 0 removed (total: 9)
