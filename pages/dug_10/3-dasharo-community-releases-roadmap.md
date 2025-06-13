---
theme: slidev-template/theme
layout: cover
background: /intro.png
class: text-center

---
## &#x1F44B; Dasharo User Group #10 &#x1F389;

### Dasharo Community Release Roadmaps

<center><img src="/img/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px"></center>

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

<center><img src="/img/dug_10/community_roadmap_meme.png" width="450"></center>

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
  - [DUG#9](https://www.youtube.com/watch?v=ZVgjzvRcnqU&list=PLuISieMwVBpKNjDQBK2MU78tbU1XWkiPD),
  [DUG#8](https://www.youtube.com/watch?v=elEYzR-kVkw&list=PLuISieMwVBpLcYtLuM7rwooWeoH7I6tEF),
    [DUG#7](https://www.youtube.com/watch?v=raxY3JfMdp0&list=PLuISieMwVBpIJQpso6QICMUqqW5z8L1S2),
    [DUG#6](https://www.youtube.com/watch?v=Q8ILsTzoUjA&list=PLuISieMwVBpIQqHtHwYqypru50eg5nxoz),
    [DUG#5](https://www.youtube.com/watch?v=n7yv9T4VoFc&list=PLuISieMwVBpKBpfYlGZnDXOcqcQKXGXCX),
    [DUG#4](https://www.youtube.com/live/EN5rBAAOdOk?feature=shared&t=3973),
    [DUG#3](https://www.youtube.com/live/xHdlDmZVVkI?feature=shared&t=8700),
    [DUG#2](https://www.youtube.com/live/ZyctrnJNTPc?feature=shared&t=3395),
    [DUG#1](https://www.youtube.com/live/fUfjWyljKNs?feature=shared&t=795)

<center><img src="/img/dug_7/dasharo_gh_milestones.png" width="650"></center>

---

<center><img src="/img/dug_7/dasharo_naming_convention.png" width="1000"></center>

* In short Dasharo Pro Package (DPP)
* Dasharo (coreboot+UEFI) Pro Package for Desktop
* Dasharo (coreboot+Heads) Pro Package for Laptops
* Dasharo (coreboot+SeaBIOS) Enterprise Package for Network Appliance

More details about it can be found in previous editions of the talk e.g. [DUG #9](https://youtu.be/bhWMc06UEiU?feature=shared&t=118).

---

<center><img src="/img/dug_10/dasharo_releases_kpis.png" width="800"></center>

<!--

- Average: 18.8 releases/year, 5.2 releases/quarter for all releases, 94 releases total since Q3'21
- 36 DCR / 58 DSPR = 0.64 DCR/DSPR (+0.08)
- Considering year by year:
  - 2021: 10
  - 2022: 31
  - 2023: 16
  - 2024: 27
  - 2025: 10

- snippets:

```
grep "^## v" docs/variants -r | grep -E "2024-(09|1[0-2])"
grep "^## v" docs/variants -r | grep -E "2024-(09|1[0-2])"|grep -E "novacustom|protectli"|grep -v"heads"
```

-->

---

<center><img src="/img/dug_10/dasharo_per_segment.png" width="800"></center>

<!--

- we need historical and last quarter to see trends

-->

---

<center><img src="/img/dug_10/dasharo_roadmap_states.png" width="800"></center>

<!--

* We have a lot of changes to report.
* To some extent this diagram say, that likelihood of change is 40%.
* And there is 5% chance of platform removal.

-->
---

<center><img src="/img/dug_10/dcs_emu_roadmap_v0.10.png" width="800" style="margin-left:-36px; margin-top:-40px"></center>

- coreboot+SeaBIOS still waiting for its prime time, it is connected with
transition to OSFV, which we are very hesitant to do because it is quite a lot
of work and we have other projects
- [GitHub Milestone Link](https://github.com/Dasharo/dasharo-issues/milestone/59) to QEMU Q35 (coreboot+SeaBIOS) v0.9.0
- [GitHub Milestone Link](https://github.com/Dasharo/dasharo-issues/milestone/45) to QEMU Q35 (coreboot+UEFI) v0.3.0 which potentially could be scheduled this year.

<!--

- DUG#9:
  - (NEW) QEMU Q35 v0.3.0 planned for Q4'25
  - (NEW) QEMU Q35 v0.2.1 planned for Q2'25
  - (RELEASED) QEMU Q35 v0.2.1 planned for Q2'25
  - (CHANGED) QEMU Q35 v0.9.0 planned for Q2'25
    - release date changed: to Q3'25
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

## QEMU Q35 v0.2.1 SBOM

<br>

* Dasharo coreboot fork based on 25.03 revision b8e6b3eb
* Dasharo EDKII fork based on edk2-stable202502 revision e8cd1856
* Dasharo iPXE fork based on 2024.07 revision 63ed3e35

<br>

### What is inside?

<br>

* The Local APIC timer is now used instead of the HPET
* Boot time improvements - some measurements show 50% bump

<br>

### Known issues

<br>

* Measured Boot PCR values don't match the TPM measurement log ([#1354](https://github.com/Dasharo/dasharo-issues/issues/1354))

---

<center><img src="/img/dug_10/dcs_network_appliance_roadmap_v0.10_pt1.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

* We successfully released v24.08.00.01. More details later.
* `v24.12` and `v25.03` were replaced with `v25.06` release.
* Work on `v25.06.00.01` will happen in Q3'25.

<!--

- DUG#10
  - (RELEASED) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) v24.08.00.01 planned for Q4'24
  - (REMOVED) PC Engines apu2/3/4/6 Dasharo (coreboot+SeaBIOS) v25.03.00.01 planned for Q3'25
  - (REMOVED) PC Engines apu2/3/4/6 Dasharo (coreboot+SeaBIOS) v25.12.00.01 planned for Q2'25
  - (NEW) PC Engines apu2/3/4/6 Dasharo (coreboot+SeaBIOS) v25.06.00.01 planned for Q2'25
  - (CHANGED) PC Engines apu2/3/4/6 Dasharo (coreboot+UEFI) v0.9.1 planned for Q2'25
    - release date changed to Q3'25 (+1)
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

## PC Engines apu2/3/4/6 v24.08.00.01 SBOM

<br>

* coreboot based on 24.08 revision fadbc031
* Dasharo Patchqueue Initiative based on 24.08.00.01 revision d944bc39
* SeaBIOS based on rel-1.16.3.1 revision ac9eb800
* sortbootorder based on v24.08.00.01 revision 6188b4f4
* iPXE based on 2024.08 revision 301644ab
* AMD binary blobls remain the same.

<br>

### What is inside?

<br>

* Support for improved version of SeaBIOS rel-1.16.3.1
* sortbootorder update to v24.08.00.01
  - fixed various compilation issues to make it compatible with new compiler
  - QEMU support needed for validation under OSFV

<br>

<!--

### Known issues

<br>

* Remain the same as in last release - no regression, but also no fixes.

-->

---

<center><img src="/img/dug_10/dcs_network_appliance_roadmap_v0.10_pt2.png" width="850" style="margin-left:-36px; margin-top:-40px"></center>

* [TrenchBoot Support was released](https://blog.3mdeb.com/2025/2025-06-10-aem-uefi/)
* Unfortunately Dasharo release requires quite a lot of resources to be invested in validation, because of that we keep delaying this.
* Although we still discussing it because we see at least two issues with it:
  * [Intel TXT doesn't work on VP4670](https://github.com/Dasharo/dasharo-issues/issues/1269) - closed as invalid.
  * [Hangs during microcode update](https://github.com/Dasharo/dasharo-issues/issues/1256) - it was identified as kernel issue and needs testing.
* [Milestone link](https://github.com/Dasharo/dasharo-issues/milestone/52)

<!--

- DUG#10
  - (CHANGED) Protectli VP4670 planned for Q2'25
    - release date changed to Q3'25 (+1)
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

<center><img src="/img/dug_10/dcs_network_appliance_roadmap_v0.10_pt4.png" width="850" style="margin-left:-36px; margin-top:-40px"></center>

* We already started work on `v0.9.1`
* It would cover some interesting features we will look into on next slide.
* [Milestone link](https://github.com/Dasharo/dasharo-issues/milestone/64)

<!--

- DUG#10
  - (CHANGED) Hardkernel Odroid-H4 Dasharo(coreboot+UEFI) v0.9.1 planned for Q2'25
    - changed to second half of Q3'25 (+1)
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

<center><img src="/img/dug_10/odroid_v0.9.1.png" width="850"></center>

<!--

* Tests on Odroid-H4 Ultra.
* Provide ME disabling menu.
* Give ability to enable/disable bifurcation.
* Give ability to enable/disable IBECC.

-->

---

# Boot time performance improvements

<center><img src="/img/dug_10/odroid_v0.9.1_boot_time.png" width="750"></center>

<!--

So you can see, that we gain 20% in case of AMI fast boot and even 50%
otherwise.

-->

---

<center><img src="/img/dug_10/dcs_laptop_roadmap_v0.10.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

* Dasharo (coreboot+Heads) for NV4x v0.9.2 was released according to plan.
* This year we have no other plans for releasing Dasharo (coreboot+Heads). Next release will be planned for 2026 when time will come.

<!--

- DUG#10:
  - (RELEASED) NV4x Dasharo (coreboot+Heads) v0.9.2 planned for Q1'25
    - release date changed to Q2'25 (+1)
  - (REMOVED) NV4x Dasharo (coreboot+SeaBIOS) v1.7.2.x planned for Q1'25
    - release scope changed to coreboot+SeaBIOS
    - release date changed to Q1'25
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

## Novacustom NV4x 12th Gen v0.9.2 SBOM

<br>

* (UPDATED) Dasharo heads fork based on v0.2.1 revision da9b8ed9
* Intel Management Engine version v16.1.30.2307
* Intel Flash Descriptor version v1.0
* Intel Firmware Support Package version ADL-P C.1.75.10
* Intel microcode version ADL L0/R0 0x00000433 revision microcode-20230808
* (UPDATED) Intel microcode version RPL J0/Q0 0x00004121 revision microcode-20240514

---

## What is inside?

* Introduced Quiet Mode for reduced technical output in logs
* Added TPM extend operations logging while maintaining quiet mode
* Added support for GPG Admin/User PIN output grabbing for Nitrokey HOTP verification
* Integrated EFF Diceware short wordlist v2 for easier passphrase generation
* Introduced automatic Secrets App reset logic for Nitrokey 3
* Unified and enhanced passphrase generation logic in recovery shell
* Quiet Mode now logs all technical details to /tmp/debug.log instead of showing them in the console
* Improved TPM2 primary handle debugging and error handling
* Refactored the OEM Factory Reset process to clarify mode-based security implications
* Improved kexec boot configuration handling with enhanced security warnings
* Transitioned from ash shell to bash for improved scripting consistency
* Suppressed unnecessary grep errors for missing /etc/config.user
* Resolved logging inconsistencies when performing TPM resets
* Fixed Secure App PIN handling during Nitrokey 3 re-ownership

---

## What is inside?

<br>

* Corrected Diceware dictionary parsing and selection method for unbiased passphrase generation
* Eliminated redundant USB Security dongle detection messages
* Add missing TPM PIRQ route for NV41
* Integrate downcoring and hyper-threading options in Alder Lake SoC

<br>

### Fixes

<br>

* Power button doesn't work in Qubes
* Reproducibility problems with libcrypto and libtss2

<br>

### Known issues

<br>

* Hotkeys (e.g KEY_PLAYPAUSE) are not implemented in Qubes OS
* Existing Qubes installation is not found as bootable after transition back to EDK2

---

<center><img src="/img/dug_10/dcs_desktop_dell_roadmap_v0.10.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

* [TrenchBoot Support was released](https://blog.3mdeb.com/2025/2025-06-10-aem-uefi/)
* Exactly the same situation as with Protectli VP4670.
* No release plans at this point.

<!--

- DUG#10
  - no plans
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

<center><img src="/img/dug_10/dcs_desktop_msi_z690_roadmap_v0.10.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

* EOL for Dasharo support for MSI PRO Z690-A is 2026 EOY.
* This year there are two upcoming releases: DPP and DCR.
* Support will most likely end next year unless there will be enough renewal to
support next release, but since that hardware is no longer sold we are concern
it would not be the case.

<!--

- DUG#10
  - (NEW) MSI Z690-A v1.1.5 planned for Q3'25
  - (CHANGED) MSI Z690-A v1.2.0 planned for Q2'24
    - release date changed to Q3'25 (+1)
  - (NEW) MSI Z690-A v1.3.0 planned for Q3'25
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

<center><img src="/img/dug_10/dcs_desktop_msi_z790_roadmap_v0.10.png" width="900" style="margin-left:-36px; margin-top:-40px"></center>

* The same situation as with Z690-A.

<!--

- DUG#10
  - (NEW) MSI Z790-A v0.9.3 planned for Q3'25
  - (CHANGED) MSI Z790-A v1.0.0 planned for Q2'24
    - release date changed to Q3'25 (+1)
  - (NEW) MSI Z790-A v1.1.0 planned for Q3'25
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

<center><img src="/img/dug_10/dcs_desktop_msi_heads_roadmap_v0.10.png" width="800" style="margin-left:-36px; margin-top:-40px"></center>

* Unfortunately, we have no new plans.

<!--

- DUG#10
  - no new plans
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

# Changelog DUG#10

- (NEW) QEMU Q35 v0.3.0 planned for Q4'25
- (NEW) QEMU Q35 v0.2.1 planned for Q2'25
- (RELEASED) QEMU Q35 v0.2.1 planned for Q2'25
- (CHANGED) QEMU Q35 v0.9.0 planned for Q2'25
- (RELEASED) PC Engines apu2/3/4/6 Dasharo (creboot+SeaBIOS) v24.08.00.01 planned for Q4'24
- (REMOVED) PC Engines apu2/3/4/6 Dasharo (coreboot+SeaBIOS) v25.03.00.01 planned for Q3'25
- (REMOVED) PC Engines apu2/3/4/6 Dasharo (coreboot+SeaBIOS) v25.12.00.01 planned for Q2'25
- (NEW) PC Engines apu2/3/4/6 Dasharo (coreboot+SeaBIOS) v25.06.00.01 planned for Q2'25
- (CHANGED) PC Engines apu2/3/4/6 Dasharo (coreboot+UEFI) v0.9.1 planned for Q2'25
- (CHANGED) Protectli VP4670 planned for Q2'25
- (CHANGED) Hardkernel Odroid-H4 Dasharo(coreboot+UEFI) v0.9.1 planned for Q2'25
- (RELEASED) NV4x Dasharo (coreboot+Heads) v0.9.2 planned for Q1'25
- (REMOVED) NV4x Dasharo (coreboot+SeaBIOS) v1.7.2.x planned for Q1'25
- (NEW) MSI Z690-A v1.1.5 planned for Q3'25

---

# Changelog DUG#10

- (CHANGED) MSI Z690-A v1.2.0 planned for Q2'24
- (NEW) MSI Z690-A v1.3.0 planned for Q3'25
- (NEW) MSI Z790-A v0.9.3 planned for Q3'25
- (CHANGED) MSI Z790-A v1.0.0 planned for Q2'24
- (NEW) MSI Z790-A v1.1.0 planned for Q3'25

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
