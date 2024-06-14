class: center, middle, intro

# Verified Boot and firmware updates

## How to do them securely and openly

### Michał Kopeć

.center[<img src="/remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">]

???

<!--
SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>

SPDX-License-Identifier: CC-BY-SA-4.0
-->

---

# whoami

- Michał Kopeć (original author)
  - Firmware Engineer at 3mdeb since 2021
  - Develops Dasharo for laptops, network appliances and other platforms
  - Uses Arch btw

- Michał Żygowski (presenter)
  - Firmware Engineer at 3mdeb since 2017
  - Develops Dasharo
  - open-source, HW and security features enthusiast

---

# Agenda

- Verified Boot
  - in Chrome
  - in Dasharo
- Problem statement
- Boot Guard
- CBFS verification
- Secure firmware updates

---

# Verified boot

- Verified Boot: Cryptographic verification of the boot process to ensure only
  code from a trusted source (e.g. device vendor) can run
- coreboot supports Vboot, Google's version of verified boot scheme
- Vboot has:
  - A root of trust
  - Verification of subsequent firmware stages
  - Signatures and public tools for self-signing
  - A special A/B update mechanism
  - Support for re-ownership
- Dasharo uses Vboot

???

- Google created Vboot for chrome devices
- In Chrome, vboot is also used for OS and EC secure boot
- We use some subset of Vboot's capabilities

---

# Verified Boot in Chrome devices

.center.image-55[![](/img/vboot/chrome_os.svg)]

- Write protection: WP# pin on the BIOS chip
  - WP# pin is controlled by Cr50 security chip (newer devices) or physical
    screw (older devices)
- Updates: An OS service handles the A/B update scheme
  - One slot is updated, and when confirmed bootable, the other slot is updated
    too
- Write protected portion of the flash is **not** updated, and serves as
  recovery
  - WP region contains the initial bootblock and verifies the A/B slots
  - When both slots fail or recovery is manually requested (e.g. by keyboard
    key), the firmware boots from the recovery partition

???

- Cr50 is a Google's TPM-like device, also known as Titan C

---

# Verified Boot in Dasharo

.center.image-20[![](/remark-templates/dasharo-presentation-template/images/dasharo-sygnet.svg)]

