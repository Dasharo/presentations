class: center, middle, intro

# Zarhus: Trustworthy Embedded Linux Distro

### &#x1F44B; Dasharo User Group #5 &#x1F389;

.center[<img src="/remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">]

???

<!--
SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>

SPDX-License-Identifier: CC-BY-SA-4.0
-->

- Hardware experience
  - Silicon Vendors
    - NXP
    - Rockchip
    - Allwiner
    - Amlogic
  - SBC
    - Gateworks
- UEFI Secure Boot
- Measured Boot
- Secure/Verified Boot
- Encrypted rootfs
- Read-only rootfs
- SBOM
- OpenWRT
- Buildroot
- WiFi Access Point
- FIDO Device Onboarding (FDO)
- Custom application integration
- CI/CD integration
- Validation
- Secure OTA
- Boot time optimization

---

# What is Zarhus?

.center.image-35[![](/img/zarhus_logo.png)]

_**Zarhus** is an embedded **Linux** distribution based on **Yocto**, developed by
3mdeb. It is designed for the community and customers who want platform
security based on an immutable **Root of Trust** tied to their own keys and to
run target applications leveraging the **Chain of Trust** of their choice._

---

# What does it mean in practice?

.center.image-99[![](/img/zarhus_in_ecosystem.png)]

???

- picture is simplified

---

# Relation to Dasharo

.center.image-90[![](/img/zarhus-dasharo-relation.png)]

---

# Value Prop

.center.image-99[![](/img/zarhus_value_prop.svg)]

---

# Supported Hardware

.center.image-99[![](/img/zarhus_supported_hw.svg)]

---

# How community can use it?

* Prerequisites:
  * At least basic Yocto understanding is required
  * Understanding of kas (setup tool for bitbake based projects) is recommended
* Keep checking progress on:
  - https://docs.zarhus.com/
  - https://github.com/zarhus
    - we create roadmap under `zarhus-issues` and will track our progress there
    - we will inform you during DUGs
* Currently most repositories are still in 3mdeb organization (32) in private gitlab (37)
  - https://github.com/3mdeb - search for `meta` keyword
  - most of the code is MIT-licensed
* In total it is 87k lines of code of 17k we already contributed upstream.
* Meanwhile for direct business needs we designed, developed and delivered over
  400k lines of code.
  - With Zarhus we want to change this proportions.

---

# Zarhus Team contribution

### 2019

* During first Qubes OS Summit Maciej (`@macpijan`) [proposed Yocto as build
  system for
  Qubes](https://3mdeb.com/events/#_qubes-os-and-3mdeb-minisummit-2019), we
  have very nice discussion with Marek (`@marmarek`) then.
* Piotr (`@pietrushnic`) present at PSEC [Yocto built TrenchBoot demo on PC
  Engines](https://3mdeb.com/events/#_platform-security-summit), slightly
  improved version is show the same year at ELCE.

### 2020

* During TPM.dev Piotr (`@pietrushnic`) present improved architecture of
  [Yocto-based TrenchBoot and safeboot
  stack](https://3mdeb.com/events/#_tpmdev-2020-miniconf).
* Norbert (`@nkaminski`) and Tomek (`@tomzy_0`)  present at our first Yocto
  Summit talking about [various management tools and how to create wic
  plugin](https://3mdeb.com/events/#_yocto-project-summit-2020).

---

# Zarhus Team contribution

### 2021

* During FOSDEM Maciej (`@macpijan`) first time presented [overview of Secure
  Boot in the ARM
  SoCs](https://archive.fosdem.org/2021/schedule/event/tee_arm_secboot/)
* Out second Yocto Summit borough Maciej (`@macpijan`) talk about [PPC64
  architecture support](https://3mdeb.com/events/#_yocto-project-summit-2021)
  and Tomek (`@tomzy_0`) [demo of OpenWRT built with
  Yocto](https://3mdeb.com/events/#_yocto-project-summit-2021)
* Durign Xen Developer and Design Summit Piotr (`@pietrushnic`) presented
  approach to [deliver modern WiFi support for BSD-based Firewall
  VM](https://3mdeb.com/events/#_xen-developer-design-summit)
* There was also another Yocto Summit that year where Tomek (`@tomzy_0`) show
  [how to deal with SELinux in
  Yocto](https://3mdeb.com/events/#_yocto-project-virtual-summit)

### 2022

* On Yocto Summit Tomek (`@tomzy_0`) presented [how to enable UEFI Secure Boot
  on x86 with Yocto](https://3mdeb.com/events/#_yocto-project-summit) together
  with Cezary who show [how to enable new platform (Nezha Allwinner D1) in
  Yocto meta-riscv](https://www.youtube.com/watch?v=QdBG6HUeE6w)

---

# Zarhus Team contribution

### 2023

* At FOSDEM Tomek (`@tomzy_0`) presented update version of [Secure Boot status
  in ARM SoCs](https://3mdeb.com/events/#_fosdem-2023)
* At Yocto Project Dev Days Maciej (`@macpijan`) and Tomek (`@tomzy_0`)
  presented two topics, [first related to maintenance and second to building
  OpenBMC](https://3mdeb.com/events/#_yocto-project-at-embedded-open-source-summit)
* During Yocto Project Summit Tomek (`@tomzy_0`) presented another approach to
  [UEFI Secure
  Boot](https://summit.yoctoproject.org/yocto-project-summit-2023-11/speaker/MCUXWY/)
  and Tymek (`@tym21k`) debut with [FIDO Device Onbarding and Yocto
  story](https://summit.yoctoproject.org/yocto-project-summit-2023-11/speaker/AQZWHX/)

---

# Business value delivery

.center.image-90[![](/img/dug_5_zarhus_value_delivery.svg)]

---

# How to buy it?

* Indirectly through Dasharo Entry Subscription or obtaining RTE (limited to
  product needs):
  - https://shop.3mdeb.com/product-category/dasharo-entry-subscription/
  - https://shop.3mdeb.com/shop/open-source-hardware/rte/
* Through productised services: https://shop.3mdeb.com/product-category/services/
  - Secure Boot integration for NXP and Rockchip
  - TPM and UEFI Secure Boot Assessment
  - TXE Secure Boot Assessment
  - Intel Boot Guard Assessment
  - U-Boot Hardening
  - Boot Time Optimization Report
  - Support Package and Workshop
  - and many more
* Through Training:
  - https://paceenterprisetraining.com
* Or just contact us: https://3mdeb.com/contact/#form

---

class: center, middle, intro

# Q&A
