---
layout: cover
background: /intro.png
class: text-center

---
## &#x1F44B; Dasharo User Group #8 &#x1F389;

### Dasharo Open Source Firmware Validation Status

<center><img src="/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px"></center>

<!--

Date of previous data snapshot: 09/09/2024
Date of data snapshot: 10/12/2024

-->

---

# Agenda

* Introduction to Dasharo Open Source Firmware Validation (OSFV)
* Current state
* Recent improvements
* Work in progress - current priorities
* Q&A

---
layout: cover
background: /intro.png
class: text-center

---

# Introduction to Dasharo OSFV

---

# <center>Introduction to Dasharo OSFV</center>

* Main purpose
  - validation of (open-source) firmware
    + can be used for any firmware, really 
  - mainly Dasharo with UEFI payload right now
* Using Robot Framework as a base

<center><img src="/common/Robot-framework-logo.png" width="200"></center>

---

# Introduction to Dasharo OSFV

* Use cases
  - testing Dasharo firmware releases
  - test-driven bug fixing (and adding new features)
  - regression testing
    + after introducing new features
    + after major changes (update base from upstream project)
  - validation of Dasharo-related tools (Dasharo Tools Suite, Dasharo
    Configuration Utility)
    + where possible, in QEMU


---

# Typical setup 

- power control
- serial over telnet
- move through firmware menus to switch certain options
- check the result
  - in firmware
  - in OS
    + Dasharo Tools Suite - reference distribution for testing purposes
    + the latest Ubuntu LTS
    + the latest Windows 11
    + QubesOS for some tests

???

TODO: graph with DUT/RTE graphics

---

# One test - step by step

<center><img src="/dug_8/dasharo_main_page.jpeg" width="500"></center>

---

# One test - step by step

<center><img src="/dug_8/dasharo_features.jpeg" width="500"></center>

---

# One test - step by step

<center><img src="/dug_8/dasharo_sec_opts.jpeg" width="500"></center>

---

# One test - step by step

```
    Power On
    ${setup_menu}=    Enter Setup Menu Tianocore And Return Construction
    ${dasharo_menu}=    Enter Dasharo System Features    ${setup_menu}
    ${network_menu}=    Enter Dasharo Submenu    ${dasharo_menu}    Dasharo Security Options
    Set Option State    ${network_menu}    Enable SMM BIOS write    ${TRUE}
    Save Changes And Reset
    Boot System Or From Connected Disk    ubuntu
    Login To Linux
    Switch To Root User
    Get Flashrom From Cloud
    ${out_flashrom}=    Execute Command In Terminal    flashrom -p internal
    Should Contain    ${out_flashrom}    SMM protection is enabled
```

---
layout: cover
background: /intro.png
class: text-center

---

# Current state 

---

# Current state

* We are still failing to define (and reach) criteria for the release
* Right now it worked more like a `rolling release` in `develop` branch
* We wanted to merge `develop` into `main` once we are "ready" but it never happens
* It is confusing to see the default branch (`main`) with very little updates
  and outdated information
* Merged `develop` branch into `main` branch
  - we might use it as the default target branch until we figure it out

<center><img src="/dug_8/osfv_branches_meme.jpg" width="400"></center>

---

# <center>Statistics - tests</center>

<center><img src="/dug_8/osfv_tests_count.png" width="700"></center>

---

# <center>Statistics - Pull Requests</center>

TBD

---

# <center>Statistics - issues</center>

TBD

---
layout: cover
background: /intro.png
class: text-center

---

# Recent improvements 

---

# <center>New tests</center>

* extended CPU suite (P/E cores, HT)
* extended DCU tests 
* introduced more thorough testing of DTS in QEMU 
* suite for TrenchBoot development
  - booting Linux and Xen from meta-trenchboot
* suite for Capsule Updates
* more

---

# <center>New platforms</center>

* Protectli VP2430 
* Protectli VP3210, VP3230
* Odroid H4
* bring back Dell Optiplex - both UEFI and SeaBIOS

???

TBD: odroid photo?

---

# <center>osfv_cli integration</center>

* Integrate low-level hardware operations into Python libraries
* Reuse the same libraries by test framework and CLI tool

<center><img src="/dug_8/osfv_cli_after.png" width="550"></center>

----

# <center>dcu integration</center>

* Alternative interface for changing fw settings*
* Instead of manual steps, we can modify SMMSTORE variables directly

<center><img src="/dug_8/osfv_dcu_integration.png" width="400"></center>

---

# <center>Kyewords docuementation</center>

<center><img src="/dug_8/osfv_keywords_docuementation.png" width="700"></center>

https://dasharo.github.io/open-source-firmware-validation/

---

# Next steps

* Finalize SeaBIOS support
* Focus on repeatability and reliability

* Stabilize the environment for the v0.3.0 release
  - finalize current priority tasks
  - full regression on selected supported platforms
      + NovaCustom
      + Protectli
      + PC Engines
      + QEMU
      + MSI

---

## <center>Dasharo/coreboot PRs</center>