- Write protection is provided by chipset (typically, can be also SPI WP#)
  - Optional feature, but enabled by default for most platforms
  - Protects against software attacks
- Updates are handled by Dasharo Tools Suite
  - Capsule Update and fwupd support is WIP
- Most updates also need to update the bootblock, so they require protection
  to be disabled for updates - obviously suboptimal
- OS secure boot is handled by UEFI SB

???

- Firmware programs protected range registers in chipset, which ensures software
  cannot write to flash
- Firmware is not physically write protected
- We find we need to update the recovery region because of:
  - Firmware layout changes
  - New features added to booblock
  - Breaking Kconfig changes
  - coreboot rebases
- Google is not affected by this because they:
  - Generally do not add new features to firmware
  - Use a fixed coreboot rev for each mainboard

---

# Problem

.center.image-40[![](/img/problem.jpg)]

- How do we improve Dasharo verified boot while staying secure and without
  taking control away from users?
  - Security: A guarantee that only firmware from a trusted vendor is run
  - Control: Ability to self-sign, to inspect and replace firmware components
- There are other verified boot schemes

.footnote[
Image source: https://picryl.com/media/question-mark-note-man-people-55a8e2
<br>Image license: Creative Commons CC0 1.0 Universal Public Domain Dedication
]

---

# Intel Boot Guard

.left-column55[

.center.image-99[![](/img/vboot/butt_guard.png)]

]

.right-column45[

- The most widely known option
- Verifies and measures the initial bootblock
- Ensures FW authenticity using keys fused to the chipset
- Different profiles with different features enabled
  - Verified boot is always enabled in all profiles
- **Ties a platform to a specific firmware vendor, forever!**
]

.footnote[
Source: [Amazon](https://www.amazon.com/Tbest-Guard%EF%BC%8CChildren-Protection-Snowboard-Anti%E2%80%91Drop/dp/B08GBBRGL9)
]

???

- Intel specific, AMD has a different but comparable secure boot scheme
  Verifies the initial bootblock, rest is up to BIOS (Vboot)
- fused: programmed into one-time programmable e-fuses inside the chipset
- Measurements are made in locality 3, so they can't be faked by malicious BIOS
- Profile 3: Verified and Measured with infinite time for remediation
- Profile 3 acts as root of trust for measurement, but not for verification
- On verification failure, the PCR0 measurements are always the same. This was
  determined experimentally.
- so users can choose to use Dasharo firmware and get measured IBB, or flash
  their own and lose measured IBB.
  - might make sense for some small percentage for users
  - does not help us a lot

---

# Boot Guard cons

.center.image-20[![](/img/vboot/Antu_selinux.svg)]

.footnote[
.center[[Antu selinux](https://commons.wikimedia.org/wiki/File:Antu_selinux.svg) CC BY-SA 3.0]
]

- Requires more blobs in firmware
  - Boot Guard ACM
- Fusing removes some owner control
- Profile 3 does not ensure initial boot block authenticity
  - Only helps us establish a root of trust for measurement
- Other profiles take away owner control completely

???

- ACM - Authenticated Code Module. Hyper-privileged, Intel signed blob that
  performs the actual BIOS verification and measurement, then hands off to the
  BIOS reset vector.

---

# CBFS Verification

.center.image-20[![](/img/coreboot.png)]

- A relatively new coreboot feature
- Cryptographically verifies components of the coreboot image
- According to documentation:
  > This only makes sense if you use some
  > out-of-band mechanism to guarantee the integrity of the bootblock
  > itself, such as Intel Boot Guard or flash write-protection.
  - Same applies to vboot's recovery region, which is ultimately trusted
- Depends on some other mechanism for signing (e.g. Boot Guard)
- Can effectively replace the portions of Vboot that Dasharo uses

???

- CBFS - coreboot's internal file system

---

# Firmware updates

- Chrome Vboot: A+B+RO
  - A and B slots for updates, RO slot contains IBB and verification code
  - Anti-rollback using TPM
  - Vboot aware OS service manages slot updates
- Dasharo:
  - Initial idea was to leave RO untouched and only update A/B slots
  - In practice, most updates introduce breaking changes that require updating
    the bootblock
  - Dasharo Tools Suite handles updates, does the entire update in one operation
    - So we don't use the A/B feature
  - Capsule Updates may help here

---

# Other firmware update mechanisms

.center.image-30[![](/img/vboot/flash.jpg)]

.footnote[
.center[[The Flash Wallpaper by kelso](https://www.hdwallpapers.net/tv-and-movies/the-flash-wallpaper-622.htm) CC BY-SA 3.0]
]

- Flashrom plugin in fwupd
  - Updates the BIOS region only
  - Is not Vboot aware
- UEFI Capsule Update
  - Most widely used in proprietary UEFIs
  - Can be made aware of which regions to update and which to preserve, verify
    signatures, handle disabling flash protections
  - WIP for Dasharo

???

- Capsule Updates are a requirement for Windows sticker certification
- Supported by Windows Update and fwupd

# Other firmware update mechanisms

- Intel BIOS Guard
  - Hooks into the SMM flash update handler to call an ACM, which authorizes
    flash writes
  - Can bypass chipset flash protections and Top Swap (configurable with
    MFIT/FIT/FITC in flash descriptor straps)
  - Can also handle EC updates
  - Proprietary feature with proprietary tooling
- Top Swap
  - Redundant bootblock feature
  - Configurable from 64KB up to 4M/8MB (maximum depending on CPU/SoC/chipset
    family) in flash descriptor straps (MFIT/FITC/FIT)
  - Potential integration with vboot?

???

- Top swap size is (barely?) enough to fit an entire Vboot RO partition
- e.g. have immutable, write-protected recovery that verifies the top swap block
  and sets the top swap bit accordingly?

---

class: center, middle, intro

# Q&A
