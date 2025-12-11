---
theme: /slidev-template/theme
layout: cover
background: /intro.png
class: text-center

---
## Dasharo Open Source Firmware Validation Status

<center><img src="../../img/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px"></center>

---

# <center> Agenda </center>

* Short introduction to OSFV
* Statistics
* Significant changes: Implemented
* Significant changes: WiP & future plans
* Q&A

---
layout: cover
background: /intro.png
class: text-center
---

# <center> Introduction to Open Source Firmware Validation </center>

---

# <center> Introduction to Open Source Firmware Validation </center>

- Open Source Validation of Open Source Firmware
- Based on Robot Framework 7.3
- Used to detect regression in next dasharo release via series of automated test cases
- Semi-manual (interactive!) test cases using Dialogs library
<img src="../../img/happy.png" width="360px" style="margin-top:8px;margin-bottom:8px"/>
- Tree-like platform configuration structure
- Several DUT control & connectivity options

---

# <center> Introduction to Open Source Firmware Validation </center>

- Dasharo test modules:
  - dasharo-compatibility
  - dasharo-performance
  - dasharo-stability
  - dasharo-security

- Other test modules:
  - utils
  - dts
  - self-tests
  - (...)

---

# <center> Introduction to Open Source Firmware Validation </center>

- Log files kept in directory tree:
  - ./logs/platform-config/dir-prefix_platform-config_time-stamp
  - DIR_PREFIX variable
  - .xml - for further processing
  - 2x .html - human-readable results
  - .log - what actually happens?

<center>
<img src="../../img/robot_log.png" width="360px" style="margin-top:32px"/>
</center>

---
layout: cover
background: /intro.png
class: text-center
---

# <center> OSFV Statistics </center>

---

# <center> PR stats </center>
### <center> open-source-firmware-validation </center>
#### <center> Total </center>

<center>
<img src="../../img/dug_12/osfv_status/dasharo_prs_osfv_total.png" width=600/>
</center>

---

# <center> PR stats </center>
### <center> open-source-firmware-validation </center>
#### <center> Difference </center>

<center>
<img src="../../img/dug_12/osfv_status/dasharo_prs_osfv_diff.png" width=600/>
</center>

---

# <center> Test modules stats </center>
#### <center> Total test cases </center>

<center>

<img src="../../img/dug_12/osfv_status/tests_final.png" width=600/>
</center>

---

# <center> Test modules stats </center>
#### <center> Difference </center>

<center>
<img src="../../img/dug_12/osfv_status/tests_against.png" width=600/>
</center>

---
layout: cover
background: /intro.png
class: text-center
---

# <center> Significant changes </center>

---

# <center> Implemented: </center>

- a possibility to run tests simultaneously
  - dasharo-performance module
  - CPT, CPF, STB suites
  - grouped & executed per ENV_ID

<img src="../../img/sequential_test_run.png" style="margin-left:60px;margin-top:10px;float:left" width="300px">
<img src="../../img/concurrent_test_run.png" style="margin-right:60px;margin-top:10px;float:right" width="300px">

---

# <center> Implemented: </center>

- a possibility to run tests simultaneously

Sequential:
<center><img src="../../img/fedora_temp.png" width="580px" style="margin-top:10px:margin-bottom:10px"></center>

<center>+<img src="../../img/fedora_frequency.png" width="580px" style="margin-top:10px:margin-bottom:10px"></center>
<center>+</center>
<center>STBxxx.202 - at least 1h</center>
Concurrent:
<center><img src="../../img/fedora_concurrent.png" width="580px" style="margin-top:10px"></center>

---

# <center> Implemented: </center>

- an OpenWrt automation: installation & basic tests for Protectli platforms<img src="../../img/OpenWrt_Logo.svg" style="float:right" width="200px">
  - OS installation via DTS network boot
  - For now, no image preseed, automated configuration after OS boot

<center><img src="../../img/openwrt_scope.png" width="580px" style="margin-top:10px"></center>

---

# <center> Implemented: </center>

- Microcode revision testing
  - based on cbmem command output
  - microcode update is sometimes included in Dasharo releases
  - introduced to avoid accidental usage of older microcode in release binary ...
  - ... or failed microcode update.

---

# <center> In progress/planned: </center>
<center><img src="../../img/Qubes_OS_Logo.svg" width="150px" style="margin-left:-20px"></center>

- QubesOS test cases in OSFV
  - ENV_ID == 203 (200 means Linux distribution, third flavour)
  - distributed between modules & suites
  - 28 automated test cases in total
  - QubesOS installation now possible with preseed

---

# <center> Priorities for the future </center>
- Reduction of DUT non-essential power cycles
- OSFV versioning & release cycle:
  - We want to return back to versioning of OSFV from the current develop branch live approach.
  - The CI will probably be expanded in the future to help with that.
  - Some platforms will automatically run some set of tests to have a proof that an OSFV release works on a set of setups

---
layout: cover
background: /intro.png
class: text-center
---

# <center> Questions? </center>

---
layout: cover
background: /intro.png
class: text-center
---

# <center> Thank you! </center>

---
