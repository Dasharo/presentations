---
theme: slidev-template/theme
layout: cover
background: /intro.png
class: text-center
---

# DUG 11 Dasharo vs HSI

---

## HSI level 3 for Dasharo on NovaCustom laptops

* Dasharo on NovaCustom V540TU and V560TU passed HSI-3 as of September 18th
* Current scope: only iGPU models, dGPU models coming soon


<figure>
  <img src="/@fs/repo/img/dug_11/dasharo_hsi_3/hsi3_theme.png" width="300px">
  <figcaption>
    HSI3 for NovaCustom laptops with Dasharo firmware
  </figcaption>
</figure>

<!-- SPEAKER NOTES
Welcome. I want to tell a short story about what it took to get Dasharo on NovaCustom laptops to HSI-3 and what that actually means.

Right now Dasharo on NovaCustom V540TU and V560TU with integrated graphics passes HSI-3. Discrete GPU variants are next in line, but today I will focus on the iGPU models that already hit that level.

The focus of this talk is not just the fact that we reached HSI-3. The interesting part is the journey. We had to line up the CPU, firmware and tools so they all agree on what the machine is actually doing. That meant fighting a couple of dragons in BootGuard and Intel ME land.

This is a fifteen minute overview, not a deep technical training. If you want the full low level details, there is a long technical blogpost that goes through all of this step by step. Here I want to give you the big picture, show you the main obstacles we had to remove and explain why this matters if you care about verifiable platform security.
-->

---

## Why a metric like HSI matters

* Platform security is a mess of low level knobs and vendor features
* HSI compresses that into a single comparable level
* Passing HSI-3 gives a concrete evidence backed claim for NovaCustom with Dasharo

<!-- SPEAKER NOTES
When people ask how secure a given machine is, the answer usually turns into a laundry list. Secure Boot, TPM, some vendor specific root of trust feature, IOMMU settings, debug straps, firmware update methods. It is very easy to get lost in those details.

Users and even many administrators have a hard time comparing two platforms when each has a different mix of marketing names and proprietary mechanisms. It is also hard to explain what is more fundamental and what is just a nice extra.

Host Security ID, or HSI, is an attempt to compress that complexity into a single metric. Instead of saying this system has feature X, Y and Z, you can say this system is HSI level 3 and that one is HSI level 1. Higher levels imply stricter and more complete security properties.

There are very few open, vendor neutral benchmarks in this space. HSI is not perfect or finished, but it is documented, it can be implemented in open source and it is evolving in public.

For NovaCustom machines with Dasharo, reaching HSI-3 means we now have a concrete, open and checkable way to talk about their platform security level.
-->

---

## How HSI works in practice

* Open specification maintained by engineers from several companies and research teams
* Implemented in fwupd, using data from firmware, kernel, TPM and Intel ME state
* Levels HSI-1 to HSI-4 accumulate requirements, with a planned HSI-5 for attestation

<figure>
  <img src="/@fs/repo/img/dug_11/dasharo_hsi_3/how_hsi_works.png" width="450px">
</figure>

<!-- SPEAKER NOTES
In concrete terms HSI is two things. It is a written specification and it is an implementation inside fwupd, the standard Linux firmware update stack.

The spec is maintained in public by people who work very close to firmware and platform security. That includes fwupd maintainers, CPU vendor engineers and independent security researchers. You can go and read the document, discuss it and point out problems.

The code side lives in fwupd. Many Linux distributions already ship fwupd for firmware updates. The same tool can now also score a host. There is no special proprietary scanner. You just run a standard command on a standard system.

fwupd collects information from several places. It reads what the firmware publishes, it checks TPM capabilities and measurements, it inspects parts of the kernel configuration and it looks at Intel ME state on Intel systems. It then evaluates a set of conditions grouped into levels HSI-1 to HSI-4. A planned HSI-5 covers external attestation.

The levels are cumulative. If you say HSI-3 you are also saying all the HSI-1 and HSI-2 conditions are satisfied. Missing one lower level requirement blocks higher levels. That is important for reasoning about real security posture instead of cherry picking a few favorite features.
-->

---

## Measured boot and Dasharo Trustroot

* Each boot stage measures what it runs into the TPM before handing over control
* Dasharo Trustroot makes that chain coherent from BootGuard through coreboot and UEFI to the OS

<figure>
  <img src="/@fs/repo/img/dug_11/dasharo_hsi_3/measured_boot_trustroot.png" width="450px">
  <figcaption>
    Measured boot chain of trust
  </figcaption>
</figure>


<!-- SPEAKER NOTES
The central idea behind measured boot is simple. Every stage in the boot process leaves a breadcrumb in the TPM before it passes control to the next stage. That breadcrumb is a hash of what actually ran.

