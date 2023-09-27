class: center, middle, intro

# &#x1F386; Dasharo Openess Score Status &#x1F386;

.center[<img src="/remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">]

???

---

# Agenda

* Short Introduction to Dasharo Openness Score (DTS)
* Exploring Dasharo Openness Score v0.1
* Upcoming Features: Dasharo Openness Score v0.2 and Beyond
* Q&A

???

---

# Dasharo Openess Score

* Dasharo Openness Score is a tool designed to quantify the openness of 
firmware images, providing insights into the ratio of open-source to
closed-source components.
* Python, MIT licensed, https://github.com/Dasharo/Openness-Score
* DRY: https://bit.ly/openness-score
* Since last DUG we made some slight progress and we would like to treat this
  presentation as opportunity to provide more details about project status as
  well some knowledge about methodology.
* Unfortunately no new releases, but ...

---

# Documentation Released
 
.center[https://dasharo.github.io/Openness-Score/]

.center.image-90[![](/img/dos_docs.png)]

* Documentation is in Sphinx at this point, but we will migrate mkdocs.

---

# Methodology UEFI

.center.image-25[![](/img/dos_methodology_uefi.svg)]

* CBFS classification is even more complex.

???

@startuml
!define Color1 #38d430
!define Color2 #272727
!define Color3 #f5f5f5

skinparam DefaultFontSize 16

skinparam partition {
    BackgroundColor Color3
    BorderColor Color2
}

skinparam activity {
    BackgroundColor Color1
    BorderColor Color2
}

start

:Identify Regions and Save Properties;
:Separate and Classify Regions;
:Extract and Identify UEFI FV;
:Calculate Metrics for UEFI FV;
:    Classify Paddings
(empty and non-empty);
:Summarize Region and UEFI FV Sizes
    (empty, data and closed-source);
:Verify Total Size;
if (Mismatch?) then (yes)
  :Adjust Data and Report Error;
else (no)
endif

:Export Data;
stop
@enduml

---

# Integration for NovaCustom 

* Back in the days we provided Dasharo Openess Score (pre-v0.1) for NV4x 11th Gen v0.5.0
  (2021/11/19).

.center.image-30[![](/img/nvc_dos_nv4x_v0.5.0.png) ![](/img/nvc_dos_nv4x_v0.5.0_2.png) ![](/img/nvc_dos_nv4x_v0.5.0_3.png)]

* Starting from upcoming:
  - NV4x, NS5x/7x ADL v1.7.0
  - NV4x, NS5x/7x TGL v1.5.0
* All Novacustom releases will contain Dasharo Openess Score v0.1

---

# Release Newsletter integration

.center.image-70[![](/img/dos_newsletterv2.png)]

* Above notes will be added to newsletters announcing releases, which include
  Dasharo Opness Score.

---

# Dasharo Universe

.center.image-45[![](/img/nvc_dos.jpg)]

---

# Example based on MSI PRO Z690-A

.center.image-50[![](/img/openness_msi_full_code.jpg) ![](/img/openness_msi_full_code_ami.jpg)]

---

# Example based on MSI PRO Z690-A

.center.image-50[![](/img/openness_msi_bios_full.jpg) ![](/img/openness_msi_bios_full_ami.jpg)]

---

# Dasharo Openess Score v0.1 integration

* ETA: Q3 2023 (v0.1 integration)
  * No code changes.
  * Integration in Dasharo Release infrastructure.
  * ~~**Increased Visibility**: Openness Score updates in newsletters and
    Dasharo User's Guide.~~
  * ~~**Documentation Upgrade**: Improving methodology explanation in
    documentation.~~

---

# Dasharo Openess Score v0.2
* ETA: Q4 2023
* Planned features
  * **CI/CD Integration**: Including Openness Score script in CI/CD
    processes.
  * **Improved Visualization**: Enhancing visual representation for
    user-friendliness.
  * **Binary Comparison**: Comparing Dasharo binary with reference binaries.
  * **Versioning & Wide Application**: Implementing versioning and supporting
    multiple platforms.
  * **Advanced Parsing**: Utilizing ifdtool for improved image parsing.
* Planned bug fixes:
  * [GitHub issue #461](https://github.com/Dasharo/dasharo-issues/issues/461) -
    Check for ME presence in coreboot images with ifdtool if flashmap does not
    indicate it
  * [GitHub issue #451](https://github.com/Dasharo/dasharo-issues/issues/451) -
    Migrate Openness Score documentation from Sphinx to mkdocs

---
class: center, middle, intro

# Q&A
