class: center, middle, intro

# Dasharo Roadmap

### &#x1F44B; Dasharo User Group #5 &#x1F389;

.center[<img src="/remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">]

???

<!--
SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>

SPDX-License-Identifier: CC-BY-SA-4.0
-->

???

- consider what feature set is provided in roadmaps
  - clearly define how community members and customers can influence our roadmap, in form of diagram
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

---

# Dasharo Roadmap Disclaimer

.center.image-55[![](/img/plan.jpg)]

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
  - [DUG#4](https://www.youtube.com/live/EN5rBAAOdOk?feature=shared&t=3973),
    [DUG#3](https://www.youtube.com/live/xHdlDmZVVkI?feature=shared&t=8700),
    [DUG#2](https://www.youtube.com/live/ZyctrnJNTPc?feature=shared&t=3395),
    [DUG#1](https://www.youtube.com/live/fUfjWyljKNs?feature=shared&t=795)
- We introduced statistics about our planning and execution effort.
- We decided to limit development stages we put on roadmap. Overall we are care
  about releases.
- All releases can be tracked as milestones in Dasharo Issues repo on Github
  .center.image-60[![](/img/dasharo_gh_milestones.png)]

---

# Dasharo Releases in time

.center.image-95[![](/img/dug_5_dasharo_releases_kpis.png)]

???

- Average: 5.58 releases/quarter
- Avararage delay of dasharo community release

---

# Dasharo Releases per segment

.center.image-95[![](/img/dug_5_dasharo_per_segment.png)]

???

- we need historical and last quarter to see trends

---

# Dasharo Roadmap States

.center.image-95[![](/img/dug_5_dasharo_roadmap_states.png)]

---

# Dasharo Emulation Roadmap

.center[
<img src="/img/dcs_emu_roadmap_v0.5.png" width="900px" style="margin-left:-36px; margin-top:-40px">
]

- Dasharo(UEFI) for QEMU Emulator Q35 Machine type was released according to
  plan on 6th Dec 2023
- We heavily use that release in Dasharo OSFV
- [v0.2.0 milestone](https://github.com/Dasharo/dasharo-issues/milestone/26) was published on Dasharo Github

???

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
<img src="/img/dcs_network_appliance_roadmap_v0.5_pt1.png" width="900px" style="margin-left:-36px; margin-top:-40px">
]

- Dasharo(coreboot+UEFI) for PC Engines is in advanced development.

???

TODO: think how to improve presentation of all those combinations on roadmap

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

.center.image-40[![](/img/desfna.png)]

- Personal use (<= 5 devices): https://dasharo.com/pcengines/buy
- Business inquiries, volume sales, OSS support:
  .center[https://www.dasharo.com/pages/contact]

---

# Dasharo Network Appliance Roadmap

.center[
<img src="/img/dcs_network_appliance_roadmap_v0.5_pt2.png" width="900px" style="margin-left:-36px; margin-top:-40px">
]

- We plan to demo TrenchBoot with Xen on this release at Xen Developers Summit in June

???

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
<img src="/img/dcs_network_appliance_roadmap_v0.5_pt3.png" width="900px" style="margin-left:-36px; margin-top:-40px">
]

- Very old embedded platform but still used in industrial and robotics market.
- Support will be based on coreboot `4.11_branch`.
- We plan to prove again our commitment to [long-term support](https://docs.dasharo.com/osf-trivia-list/dasharo/#what-value-dasharo-provides-in-comparison-to-coreboot).
- Dasharo TrustRoot support.

???

- DUG#5
  - (NEW) MinnowBoard Turbot Dasharo(coreboot+UEFI) planned for Q2'24

---

# Dasharo Laptops Roadmap

.center[
<img src="/img/dcs_laptop_roadmap_v0.5.png" width="900px" style="margin-left:-36px; margin-top:-40px">
]

- v0.9.0 released according to plan, more information [here](https://docs.dasharo.com/variants/novacustom_nv4x_adl/heads/#v090-2024-02-29)
- v0.9.1 and v1.8.0: Dasharo TrustRoot using Dasharo or Customer keys

???

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
<img src="/img/dcs_desktop_lenovo_roadmap_v0.5.png" width="900px" style="margin-left:-36px; margin-top:-40px">
]

- Hardware model correction it should be M900 not M920Q
- Port was [merged to coreboot](https://review.coreboot.org/c/coreboot/+/80610/8). Congratulations to Michał (`@mkc`)

???

- DUG#6:
  - (TBD) Lenovo ThinkCentre M700/M900 Tiny planned for Q2'24
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
<img src="/img/dcs_desktop_dell_roadmap_v0.5.png" width="900px" style="margin-left:-36px;margin-top:-40px">
]

- Dasharo(coreboot+SeaBIOS) v0.1.0 is planned to be demoed with TrenchBoot on
  Xen Developers Summit in June
- We removed T1650 because we don't think we will have time for it in
  foreseeable future.

???

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
<img src="/img/dcs_desktop_msi_z690_roadmap_v0.5.png" width="900px" style="margin-left:-36px;margin-top:-40px">
]

???

- [v1.1.3](https://docs.dasharo.com/variants/msi_z690/releases/#v113-2024-01-22) was released according to plan. Hardware going in unbotanium mode.
- Community release has low priority because of other activities.

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
<img src="/img/dcs_desktop_msi_z790_roadmap_v0.5.png" width="900px" style="margin-left:-36px;margin-top:-40px">
]

???

- [v0.9.1](https://docs.dasharo.com/variants/msi_z790/releases/#v091-2024-01-22)
  was released according to plan.
- Community release has low priority because of other activities.

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
<img src="/img/dcs_desktop_msi_heads_roadmap_v0.5.png" width="900px" style="margin-left:-36px;margin-top:-40px">
]
???

- Release is planned at the end of March, so it is considered on track.

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
<img src="/img/dcs_desktop_asrock_roadmap_v0.5.png" width="900px" style="margin-left:-36px;margin-top:-40px">
]

- Decision was made to pursue OpenSIL path, but this target may be replaced by
  AMD Phoenix-based one.
- Dasharo Supporting Partner discussion with multiple parties.
- There is no clear roadmap for x370 or x570 in Dasharo.

???

---

# Dasharo Workstation Roadmap

.center[
<img src="/img/dcs_workstation_roadmap_v0.5.png" width="900px" style="margin-left:-36px;margin-top:-40px">
]

- KGPE-D16 removed from Dasharo roadmap.
  - There are some parties interested in development.
  - FSFE probably will sponsor Denis 'GNUtoo' Carikli.
  - Also received communication from Adrien 'neox' Bourmault.
- Dasharo (coreboot+Heads) v0.8.0 for Talos II moved to Q2'24.'

???

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
<img src="/img/dcs_server_roadmap_v0.5.png" width="900px" style="margin-left:-36px;margin-top:-40px">
]

- Most likely we should remove this target if nothing will happen.
- We have other strategic approach in desktop/workstation market segment.

???

- DUG#6
  - proposal:
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
