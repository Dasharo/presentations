class: center, middle, intro

# &#x1F386; Dasharo Open Source Firmware Validation &#x1F386;

.center[<img src="/remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">]

???

---

# TBD: Agenda

* Introduction to Dasharo Open Source Firmware Validation (OSFV)
* Exploring OSFV v0.2
* Recent improvements
* Getting started with OSFV
* Upcoming Features: OSFV v0.3 and Beyond
* Q&A

???

---

# Current state

* No release since the last presentation
* Still quite intense development in the `develop` branch
  - all improvements target this branch now
  - if you want to experiment, this should be a starting point
  - we are aiming for something "stable enough" to merge into `main` and
    release v0.3.0 version

---

# Contribution stats?? TBD

---

# Recent improvements

* "Recent" - since the last presentation (~6m)
* Notable changes
* New platforms
* New tests
* Continuation of refactoring activities
* Multiple fixes and minor improvements

---

# Recent improvements

### **Notable changes - configs rework**

* Reduced code duplication across platforms, added comomon includes

.center.image-90[![](/img/platform-configs-protectli.png)]

---

# Recent improvements

### **Notable changes - documentation**

* Split documentation under docs directory
  - how to add new platform
  - contributing guidelines
  - workflow with QEMU
  - platform-specific quirks

---

# Recent improvements

### **Notable changes - documentation**

.center.image-90[![](/img/osfv_adding_new_platform.png)]

---

# Recent improvements

### **Notable changes - switch Sonoff API**

* Reflashed firmware on Sonoffs in the lab to a more stable one
  - https://tasmota.github.io/docs/devices/Sonoff-S26-Smart-Socket/

.center.image-30[![](/img/osfv_sonoff_r26.png)]

---

# Recent improvements

### **Notable changes - new tests**

* Checking for unexpected errors in logs (dmesg)
* Watchdog suite
* APU-specific features
* Suite for DCU tool
* Correctness of CPU / memory information in the main menu

---

# Recent improvements

### **Notable changes - new platforms**

* New platforms
  - Protectli V1000 series (V1210, V1410, V1610)
  - Protectli VP6000 series (VP6650, VP6670)
  - PC Engines APU2-6
  - Minnowboard Turbot
  - NovaCustom MTL models

---

# In progress - current priorities

### **DCU integration**

* Alternative interface for changing firmware settings
* Instead of manual steps via PiKVM / serial, we can modify SMMSTORE variables directly
* More details in DCU presentation

---

# In progress - current priorities

### **Generate documentation from test code**

* PR: https://github.com/Dasharo/open-source-firmware-validation/pull/293/files
* To be hosted on github pages for starters (not hosted yet)

.center.image-80[![](/img/osfv_keywords_docuementation.png)]

---

# In progress - current priorities

### **osfv_cli integration**

* Integrate low-level hardware operations into Python libraries
* Reuse the same libraries by test framework and CLI tool

.center.image-40[![](/img/osfv_cli_arch.png)]

???

* Avoid doing that in RF, it is often tedious

---

# osfv_cli - motivation

.center.image-80[![](/img/osfv_cli_before.png)]

---

# osfv_cli - motivation

.center.image-80[![](/img/osfv_cli_after.png)]

---

# osfv_cli - developer usage scenario

.code-13px[```bash

# Reserve platform

osfv_cli snipeit check_out --rte_ip $RTE_IP

# Read backup firmware

osfv_cli rte --rte_ip $RTE_IP flash read --rom backup.rom

# Flash new firmware

osfv_cli rte --rte_ip $RTE_IP flash read --rom backup.rom

# Apply power to platform

osfv_cli rte --rte_ip $RTE_IP rel set high

# Get logs from serial

osfv_cli rte --rte_ip $RTE_IP serial

# Reset platform

osfv_cli rte --rte_ip $RTE_IP pwr reset
```]

---

# Next steps

* Stabilize the environment for the v0.3.0 release
  - finalize current priority tasks
  - full regression on selected supported platforms
    + NovaCustom
    + Protectli
    + PC Engines
    + QEMU
    + MSI

---
class: center, middle, intro

# Q&A
