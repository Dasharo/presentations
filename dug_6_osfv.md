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

* DCU integration
  - alternative interface for changing firmware settings
  - instead of manual steps via PiKVM / serial, we can modify SMMSTORE variables directly
  - more details in DCU presentation
* Generate documentation from test code
  - host on github pages for starters
* osfv_cli integration
  - integrate low-level hardware operations into Python libraries
  - avoid doing that in RF, it is often tedious

---

# osfv_cli

* https://github.com/Dasharo/osfv-scripts/tree/main/osfv_cli

.center.image-50[![](/img/osfv_cli_arch.png)]

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
