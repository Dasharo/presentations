<!--
SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>

SPDX-License-Identifier: CC-BY-SA-4.0
-->

class: center, middle, intro

# Dasharo Features

### Dasharo User Group #1

## Michał Żygowski

.center[.image-10[![](remark-templates/dasharo-presentation-template/img/dasharo-sygnet-white.svg)]]

---

# Agenda

### What is this presentation gonna be about?

Current status and feature plans for:

* Supermicro X11SSH (server)
* Dell OptiPlex 7010/9010 (desktop)
* Dell Precision T1650 (desktop/NAS)
* MSI Z690-A/Z790-P (desktop)

---

# Dasharo Server Roadmap

.center[
<img src="img/dcs_server_roadmap_v0.1.png" width="900px" style="margin-left:-75px">
]

---

# Supermicro X11SSH

### v0.1.0 Community Release

Current status: **Porting**

* We have a working release candidate
* X11SSH-TF installed in the 3mdeb lab
* Basic Dasharo System Features and UEFI boot included
* iKVM keyboard does not want to work in the firmware, but does in OS (needs
  debugging)
* SOL works, Debian 11 checked and working
* **Sh*t tons** of ways of flashing with SUM, SMCIPMITool, flashrom, BMC GUI
  but **only BMC GUI** is working properly (and yet not always)...
* iKVM keyboard fix and some documentation is needed to switch to
  **Validation**

---

# Supermicro X11SSH

### What's next? v0.2.0

Features ideas for next release:

* UEFI IPMI drivers for OOB management, SMBus ASF, BMC event logging?
* OpenBMC port? There are [Supermicro open-source packages](https://www.supermicro.com/wdl/GPL/SMT/)
  which resemble a BMC project (to be analyzed)

.center.image-50[![](/img/x11ssh-tf.png)]

---

# Dasharo Desktop Roadmap

.center[
<img src="img/dcs_desktop_dell_roadmap_v0.1.png" width="680px" style="margin-left:30px;margin-top:-40px">
]

---

# Dell OptiPlex 7010/9010

### v0.1.0 Community Release

Current status: **Validation**

.right-column70[
* We have a working release candidate for quite some time
* Basic Dasharo System Features and UEFI boot included
* SMBIOS UUID and serial number migration
* Need to perform testing to finally switch to **Release** phase
* [GitHub v0.1.0 milestone](https://github.com/Dasharo/dasharo-issues/milestone/6)
* [GitHub Project](https://github.com/Dasharo/dasharo-issues/projects/7)
]
.left-column30[
.center.image-100[![](/img/optiplex.png)]
]

---

# Dell OptiPlex 7010/9010

### What's next? v0.2.0

Feature ideas for next release:
.right-column70[
* We don't know yet :)
* Ideas welcome
* Most likely inclusion of features developed for other platforms
]
.left-column30[
.center.image-100[![](/img/optiplex.png)]
]

---

# Dell Precision T1650

### v0.1.0 Community Release

Current status: **Porting**

.right-column70[
* Board support available in upstream coreboot
* Nothing started yet so we need to prepare everything:
  * Whole documentation
  * Dasharo System Features enabling
  * installation in 3mdeb lab
* [GitHub v0.1.0 milestone](https://github.com/Dasharo/dasharo-issues/milestone/7)
* [GitHub Project](https://github.com/Dasharo/dasharo-issues/projects/8)
]
.left-column30[
.center.image-100[![](/img/Dell-Precision-T1650.png)]
]

---

# Dell Precision T1650

### What's next? v0.2.0

Feature ideas for next release:

.right-column70[
* Precision T1650 would be specifically intended for NAS use due to ECC RAM, so
  it needs a runtime option to configure platform behavior after power failure
* Most likely inclusion of features developed for other platforms
]
.left-column30[
.center.image-100[![](/img/Dell-Precision-T1650.png)]
]

???

One would expect NAS to automatically power on after power failure to return to
the full operation ASAP

---
class: center, middle, intro

# Now the ones that you were probably longing for...

---

# Dasharo Desktop Roadmap

.center[
<img src="img/dcs_desktop_msi_roadmap_v0.1.png" width="900px" style="margin-left:-75px; margin-top:-30px">
]

---

# MSI Z690-A

### v1.1.2 - Supporters Release

Current status: **Validation**

* RPL-S CPU support in review upstream (not tested yet)
* MSI ACPI identification in Windows 11 to install MSI software and drivers
  automatically (done)
* ACPI interrupt routing fix (done) - my dual dGPU setup pays off...
* Fan control (almost finished) - few weekends gone, just like that... &#128517;
* FlashBIOS button (in progress) - yesss...
* [GitHub v1.1.2 milestone](https://github.com/Dasharo/dasharo-issues/milestone/8)
* [GitHub Project](https://github.com/Dasharo/dasharo-issues/projects/9)

Features also planned for this release:

* Add option to skip PS/2 keyboard detection to make all pS/2 keyboard work
  hopefully (legacy stuff always problematic)
* Runtime options for: PL1/PL2, VR loadline, memory XMP profile selection

???

The ACPI interrupt routing bug which caused by Nvidia audio to not work in
Windows, but worked in Linux...

---

# MSI Z690-A

### v1.2.0 - Community Release

* All features from v1.1.2 for everyone
* What else? We will see &#128512;

.center[.image-60[![](/img/msi_z690_a.png)]]

???

What else? It depends on community bug reports etc.

---

# MSI Z690-A - FlashBIOS button

* Decided to go with SpiSpy
* Inspired by the famous open-source activist, `programmer, photographer and
  frequent hacker`: Trammel Hudson
* https://trmm.net/Spispy/

.center[.image-70[![](/img/spispy.png)]]

---

# MSI Z690-A - FlashBIOS button

* There is one interesting feature in SpiSpy - TOCTOU mode!
* It can hijack SPI cycles from the chipset and respond with data present on
  the SpiSpy SDRAM (programmed with our custom firmware binary)
* Nobody said it will not hijack SPI cycles coming from 3rdparty chip
  responsible for FlashBIOS functionality!
* Plan: gather a trace of the FLashBIOS recovery process and determine vendor
  firmware structures responsible for binary validation
* Goal: Make FlashBIOS feature work with Dasharo builds (v1.1.2 or v1.2.0?)

???

The more features we add to setup, the more recovery process will be needed as
well.

---

# MSI Z790-P

### v1.0.0 - Community Release

Current status: **Discovery (Waiting for funds to start Evaluation)**

* Around 23'Q4 or 24'Q1!? I know.. I know... So frickin' late... &#128546;
* The more supporters we have the quicker we may satisfy the community needs!

.center[.image-50[![](/img/msi_z790_p.png)]]

---

# Open questions

* Is MSI EZ LED debug support of any importance?

* What options do you see as most important to be implemented in near future?

---

## .center[Q&A]

---
class: center,middle, intro

# Thank you
