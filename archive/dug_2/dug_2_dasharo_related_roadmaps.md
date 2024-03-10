<!--
SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>

SPDX-License-Identifier: CC-BY-SA-4.0
-->

class: center, middle, intro

# &#x1F386; Other Dasharo-related Projects Roadmaps &#x1F386;

.center[<img src="/remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">]

???

---

# Agenda

* Introduction to Dasharo Tools Suite (DTS)
* Overview of DTS v1.2.0
* Future Plans: DTS v2.0.0 and Beyond
* Unveiling the Dasharo Openness Score
* Exploring Dasharo Openness Score v0.1
* Upcoming Features: Dasharo Openness Score v0.2 and Beyond
* Q&A

???

---

# Dasharo Tools Suite a.k.a. DTS

.center.image-99[![](/img/dts-logo.jpg)]

* Set of tools and scripts running in minimal Linux environment
  - https://docs.dasharo.com/dasharo-tools-suite/overview
* **Vision**
	- **_Versatility_**: Swiss army knife for Dasharo users and the open-source
firmware community, providing a broad range of tools and scripts that simplify
firmware operations.
	- **_Simplified Deployment_**: Efficient firmware deployment, updates and recovery to
improve open-source firmware adoptability.
	- **_User-friendly Interface_**: Shiny, beautiful, and most importantly,
user-friendly interface for sensitive operions related to firmware.
	- **_Diagnostics and System Verification_**: Accessible trustworthiness
verification, assisting in platform security features provisioning and
attestation.

???

Dasharo Tools Suite (DTS) is envisioned as the go-to solution for a myriad of
firmware operations in the open-source firmware community. With its minimal
Linux environment running a diverse array of tools and scripts, it strives to
be a comprehensive firmware management suite that goes beyond just flashing,
providing reliable information about hardware, and enabling a seamless user
experience. It's the versatile swiss army knife every Dasharo user needs,
adding tangible value at every step of the firmware journey.

The DTS is not just a tool, but a key enabler in democratizing access to
reliable, open-source firmware management. As we plan to include QEMU images
with basic system tests, a more intuitive UI, and a zero-touch initial
deployment feature for a range of platforms, we aim to propel DTS as an
all-encompassing solution.

In our vision for DTS, we see it growing to become a trusted authority for
firmware provisioning, attestation, and trustworthiness verification. As a key
player in firmware validation environments, DTS will stand shoulder to shoulder
with UEFI Shell/Setup menus, Windows, and Ubuntu LTS. Our roadmap includes
continual enhancements and bug fixes, responding to the needs of the Dasharo
community.

Moreover, the DTS's design revolves around facilitating an efficient and
user-friendly experience. With a proposed DTS logo and improvements in the
Dasharo deployment procedure, DTS aims to foster an identity of reliability,
functionality, and ease of use.

DTS is positioned to be an integral part of the open-source firmware ecosystem,
a testament to our commitment to driving innovation and accessibility in
firmware management. By ensuring that the DTS is equipped with up-to-date tool
versions and provides a secure way of deployment 'as is', we are focused on
empowering users with control and convenience.

Through Dasharo Tools Suite, our vision is to build a world where open-source
firmware management is efficient, reliable, and user-friendly, putting the
power of firmware management into the hands of users and businesses alike.

---

# DTS v1.2.0

* Released: 2023-05-10 (initially planned for: March 2023)
* Changelog
	* Added Dasharo firmware update option, in DTS menu, for supported platforms.
	* Updated Dasharo firmware versions to latest released compatible with deploy
    script.
	* Disabled SSH server by default and added DTS menu option to start/stop SSH
    server.
	* Improved versions comparision so update from any rc or dev version of
    Dasharo firmware is possible.
	* Improved UX a little by saving flashrom logs to /var/local/flashrom.log.
	* Added IXGBE driver as a module, what enables DTS on Supermicro X11SSH.
	* Fixed CI workflows.

---

# DTS v1.2.0 menu

```shell
  DTS version v1.2.0

  1) Dasharo HCL report - dump hardware information from this device
  3) Restore firmware from Dasharo HCL report
  4) Load SE keys
  5) Update Dasharo firmware
  9) Shell
  10) Power off system
  11) Reboot system
```

* We keep working on improving the way we leverage HCL reports we received from
  community.
* Our goal is to make HCL Dasharo documentation part of our CI/CD pipeline.

---

# DTS v2.0.0