<center><img src="/dug_8/coreboot_prs.png" width="600"></center>
<center><img src="/dug_8/dasharo_coreboot.png" width="650"></center>

<!--

* We keep tempo of around 30 PRs merged per quarter.
* Number of open PRs keep growing at bigger and bigger scale, we trying to
extend our team to support customer requirements.

Modify and run:
./diagrams/dasharo_forks.py

-->

---
layout: two-cols
---

## Dasharo Beta Testing Group

There is not much interest in joining Beta Testing group, so we will hold on
with this effort for some time.

**Tech Preview** - we still plan to introduce some experimental releases, which
would be available to Beta Tester and as paid option to everyone else. Those
will cover some advanced security features like: TrenchBoot, SMI Transfer
Monitor, Intel Boot Guard or similar. This more likely will happen in 2025.

::right::

<center><img src="/dug_7/dasharo_beta_tester.png" width="350"></center>

---

## Free (as free &#x1F37A;&#x1F37B;)

For all those brave souls who are not afraid of bricking their systems we
provide free untested binaries, which are artifacts of our CI/CD.

<center><img src="/dug_8/dasharo_cicd1.png" width="900"></center>

---

## Free (as free &#x1F37A;&#x1F37B;)

<center><img src="/dug_8/dasharo_cicd2.png" width="900"></center>

---

## <center>Dasharo/coreboot upstreaming</center>

<center><img src="/dug_8/coreboot_upstreaming.png" width="600"></center>
<center><img src="/dug_8/dasharo_coreboot_upstraming.png" width="600"></center>

<!--

Top is total:

```shell
./contribution-stats list -r coreboot -s 01/01/2000 -e 06/10/2024 -o dug6.csv
```

Bottom:

```shell
./contribution-stats list -r coreboot -s 03/11/2000 -e 06/10/2024 -o dug6.csv
```

```shell
awk -F';' '{sum += $6} END {print sum}' dug6.csv #added lines
awk -F';' '{sum += $7} END {print sum}' dug6.csv #removed lines
```

-->

---

### <center>Delta `dasharo` branch vs upstream v24.08 tag</center>

<br>

#### <center>`700 files changed, 40702 insertions(+), 2653 deletions(-)`</center>

<br>

### <center>Top Upstreamers</center>

- **Michał Żygowski (miczyg):** +48
  - _soc/intel/cannonlake,skylake: Fix locking SMRAM_
  - _util/superiotool/ite: Add extra dumps for IT8613E EC_
- **Sergii Dmytruk (sergiid):** +2
  - _payloads/edk2/Makefile: detect invalid commit hash on checkout_

<!--

Open file in LibreOffice and sort after lines added, you can limit file by:

```shell
./contribution-stats list -r coreboot -s 06/11/2024 -e 09/09/2024 -o dug6-7.csv
```

-->

---

## <center>Dasharo/edk2 PRs</center>

<center><img src="/dug_8/edk2_prs.png" width="650"></center>
<center><img src="/dug_8/dasharo_edk2.png" width="650"></center>

---

## <center>Dasharo star history</center>

<center><img src="/dug_8/star-history.png" width="650"></center>

<!--

https://star-history.com/#Dasharo/coreboot&Dasharo/docs&Dasharo/dasharo-issues&2024-03-12

-->

---

## <center>Dasharo Matrix Community</center>

### <center>Messages and Users</center>

<center><img src="/dug_8/dasharo_general_matrix.png" width="500"></center>

### <center>Top contributors</center>

<center><img src="/dug_8/dasharo_general_matrix_users.png" width="500"></center>

<!--

* shall we count hanetzer, since he started cooperation with 3mdeb
* tlaurion advanced to top5, he is kind of on par with Demi

Getting number of messages for every user:

```shell
grep -E "\-.+:\s" matrix\ -\ Dasharo\ -\ General\ -\ Chat\ Export\ -\ 2024-03-12T11-16-54.063Z.txt |cut -d"-" -f2|cut -d":" -f1|grep -E "^ "|sort|uniq -c|grep -v "banned"|sort -h|grep -v import|grep -v "'"|grep -v "removed"|grep -v coreboot
```

To count messages add after pipe:

```shell
awk '{sum += $1} END {print sum}'
```

-->

---

<center><img src="/dug_8/dasharo_users.png" width="800"></center>

---

### <center>Most active Dasharo Community Matrix channels since last DUG</center>

<br>

#### <center>Random (`#dasharo-random:matrix.org`)</center>
<br>

#### <center>Dasharo Developers vPub (`#dasharo-osf-vpub:matrix.org`)</center>
<br>

#### <center>Support (`#dasharo-support:matrix.org`)</center>
<!--

General: 32683 (+1648)
Random: 8416 (+601)
vPub: 3888 (+332)
Support: 4018 (+159)
Supermicro: 1659
OSFV: 1112 (+22)

-->
---
layout: cover
background: /intro.png
class: text-center

---

# Questions?

<!--

Comment to satisfy pre-commit

-->
