---
layout: cover
background: /intro.png
class: text-center

---
## &#x1F44B; Dasharo User Group #8 &#x1F389;

### Dasharo Open Source Firmware Validation Status

<center><img src="/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px"></center>

<!--

Date of previous data snapshot: 09/09/2024
Date of data snapshot: 10/12/2024

-->

---

# Agenda

* Introduction to Dasharo Open Source Firmware Validation (OSFV)
* Current state
* Recent improvements
* Next steps
* Q&A

---
layout: cover
background: /intro.png
class: text-center

---

# Introduction to Dasharo OSFV

---

# <center>Introduction to Dasharo OSFV</center>

* Main purpose
  - validation of (open-source) firmware
    + can be used for any firmware, really
  - mainly Dasharo with UEFI payload right now
* Using Robot Framework as a base

<center><img src="/common/Robot-framework-logo.png" width="200"></center>

---

# <center>Introduction to Dasharo OSFV</center>

* Use cases
  - testing Dasharo firmware releases
  - test-driven bug fixing (and adding new features)
  - regression testing
    + after introducing new features
    + after major changes (update base from upstream project)
  - validation of Dasharo-related tools (Dasharo Tools Suite, Dasharo
    Configuration Utility)
    + where possible, in QEMU

---

# <center>Typical setup</center>

- Power control (power supply, power button)
- Serial console over telnet
- Move through firmware menus to switch certain options
- Check the result
  - In firmware
  - In OS
    + Dasharo Tools Suite - reference distribution for testing purposes
    + The latest Ubuntu LTS
    + The latest Windows 11
    + QubesOS for some tests

---

# <center>One test - step by step</center>

<center><img src="/dug_8/dasharo_main_page.jpeg" width="500"></center>

---

# <center>One test - step by step</center>

<center><img src="/dug_8/dasharo_features.jpeg" width="500"></center>

---

# <center>One test - step by step</center>

<center><img src="/dug_8/dasharo_sec_opts.jpeg" width="500"></center>

---

# <center>One test - step by step</center>

```python
    Power On
    ${setup_menu}=    Enter Setup Menu Tianocore And Return Construction
    ${dasharo_menu}=    Enter Dasharo System Features    ${setup_menu}
    ${network_menu}=    Enter Dasharo Submenu    ${dasharo_menu}    Dasharo Security Options
    Set Option State    ${network_menu}    Enable SMM BIOS write    ${TRUE}
    Save Changes And Reset
    Boot System Or From Connected Disk    ubuntu
    Login To Linux
    Switch To Root User
    Get Flashrom From Cloud
    ${out_flashrom}=    Execute Command In Terminal    flashrom -p internal
    Should Contain    ${out_flashrom}    SMM protection is enabled
```

---
layout: cover
background: /intro.png
class: text-center

---

# Current state

---

# <center>Current state</center>

* 😞 No release 😞
* We are still failing to define (and reach) criteria for tagged release of test environment
* Right now it worked more like a `rolling release` in `develop` branch
* We wanted to merge `develop` into `main` once we are "ready" but it never happens
* It is confusing to see the default branch (`main`) with very little updates
  and outdated information
* Merged `develop` branch into `main` branch yesterday
  - we might use it as the default target branch until we figure it out

<center><img src="/dug_8/osfv_branches_meme.jpg" width="400"></center>

---

# <center>Statistics - Pull Requests</center>

<center><img src="/dug_8/dasharo_prs_osfv.png" width="700"></center>

---

# <center>Statistics - Pull Requests</center>

<center><img src="/dug_8/dasharo_prs_osfv_cli.png" width="700"></center>

---

# <center>Statistics - tests</center>

<center><img src="/dug_8/osfv_tests_count.png" width="700"></center>

---
layout: cover
background: /intro.png
class: text-center

---

# Recent improvements

---

# <center>New tests</center>

* Extended CPU suite (P/E cores, HT)
* Extended DCU tests
* Introduced more thorough testing of DTS in QEMU
* Suite for TrenchBoot development
  - Booting Linux and Xen from meta-trenchboot
* Suite for Capsule Updates
* More

---

# <center>New platforms</center>

* Protectli VP2430
* Protectli VP3210, VP3230
* Odroid H4
* Bring back Dell Optiplex - both UEFI and SeaBIOS

<center><img src="/dug_8/odroid_h4.jpg" width="350"></center>

---

# <center>osfv_cli integration</center>

* Integrate low-level hardware operations into Python libraries
* Reuse the same libraries by test framework and CLI tool

<center><img src="/dug_8/osfv_cli_after.png" width="550"></center>

---

# <center>dcu integration</center>

* Alternative interface for changing fw settings*
* Instead of manual steps, we can modify SMMSTORE variables directly

<center><img src="/dug_8/osfv_dcu_integration.png" width="400"></center>

---

# <center>Keywords documentation</center>

<center><img src="/dug_8/osfv_keywords_docuementation.png" width="700"></center>

https://dasharo.github.io/open-source-firmware-validation/

---

# <center>Next steps</center>

* Finalize SeaBIOS support
* Need to focus more on repeatability and reliability than adding new tests/features
  - resolve Power On reliability: https://github.com/Dasharo/open-source-firmware-validation/issues/607
  - identify other areas generating problems, implement stress testing of these areas
  - add some HW into CI loop next to the QEMU tests
    + serial + relay - one of the Protectli boards
    + serial + PiKVM + Sonoff - one of the MSI boards

---

# <center>Questions?</center>

<!--

Comment to satisfy pre-commit

-->
