---
layout: cover
background: /intro.png
class: text-center

---
## &#x1F44B; Dasharo User Group #9 &#x1F389;

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
- Features matrix concept
- Inform about our priorities
- Average Delay of Dasharo Community Release
- Average Time To Dasharo Community Release
- Explain Dasharo TrustRoot
- Dasharo Certification Lab

-->

---

<center><img src="/dug_9/community_roadmap_meme.png" width="450"></center>

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
  - [DUG#8](https://www.youtube.com/watch?v=elEYzR-kVkw&list=PLuISieMwVBpLcYtLuM7rwooWeoH7I6tEF),
    [DUG#7](https://www.youtube.com/watch?v=raxY3JfMdp0&list=PLuISieMwVBpIJQpso6QICMUqqW5z8L1S2),
    [DUG#6](https://www.youtube.com/watch?v=Q8ILsTzoUjA&list=PLuISieMwVBpIQqHtHwYqypru50eg5nxoz),
    [DUG#5](https://www.youtube.com/watch?v=n7yv9T4VoFc&list=PLuISieMwVBpKBpfYlGZnDXOcqcQKXGXCX),
    [DUG#4](https://www.youtube.com/live/EN5rBAAOdOk?feature=shared&t=3973),
    [DUG#3](https://www.youtube.com/live/xHdlDmZVVkI?feature=shared&t=8700),
    [DUG#2](https://www.youtube.com/live/ZyctrnJNTPc?feature=shared&t=3395),
    [DUG#1](https://www.youtube.com/live/fUfjWyljKNs?feature=shared&t=795)

<center><img src="/dug_7/dasharo_gh_milestones.png" width="450"></center>

---

<center><img src="/dug_7/dasharo_naming_convention.png" width="1000"></center>

* In short Dasharo Pro Package (DPP)
* Dasharo (coreboot+UEFI) Pro Package for Desktop
* Dasharo (coreboot+Heads) Pro Package for Laptops
* Dasharo (coreboot+SeaBIOS) Enterprise Package for Network Appliance

!!! notice
    We finished transition announced in [#762](https://github.com/Dasharo/dasharo-issues/issues/762). Official documentation can be found on [Dasharo Universe](https://docs.dasharo.com/dasharo-naming-convention/) website.

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

<center><img src="/dug_9/dasharo_releases_kpis.png" width="800"></center>

<!--

There are still at least 2 community releases coming:
- PC Engines and QEMU
- Average: 21 releases/year, 5 releases/quarter for all releases, 89 releases total since Q3'21
- 32 DCR / 57 DSPR = 0.56 DCR/DSPR (+0.01)
- Considering year by year:
  - 2021: 10
  - 2022: 31
  - 2023: 16
  - 2024: 27
  - 2025: 5
- snippets:

```
grep "^## v" docs/variants -r | grep -E "2024-(09|1[0-2])"
grep "^## v" docs/variants -r | grep -E "2024-(09|1[0-2])"|grep -E "novacustom|protectli"|grep -v"heads"
```

-->

---

<center><img src="/dug_9/dasharo_per_segment.png" width="800"></center>

<!--

- we need historical and last quarter to see trends

-->

---

<center><img src="/dug_9/dasharo_roadmap_states.png" width="800"></center>

<!--

* To some extent this diagram say, that likelihood of change is 40%.
* And there is 5% chance of platform removal.

-->
---

<center><img src="/dug_9/dcs_emu_roadmap_v0.9.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

- This is still the same unreleased milestone based on our experience with Dasharo (coreboot+SeaBIOS) for PC Engines, we plan to release the same code for QEMU Q35.
- This will improve CI/CD and automatic validation of coreboot+SeaBIOS and [sortbootorder](https://github.com/pcengines/sortbootorder) payload.
- [GitHub Milestone Link](https://github.com/Dasharo/dasharo-issues/milestone/59) to QEMU Q35 (coreboot+SeaBIOS)
- [GitHub Milestone Link](https://github.com/Dasharo/dasharo-issues/milestone/45) to QEMU Q35 (coreboot+UEFI) which potentially could be scheduled this year.

<!--

- DUG#9:
  - (CHANGED) QEMU Q35 v0.9.0 planned for Q1'25
    - release name changed: v24.08.00.01 to v0.9.0
    - release date changed: to Q2'25
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

<center><img src="/dug_9/dcs_network_appliance_roadmap_v0.9_pt1.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

* According to information on mailing list next release will happen in lat
March and it will be `v25.03`.
* Unfortunately, because of big backlog we will most likely tune in to `v25.03.00.01` in Q3'25.
* This is due to fact that v24.08.00.01 already need **_just_** validation.

<!--

- DUG#9
  - (NEW) PC Engines apu2/3/4/6 Dasharo (coreboot+SeaBIOS) v25.03.00.01 planned for Q3'25
  - (NEW) PC Engines apu2/3/4/6 Dasharo (coreboot+SeaBIOS) v25.12.00.01 planned for Q2'25
  - (CHANGED) PC Engines apu2/3/4/6 Dasharo (coreboot+UEFI) v0.9.1 planned for Q1'25
    - release date changed to Q2'25 (+1)
  - (CHANGED) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) v24.08.00.01 planned for Q4'24
    - release date changed to Q2'25 (+2)
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

-->

---

<center><img src="/dug_9/dcs_network_appliance_roadmap_v0.9_pt2.png" width="850" style="margin-left:-36px; margin-top:-40px"></center>

* Now this release is under risk and most likely will be replaced by release Dasharo (coreboot+UEFI) with TrenchBoot support for that platform.
* Although we still discussing it because we see at least two issues with it:
  * [Intel TXT doesn't work on VP4670](https://github.com/Dasharo/dasharo-issues/issues/1269) - when platform does not enable `GETSEC[SENTER]`.
  * [Hangs during microcode update](https://github.com/Dasharo/dasharo-issues/issues/1256) when platform sometimes fails on OS microcode update.
* [Milestone link](https://github.com/Dasharo/dasharo-issues/milestone/52)

<!--

- DUG#9
  - (CHANGED) Protectli VP4670 planned for Q1'25
    - release date changed to Q2'25 (+1)
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

<center><img src="/dug_9/dcs_network_appliance_roadmap_v0.9_pt4.png" width="850" style="margin-left:-36px; margin-top:-40px"></center>

* We finally released support for Odroid-H4+.
* It is simple and minimalistic release. We aim to extend support in upcoming quarter.

<!--

- DUG#9
  - (RELEASED) Hardkernel Odroid-H4 Dasharo(coreboot+UEFI) planned for Q4'24
  - (NEW) Hardkernel Odroid-H4 Dasharo(coreboot+UEFI) v0.9.1 planned for Q2'25
- DUG#8
  - (CHANGED) Hardkernel Odroid-H4 Dasharo(coreboot+UEFI) planned for Q4'24
    - changed to second half of Q4'24'
- DUG#7
  - (ON TRACK) Hardkernel Odroid-H4 Dasharo(coreboot+UEFI) planned for Q4'24
- DUG#6
  - (NEW) Hardkernel Odroid-H4 Dasharo(coreboot+UEFI) planned for Q4'24

-->

---

### Hardkernel Odroid-H4 v0.9.0 SBOM

* Firmware framework: Dasharo downstream based on coreboot 24.02
* Payload: Dasharo downstream based on edk2-stable202402
* iPXE based on 2024.05
* vboot: Dasharo downstream version
* FSP: IoT ADL-N MR4 (5061_00)
* Intel Management Engine version v16.50.10.1351
* Intel microcode version ADL-N N0 0x17 07/12/2023

---
layout: two-cols
---

* Initial support for the Hardkernel ODROID H4 device, based on Intel Alder Lake N
* UEFI compatible interface
* Support for discrete TPM
* UEFI Secure Boot support
* Boot logo customization support
* USB boot support
* NVMe boot support
* TPM Measured Boot
* UEFI Shell
* Network boot
* Windows 11 booting
* Ubuntu LTS booting

::right::

* Serial port console redirection
* Vboot Verified Boot
* Intel ME HAP disable
* BIOS flash protection for Vboot recovery region
* Setup menu password configuration
* SMM BIOS write protection
* USB stack disable option in setup menu
* Network stack disable option in setup menu

---

### Known issues

!!! bug
    When performing SUSP005.001 test that performs 15 s3 sleep and resume cycles using fwts 1/15 cycles is always too short 15~18s as opposed to expected 30s.

<!--

This may be false negative, since we suspect sleep cycle could be delayed on OS
side, but we will investigate that.

-->

---

### Planned features

* Tests on Odroid-H4 Ultra.
* Provide ME disabling menu.
* Give ability to enable/disable bifurcation.
* Give ability to enable/disable IBECC.

<!--

Hopefully during next roadmap presentation we will add the milestone on github.

-->
---

<center><img src="/dug_9/dcs_laptop_roadmap_v0.9.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

* Dasharo (coreboot+Heads) for V56TU v0.9.0 new Intel Meteor
  Lake laptops was released.
* Our next priority would update of NV4x, because of other priorities we had to shift
  it by one quarter.
* Since NV4x is out of stock in Novacustom we decided to drop TrenchBoot as
  Qubes OS AEM release for that platform.

<!--

- DUG#9:
  - (RELEASED) V56TU Dasharo (coreboot+Heads) v0.9.0 planned for Q4'24
  - (CHANGED) NV4x Dasharo (coreboot+Heads) v0.9.2 planned for Q1'25
    - release date changed to Q2'25 (+1)
  - (REMOVED) NV4x Dasharo (coreboot+SeaBIOS) v1.7.2.x planned for Q1'25
    - release scope changed to coreboot+SeaBIOS
    - release date changed to Q1'25
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

### V56TU Dasharo (coreboot+Heads) v0.9.0 SBOM

* Firmware framework: Dasharo downstream based on heads v0.2.1
* Dasharo fork of System76 EC
* vboot: Dasharo downstream version
* Intel Management Engine version v18.0.5.2040
* Intel Firmware Support Package for Meteor Lake-H version 2024/04/30 v4122_12
* Intel microcode version MTL C0 0x1c 03/01/2024

<!--

Not that heads version has any meaning. Heads is rolling release.

-->

---

<center><img src="/dug_9/dcs_desktop_dell_roadmap_v0.9.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

* We released v0.1.1 on time, but we decide to change it to Dasharo (coreboot+UEFI) instead of SeaBIOS.
* We plan version that will support DRTM, but it is to early to announce it.

<!--

- DUG#9
  - (RELEASED) Dell OptiPlex 7010/9010 v0.1.1 planned for Q4'24
    - release date changed to Q4'24
    - release scope changed to v0.1.1
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

### Dell OptiPlex 7010/9010 v0.1.1 SBOM

* Firmware framework: Dasharo downstream based on coreboot 24.02
* Payload: Dasharo downstream based on edk2-stable202405
* Latest Intel published microcode-20190514

---

* Support for Dell OptiPlex 7010/9010
* UEFI Boot Support
* Configurable boot order
* Configurable boot options
* UEFI Secure Boot support
* Custom boot logo
* Dasharo setup menu full screen mode support
* SMM BIOS write protection
* Firmware update mode
* Setup menu password configuration
* USB stack disable option in setup menu
* Network stack disable option in setup menu
* Serial Console Redirection option

---

<center><img src="/dug_9/dcs_desktop_msi_z690_roadmap_v0.9.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

* This year we plan just one release, which would be Dasharo Community Release.
* It will include all recent fixes and modifications most likely rebased on top of  recent version of coreboot and EDKII.
* Release will be free and open access to whole community.

<!--

* We decided to not combine Dasharo Pro Package release and Dasharo Community
Release.

- DUG#9
  - (CHANGED) MSI Z690-A v1.2.0 planned for Q1'24
    - release date changed to Q2'25 (+1)
- DUG#8
  - (RELEASED) MSI Z690-A v1.1.4 planned for Q4'24
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

<center><img src="/dug_9/dcs_desktop_msi_z790_roadmap_v0.9.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

* The same situation as with Z690-A.

<!--

- DUG#9
  - (CHANGED) MSI Z790-P v1.0.0 planned for Q1'25
    - release date changed to Q2'25 (+1)
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

<center><img src="/dug_7/dcs_desktop_msi_heads_roadmap_v0.7.png" width="800" style="margin-left:-36px; margin-top:-40px"></center>

* Unfortunately, we have no new plans.

<!--

- DUG#9
  - no new plans
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

# Changelog DUG#9

- (CHANGED) QEMU Q35 v0.9.0 planned for Q1'25
- (NEW) PC Engines apu2/3/4/6 Dasharo (coreboot+SeaBIOS) v25.03.00.01 planned for Q3'25
- (NEW) PC Engines apu2/3/4/6 Dasharo (coreboot+SeaBIOS) v25.12.00.01 planned for Q2'25
- (CHANGED) PC Engines apu2/3/4/6 Dasharo (coreboot+UEFI) v0.9.1 planned for Q1'25
- (CHANGED) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) v24.08.00.01 planned for Q4'24
- (CHANGED) Protectli VP4670 planned for Q1'25
- (RELEASED) Hardkernel Odroid-H4 Dasharo(coreboot+UEFI) planned for Q4'24
- (NEW) Hardkernel Odroid-H4 Dasharo(coreboot+UEFI) v0.9.1 planned for Q2'25
- (RELEASED) V56TU Dasharo (coreboot+Heads) v0.9.0 planned for Q4'24
- (CHANGED) NV4x Dasharo (coreboot+Heads) v0.9.2 planned for Q1'25
- (REMOVED) NV4x Dasharo (coreboot+SeaBIOS) v1.7.2.x planned for Q1'25
- (RELEASED) Dell OptiPlex 7010/9010 v0.1.1 planned for Q4'24
- (CHANGED) MSI Z690-A v1.2.0 planned for Q1'24
- (CHANGED) MSI Z790-P v1.0.0 planned for Q1'25

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
