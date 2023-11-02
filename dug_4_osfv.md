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

* We use OSFV at least since 2018, when we started validate PC Engines releases
* Using those scripts we over **50k** tests publicly releasing **150+** binaries
  based on open-source firmware.
* Initially it was closed source because of assumption that validation provides
  majority of the value in open-source firmware development.

---

# Dasharo OSVF

.center[https://github.com/Dasharo/open-source-firmware-validation]

* Dasharo Open Sourve Firmware Validation consist of MIT-licensed scripts
  written in Robot Frameworks with the purpose of validation of open-source
  firmware (mainly Dasharo).
* Robot Framework is a generic open source automation framework. It can be used
  for test automation and robotic process automation (RPA).
    - Used by OpenBMC among other organizations.
* Key Features of OSFV:
    - **Hardware Compatibility Testing**: audio, cpu, fan, network, docking
    stations, displays, network, thunderbolt, USB and more.
    - **Performance and Stability Testing**: boot time, cpu frequency and
    temperature, power cycle testing.
    - **Dashro Security Features Testing**: UEFI Secure Boot, measured boot, TPM,
    verified boot, TCG OPAL, ME, DMA protection and more.
* To maximize use of Dasharo OSFV you need dedicated infrastructure.

---

# OSFV Lab

.center.image-70[![](/img/osfv_arch.png)]

---

# OSFV Supported Platforms

.center.image-60[![](/img/osfv_supported_platforms.png)]

---

# OSFV v0.2

.center.image-90[![](/img/osfv_warn.png)]

* v0.2 was a silent release (no announcements)
* It started very active migration from our private repositories to the public.
* Goal is to start adoption among Dasharo and other projects open-source
  firmware developers.
* We hope that pairing Dasharo (UEFI) for QEMU Q35 v0.1.0 with OSFV can build
  reliable environment for rapid test development as well as the space for
  CI/CD testing of Dasharo and OSFV.

---

# Recent improvements

* Reduced `keywords.robot` from ~4000 lines to ~2000 lines
    - we are splitting that into more manageable modules under `lib/`
* Added `pre-commit` along with `robotody`, `robocop`, `black`, to autoformat
  RF and Python code for consistency
* Added support for running selected tests in QEMU (using Dasharo OvmfPkg
  release for QEMU)
* Added tests under `self-tests` directory, which are a variant of unit tests
  (run in QEMU), testing if basic kywords (such as moving in the Dasharo menus)
  still function as expected
* Reworked keywords for parsing and moving around in the Dasharo menus (see:
  `lib/bios/menus`)
    - better code readability
    - reduced duplicate keywords
    - improved reliability (entering to the desired menus, even if something
    changes in menus, such as new options gets added)
* Added CI checks
    - pre-commit checks
    - keywords `self-tests` in QEMU
    - a very basic (`dasharo-compatibility/custom-boot-menu-key.robot`) test on two hardware units: `MSI Z690A`, `Protectli VP4630`

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
* How do I run existing test on supported platform?
* How do I write a new test on supported platform?
* How do I add support for a new platform?

---

# What do I need to learn first?

* Some basic RF knowledge
    - go through basics in User Guide:
    https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
    - go through basic RF libraries: https://robotframework.org/robotframework/
        - especially `BuiildIn`, `Collections`, `Strings`, `Telnet` and `SSHLibrary` http://robotframework.org/SSHLibrary/SSHLibrary.html
        - add them to your bookmarks, you will need them often
* Some basic Python knowlednge
    - there are plenty of learning materials, pick your favourite one

???

https://3mdeb.gitlab.io/human-resources/processes/teams/test-automation-team/TAT_newcomer_cheatsheet/

---

# How do I run existing test on supported platform?

* Consult README for:
    - [supported platforms](https://github.com/Dasharo/open-source-firmware-validation/#supported-platforms)
    - [getting started](https://github.com/Dasharo/open-source-firmware-validation/#getting-started)
    - [running single tests](https://github.com/Dasharo/open-source-firmware-validation/#running-tests)
* Look through existing tests in:
    - `dasharo-compatibility`
    - `dasharo-security`
    - `dasharo-performance`
    - `dasharo-stability`
* Check if selected test is supported by the given platform
    - in `platform-configs/qemu.robot`: ``${CUSTOM_BOOT_MENU_KEY_SUPPORT}=    ${TRUE}``
    - in
    [dasharo-compatibility/custom-boot-menu-key.robot](https://github.com/Dasharo/open-source-firmware-validation/blob/main/dasharo-compatibility/custom-boot-menu-key.robot#L32C16-L32C16)
    `Skip If    not ${CUSTOM_BOOT_MENU_KEY_SUPPORT}    CBK001.001 not supported`

---

# How do I write a new test on supported platform?

TBD

???

https://3mdeb.gitlab.io/human-resources/processes/teams/test-automation-team/coding-guideline/#documentation

---

# How do I add support for a new platform?

TBD

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

---
class: center, middle, intro

# Q&A
