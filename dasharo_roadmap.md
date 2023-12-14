class: center, middle, intro

# Dasharo Roadmap

.center[<img src="/remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">]

---

# Dasharo Roadmap Disclaimer

.center.image-50[![](/img/tenor.gif)]

_Please note that the roadmap for the Dasharo Community Support Program is
subject to change and may not represent final release candidates or end of
support dates. This roadmap is intended to provide guidance and direction for
the program's development, but is not a guarantee of specific timelines or
outcomes. For more information on release candidates or release dates, please
contact the Dasharo Team directly._

???

---

# From OST2 to Dasharo Support Package

.center.image-85[![](/img/ost2_to_dasharo_packages.svg)]

???

* How to improve that information?
* Maybe focus more on OST2 and tracking deliverables for it.

---

# Dasharo Community Support Process

.center[
<img src="/img/dcs-process-v0.3.png" width="900px" style="margin-left:-75px">
]

* How we qualify platforms for Dasharo Community Support?
* Business goals alignment with 3mdeb.
* Synergy with other projects e.g. TrenchBoot.
* Above stages very roughly map to real work/tasks performed by team.

???

* DCP means executing and delivering test results according to specs defined in
  earlier stages.
* This process shows how flow look like for new platforms, already supported
  platforms typically get through Validation/Release cycle.
* TODO:
    - define publicly visible deliverables of each phase
    - document frameworks and tools on which given release will be based on

* We need more focused slides, saying precisely what we plan for given release,
  what features what will be validated etc.
* Dasharo development unification
* Customer stories?
* Dasharo Team release performance metrics
* Other 3mdeb roadmaps
    - EST
    - UEFI Secure Boot focus - OSFV
* Features matrix concept
* Inform about our priorities

---

# Dasharo Emulation Roadmap

.center[
<img src="/img/dcs_emu_roadmap_v0.4.png" width="900px" style="margin-left:-75px; margin-top:-40px">
]

* Dasharo OSFV release provided infrastructure for validation.
* QEMU tests were proven to work and it is just matter to run set of tests
  defined by test matrix, prepare release notes and send newsletter.
* We will do that in Q4'23.

???

- DUG#1: QEMU Q35 v0.1.0 planned for Q3'23
- DUG#2: (CHANGED) QEMU Q35 v0.1.0 planned for Q3'23
    - release date changed to Q4'23 (+1)
- DUG#3: QEMU Q35 v0.1.0 planned for Q4'23
- DUG#4: QEMU Q35 v0.1.0 release

Notes for expanding this part of the roadmap:
- new potential vendors/products: Intel Simics, AMD SimNow
- new potential release types to be supported for QEMU Q35 target
    - Dasharo (coreboot+UEFI)
    - Xen target (XCP-ng) although I'm not sure how how much firmware would be
    different, there is definitely stuff Xen-specific in OvmfPkg
- show milestone on github

---

# Dasharo Emulation Roadmap: Vision

- shift left firmware development
- new potential vendors/products: Intel Simics, AMD SimNow
- new potential release types to be supported for QEMU Q35 target
    - Dasharo (coreboot+UEFI)
    - Xen target (XCP-ng) although I'm not sure how how much firmware would be
    different, there is definitely stuff Xen-specific in OvmfPkg
