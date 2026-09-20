---
theme: slidev-template/theme
layout: cover
background: /intro.png
class: text-center
---

# Host Security ID (HSI) on AMD servers today and tomorrow

<!-- SPEAKER NOTES
Welcome. This talk is about what happened when we pointed fwupd's Host
Security ID at a real AMD server running open-source firmware, and what we
think it would take to make that score mean the same thing everywhere.

It is a report from the field, not a spec walkthrough. Thirty minutes,
roughly fifteen slides, plenty of room for questions at the end.
-->

---

# `$ whoami`

<center><img src="/slides/img/michal_zygowski.png" width="150px">
  <b>Michał Żygowski</b><br>
  <i>3mdeb Senior Firmware Engineer</i>
</center>

* Core developer of coreboot.
* Maintainer of Braswell SoC, PC Engines, Protectli, MSI and Libretrend
  platforms.
* Interested in advanced hardware features, security and coreboot.
* Open-source firmware enthusiast and conference speaker.

<!--

Time: 1min

One thing that I want to mention, which is maybe not widely known:
- What is OpenSecurityTraining2
- What is my role in OpenSecurityTraining2

-->

---

# Contact Information

<div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
  <img src="/slides/img/michal_zygowski.png" style="width: 100px; border-radius: 50%;" alt="Profile Picture">
  <div>
    <b style="font-size: 1.5em;">Michał Żygowski</b><br>
    <i style="font-size: 1.2em;">3mdeb Senior Firmware Engineer</i>
  </div>
</div>

<div style="display: flex; justify-content: space-between; align-items: center; font-size: 1.2em;">
  <div>
    🔑 <code>00B8 8FB2 5FD6 375B C5FF  195D 6B5B A214 D21F CEB2</code><br>
    ✉️ <a href="mailto:michal.zygowski@3mdeb.com">michal.zygowski@3mdeb.com</a><br>
    🐦 <a href="https://x.com/_miczyg_">@_miczyg_</a><br>
    🔗 <a href="https://www.linkedin.com/in/miczyg/">LinkedIn: miczyg</a><br>
    🌐 <a href="https://www.3mdeb.com">3mdeb.com</a><br>
    💻 <a href="https://github.com/miczyg1">GitHub: miczyg1</a><br>
  </div>
</div>

<!--

Time: 1min

-->

---

# Agenda

<br>

- What HSI is and why it exists
- A real AMD server put through HSI testing
- Where the score and the platform disagree, and why
- Where the current specification runs out of vendor coverage
- What we think HSI could look like across silicon vendors

<!-- SPEAKER NOTES
Four blocks. First a short refresher on HSI itself, since not everyone in
the room will have used it. Then the case study: a Dasharo AMD server and
what its HSI report actually says. Then the friction points we hit, some of
which are AMD-specific and some of which are just reporting problems. And
finally the forward-looking part: cross-vendor alignment and where the
specification could grow.
-->

---

# What HSI actually is

<br>

- A specification for scoring a running platform's security posture
- From HSI-1 to HSI-4, each level built on the ones below it:
- Implemented in fwupd, exposed through `fwupdmgr security`/`fwupdtool
  security`
- Checks firmware, kernel, TPM and silicon-specific state directly, not
  marketing claims

<br>

<center><img src="/slides/img/fwupd-hsi-levels.svg"></center>

!!! info HSI5 is unobtanium
    "This security level corresponds to out-of-band attestation
    of the system firmware. There are currently no tests implemented
    for HSI:5 and so this security level cannot yet be obtained."

<!-- SPEAKER NOTES

HSI compresses a long list of low level firmware and platform security
properties into a single number. Instead of asking someone to manually check
SPI write protection, IOMMU state, TPM PCRs and a dozen other things, you run
one command and fwupd tells you the level.

The levels are cumulative. Claiming HSI-3 means every HSI-1 and HSI-2
requirement is also satisfied. That is useful, because it stops people
cherry picking one good feature and calling the whole platform secure.