On platforms with Intel BootGuard the very first link in this chain is in hardware. The CPU checks that the boot block is signed with the correct key and if that passes it extends a hash of that block into PCR0 in the TPM. That happens before any of our own firmware code executes.

After that coreboot and the Dasharo UEFI payload continue the measurement chain. They measure what they load and configure, and they add entries to an event log in memory. The operating system can read that event log and the TPM registers.

Dasharo Trustroot is the set of conventions and code that make this chain coherent. We make sure that BootGuard measurements are reconstructed correctly, that coreboot and UEFI agree on which TPM bank and which event log to use and that the operating system sees a single consistent story.

From the point of view of fwupd and other tools, this becomes a clear line from BootGuard through Dasharo firmware to the operating system, backed by concrete measurements instead of promises.
-->

---

## Dragon I: PCR0 reconstruction and TPM locality

* At first hardware, firmware and tools disagreed on what BootGuard put into PCR0
* A policy register bit and a non default TPM locality changed how the hash should be computed and interpreted
* After fixing reconstruction and logging, HSI now reports valid PCR0 reconstruction

<figure style="float:left; width:400px; text-align:center">
  <img src="/@fs/repo/img/dug_11/dasharo_hsi_3/dragon_one.png">
</figure>

<figure style="float:right; width:400px; text-align:center">
  <img src="/@fs/repo/img/dug_11/dasharo_hsi_3/dragon_alt.png" width="200px">
  <figcaption>
    Dragon I
  </figcaption>
</figure>


<!-- SPEAKER NOTES
The first dragon we had to fight was PCR0 reconstruction. PCR0 is special in HSI because it anchors the hardware based trust chain. If firmware cannot reproduce what BootGuard put into PCR0, you cannot really claim a solid root of trust.

On NovaCustom Meteor Lake systems three things combined to cause trouble. A masking bit in the ACM policy register changes how its value is treated when BootGuard computes the hash. BootGuard also uses TPM locality 3 for startup, which older tools did not expect. And early coreboot code did not record this locality information properly in the event log.

The result was that hardware, firmware and user space tools all had slightly different views. In some cases firmware reconstructed a different hash than BootGuard had extended. In others the hash was actually correct, but tpm2 tools and fwupd misinterpreted the log because they assumed locality 0 and printed a mismatch.

We fixed the ACM policy handling in firmware, we made sure coreboot and EDK2 log the correct locality and we updated the event log layout so BootGuard and Dasharo measurements line up. Once all three layers agreed, the HSI line for PCR0 reconstruction turned green and reflected what BootGuard actually did in hardware.
-->

---

## Dragon II: fused BootGuard, Intel ME and updates

* Fused platforms permanently lock BootGuard policy, flash layout and ME related settings
* Classic one shot capsule updates assume a warm reset with the capsule kept in RAM, while safe ME updates need ME disabled and a cold reset
* Dasharo moved fused systems to a staged update path that keeps ME updatable without weakening the fused security model

<figure>
  <img src="/@fs/repo/img/dug_11/dasharo_hsi_3/dragon_alt.png" width="200px">
  <figcaption>
    Dragon II
  </figcaption>
</figure>

<!-- SPEAKER NOTES
The second dragon lives at the intersection of BootGuard, Intel ME and firmware updates.

For higher HSI levels you want a fused and locked platform. That means BootGuard policy is fused, the flash descriptor is locked and ME related configuration bits cannot be changed from the operating system any more. From a security point of view this is what you want. From an update point of view it breaks old assumptions.

The traditional capsule model assumes you can place a complete flash image in RAM, trigger a warm reset and let firmware reflash everything, including the descriptor and ME. That depends on RAM surviving across the reset.

Safe ME handling requires the opposite. You disable ME and do a cold reset so the management engine actually restarts in a controlled way. A cold reset clears RAM, so any capsule stored there is gone.

We investigated whether ME override commands like HMRFPO could bridge this, but experiments showed they do not survive the warm reset the way some documents suggest. In practice you cannot rely on them.

The conclusion is that fused platforms need a different update model. In Dasharo we moved to a staged update path. One BIOS update prepares a safe ME update channel under the fused constraints. A follow up update uses that channel to refresh ME. This lets us keep ME updatable without loosening the permanent security properties that HSI expects.
-->

---

## Hardware limits and path to HSI-4

* HSI-4 needs SMAP plus full RAM encryption via Total Memory Encryption
* Current NovaCustom Meteor Lake CPUs lack usable TME, so they are capped at HSI-3
* Dasharo can reach HSI-4 as soon as it runs on hardware that actually exposes TME

<figure>
  <img src="/@fs/repo/img/dug_11/dasharo_hsi_3/hw_limit.png" width="400px">
  <figcaption>
    Hardware limit: no Total Memory Encryption
  </figcaption>
</figure>


