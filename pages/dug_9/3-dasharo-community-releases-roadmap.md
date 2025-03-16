---
layout: cover
background: /intro.png
class: text-center

---
## &#x1F44B; Dasharo User Group #8 &#x1F389;

### Dasharo Community Release Roadmaps

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

<center><img src="/dug_8/community_roadmap_meme.png" width="450"></center>

_Please note that the roadmap for the Dasharo Community Support Program is
subject to change and may not represent final release candidates or end of
support dates. This roadmap is intended to provide guidance and direction for
the program's development, but is not a guarantee of specific timelines or
outcomes. For more information on release candidates or release dates, please
contact the Dasharo Team directly._

<!--

We consider to be more conservative in adding new platforms to the roadmap.

-->

---

- For those watching this presentation first time we really encourage to look
  at past videos to get better context and understanding of the format.
  - [DUG#7](https://www.youtube.com/watch?v=raxY3JfMdp0&list=PLuISieMwVBpIJQpso6QICMUqqW5z8L1S2),
    [DUG#6](https://www.youtube.com/watch?v=Q8ILsTzoUjA&list=PLuISieMwVBpIQqHtHwYqypru50eg5nxoz),
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

Note about [Dasharo Naming
Convention](https://docs.dasharo.com/dasharo-naming-convention/) to which we
fully switching starting from beginning of the 2025.

<center><img src="/dug_7/dasharo_naming_convention.png" width="1000"></center>

* Dasharo (coreboot+UEFI) Pro Package for Desktop
* Dasharo (coreboot+Heads) Pro Package for Laptops
* Dasharo (coreboot+SeaBIOS) Enterprise Package for Network Appliance

!!! notice
    Until EOQ4'24 we are in transition period. More information in [#762](https://github.com/Dasharo/dasharo-issues/issues/762).

---

<center><img src="/dug_8/dcs_sample_roadmap_v0.8.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

<!--

* For those who attending this presentation first time, let me briefly explain
how I would present roadmap.
* Let's start with some brief explanation of funding sources for Dasharo
releases:
  * Dasharo Support Package - annual or multi-year contract with OEM, which leads to providing free as free beer releases in unlimited amount (limited only by Dasharo Team capacity and vendor willingness to create more releases).
  * Dasharo Community Releases - support from other sources, donations, grants, Dasharo Revenue Sharing program discussed in the past as well as Dasharo Pro Package and Dasharo Enterprise Package.
* In this presentation we discuss only Dasharo Community Releases, despite the fact that statistics showing also releases made as part of of Dasharo Support Package.

-->

---

<center><img src="/dug_8/dasharo_releases_kpis.png" width="800"></center>

<!--

There are still at least 3 community releases coming:
- Odroid, PC Engines and Dell OptiPlex 7010/9010, QEMU?
- Average: 5.78 releases/quarter for all releases, 81 releases total since Q3'21
- 29 DCR / 52 DSPR = 0.55 DCR/DSPR (+0.01)
- Considering year by year:
  - 2021: 10
  - 2022: 30
  - 2023: 16
  - 2024: 24
- snippets:

```
grep "^## v" docs/variants -r|grep -E "2024-0[1-3]"
grep "^## v" docs/variants -r|grep 2024-0[4-6]|grep -E "novacustom|protectli"|grep -v"heads"
grep "^## v" docs/variants -r|grep 2024-0[4-6]
```

-->

---

<center><img src="/dug_8/dasharo_per_segment.png" width="800"></center>

<!--

- we need historical and last quarter to see trends

-->

---

<center><img src="/dug_8/dasharo_roadmap_states.png" width="800"></center>

<!--

* To some extent this diagram say, that likelihood of change is 40%.
* And there is 5% chance of platform removal.

-->
---

<center><img src="/dug_8/dcs_emu_roadmap_v0.8.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

- Based on our experience with Dasharo (coreboot+SeaBIOS) for PC Engines, we plan to release the same code for QEMU Q35.
- This will improve CI/CD and automatic validation of coreboot+SeaBIOS.
- It will also enhance OSFV validation scope to the [sortbootorder](https://github.com/pcengines/sortbootorder) payload.

<!--

- DUG#8:
  - (NEW) QEMU Q35 v24.08.00.01 planned for Q1'25
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

<center><img src="/dug_8/dce_emu_release.png" width="700" style="margin-left:-36px; margin-top:-40px"></center>

---

<center><img src="/dug_8/pce_dasharo.png" width="800" style="margin-left:-36px; margin-top:-40px"></center>

<!--

Some binary artifacts can be downloaded from Dasharo Patchqueue Initiative repo.

-->

---

<center><img src="/dug_8/dcs_network_appliance_roadmap_v0.8_pt1.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

* According to information on mailing list next release will happen in lat
December and it will be `v24.12`.
* We will most likely schedule release of Dasharo based on it in Q1'25.

<!--

- DUG#8
  - (REMOVED) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) legacy planned for Q4'24
  - (CHANGED) PC Engines apu2/3/4/6 Dasharo (coreboot+UEFI) v0.9.1 planned for Q4'24
    - release date changed to Q1'25
  - (CHANGED) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) v24.08.00.01 planned for Q3'24
    - release date changed to Q4'24
- DUG#7
  - (RELEASED) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) v24.05.00.01 planned for Q2'24
  - (NEW) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) v24.08.00.01 planned for Q3'24
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

