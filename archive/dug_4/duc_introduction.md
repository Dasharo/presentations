<!--
SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>

SPDX-License-Identifier: CC-BY-SA-4.0
-->

class: center, middle, intro

# &#x1F386; Dasharo Configuration Utiliyt Introduction &#x1F386;

.center[<img src="/remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">]

???

---

# Agenda

* Short Introduction to Dasharo Configuration Utility (DUC)
* Exploring Dasharo Configuration Utility v0.2.1
* Q&A

???

---

# Dasharo Configuration Utility

.center.image-80[![](img/dcu_gh.png)]

* The Dasharo Configuration Utility is a tool designed to configure Dasharo
  firmware binary images. It includes task such as customizing the boot logo,
  and setting unique UUIDs or Serial Numbers in SMBIOS tables.
* DCU can be run in two modes - standalone, or as a container. The container
  setup contains all of the prerequisites, so it should be easier to use.
* Bash, Apache 2.0 licensed, https://github.com/Dasharo/dcu

???

* Add link to previous talk, as DRY
* make sure this presentation will be linked in DCU documentation

---

# DCU Vison

### Support for Mass Deployment Features

- **Custom Configuration Profiles**: Enable the creation of custom
  configuration profiles that can be applied across multiple systems, ensuring
  consistency in deployment.
- **Sane Defaults Verification**: Integrate a feature in DCU for verifying and
  aligning user configurations with established sane defaults, ensuring optimal
  security and performance settings for various hardware setups.

### Simplifying Data Transition

- **Data Migration Tools**: Develop options within DCU to facilitate the smooth
  transition of data and settings from proprietary BIOS to Dasharo firmware.

---

# DCU Vison

### Enabling Dasharo Enterprise Features

- **Intel Boot Guard Integration**: Integrate capabilities for fusing Intel
  Boot Guard with customer or user keys during the first boot, enhancing
  security.
- **Enterprise Security Features**: Include advanced security features like TPM
  configuration, secure boot customization, and hardware-based encryption
  support.
- **Chipsec and HSI Checks Integration**: Enhance DCU by incorporating Chipsec
  for in-depth security analysis and Host Security ID (HSI) checks, along with
  other fwupd related assessments, to provide a comprehensive security audit of
  the firmware and hardware.

---

# DCU Vison

### Enabling Dasharo Enterprise Features

- **Integration with Commercial Tools like Binarly**: Expand DCU's capabilities
  by integrating commercial tools such as Binarly Scanner, offering advanced
  scanning and analysis for firmware vulnerabilities, thus elevating the
  utility's effectiveness in identifying and mitigating security risks.

---

# Getting Started

* Clone repo:

```bash
git clone git@github.com:Dasharo/dcu.git
```

* Run container:

```bash
cd dcu && ./dcuc
```

---

# Getting Started

.medium-code[
```text
Unable to find image 'ghcr.io/dasharo/dasharo-sdk:v1.2.0' locally
v1.2.0: Pulling from dasharo/dasharo-sdk
8285c3e1284d: Pull complete
0f8ccaf821af: Pull complete
6e515abfab04: Pull complete
f3904770b5ac: Pull complete
a442011cbbb3: Pull complete
ff420ae8a2ab: Pull complete
0f1475b56e0c: Pull complete
ec99378fd72f: Pull complete
d650a0f92b92: Pull complete
Digest: sha256:12044628c33a77989822f416ef884609d60b7fc5c045183c53e4f97a7080019a
Status: Downloaded newer image for ghcr.io/dasharo/dasharo-sdk:v1.2.0
dcu - Dasharo Configuration Utility

Usage:
  dcu COMMAND
  dcu [COMMAND] --help | -h
  dcu --version | -v

Commands:
  smbios   Edit SMBIOS data in a firmware image
  logo     Insert custom logo boot splash into firmware image
```
]

---

# Feature set

.dp-code[
```bash
dcu - Dasharo Configuration Utility

Usage:
  dcu COMMAND
  dcu [COMMAND] --help | -h
  dcu --version | -v

Commands:
  smbios   Edit SMBIOS data in a firmware image
  logo     Insert custom logo boot splash into firmware image
```
]

---

# Feature set

.medium-code[
```bash
dcu logo - Insert custom logo boot splash into firmware image

Alias: l

Usage:
  dcu logo DASHARO_ROM_FILE [OPTIONS]
  dcu logo --help | -h

Options:
  --logo, -l LOGO (required)
    Custom logo in BMP/PNG/JPG/SVG format to be displayed on boot

  --help, -h
    Show this help

Arguments:
  DASHARO_ROM_FILE
    Dasharo firmware file (e.g. coreboot.rom)

Examples:
  dcu logo coreboot.rom -l bootsplash.bmp
```
]

---

# Feature set

.medium-code[
```bash
dcu smbios - Edit SMBIOS data in a firmware image

Alias: s

Usage:
  dcu smbios DASHARO_ROM_FILE [OPTIONS]
  dcu smbios --help | -h

Options:
  --uuid, -u UUID
    UUID in RFC4122 format to be set in SMBIOS type 1 structure

  --serial-number, -s SERIAL
    Serial number to be set in SMBIOS type 1 and type 2 structure

  --help, -h
    Show this help

Arguments:
  DASHARO_ROM_FILE
    Dasharo firmware file (e.g. coreboot.rom)

Examples:
  dcu smbios coreboot.rom -u 96bcfa1a-42b4-6717-a44c-d8bbc18cbea4
  dcu smbios coreboot.rom -s D07229051
  dcu smbios coreboot.rom -u 96bcfa1a-42b4-6717-a44c-d8bbc18cbea4 -s D07229051

```
]

---
class: center, middle, intro

# Q&A