* ETA: Q3 2023
* [GitHub Milestone](https://github.com/Dasharo/dasharo-issues/milestone/5)
* Planned features
  - add QEMU image with sets of basic tests of the system
  - update UI; make it shiny, beautiful and what more important - user friendly
  - enable Dasharo zero-touch initial deployment on Dell Precision T1650
  - work on DTS logo
  - introduce nightly/develop builds

---

# DTS Roadmap

* Device authentication to improve Dasharo firmware update
  - client authentication mechanism working with updates
  - ETA: Q4 2023
  - [GitHub issue #55](https://github.com/Dasharo/dasharo-issues/issues/55)
* Expanding DTS root file system via NFS or other solution
  - adds posibility to load custom kernel modules
  - protects against endless growth of root file system size
  - ETA: Q4 2023
  - [GitHub issue #366](https://github.com/Dasharo/dasharo-issues/issues/366)
* DTS zero touch initial deployment for firmware `as is`
  - multistage approach to improve open-source firmware adoptability
  - ETA: Q1 2024
  - [GitHub issue #384](https://github.com/Dasharo/dasharo-issues/issues/384)
* DTS security features provisioning and attestation
  - improve the trustworthiness of computing device
  - ETA: Q2 2024
  - [GitHub issue #385](https://github.com/Dasharo/dasharo-issues/issues/385)

???

* all dealines shifted by 1Q
* Other ideas
	- automatic bug reporting from DTS

---

# Dasharo Openess Score

* Dasharo Openness Score is a tool designed to quantify the openness of 
firmware images, providing insights into the ratio of open-source to
closed-source components.
* Python, MIT licensed, https://github.com/Dasharo/Openness-Score
* **Vision**
    * **_Universal Standard_**: Establish Dasharo Openness Score as the benchmark for firmware openness.
    * **_Visual Clarity_**: Provide visually appealing and easily understandable results.
    * **_Integration and Engagement_**: Embed within CI/CD processes and regularly update in community platforms.
    * **_Certification Component_**: Make it a pivotal element of the Dasharo Certification Program.
    * **_Transparency in Open-Source_**: Create a clear measure of openness in the open-source firmware community.

???

* Uses lists of known components and their openness status, along with tools
like cbfstool or UEFIExtract to decompose and parse firmware images.

---

# Dasharo Openess Score v0.1

* Released: 2023-05-31
* Changelog
	* Supports both coreboot images and vendor UEFI images.
	* Automatically parses coreboot fmap layout to extract regions' properties.
	* Identifies fmap regions with CBFSes.
	* Parses CBFSes regions to extract file properties.
	* Checks for required utilities (cbfstool, UEFIExtract).
	* Categorizes components as open-source, closed-source, or data.
	* Calculates total size of open-source, closed-source, and data components per region, CBFS, or the whole image.
	* Extracts coreboot config to verify known open-source and closed-source components.
	* Creates pie charts illustrating the percentage share of each type of component in the image.
	* Exports numerical statistics to CSV files.

---

# Dasharo Openess Score v0.1

.center.image-45[![](/img/msi_ms7d25_v1.1.1_ddr4.rom_openness_chart.png) ![](/img/E7D25IMS.120_openness_chart.png)]

* Dasharo compatible with MSI PRO Z690-A vs vendor firmware.

---

# Dasharo Openess Score v0.1

.center.image-45[![](/img/heads-x230-maximized-v0.2.0-1554-g21b87ff.rom_openness_chart.png) ![](/img/asus_kgpe-d16_v0.4.0_16M_vboot_notpm.rom_openness_chart.png)]

* Heads compatible with x230 maximized vs Dasharo compatilbe with ASUS KGPE-D16 16M vboot no-TPM

---

# Dasharo Openess Score v0.2

* ETA: Q3 2023
* Planned features
  * **Improved Visualization**: Enhancing visual representation for
    user-friendliness.
  * **CI/CD Integration**: Including Openness Score script in CI/CD
    processes.
  * **Increased Visibility**: Openness Score updates in newsletters and
    Dasharo User's Guide.
  * **Binary Comparison**: Comparing Dasharo binary with reference binaries.
  * **Documentation Upgrade**: Improving methodology explanation in
    documentation.
  * **Versioning & Wide Application**: Implementing versioning and supporting
    multiple platforms.
  * **Advanced Parsing**: Utilizing ifdtool for improved image parsing.

---
class: center, middle, intro

# Q&A
