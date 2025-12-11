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

---

# <center> Implemented: </center>

- an OpenWrt automation: installation & basic tests
  - Protectli platforms
  - OS installation via DTS network boot
  - For now, no image preseed, automated configuration after OS boot
- Microcode revision testing
  - based on cbmem output

---

# <center> In progress/planned: </center>
<center><img src="../../img/Qubes_OS_Logo.svg" width="150px" style="margin-left:-20px"></center>

- QubesOS test cases in OSFV
  - ENV_ID == 203 (200 means Linux distribution, third flavour)
  - distributed between modules & suites
  - QubesOS installation now possible with preseed

---

# <center> Priorities for the future </center>
- Reduction of DUT non-essential power cycles
- OSFV versioning & release cycle: TBA

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