TODO: show what is new and what is old

-->

---

<center><img src="/dug_8/dcs_network_appliance_roadmap_v0.8_pt2.png" width="850" style="margin-left:-36px; margin-top:-40px"></center>

* Shifted again. We are kept busy with other projects and implementation didn't
left PoC phase.
* If it will be published it would be Tech Preview.
* [Milestone link](https://github.com/Dasharo/dasharo-issues/milestone/52)

<!--

- DUG#8
  - (CHANGED) Protectli VP4670 planned for Q4'24
    - release date changed to Q1'25 (+1)
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

<center><img src="/dug_8/dcs_network_appliance_roadmap_v0.8_pt3.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

* Unfortunately we canceled this effort for now.
* Main issue were random soft locks described in [issue #1000](https://github.com/Dasharo/dasharo-issues/issues/1000)
* `@miczyg` suspect issue with C6 state and C6 DRAM which ought to be reserved
for it.
* Interestingly coreboot 4.11 does not have this problem, so it may mean that
it is because of using MRC binary for memory initialization.
* Good news are that rebased code base sitting in our repo [here](https://github.com/Dasharo/coreboot/pull/542) and it based on recent coreboot 24.02.01.

<!--

- DUG#8
  - (REMOVED) MinnowBoard Turbot Dasharo(coreboot+UEFI) planned for Q3'24
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

<center><img src="/dug_8/dcs_network_appliance_roadmap_v0.8_pt4.png" width="850" style="margin-left:-36px; margin-top:-40px"></center>

* Unfortunately, we still didn't released binary despite we should be quite
close.
* We have code complete and platform ready for validation.
* We just didn't have resources to assign anyone to that activity because of other priorities.
* Our plan is to release validated binary by the end of 2024.
* `v0.9.0-rc3` is available [here](https://github.com/Dasharo/coreboot/actions/runs/12255193797).

<!--

- DUG#8
  - (CHANGED) Hardkernel Odroid-H4 Dasharo(coreboot+UEFI) planned for Q4'24
    - changed to second half of Q4'24'
- DUG#7
  - (ON TRACK) Hardkernel Odroid-H4 Dasharo(coreboot+UEFI) planned for Q4'24
- DUG#6
  - (NEW) Hardkernel Odroid-H4 Dasharo(coreboot+UEFI) planned for Q4'24

-->

---

<center><img src="/dug_8/dcs_laptop_roadmap_v0.8.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

<!--

* We plan couple releases here.
* First in line is Dasharo (coreboot+Heads) for V56TU v0.9.0 new Intel Meteor
Lake laptops. Those units are also targeted for Qubes OS certification.
  - We still discuss a lot of details, like S3 support, feature freeze in Heads
    and more., so worst case release can shift to Q1'25.
* Our next priority would update of NV4x, assuming that V56TU release can be
managed in reasonable resources.
* Finally we would like to release TechPreview with Qubes OS AEM support, but
it has low priority to fact that NV4x may be our of stock when we will get to that release.

- DUG#8:
  - (NEW) V56TU Dasharo (coreboot+Heads) v0.9.0 planned for Q4'24
  - (NEW) NV4x Dasharo (coreboot+Heads) v0.9.2 planned for Q1'25
  - (CHANGED) NV4x Dasharo (coreboot+SeaBIOS) v1.7.2.x planned for Q1'25
    - release scope changed to coreboot+SeaBIOS
    - release date changed to Q1'25
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

<center><img src="/dug_8/dcs_desktop_dell_roadmap_v0.8.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

* Release is very close to be published. All code related tasks are completed.
* We are now validating the platform. We face some struggles because of OSFV lack support for SeaBIOS (hence QEMU Q35 coreboot+SeaBIOS release). More about that in OSFV status presentation.
* After adding SeaBIOS support we should get more streamlined support for Dell OptiPlex and PC Engines releases.

<!--

- DUG#8
  - (CHANGED) Dell OptiPlex 7010/9010 v0.1.0 planned for Q3'24
    - release date changed to Q4'24
    - release scope changed to v0.1.1
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

<center><img src="/dug_8/dcs_desktop_msi_z690_roadmap_v0.8.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

* `v1.1.4` was released according to schedule. Release notes can be found [here](https://docs.dasharo.com/variants/msi_z690/releases/#v114-2024-12-10).
* Since releases for MSI PRO Z690-A and Z790-P are identical we will discuss
those in details on later slides.

<!--

* We decided to not combine Dasharo Pro Package release and Dasharo Community
Release.

- DUG#8
  - (RELEASED) MSI Z690-A v1.1.4 planned for Q4'24
  - (CHANGED) MSI Z690-A v1.2.0 planned for Q4'24
    - release date changed to Q1'25 (+1)
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

<center><img src="/dug_8/dcs_desktop_msi_z790_roadmap_v0.8.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

* `v0.9.2` was released according to schedule. Release notes can be found [here](https://docs.dasharo.com/variants/msi_z790/releases/#v092-2024-12-10).

<!--

- DUG#8
  - (RELEASED) MSI Z790-P v0.9.2 planned for Q4'24
  - (CHANGED) MSI Z790-P v1.0.0 planned for Q4'24
    - release date changed to Q1'25 (+1)
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

<center><img src="/dug_8/uefi-capsule-update.png" width="450"></center>

- [UEFI Update Capsules for Open Source firmware](https://blog.3mdeb.com/2024/2024-12-10-uefi-capsule-updates/)
- [UEFI Capsule Update in Dasharo Universe](https://docs.dasharo.com/kb/capsule-updates-overview/)

<!--

Before going to deep into details I really recommend reading Sergii Dmytruk
blog post on 3mdeb website about introduction of UEFI Capsule Update to
coreboot ecosystem.

MSI PRO Z690-A and Z790-P are first boards which get support for it in coreboot
and Dasharo. Starting from now those BIOS for those mainbards can be updated
without disabling write protection mechanisms and is open to gain support in LF
fwupd/LVFS.

Main goal of UEFI Capsule Update is to provide more user friendly and
convenient update process. UEFI Capsule Update is defined in UEFI spec and use
special format of firmware called capsule.

What value it provides:
- update process validates if underlying hardware is supported by provided firmware update binary,
- user data and configuration is preserved,
- since update is applied at early stage of boot process various protections mechanisms are not yet enabled, what means user doesn't have to disable those
- capsule update does not need OS, but most often update will go through it, in that way LF fwupd/LVFS project can deliver updates

Blog post also discuss and point to upstreaming effort. Novacustom laptops are
first in line to gain support.

There is more information in documentation:
https://docs.dasharo.com/kb/capsule-updates-overview/

UEFI Capsule Update will be supported by DTS.

-->

---

<center><img src="/dug_8/cpu_config1.jpg" width="450"></center>

- [CPU Configuration in Dasharo Universe](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#cpu-configuration)
* Now you can change:
  - **Number of Active P-cores**
  - **Number of Active E-cores**
  - **Hyper-Threading** status

<!--

We added new submenu which contains options related to CPU:

- **Number of Active P-cores:**

On hybrid CPUs (e.g., Intel 12th gen), you can choose how many Performance
cores (P-cores) are active. By default, all are enabled. Reducing the count
disables some P-cores. At least one must remain active if any are present.

- **Number of Active E-cores:**

Similarly, you can adjust the number of Efficient cores (E-cores). By default,
all are active. Reducing them will disable some E-cores. If there are no
P-cores, at least one E-core must stay active. Otherwise, you can disable all
E-cores.

- **Hyper-Threading:**

By default, P-cores use Hyper-Threading providing two threads per core.
Disabling this feature turns off all secondary threads, leaving one thread per
P-core. This can simplify testing or help tailor performance for specific
workloads. It also can mitigate some speculative attacks.

-->

---

<center><img src="/dug_8/cpu_config3.jpg" width="650"></center>

---

<center><img src="/dug_8/cpu_config2.jpg" width="650"></center>

---

* Dasharo EDKII fork updated from `edk2-stable202002` to `edk2-stable202402`.
* It is hard to enumerate all issues this update fixes.
* Roughly looking at sum of TianoCore Bugzilla tickets that updates cover over
1100 of those.
  - `7055 files changed, 1046876 insertions(+), 528841 deletions(-)`
  - Of course not all are relevant to Dasharo use of EDKII.
* Some notable fixes, which catch our eye:
  - [(CVE-2022-36763) - Heap Buffer Overflow in Tcg2MeasureGptTable()](https://bugzilla.tianocore.org/show_bug.cgi?id=4117)
  - [CryptoPkg: consume OpenSSL 3.0](https://bugzilla.tianocore.org/show_bug.cgi?id=3466)
  - [When setting a new PK in setup mode, PK should not be required to be self-signed](https://bugzilla.tianocore.org/show_bug.cgi?id=2506)
  - [Make package and platform builds reproducible across source format changes](https://bugzilla.tianocore.org/show_bug.cgi?id=3688)
  - XHCI fixes
  - Coverity scan fixes
  - ACPI 6.4 support
* If you are interested in full story behind this update please check [issue #432](https://github.com/Dasharo/dasharo-issues/issues/432).
* New EDKII base would be gradually introduced in all Dasharo (coreboot+UEFI)
releases.

<!--

We also managed to rebase whole Dasharo EDKII fork to edk2-stable202402,
previously we used version which was four years older edk2-stable202002, so it is huge jump.

-->

---

### Prioritize TPM2.0 usage and support multiple TPMs in coreboot

<br>

<center><img src="/dug_8/tpm_unification.png" width="650"></center>

---

<center><img src="/dug_7/dcs_desktop_msi_heads_roadmap_v0.7.png" width="800" style="margin-left:-36px; margin-top:-40px"></center>

* Dasharo (coreboot+Heads) for MSI plans will be announced during next DUG, it is very likely releases will have in first half of 2025.

<!--

- DUG#8
  - no new plans
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

# Changelog DUG#8

- (NEW) QEMU Q35 v24.08.00.01 planned for Q1'25
- (REMOVED) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) legacy planned for Q4'24
- (CHANGED) PC Engines apu2/3/4/6 Dasharo (coreboot+UEFI) v0.9.1 planned for Q4'24
- (CHANGED) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) v24.08.00.01 planned for Q3'24
- (CHANGED) Protectli VP4670 planned for Q4'24
- (REMOVED) MinnowBoard Turbot Dasharo(coreboot+UEFI) planned for Q3'24
- (CHANGED) Hardkernel Odroid-H4 Dasharo(coreboot+UEFI) planned for Q4'24
- (NEW) V56TU Dasharo (coreboot+Heads) v0.9.0 planned for Q4'24
- (NEW) NV4x Dasharo (coreboot+Heads) v0.9.2 planned for Q1'25
- (CHANGED) NV4x Dasharo (coreboot+SeaBIOS) v1.7.2.x planned for Q1'25
- (CHANGED) Dell OptiPlex 7010/9010 v0.1.0 planned for Q3'24
- (RELEASED) MSI Z690-A v1.1.4 planned for Q4'24
- (CHANGED) MSI Z690-A v1.2.0 planned for Q4'24

---

# Changelog DUG#8

- (RELEASED) MSI Z790-P v0.9.2 planned for Q4'24
- (CHANGED) MSI Z790-P v1.0.0 planned for Q4'24

---
layout: cover
background: /intro.png
class: text-center

---

# Q&A
