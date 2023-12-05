class: center, middle, intro

# &#x1F386; Dasharo Open Source Firmware Validation &#x1F386;

.center[<img src="/remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">]

???

---

# Agenda

* Introduction to Dasharo Open Source Firmware Validation (OSFV)
* Exploring OSFV v0.2
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

---

# OSFV Supported Platforms

.center.image-60[![](/img/osfv_supported_platforms.png)]

---
class: center, middle, intro

# Q&A
