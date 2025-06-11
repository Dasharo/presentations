---
theme: ../../slidev-template/theme
layout: cover
background: /intro.png
class: text-center

---

## Enhancements in Dasharo CI: Automatic DBX and microcode refresh

---

## Agenda

- Introduction
- DBX and microcode
- Automations
- Closing thoughts

---

## Introduction

<div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
  <img src="/../../img/mkopec.jpg" style="width: 100px; border-radius: 50%;" alt="Profile Picture">
  <div>
    <b style="font-size: 1.5em;">Michał Kopeć</b><br>
    <i style="font-size: 1.2em;">Firmware Engineer</i>
  </div>
</div>

<div style="display: flex; justify-content: space-between; align-items: center; font-size: 1.2em;">
  <div>
    🔑 <code>869E 9AE8 AFDB 5FAE 6068  338B 99BD 2EEE E2D0 CE31</code><br>
    ✉️ <a href="mailto:michal.kopec@3mdeb.com">michal.kopec@3mdeb.com</a><br>
    🔗 <a href="https://www.linkedin.com/in/michał-kopeć-a8b216200/">LinkedIn</a><br>
    💻 <a href="https://github.com/mkopec">GitHub</a><br>
  </div>
</div>

- Firmware Engineer working primarily with coreboot and EDK2 but also Heads and
  Linux
- Have been at 3mdeb for 4 years now
- Free and open source software enthusiast
- ThinkPad collector

---

## Key Security Components & Trust

* **Microcode Updates:**
  - Processor-level fixes/mitigations (e.g., Spectre, Meltdown).
  - Applied very early by coreboot.
* **UEFI DBX (Revocation Database):**
  - Part of UEFI Secure Boot.
  - Revokes compromised binaries (e.g., BootHole exploit) and signing certificates.
* **Firmware Chain of Trust:**
  - Microcode -> coreboot -> UEFI -> Bootloader -> OS.
  - Each stage verifies the next.

<center><img src="/../../img/dug_10/dasharo_boot_diagram.png" width="900"></center>

---

## Our Goal: Consistent & Timely Security

* Ensure critical components (Microcode, DBX) are **always** up-to-date.
* Reduce risk of oversight.
* Free up developer resources.
* **Solution:** Automation!

---

## The Intel boot process

<center><img src="/../../img/dug_10/intel-boot-diagram.png" width="600"></center>

- PMC starts executing -> CSME loads code from ROM -> CSME executes boot
  extensions and begins bringup -> Releases CPU from reset
- CPU loads ucode and ACMs (optional) from FIT table -> BtG ACM verifies BIOS ->
  BIOS is allowed to execute

<!--
- CSME has a MinuteIA processor core that behaves much like a regular 486
- CSME ROM is protected by fuse that is burned by Intel during production
- CSME ROM acts like a 486 BIOS
- CSME maps the ROM Boot Extensions partition from SPI flash
- RBE verifies and loads the CSME OS, performs antirollback check, initializes
  secure components
- RBE initiates the Bring-up phase
- BUT initializes services
- CPU is finally released from reset
- CPU starts with loading ucode from the FIT table
- CPU loads BtG ACM from FIT if present, which enforces BIOS verification
- BIOS is allowed to run
-->

---

## Component Deep Dive: Intel Microcode

