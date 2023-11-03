class: center, middle, intro

# &#x1F386; Dasharo Open Source Firmware Validation &#x1F386;

.center[<img src="/remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">]

???

---

# Agenda

* Introduction to Dasharo Open Source Firmware Validation (OSFV)
* Exploring OSFV v0.2
* Recent improvements
* Getting started with OSFV
* Upcoming Features: OSFV v0.3 and Beyond
* Q&A

???

---

# History

.center.image-99[![](/img/osfv.png)]

* We've been using OSFV at least since 2018, when we've started validating PC
  Engines coreboot releases on a monthly basis
* Using those scripts we've executed over **50k** tests publicly releasing **150+**
  binaries based on open-source firmware
* Initially, it was closed source because of assumption that validation provides
  majority of the value in open-source firmware development

---

# Dasharo OSVF

.center[https://github.com/Dasharo/open-source-firmware-validation]

* Since then, these scripts came through many iterations, supporting more
  different products
* At some pint we have decided to open-source what we have and start
  maintaining and iproving it as an open-source product
* Dasharo Open Source Firmware Validation purpose is the validation of
  open-source firmware (mainly Dasharo)
* Scripts written in:
    - mostly Robot Framework (keywords, test suites)
    - some Python (for some keywords, sometimes more suitable than RF)
    - shell scripts (mostly some wrappers for test execution)

???

* Key Features of OSFV:
    - **Hardware Compatibility Testing**: audio, cpu, fan, network, docking
    stations, displays, network, thunderbolt, USB and more
    - **Performance and Stability Testing**: boot time, cpu frequency and
    temperature, power cycle testing
    - **Dashro Security Features Testing**: UEFI Secure Boot, measured boot, TPM,
    verified boot, TCG OPAL, ME, DMA protection and more
* To maximize use of Dasharo OSFV you need dedicated infrastructure

---

# Robot Framework

* Robot Framework is a generic open source automation framework
* It can be used for test automation and Robotic Process Automation (RPA)
* Used widely for web apps testing (with Selenium), but not only
* Used by OpenBMC (firmware, embedded Linux) for test automation
    - https://github.com/openbmc/openbmc-test-automation
* Active community, quality documentation
    - https://robotframework.org/#community
    - https://docs.robotframework.org/docs
* Robot Framework Conference
    - https://robocon.io/

.center.image-20[![](/img/Robot-framework-logo.png)]

---

# OSFV Lab

.center.image-70[![](/img/osfv_arch.png)]

???

We have two more options, not displayed here:
- PiKVM + RTE + Sonoff
- PiKVM + Sonoff

---

# OSFV Supported Platforms

.center.image-60[![](/img/osfv_supported_platforms.png)]

---

# OSFV v0.2

.center.image-90[![](/img/osfv_warn.png)]

* v0.2 was a silent release (no announcements)
* It started very active migration from our private repositories to the public
* The goal is to start adoption among Dasharo and open-source firmware
  developers

---

# Recent improvements

* Reduced `keywords.robot` from ~4000 lines to ~2000 lines
    - we are splitting that into more manageable modules under `lib/`
* Added `pre-commit` to enforce rules on commit and code style
    - [robocop](https://robocop.readthedocs.io/en/stable/)
    - [robotidy](https://robotidy.readthedocs.io/en/stable/)
    - [black](https://black.readthedocs.io/en/stable/)
    - [conform](https://github.com/siderolabs/conform)
* Applied these rules tree-wide

.center[.image-15[![](/img/robocop_logo_small.png) ![](/img/robotidy_logo_small.png) ![](/img/pre-commit-logo.svg)]]

---

# Recent improvements

* Added support for running selected tests in QEMU (using Dasharo OvmfPkg
  release for QEMU)
    - https://docs.dasharo.com/variants/qemu_q35/releases/
    - https://github.com/Dasharo/edk2/releases

.center.image-60[![](/img/dasharo_on_qemu.png)]

---

# Recent improvements

* Added tests under `self-tests` directory
    - a form of unit tests, testing if basic kywords (such as moving in the Dasharo menus)
    still function as expected
    - `self-tests/boolean-options.robot`

.code-11px[```markdown
Documentation       This suite verifies the correct operation of keywords
...                 getting and setting state of boolean options.

***Test Cases***
Set boolean option to true
    [Documentation]    Checks whether the boolean option can be set to TRUE.
    Power On

Set boolean option to false
    [Documentation]    Checks whether the boolean option can be set to FALSE.

Toggle boolean option 3 times
    [Documentation]    Checks whether the boolean option can be toggled
    ...    FALSE/TRUE 3 times in a rew.
```]

.code-11px[```text
==============================================================================
Boolean-Options :: This suite verifies the correct operation of keywords ge...
==============================================================================
Set boolean option to true :: Checks whether the boolean option ca... | PASS |
------------------------------------------------------------------------------
Set boolean option to false :: Checks whether the boolean option c... | PASS |
------------------------------------------------------------------------------
Toggle boolean option 3 times :: Checks whether the boolean option... | PASS |
------------------------------------------------------------------------------
Boolean-Options :: This suite verifies the correct operation of ke... | PASS |
3 tests, 3 passed, 0 failed
==============================================================================
```]

---

# Recent improvements

* Reworked keywords for parsing and moving around in the Dasharo menus (see:
  `lib/bios/menus`)
    - better code readability reduced duplicate keywords
    - improved reliability (entering to the desired menus, even if something
    changes in menus, such as new options gets added)
* Added CI checks
    - pre-commit checks
    - keywords `self-tests` in QEMU
    - a basic test on two hardware units: `MSI Z690A`, `Protectli VP4630`

.center[.image-50[![](/img/osfv_ci.png)]]

---

# OSFV v0.3 and beyond

* **variables** - use Python/YAML, not robot syntax, currently used variables
  system for keeping configuration is not robust to be used at scale (too error
  prone), we have to switch to something manageable
* **platform-configs** - get rid of duplication, and unused data, simplify way of
  adding new platforms,
* **improve tests organization** - separate test for different OS into different
  suites, look for inspiration in other projects about test organization,
* **prepare the OS for running test suite via some dedicated tools (e.g. Ansible,
  SaltStack)**, rather than implementing keywords for that from scratch - the
  problem is that writing robot keywords is expensive and RF is not dedicated
  tool for system configuration

---

# OSFV v0.3 and beyond

* **reduce the number of unnecessary power events** - too many power cycles drain
  energy and make tests slow,
* improve overall code quality by enabling back more robocop checks we cannot
  pass right now,
* Enforce documntation sections for all keywords and tests
* Automatically generate and publish docuemntation for keywords and tests
    - kyewords - useful for developers
    - tests - useful for following the test scenario and reproducing it manually
    - the goal is to document tests via automated tests, not via dedicated test manuals
        - it is expensive to maintain this separately
        - it is difficult to keep it in sync with automated cases

---

# Getting started with OSFV

* What do I need to learn first?
* How do I run existing test?
* How do I write a new test?
* How do I add support for a new platform?

---

# What do I need to learn first?

* Some basic RF knowledge
    - go through basics in
      [User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html):
    - go through basic
      [RF libraries](https://robotframework.org/robotframework/):
        - `BuiildIn`, `Collections`, `Strings`, `Telnet`
        - add them to your bookmarks, you will need them often
    - check out [SSHLibrary](http://robotframework.org/SSHLibrary/SSHLibrary.html)
* Some basic Python knowlednge
    - there are plenty of learning materials, pick your favourite one

???

https://3mdeb.gitlab.io/human-resources/processes/teams/test-automation-team/TAT_newcomer_cheatsheet/

---

# How do I run existing test?

* Consult README for:
    - [supported platforms](https://github.com/Dasharo/open-source-firmware-validation/#supported-platforms)
    - [getting started](https://github.com/Dasharo/open-source-firmware-validation/#getting-started)
    - [running single tests](https://github.com/Dasharo/open-source-firmware-validation/#running-tests)
* Look through existing tests in:
    - `dasharo-compatibility`
    - `dasharo-security`
    - `dasharo-performance`
    - `dasharo-stability`
---

# How do I run existing test?

* Check if selected test is supported by the given platform
* In `platform-configs/qemu.robot`:

.code-11px[```markdown
${CUSTOM_BOOT_MENU_KEY_SUPPORT}=    ${TRUE}
```]

* `In dasharo-compatibility/custom-boot-menu-key.robot`

.code-11px[```markdown
Skip If    not ${CUSTOM_BOOT_MENU_KEY_SUPPORT}    CBK001.001 not supported
```]

* Example on hardware:

.code-11px[```text
$ robot  -L TRACE -v config:protectli-vp4630 -v rte_ip:192.168.10.244 dasharo-compatibility/custom-boot-menu-key.robot

==============================================================================
Custom-Boot-Menu-Key
==============================================================================
CBK001.001 Custom boot menu key :: Check whether the DUT is config... | PASS |
------------------------------------------------------------------------------
CBK002.001 Custom setup menu key :: Check whether the DUT is confi... | PASS |
------------------------------------------------------------------------------
Custom-Boot-Menu-Key                                                  | PASS |
2 tests, 2 passed, 0 failed
==============================================================================
Output:  /home/macpijan/projects/github/dasharo/open-source-firmware-validation/output.xml
Log:     /home/macpijan/projects/github/dasharo/open-source-firmware-validation/log.html
Report:  /home/macpijan/projects/github/dasharo/open-source-firmware-validation/report.html
```]

---

# How do I write a new test?

* Refer to the existing tests
  - `self-tests` are good examples
  - other commonly used tests
    - `dasharo-security/bios-lock.robot`
    - `dasharo-security/me-neuter.robot`
    - `dasharo-security/smm-bios-write-protection.robot`
    - `dasharo-compatibility/network-boot.robot`
    - `dasharo-compatibility/network-boot-utilities.robot`
  - some tests may currently not work or be of a lower quality

???

https://3mdeb.gitlab.io/human-resources/processes/teams/test-automation-team/coding-guideline/#documentation

---

# How do I add support for a new platform?

* Pick a similar board from `platform-config` and adjust it
* Power control
  - [RTE](https://3mdeb.com/open-source-hardware/),
    [Sonoff WiFi Smart Plug](https://sonoff.tech/product/smart-plugs/s26/),
    or both (or something else, which is not supported yet)
* Flashing
  - preferably external flashing is supported - like SOIC clip connected to RTE
    all the time
* Serial connection
  - [ser2net service](https://github.com/cminyard/ser2net) to expose serial
    via telnet
* Hardware setup may be complex
  - https://docs.dasharo.com/variants/asus_kgpe_d16/setup/

???

https://gitlab.com/3mdeb/rte/open-firmware-rte/-/blob/master/docs/enabling-platforms.md

---

# Contributing to OSFV repository

* Many parties can contribute there
* By contributing you get the benefits such as:
    - access to test developed by 3mdeb or other parties
    - stable environment tested in more scenarios
* 3mdeb maintains repository to make sure changes from external parties does
  not break others, and can be shared between them
    - access to all supported platforms
    - experience
* Standard GH issues and PR flow for contributors
* Join Dasharo Matrix Space https://matrix.to/#/#dasharo:matrix.org
* Join Dasharo OSFV Matrix room: https://matrix.to/#/#osfv:matrix.3mdeb.com

---
class: center, middle, intro

# Q&A