The catch, which is the whole subject of this talk, is that the checks
fwupd runs were written against Intel's feature set first, and AMD and
everyone else were fitted in afterwards. ARM does not exist yet.

Can quickly expose vendor's insecure firmware configuration, but may also
confuse users about insecure state if checks do not apply to given hardware.
-->

---

# The platform under test

<center><img src="/slides/img/gigabyte_mz33_ar1.webp" width="250px"></center>

- Gigabyte MZ33-AR1, an AMD server board
- Dasharo firmware: coreboot and EDK2, fully open source down to the payload
- Goal: run `fwupdmgr security`, see what comes back, and understand every
  line of the report

<!-- SPEAKER NOTES
The MZ33-AR1 is a Gigabyte server board built around an AMD EPYC processor.
We ported Dasharo to it, meaning coreboot handles early hardware bring-up and
EDK2 provides the UEFI environment on top.

Because it is server hardware and open firmware, it does not look like the
laptops HSI was mostly validated against. That mismatch is exactly what
makes this an interesting test subject.
-->

---
layout: two-cols-header
---

# HSI today

::left::

<center><img src="/slides/img/gigabyte_mz33_ar1_hsi.png" width="270px"></center>

::right::

<center><img src="/slides/img/gigabyte_mz33_ar1_hsi_new.png" width="270px"></center>

<style>
.two-cols-header {
  column-gap: 10px; /* Adjust the gap size as needed */
  grid-template-rows: auto 1fr; /* header shrinks to fit its content */
}
</style>

<!-- SPEAKER NOTES
Here is the headline result. The board reaches HSI-2 as a certified level.
But if you go through the individual requirements that HSI-4 asks for, one
by one, the platform satisfies every single one of them on its own merits.

That gap between the certified level and the underlying reality is the
story of the rest of this talk. It is not one bug. It is a handful of
separate, unrelated reasons, and each one teaches something different about
how HSI interacts with real hardware.
-->

---

# Gap one: SPI replay protection

<center><img src="/slides/img/bad_chip.svg" width="200px"></center>

- HSI-4 requires the SPI flash to reject replayed write transactions (RPMC)
- The MZ33-AR1's flash chip does not implement this, a board design choice
independent of AMD silicon

<br>

### Solution

<br>

- Swap the flash chip for one that supports replay protection, and this
requirement is satisfied
- Not an AMD limitation, not a firmware limitation, a bill-of-materials
limitation

<!-- SPEAKER NOTES
This is the cleanest gap of the three, because it has nothing to do with AMD
at all. SPI replay protection depends on a feature of the flash chip itself.
The chip Gigabyte selected for this board does not have it.

If a future board revision, or a different SKU, uses a flash chip that
supports replay protection, this line turns green with zero firmware
changes. It is worth calling out precisely because it shows that not every
red line in an HSI report is a silicon or firmware problem. Sometimes it is
a part number.
-->

---
layout: two-cols-header
---

# Gap two: sudo changes the answer

