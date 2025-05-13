---
theme: ../../slidev-template/theme
layout: cover
background: /intro.png
class: text-center

---
## But can it run coreboot?

### Checking your AMD platform for Platform Secure Boot

---

## whoami

- Michał Kopeć
- Firmware Engineer working primarily with coreboot and EDK2
- Have been at 3mdeb for 3 years now
- Free and open source software enthusiast

---

## Agenda

- What do we need to be able to run coreboot?
- What is Platform Secure Boot?
- How do I check if I have it?
- Demo
- Future plans
- Discussion

---

## Can [x] run coreboot?

### Abridged checklist

1. Is there existing code for the silicon in question?
    - check coreboot/src/soc directory

2. Does [x] have any hardware RoT fused to vendor's keys?
    - On x86: Intel Boot Guard, AMD Platform Secure Boot
    - Can also be external to the silicon platform, e.g. BMC

Step 1 can be checked fairly easily, and because Google has many vendors for
chromebooks and chromeboxes, mobile/laptop SoCs are often supported ahead of
release

Step 2 is more tricky :)

---

## What is AMD Platform Secure Boot?

- AMD's version of Intel Boot Guard
- In summary, AMD ASP is fused to only accept BIOS images signed by board
  vendor's private key
  - Fuses are on the CPU package itself, whereas on Intel they're in the PCH
  - This means that on socketed desktop platforms, bypassing PSB is as simple
    as replacing the CPU
  - Also means that once fused, a CPU will only be usable inside boards from
    that specific vendor, or even only in that device model
  - Kills used CPU market, so it's seldom used in enthusiast / DIY boards

<center><img src="/dug_8/sth-psb.png" width="600">Source: ServeTheHome</center>

---

## How do I check if I have it?

- For Intel, we have Felix Singer's bootguard-status project:
  https://github.com/felixsinger/bootguard-status
- For AMD, there wasn't a comparable tool, so I wrote psb_status
  - Very small bash script (32 LoC)
  - Based on coreboot's implementation of PSB
  - Checks for FUSE_PLATFORM_SECURE_BOOT_EN bit in PSB_STATUS_OFFSET register
  - I also compile a list of user reports, so feel free to contribute :)

<center><img src="/dug_8/psb-mobile.png" width="400" align="left"><img src="/dug_8/psb-pr.png" width="400" align="right"></center>

---
layout: cover
background: /intro.png
class: text-center

---

## Demo

---

## Future plans

- Make checking more reliable
  - One user reported discrepancy between psb_status and fwupd HSI
  - Check more status bits
- Make it easier to submit results
- Remove dependency on external tools (iotools)
- Offline analysis of BIOS binaries

---
layout: cover
background: /intro.png
class: text-center

---

# Discussion