* **Source:** [Intel's GitHub](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files)
* **Purpose:** Fix security advisories, functional issues, and errata.
  - Often essential for basic CPU operation.
* **Loading:**
  - By coreboot via Firmware Interface Table (FIT) – _before coreboot itself runs!_
  - OS can load updates, but firmware-level is earlier & more comprehensive.
* **Example Vulnerability Patched:**
  - **INTEL-SA-01139:** Privilege escalation via UEFI module input validation.

---

## Component Deep Dive: UEFI DBX

* **Source:** [UEFI Forum](https://uefi.org/revocationlistfile) / [Microsoft GitHub](https://github.com/microsoft/secureboot_objects)
  - We use Microsoft's Git repo for easier automation & prompt updates.
  - Discrepancy highlights need for reliable, scriptable sources.
* **Purpose:** Revokes signatures of previously approved firmware/software.
  - Critical for mitigating bootkits (e.g., BlackLotus) and compromised bootloaders.
  - Revoking certificates is powerful: invalidates many binaries with one update.
* **Example Vulnerability Mitigated:**
  - **CVE-2022-21894 (BlackLotus):** Persistent UEFI bootkit bypassing Secure Boot.

---

## The Automation: GitHub Actions

* **Why GitHub Actions?**
  - Tight integration with our GitHub codebase.
  - Declarative YAML syntax.
  - Wide range of community-supported actions (e.g., for creating PRs).
* Daily checks for updates to Microcode and DBX.

<center><img src="/../../img/dug_10/gha_logo.png" width="150"></center>

---
layout: two-cols-header
---

## Automation: Microcode Update Workflow

::left::

```yaml
# Microcode Check Snippet
- name: Check if µcode submodule is up to date
  run: |
    git submodule update --init --checkout 3rdparty/intel-microcode
    pushd 3rdparty/intel-microcode
    current=<span class="math-inline">\(git log \-1 \-\-pretty\=format\:"%H"\)
git checkout main \# Switch to main to get the latest
new\=</span>(git log -1 --pretty=format:"%H")
    if [[ $current == $new ]]; then
      echo "Intel µcode submodule is up-to-date."
    else
      echo "Intel µcode submodule is out of date!"
      exit 1
    fi
    popd
```

::right::

<center><img src="/../../img/dug_10/ucode-update-diagram-a.png" width="200"></center>

---
layout: two-cols-header
---

## Automation: Microcode Update Workflow (Cont.)

::left::

### 2. Update & Create PR (if check failed)
* Checkout Dasharo code.
* Update intel-microcode submodule to its main branch.
* Use peter-evans/create-pull-request action to submit a PR.
* Design Rationale: Git submodule pins specific versions & tracks changes transparently.

::right::

<center><img src="/../../img/dug_10/ucode-update-diagram-b.png" width="200"></center>

---

## Automation: UEFI DBX Update Workflow

### 1. Check Daily
* Checkout Dasharo edk2 code.
* Checkout microsoft/secureboot_objects repository.
* Calculate SHA256 of current DBXUpdate.bin in Dasharo.
* Calculate SHA256 of latest DBXUpdate.bin from Microsoft.
* If checksums differ -> exit 1.

```yaml
# DBX Check Snippet
- name: Check if DBX is out-of-date
  run: |
    old=$(sha256sum edk2/DasharoPayloadPkg/SecureBootDefaultKeys/DBXUpdate.bin | awk '{ print <span class="math-inline">1 \}'\)
new\=</span>(sha256sum secureboot_objects/PostSignedObjects/DBX/amd64/DBXUpdate.bin | awk '{ print $1 }')
    if [ "$old" = "$new" ]; then
      echo 'UEFI DBX is up-to-date.'
    else
      echo 'UEFI DBX is out of date.'
      exit 1
    fi
```

---

## Automation: UEFI DBX Update Workflow (Cont.)

### 2. Update & Create PR (if check failed)
* Copy the new DBXUpdate.bin from secureboot_objects into Dasharo edk2 tree.
* Use peter-evans/create-pull-request action to submit a PR.
* Design Rationale: Checksum comparison is straightforward for single-file artifacts.

---

## Human Oversight: The PR Review Process

* Automated PRs are not automatically merged!
* Standard Dasharo Review Process:
  - Developers review changes.
  - Ensure correct integration.
  - Test on relevant hardware platforms.
* Result: Balances timeliness with stability.

---

## Benefits: Security & Transparency

* Enhanced Security:
  - Regular, automated updates minimize vulnerability windows.
* Increased Transparency:
  - Open repositories and CI workflows.
  - Users can see update status and history.
  - Community can audit processes and adapt methods.
* Contrast: Many proprietary firmware solutions are opaque about update contents and schedules.

---

## Closing Thoughts

* Automated checks for microcode and DBX make Dasharo firmware:
  - More Secure: By ensuring timely updates.
  - More Transparent: Through open processes.
* Builds user trust and empowers them with knowledge.
* We hope this makes Dasharo safer and more worthy of our users' trust.
* The code is open, feel free to check it out and post your improvements!