Reported upstream: [fwupd#10162](https://github.com/fwupd/fwupd/issues/10162)

::left::

### sudo

<center><img src="/slides/img/gigabyte_mz33_ar1_hsi_new.png" width="230px"></center>

::right::

### no sudo

<center><img src="/slides/img/gigabyte_mz33_ar1_hsi_nosudo.png" width="200px"></center>

<style>
.two-cols-header {
  column-gap: 10px; /* Adjust the gap size as needed */
  grid-template-rows: auto 1fr; /* header shrinks to fit its content */
}
</style>

<!-- SPEAKER NOTES
- Some HSI tests read state that is only accessible with elevated privileges
- Running `fwupdmgr security` as a normal user versus with `sudo` produces
  different results on the same, unchanged system
- The actual security state of the machine did not change between the two runs,
  only what the tool was allowed to see
- Some test only appear in the non-sudo invocation

This one is uncomfortable because it looks like the platform got less
secure just by running a command differently. It did not. Certain register
reads that back specific AMD checks require root, and when the test runs
without it, fwupd cannot tell the difference between "this feature is
missing" and "I was not allowed to look."

Right now those two cases are reported the same way, as a failure. That is
a tooling and reporting problem, not a platform problem, but it directly
undermines trust in the HSI state if two runs on the same machine give two
different scores.
-->

---

# Gap three: suspend-to-idle

<br>

### How lack of sleep states support makes you "insecure"

<br>

<center><img src="/slides/img/hsi_power_saving.png" width="900px"></center>

<br>

- HSI checks for suspend-to-idle support as a laptop-oriented power-saving
  feature
- A server board like the MZ33-AR1 does not support laptop-style S0i3 idle
  states on silicon level
- **Lack of suspend = insecure firmware**
- Related: [Suspend-to-Idle not supported should not decrease HSI level on
  servers](https://github.com/fwupd/fwupd/issues/10068)

<!-- SPEAKER NOTES
Suspend-to-idle is a real security-relevant feature on laptops, related to
how memory is protected across sleep states. On a server, it is simply not
a design goal. Nobody suspends a rack server to idle.

The current test does not know that. It sees the feature absent and marks
it as a gap, the same way it would on a laptop that genuinely lacks the
capability for a bad reason. Server-class hardware needs the test to either
not apply, or to be interpreted against a different baseline. This is upstream
interpretation catching up with a hardware class HSI was not originally
written for.
-->

---

# Reporting problems aren't only ours

<br>

- Independent reports of confusing or inconsistent HSI output on other
  platforms:
  - [Pre-boot DMA protection HSI check is not
    accurate](https://github.com/fwupd/fwupd/issues/7533)
  - [AMD RAM Encryption not enabled in security report despite enabled in
    hardware](https://github.com/fwupd/fwupd/issues/10066):
- A security score only works if people trust what it says
- Users need know how to reconfigure the environment properly for maximum
  possible score

<!-- SPEAKER NOTES
We are not the only ones running into cases where the report is hard to
interpret or seems to contradict itself between runs or between tools. These
two issues are other people's platforms, other symptoms, same underlying
theme: the reporting layer needs as much attention as the checks themselves.

Pre-boot DMA protection may be a flag, which is set depending on firmware
option/variable. WHole the real protection enabling is separate firmware
option/variable.

AMD RAM Encryption will only report as enabled, if instructed the kernel to
use it (`mem_encrypt=on`). Otherwise, just enabled state in firmware does not
pass the test.

If a firmware engineer cannot confidently explain their own HSI report, an
end user has no chance. That is a problem worth fixing before we even start
talking about cross-vendor comparisons.
-->

---

## Same score, different silicon

<br>

- Intel and AMD expose different features, so HSI's Intel-shaped checks
  translate imperfectly to AMD
- ARM is not supported by HSI at all today
- On ARM, security-sensitive state often lives behind the non-secure/secure
  world boundary, unreachable from the OS-facing side HSI inspects

<!-- SPEAKER NOTES
Even setting aside our specific gaps, there is a structural issue. HSI's
checks grew up around Intel features: Boot Guard, Intel ME state, SMAP,
TME. AMD has equivalent concepts, but they are not identical, and every port
of a check to AMD is a judgment call about what counts as equivalent.

ARM is further behind. The non-secure world, where Linux runs, frequently
cannot query the security-relevant registers that live in the secure world
or in a separate management processor. You cannot check what you cannot
read. That is not a missing feature in HSI, it is a missing capability in
the access model, and it needs a different approach, not just more checks.
-->

---

## Borrow HSTI instead of reinventing the wheel

<br>

- Microsoft's [Hardware Security Testability
  Specification](https://learn.microsoft.com/en-us/windows-hardware/test/hlk/testref/hardware-security-testability-specification)
  already defines vendor-neutral hardware and firmware security queries via
  EFI protocols
- It separates hardware-vendor checks from BIOS/firmware-vendor checks, which
  maps well onto how HSI wants to score a platform
- **Already present in Gigabte MZ33-AR1 vendor firmware**
- Some existing Intel HSTI definitions in edk2-platforms:
  - [Silicon/Intel/KabylakeSiliconPkg/Include/HstiFeatureBit.h](https://github.com/tianocore/edk2-platforms/blob/devel-MinPlatform/Silicon/Intel/KabylakeSiliconPkg/Include/HstiFeatureBit.h)
  - [Platform/Intel/MinPlatformPkg/Include/HstiIbvFeatureBit.h](https://github.com/tianocore/edk2-platforms/blob/devel-MinPlatform/Platform/Intel/MinPlatformPkg/Include/HstiIbvFeatureBit.h)

Example for Intel Boot Guard, AMD Platform Secure Boot and ARM Hardware
Validated Boot:

```text
5. [CS]Boot Integrity Support
  a. Do you support Boot Integrity and is it enabled by default?
...
9. What are the security fuses you have (vendor specific)
  a. SOC SecureBoot fuse
```

<!-- SPEAKER NOTES

HSTI already solved a version of this problem for Windows hardware
certification. It asks a platform to answer a fixed set of security
questions, split between what the silicon vendor guarantees and what the
firmware vendor guarantees, without assuming Intel-specific mechanisms.

That split is exactly what HSI is missing. Instead of writing a new AMD
check every time AMD does something different from Intel, HSI could ask an
HSTI-shaped question and let each vendor answer it in their own terms.

It could also standardize how OTP-ROM backed root of trust is verified,
today implemented differently for every vendor: Intel Boot Guard, AMD
Platform Secure Boot, ARM Hardware Validated Boot, HP Sure Start, and the
emerging [OCP Caliptra](https://github.com/chipsalliance/caliptra)

The root of trust case is the clearest example. Boot Guard, PSB, Hardware
Validated Boot, Sure Start and Caliptra all do the same job: verify the
first piece of firmware using a key fused into silicon. They are not
interchangeable in implementation, but a well-designed abstraction could
verify "is there a valid fused root of trust" once, and let each vendor
plug in underneath.
-->

---

## HSTI on AMD server

<br>

<center><img src="/slides/img/amd_hsti.png" width="600px"></center>

<!--

HSTI does not cover everything though. Intel and AMD may have their own
definitions of bitfields. Not all of them may be reported, required and
verified. And we rely on what firmware tells us (it may lie about HSTI as well).

Candidates for AMD-specific extensions:

Beyond the structural HSTI idea, here are four concrete things we think HSI
could check on AMD platforms today, independent of any spec rewrite.

Secure Launch gives you a dynamic root of trust measurement, useful as a
second, independent line of evidence alongside the static boot chain.

IOMUX lock and Data Fabric register lock are both about configuration
surfaces that, if left unlocked, let a later, less trusted stage of boot or
even the OS quietly change security-relevant hardware behavior.

SMM Supervisor attestation is about the highest-privilege code path on the
platform. If HSI is going to claim anything meaningful about runtime
security, it needs a way to say whether that supervisor is present and
verified.

Each of these maps to a real attack surface, and each has a plausible
implementation path inside fwupd's existing plugin model. None of them are
trivial, verification always ends up platform-specific in the details, but
they are a concrete next step, not a wishlist.
-->

---

## Summary

<br>

- A open-source AMD server reaches HSI-1 today (HSI-2 if PSB enabled), with
  every HSI-4 requirement met individually, held back by one part choice and
  two interpretation gaps
- Some of what looks like a security regression is actually a reporting
  problem: privilege level and hardware class both change the verdict without
  changing the security profile
- Cross-vendor alignment is the bigger, structural problem, and HSTI is a
  credible foundation to build it on
- We have to act and force vendors to report the security properties of their
  products in a standardized manner

<!-- SPEAKER NOTES
To close: the platform is in good shape. The score does not fully reflect
that yet, for reasons ranging from a flash chip on a bill of materials to a
genuine blind spot in how the test suite reasons about server hardware.

If you take one thing away from this talk, it should be that a security
score is only as trustworthy as its edge cases. We would rather surface
those edge cases in public than let a number stand in for a real
conversation about what a platform does and does not guarantee.

Happy to talk to anyone working on AMD, ARM or general HSI tooling. Thanks
for listening, on to questions.
-->