- firmware will play role in Confidential VMs
- references:
    - [MSFT talk about CVM](https://youtu.be/2GxaBAS2_no)
    - MSFT: DCasv5 and ECasv5
    - [Edgeless Systems](https://www.edgeless.systems/blog/how-confidential-computing-and-ai-fit-together/)

---

# Dasharo Emulation Roadmap: Features

Following features can be fully used:

- Configurable boot order
- Configurable boot options
- [Custom boot menu keys](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/303-custom-boot-menu-key/)
- [UEFI shell](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/30P-uefi-shell/)
- [UEFI Secure Boot](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/)
- [TPM Support](https://docs.dasharo.com/unified-test-documentation/dasharo-security/200-tpm-support/)
- [Dasharo setup password](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20R-uefi-setup-password/)
- [Serial Port Configuration menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#serial-port-configuration)
- [iPXE network boot](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/315-network-boot/)
- [ESP partition scanning in look for grubx64.efi or shimx64.efi or Windows bootmgr](https://github.com/Dasharo/dasharo-issues/issues/94)

---

# Dasharo Emulation Roadmap: Features

Following features are visible in setup menu and can be used for testing the menus,
but have no actual backend hooked up:

- [PS/2 Controller enable/disable option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#chipset-configuration)
- [Watchdog configuration menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#chipset-configuration)
- [Early boot DMA protection menu option](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20L-early-boot-dma-protection/)
- [Intel ME disable support and menu options](https://docs.dasharo.com/unified-test-documentation/dasharo-security/20F-me-neuter/)
- [SED/OPAL disk password support](https://docs.dasharo.com/unified-test-documentation/dasharo-security/208-opal-disk-password-support/)
- [SATA disk password support](https://docs.dasharo.com/dasharo-menu-docs/device-manager/#hdd-security-configuration)
- SMM BIOS Write Protection support and enable/disable option
- [USB stack and mass storage enable/disable option](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#usb-configuration)
- [Firmware Update Mode feature](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- [One of the two fan profiles can now be selected in Setup Menu](https://docs.dasharo.com/unified/novacustom/fan-profiles/)
- [Setup menu option for switching between S0ix and S3 suspend mode](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#power-management-options)
- [Wi-Fi / Bluetooth module disable option in setup menu](https://docs.dasharo.com/dasharo-menu-docs/dasharo-system-features/#dasharo-security-options)
- ...

---

# Dasharo Network Appliance Roadmap

.center[
<img src="/img/dcs_network_appliance_roadmap_v0.4_pt1.png" width="900px" style="margin-left:-75px; margin-top:-40px">
]

* We will prioretize Dasharo(coreboot+UEFI) for PC Engines in Q1'24
* There should be two options for buying DES
* We would like to enable as many Dasharo features as possible, especially
  important for us are security features (measured boot, TPM2.0 support,
  verified boot, UEFI Secure Boot).

???

- DUG#3:
    - (NEW) PC Engines apu3 planned for Q4'23
- DUG#4:
    - (CHANGED) PC Engines apu3 planned for Q4'23
        - release date changed to Q1'23 (+1)
        - add support for apu2 and apu6
- DUG#3: (NEW) Protectli VP4670 planned for Q2'24

---

# Dasharo Network Appliance Roadmap

.center[
<img src="/img/dcs_network_appliance_roadmap_v0.4_pt2.png" width="900px" style="margin-left:-75px; margin-top:-40px">
]

* Does Dasharo(coreboot+SeaBIOS) with TrenchBoot/D-RTM make sense on 10th Gen?

???

* Legacy boot is deprecated by Intel since 11th Gen
* To make it work with Dasharo(coreboot+UEFI) we have to complete TB AEM P5

- DUG#3:
    - (CHANGED) Protectli VP4670 planned for Q2'24
        - release date changed to Q3'23 (+1)

---

# Dasharo Laptops Roadmap

.center[
<img src="/img/dcs_laptop_roadmap_v0.4.png" width="900px" style="margin-left:-75px; margin-top:-40px">
]

* Dasharo(coreboot+Heads) v0.9.0
* Shifted because of our engagement in NV4x/NS5x/7x 11th Gen v1.5.x and
  NV4x/NS5x/7x 12th Gen v1.7.x release series
* High priority release for Q1'24

???

- DUG#3:
    - (NEW) Novacustom NV4x Dasharo (coreboot+Heads) v0.9.0 planned for Q4'23
- DUG#4:
    - (CHANGED) Novacustom NV4x Dasharo (coreboot+Heads) v0.9.0 planned for Q4'23
        - release date changed to Q1'24 (+1)

---

# Dasharo Desktop Lenovo Roadmap

.center[
<img src="/img/dcs_desktop_lenovo_roadmap_v0.4.png" width="900px" style="margin-left:-75px; margin-top:-40px">
]

System is Intel Boot Guard Ready, verified boot disabled, ME not in
Manufacturing Mode - Dasharo Porting Ready.

???

- DUG#3:
    - (NEW) Lenovo M920Q planned for Q2'24
- DUG#4:
    - (CHANGED) Lenovo M920Q planned for Q2'24
        - release date changed to Q3'24 (+1)

- progress regarding Lenovo ThinkCenter M700: https://github.com/Dasharo/coreboot/pull/121

---

# Dasharo Desktop Dell Roadmap

.center[
<img src="/img/dcs_desktop_dell_roadmap_v0.4.png" width="900px" style="margin-left:-75px;margin-top:-40px">
]

???

- DUG#1
- Dell OptiPlex 7010/9010 v0.1.0 planned for Q2'23
- Dell T1650 v0.1.0 planned for Q3'23
- DUG#2
- (CHANGED) Dell OptiPlex 7010/9010 v0.1.0 planned for Q2'23
    - release date changed to Q4'23 (+2)
- (CHANGED) Dell T1650 v0.1.0 planned for Q3'23
- release date changed to Q1'24 (+2)
- DUG#3
- (CHANGED) Dell OptiPlex 7010/9010 v0.1.0 planned for Q4'23
    - release type changed to DES
- (CHANGED) Dell T1650 v0.1.0 planned for Q1'24
    - release type changed to DES
- DUG#4
- (CHANGED) Dell OptiPlex 7010/9010 v0.1.0 planned for Q4'23
    - release date changed to Q1'24 (+1)
- (CHANGED) Dell T1650 v0.1.0 planned for Q1'24
    - release date changed to Q3'24 (+2)

---

# Dasharo Desktop MSI Z690-A Roadmap

.center[
<img src="/img/dcs_desktop_msi_z690_roadmap_v0.4.png" width="850px" style="margin-left:-60px">
]

Community Release date changed because of PC Engines and NovaCustom.

???

- DUG#1
    - MSI Z690-A v1.1.2 planned for Q3'23
    - MSI Z690-A v1.2.0 planned for Q4'23
- DUG#2
    - MSI Z690-A v1.1.2 planned for Q3'23
    - (NEW) MSI Z690-A v1.1.3 release planned for Q4'23
    - (CHANGED) MSI Z690-A v1.2.0 planned for Q4'23
        - release date changed to Q1'24 (+1)
- DUG#3
    - (RELEASED) MSI Z690-A v1.1.2 planned for Q3'23
    - MSI Z690-A v1.1.3 release planned for Q4'23
    - MSI Z690-A v1.2.0 planned for Q1'24
- DUG#4
    - (CHANGED) MSI Z690-A v1.2.0 planned for Q1'24
        - release date changed to Q2'24 (+1)

---

# Dasharo Desktop MSI Z790-P Roadmap

.center[
<img src="/img/dcs_desktop_msi_z790_roadmap_v0.4.png" width="850px" style="margin-left:-60px">
]

Community Release date changed because of PC Engines and NovaCustom.

???

- DUG#1
    - MSI Z790-A v1.0.0 planned for Q1'24
- DUG#2
    - (NEW) MSI Z790-A v0.9.0 planned for Q3'23
    - (NEW) MSI Z790-A v0.9.1 planned for Q4'23
    - MSI Z790-A v1.0.0 planned for Q1'24
- DUG#3
    - (RELEASED) MSI Z790-A v0.9.0 planned for Q3'23
    - MSI Z790-A v0.9.1 planned for Q4'23
    - MSI Z790-A v1.0.0 planned for Q1'24
- DUG#4
    - (CHANGED) MSI Z790-A v1.0.0 planned for Q1'24
        - release date changed to Q2'24 (+1)

---

# Dasharo Desktop MSI Roadmap

.center[
<img src="/img/dcs_desktop_msi_z790_heads_roadmap_v0.4.png" width="850px" style="margin-left:-60px">
]

* We have to figure out better naming scheme.
* We plan to deliver this solution one quarter earlier.
* Status from call with ThePlexus.

???

- DUG#3
    - (NEW) MSI Z790-A Dasharo (coreboot+Heads) v1.0.1 planned for Q2'24
- DUG#4
    - (CHANGED) MSI Z790-A Dasharo (coreboot+Heads) v0.9.0 planned for Q1'24
        - release date changed to Q1'24 (-1)
        - version changed to v0.9.0

---

# Dasharo Desktop ASRock Roadmap

.center[
<img src="/img/dcs_desktop_asrock_roadmap_v0.4.png" width="900px" style="margin-left:-75px">
]

* Dasharo Supporting Partner discussion.
* Potential paths: AMD FSP or AGESA.

???

* Shop, DRS etc.
* Discussion with hanetzer about possible avenues
* Access to AMD FSP by 3mdeb - very inlikely
* 3mdeb delivering AGESA for AM4/AM5 possible when support for hardware will be
  available, but wrapping AGESA code is huge headach in light of OpenSIL

---

# Dasharo Workstation Roadmap

.center[
<img src="/img/dcs_workstation_roadmap_v0.4.png" width="840px" style="margin-left:-40px">
]

* There is almost no hope for KGPE-D16
* New milestone for Dasharo(coreboot+Heads) v0.8.0 for Talos II

???

- DUG#1
    - ASUS KGPE-D16 v0.5.0 planned for Q3'23
    - RCS Talos II v0.7.0 planned for Q3'23
- DUG#2
    - (CHANGED) ASUS KGPE-D16 v0.5.0 planned for Q3'23
        - release date changed to Q1'24 (+2)
    - RCS Talos II v0.7.0 planned for Q3'23
- DUG#3
    - (CHANGED) ASUS KGPE-D16 v0.5.0 planned for Q1'24
        - release type changed to DES
        - release date changed to Q2'24 (+1)
    - (RELEASED) RCS Talos II v0.7.0 planned for Q3'23
- DUG#4:
    - no response from Immunefi
    - we have to cancel KGPE-D16 from roadmap at some point
    - (CHANGED) ASUS KGPE-D16 v0.5.0 planned for Q2'24
        - release date changed to Q3'24 (+1)
    - (NEW) RCS Talos II v0.8.0 planned for Q1'24
        - depends on agreeing on Heads commit on which we should inteagrate things,
      we already one month blocked because lack of decision

---

# Dasharo Server Roadmap

.center[
<img src="/img/dcs_server_roadmap_v0.4.png" width="900px" style="margin-left:-75px">
]

* Low priority, but there is some market interest.

???

- DUG#1
    - Supermicro X11SSH-TF v0.1.0 planned for Q4'23
- DUG#2
    - (CHANGED) Supermicro X11SSH-TF v0.1.0 planned for Q4'23
        - release date changed to Q1'24 (+1)
- DUG#3
    - (CHANGED) Supermicro X11SSH-TF v0.1.0 planned for Q1'24
        - release date changed to Q2'24 (+1)
- DUG#4
    - (CHANGED) Supermicro X11SSH-TF v0.1.0 planned for Q2'24
        - release type changed to DES

---
class: center, middle, intro

# Q&A

---
class: center, middle, intro

# CHANGELOG

---

# Changelog DUG#1

- (NEW) QEMU Q35 v0.1.0 planned for Q3'23
- (NEW) Dell OptiPlex 7010/9010 v0.1.0 planned for Q2'23
- (NEW) Dell T1650 v0.1.0 planned for Q3'23
- (NEW) MSI Z690-A v1.1.2 planned for Q3'23
- (NEW) MSI Z690-A v1.2.0 planned for Q4'23
- (NEW) MSI Z790-A v1.0.0 planned for Q1'24
- (NEW) ASUS KGPE-D16 v0.5.0 planned for Q3'23
- (NEW) RCS Talos II v0.7.0 planned for Q3'23
- (NEW) Supermicro X11SSH-TF v0.1.0 planned for Q4'23
- Summary: 9 new

---

# Changelog DUG#2

- (CHANGED) QEMU Q35 v0.1.0 planned for Q3'23
    - release date changed to Q4'23 (+1)
- (CHANGED) Dell OptiPlex 7010/9010 v0.1.0 planned for Q2'23
    - release date changed to Q4'23 (+2)
- (CHANGED) Dell T1650 v0.1.0 planned for Q3'23
    - release date changed to Q1'24 (+2)
- MSI Z690-A v1.1.2 planned for Q3'23
- (NEW) MSI Z690-A v1.1.3 release planned for Q4'23
- (CHANGED) MSI Z690-A v1.2.0 planned for Q4'23
    - release date changed to Q1'24 (+1)
- (NEW) MSI Z790-A v0.9.0 planned for Q3'23
- (NEW) MSI Z790-A v0.9.1 planned for Q4'23
- MSI Z790-A v1.0.0 planned for Q1'24
- (CHANGED) ASUS KGPE-D16 v0.5.0 planned for Q3'23
    - release date changed to Q1'24 (+2)

---

# Changelog DUG#2

- RCS Talos II v0.7.0 planned for Q3'23
- (CHANGED) Supermicro X11SSH-TF v0.1.0 planned for Q4'23
    - release date changed to Q1'24 (+1)
- Summary: 3 new, 6 changed, 3 on track (total: 12)

---

# Changelog DUG#3

- QEMU Q35 v0.1.0 planned for Q4'23
- (NEW) PC Engines apu3 v0.9.0 planned for Q4'23
- (NEW) Protectli VP4670 v0.9.0 planned for Q2'24
- (NEW) Novacustom NV4x Dasharo (coreboot+Heads) v0.9.0 planned for Q2'24
- (NEW) Lenovo M920Q v0.9.0 planned for Q2'24
- (CHANGED) Dell OptiPlex 7010/9010 v0.1.0 planned for Q4'23
    - release type changed to DES
- (CHANGED) Dell T1650 v0.1.0 planned for Q1'24
    - release type changed to DES
- (RELEASED) MSI Z690-A v1.1.2 planned for Q3'23
- MSI Z690-A v1.1.3 release planned for Q4'23
- MSI Z690-A v1.2.0 planned for Q1'24
- (RELEASED) MSI Z790-A v0.9.0 planned for Q3'23

---

# Changelog DUG#3

- MSI Z790-A v0.9.1 planned for Q4'23
- MSI Z790-A v1.0.0 planned for Q1'24
- (NEW) MSI Z790-A Dasharo (coreboot+Heads) v1.0.1 planned for Q2'24
- (CHANGED) ASUS KGPE-D16 v0.5.0 planned for Q1'24
    - release type changed to DES
    - release date changed to Q2'24 (+1)
- (RELEASED) RCS Talos II v0.7.0 planned for Q3'23
- (CHANGED) Supermicro X11SSH-TF v0.1.0 planned for Q1'24
    - release date changed to Q2'24 (+1)
- Summary: 5 new, 4 changed, 5 on track, 3 released (total: 17)
