---
layout: cover
background: /intro.png
class: text-center

---
## Introduction to deguard

---

## whoami

- Filip Lewiński
- Junior Firmware Engineer @ 3mdeb

---

## Agenda

- What is Intel Boot Guard? + demo #1
- What does it mean for coreboot?
- What is deguard?
- How can I use it?
- Demo #2 - deguarded T480 running coreboot
- Discussion

---

## What is Intel Boot Guard?

Intel Boot Guard is a security feature that ensures only trusted firmware
runs when a computer starts.

* OEM Public Key and Boot Guard Policy are fused into the platform
* Field Programmable Fuses
* The firmware (Initial Boot Block - IBB) is signed by the manufacturer.
* Intel ME makes sure the CPU checks this signature before execution.
* Introduced with the 4th generation of Intel CPUs (Haswell)

---

## Demo #1 - BootGuarded T480

### Finding out if you have Boot Guard enabled

```bash
$ sudo rdmsr 0x13a
(...)  <--- non-zero output
```

Any **non-zero** value in the 0x13a Model Specific Register means
Boot Guard is enabled.

---

## What does it mean for coreboot?

In theory, Intel Boot Guard makes coreboot development impossible on a given
platform. This is why coreboot has _largely_ revolved around pre-Haswell boards.

In practice, there have been already a few exceptions:

* Buying unfused platforms from hardware vendors in bulk
  * NovaCustom
  * Protectli
* Some large OEMs choose not to / fail to fuse their platforms
  * Felix Singer's [BootGuard status](https://github.com/felixsinger/bootguard-status)
  * Successful coreboot port example: [ThinkCentre M700/M900 Tiny](https://review.coreboot.org/c/coreboot/+/80610)
* Using leaked IBG OEM keys to sign a coreboot binary
  * Popular in the [WinRaid](https://winraid.level1techs.com/) and [CSDN](https://www.csdn.net/)
    BIOS modding communities

---

## Deguard

[Deguard](https://codeberg.org/libreboot/deguard)
is a tool written by Mate Kukri that bypasses Intel BootGuard on Skylake, Kaby
Lake, and some Coffee Lake platforms.

### What does it do?

* It exploits
  [CVE-2017-5705](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00086.html)
  in vulnerable ME 11.x firmware.
* It downgrades ME via SPI flash overwrite
* It modifies BootGuard fuses in SRAM allowing execution of unsigned firmware.
* Works out of the box on the Lenovo T480 and Dell OptiPlex 3050
* Can be used to bypass BootGuard on other ME 11.x platforms, using a
provided script to generate the required metadata.

---

## Deguard

### coreboot ports enabled by deguard

* [Thinkpad T480(s)](https://review.coreboot.org/c/coreboot/+/83274) **WIP**
* [Dell OptiPlex 3050](https://review.coreboot.org/c/coreboot/+/82053) **Merged**

## How can I use it?

* Read the SPI flash
* Extract your platform-specific ME settings with `generatedelta.py`
  OR use already contributed settings if your board is supported
* Obtain a donor ME 11.6.0 image
* Patch the donor image with your settings and fake FPFs with `finalimage.py`
* Pack it into your flash image with `ifdtool` and flash it back onto the
  platform _(spoiler: that's what I'm doing with the T480 right now)_
* Open a PR adding your platform's ME settings

---

## How can I contribute and use it?

### Potential issues

There's been two issues so far suggesting that the `generatedelta.py` script
has trouble handling different platforms due to hardcoded offsets and being
tailored for the T480

* [Invalid checksum assert generating delta for T460s (ME 11.8.xxx)](https://codeberg.org/libreboot/deguard/issues/1)
* [Deguarding an Optiplex 5050](https://codeberg.org/libreboot/deguard/issues/2)

---

## Demo #2 - deguarded T480, running coreboot

<center><img src="../../img/dug_9/coreboot_logo.png" width="400"></center>
---

# Discussion

---

## Discussion

### Question 1

Do you consider a deguarded platform compromised/flawed in terms of security?
How would you rank
- a deguarded platform
- one that's never had bootguard support
- one whose private IBG keys had been leaked

### Question 2

Have you tried to do it, do you have platforms you'd really like to see ported?
