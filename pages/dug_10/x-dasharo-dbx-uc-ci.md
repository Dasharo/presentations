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

- Michał Kopeć
- Firmware Engineer working primarily with coreboot and EDK2 but also Heads and
  Linux
- Have been at 3mdeb for 4 years now
- Free and open source software enthusiast
- ThinkPad collector

---

## Microcode

- Microcode is loaded before the CPU begins executing any BIOS code
- It is signed, encrypted and obfuscated and is the root of the overall security
  of your platform
- Modern CPUs will not do anything unless you provide a microcode update
- coreboot's resposibility is to provide microcode updates in the Firmware
  Interface Table (Intel specific)
- For Intel: binaries available in a GitHub repository

---

## DBX

- DBX is the UEFI Secure Boot Revocation database
- Contains hashes of revoked binaries, keys and certificates
- Provides a mechanism to revoke trust in previously trusted entitiess
  - e.g. vulnerable bootloaders
- Updating it is crucial for firmware security
- Provided by the UEFI Forum on a website, and by Microsoft in a GitHub repo
- Microcode sits at the very beginning of the firmware trust chain, and UEFI
  DBX sits at the very end

---

## Updates

- Keeping up to date with each dependency can grow tedious
- We implemented an automation to make the process of updating DBX and ucode
  seamless
- Leverage GitHub Actions to make automations quickly and easily in YAML

---

## Demo

---