<!-- SPEAKER NOTES
HSI levels are not only about firmware configuration. At the higher levels they depend directly on CPU and memory controller features.

HSI-4 specifically requires two things at once. The first is SMAP, a CPU feature that enforces separation between user and kernel memory accesses. The second is full RAM encryption, and on Intel that means Total Memory Encryption implemented in the memory controller.

On current NovaCustom Meteor Lake laptops TME is not exposed in a way that makes it usable for this purpose. That means they are capped at HSI-3 no matter how much effort we put into firmware. You cannot get HSI-4 without those silicon features.

The good news is that the firmware side is ready. Dasharo Trustroot is designed to take advantage of SMAP and TME when they exist. Once Dasharo runs on hardware that properly implements and exposes TME, the same approach can drive those platforms to HSI-4.

So HSI makes the boundary clear. Firmware cannot invent features the CPU does not have, but it can fully use and expose whatever the hardware provides, and you can see that reflected in the level.
-->

---

## How you can verify it yourself

* From the OS, cbmem and tpm2 tools show BootGuard status and PCR0 details
* Dasharo Setup UI exposes BootGuard state without parsing logs
* fwupdmgr security or fwupdtool security give a high level HSI score backed by the same evidence

<figure>
  <img src="/@fs/repo/img/dug_11/dasharo_hsi_3/check_yourself.png" width="400px">
</figure>

<!-- SPEAKER NOTES
One important part of this story is that you do not have to take anyone’s word for it. You can see the evidence yourself.

From the operating system side, cbmem shows coreboot’s view of CBnT and BootGuard. You see whether the BIOS is trusted, which TPM locality was used for startup and what PCR0 digest was calculated for the measured S CRTM.

tpm2_eventlog reads the same information from the TPM event log. There you can see the startup locality event and an action entry that decodes to Boot Guard Measured S CRTM with the same hash value. That ties the digest to a specific measurement in the chain.

If you prefer a more user friendly view, Dasharo’s Setup UI has a menu page that shows BootGuard state graphically. You can confirm at a glance that BootGuard is active and how it is configured, without running any tools.

On top of that you have fwupdmgr security or fwupdtool security. These commands combine all of this information into a single HSI report. You get the overall level at the top and a list of checks per level, so you can see both the summary and the underlying conditions on a real machine.
-->

---

## Value proposition and call to action

* HSI-3 on NovaCustom means hardware, firmware and tools now agree on one verifiable story
* Open coreboot and EDK2 firmware make every measurement, policy and update path auditable
* Dasharo Trustroot is a ready implementation of a hardware root of trust that passes HSI checks on supported platforms
* We help with hardware root of trust deployments, platform bring up and custom firmware projects
* To talk about your platform, contact [contact@3mdeb.com](mailto:contact@3mdeb.com) or subscribe to the Dasharo newsletter

<figure>
  <img src="/@fs/repo/img/dug_11/dasharo_hsi_3/trustroot.png" width="300px">
</figure>


<!-- SPEAKER NOTES
Getting to HSI-3 on NovaCustom was not a matter of flipping a configuration bit and printing a new logo. It meant getting the CPU, the firmware stack and user space tools to line up so they all report the same measurements and the same policies. The dragons we discussed were real problems that had to be solved before the level could be claimed honestly.

Because Dasharo is built on coreboot and EDK2, and because we work in the open, every part of this is visible. The code, the event formats and the logs are all available for review and for independent testing. That is a different model from closed firmware that only tells you to trust it.

Dasharo Trustroot is the concrete implementation that comes out of this work. On supported platforms it gives you a hardware based root of trust that passes HSI checks and a toolbox you can use to verify it yourself.

If you want similar properties on your own hardware, we can help. That includes designing and deploying hardware roots of trust, bringing up new platforms with BootGuard and measured boot and tailoring firmware behavior to your use case. To discuss a project you can email contact@3mdeb.com or reach out through the Dasharo newsletter and we can continue the conversation from there.
-->

---

## DEMO

We're going to SSH into two laptops, 

* NovaCustom V560TU, newest Dasharo, set up to reach HSI 3
* Lenovo Thinkpad T460s, WiP coreboot port

...and we're going to compare HSI reports in real time.

<figure>
  <img src="/@fs/repo/img/dug_11/dasharo_hsi_3/demo.png" width="400px">
  <figcaption>
    ThinkPad T460s vs NovaCustom V56
  </figcaption>
</figure>

<!-- SPEAKER NOTES

I'll share my screen and SSH into two laptops, the HSI-3 V56 and a Thinkpad
T460s. If anyone remembers my previous talk on deguard and lifting BootGuard
on 6th-8th gen Intels, this is an update - I've confirmed deguard works on
the T460s, and I've got a base port of coreboot in progress.

-->

