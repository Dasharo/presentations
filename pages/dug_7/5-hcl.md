---
theme: ../../slidev-template/theme
layout: cover
background: /intro.png
class: text-center

---

## &#x1F44B; Enhancing Hardware Compatibility: Best Practices and Tools for Dasharo HCL Maintainers &#x1F44B;

<center><img src="/../../img/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px"></center>

---

# What is HCL?

> A Hardware Compatibility List (HCL) is a curated list that specifies which
> hardware components are officially supported by a specific operating system,
> software platform, or firmware. It helps users and administrators ensure that
> the hardware they intend to use is compatible and will work optimally with
> their system or software environment.

* Serious UEFI BIOS development is function of hardware you can validate.
* HCL remove obstacles for buyers: _Is this GPU/CPU/memory model compatible
Dasharo?_
* Lack of awareness about hardware capabilities leads to inability to evaluate
system posture from security,performance,compliance, (.etc) perspective.

<!--

1. **Introduction to HCL and its Importance (3 min)**
   - Briefly define what an HCL is and its role in open-source firmware.
   - Explain why maintaining an accurate and up-to-date HCL is crucial for the Dasharo firmware ecosystem.

2. **Overview of the Dasharo HCL (3 min)**
   - Provide context on Dasharo's approach to managing HCL.
   - Mention the Dasharo HCL Maintainer documentation and its purpose for maintainers.

3. **Best Practices for HCL Maintenance (4 min)**
   - Discuss the key principles of maintaining an HCL.
   - Emphasize the importance of consistency, clarity, and regular updates.
   - Outline common challenges and how to avoid them.

4. **Tools and Methodologies for HCL Management (6 min)**
   - Introduce the essential tools like the **DTS Hardware Configuration Generator (dts-hw-conf-gen)** and other scripts.
   - Demonstrate how these tools streamline the process of verifying and reporting hardware compatibility.
   - Walk through a typical workflow for parsing and updating HCL reports, using examples where appropriate.

5. **Extending and Maintaining the HCL (3 min)**
   - Discuss how developers and maintainers can contribute to expanding the HCL.
   - Highlight the collaborative nature of the process and encourage participation in maintaining the HCL for robust hardware support.

-->

---

<center><img src="/../../img/dug_7/dasharo_hcl.png" width="550"></center>

<!--

Problem statement: Dasharo HCL is update way to rarely

-->

---

<center><img src="/../../img/dug_7/dasharo_hcl_page.png" width="750"></center>

<!--

Where to find Dasharo HCL?

Go to docs.dasharo.com->Supported Hardware ...

-->

---

* In 3mdeb we currently sitting on 10 GB of compressed HCL reports compressed.
* Last update of HCL for MSI Pro series was 20th July 2023.
* In this 10GB of data we gathered:
  * 1331 HCL reports.
  * 385 for devices booted using Dasharo.
  * 17 unique Dasharo supported hardware platforms.

<!--

Following command print all tar.gz (assuming HCL) files:

```shell
unzip -l dasharo_hcl_reports.zip|grep tar.gz|awk '{for(i=4;i<=NF;++i) printf "%s%s", $i, (i==NF?ORS:OFS)}'|awk -F'/' '{print $NF}'|wc -l
```

-->

---

* Among HCLs dumped are many interesting vendors without Dasharo support:

```shell
BROUNION_R86S_5.19
GoWin_Solution_R86S_JSP18418
Hewlett-Packard_HP_Compaq_8200_Elite_SFF_PC_J01_v02.33
Hewlett-Packard_HP_Compaq_Elite_8300_SFF_K01_v02.98
LENOVO_20351_9ACN25WW
LENOVO_2325B15_G2ETB1WW_(2.71_)
LENOVO_2325L19_CBET4000_4.16-1239-gd5c31acee4-dirty
MSI_MS-7817_V17.5
NZXT,_Inc._MS-7D25_1.70
PC_Specialist_LTD_NS50MU_1.07.15N
PC_Specialist_LTD_NV4XMB,ME,MZ_1.07.14NRTR1
System_manufacturer_System_Product_Name_3601
TAROX_Lightpad_1550_1.07.11NTBCA3
Techvision_TVI7309X_5.19
Thomas-Krenn.AG_Super_Server_2.0b
VPU_Company_VWNC71429_V1.8.X
Wortmann_AG_1220767;1470407_1.07.09
bluechip_bluechip_SERVERline_3.3
sugon_24000635_3309___
(...)
```

* We are very happy there is so big interest in Dasharo HCL.

<!--

TODO: what is redundancy level?

-->

---

## Dasharo Tools Suite Hardware Compatibility List Manager

Written in BASH with CLI auto-generated by [bashly](https://bashly.dannyb.co/).
Apache 2.0 licensed.

```shell
dts-hclmgr - Dasharo Tools Suite Hardware Compatibility List Manager

Usage:
  dts-hclmgr [OPTIONS] COMMAND
  dts-hclmgr [COMMAND] --help | -h
  dts-hclmgr --version | -v

Commands:
  cpu         Generate CPU compatibility list documentation for Dasharo Universe website.
  memory      Generate memory compatibility list documentation for Dasharo Universe website.
  gpu         Generate GPU compatibility list documentation for Dasharo Universe website.
  mainboard   Generate mainboard compatibility list documentation for Dasharo Universe website.

(...)
```

<center>

## https://github.com/Dasharo/dts-hw-conf-gen

</center>

---

Using it for mass analysis:

```shell {all|1|2|3|all}
unzip -o /tmp/filename.zip && \
find . -name "platform_name_prefix*.tar.gz" -print0 | \
xargs -0 -n1 bash -c './dts-hclmgr cpu "$0"'
```

Of course we would like to gather HCL for `cpu`, `gpu`, `memory` and
`mainboard`.

Support for `gpu` is limited and `mainboard` at this point is not supported. We
still wonder if there is value for it.

Example call of command may look as follows:

```shell
unzip -o workspace/dasharo_hcl_reports.zip && \
find . -name "Micro-Star_International_Co.,_Ltd._MS-7D25*.tar.gz" -print0 | \
xargs -0 -n1 bash -c './dts-hclmgr cpu "$0"'
```

<!--

[click]
- `unzip -o`: Extracts the contents of `/tmp/filename.zip` into the current directory. It is our 10GB of HCLs.

[click]
- `find .`: Searches recursively in the current directory (`.`) for files.
- `-name "platform_name_prefix*.tar.gz"`: Looks for files whose names start with `platform_name_prefix` and end with `.tar.gz`. We mean Dasharo Supported hardware. Details in README.md
- `-print0`: Outputs the file names found in the previous step, separating them with a null character (`\0`) rather than a newline. This is useful to handle file names that may contain spaces or special characters.

[click]
- `xargs -0`: Reads the null-terminated output from `find` (produced by `-print0`) to handle file names safely.
- `-n1`: Ensures that `xargs` passes one file at a time to the command.
- `bash -c './dts-hclmgr cpu "$0"'`: Executes the command in a Bash shell.
  - `./dts-hclmgr cpu "$0"`: Runs the script or executable `dts-hclmgr` with the argument `cpu` and passes the `.tar.gz` file as an additional argument (`$0` is the current argument in the Bash shell context).

-->

---

## MSI PRO Z690-A CPU HCL results

* `cpuinfo` changed for 14th Gen Intel Core CPUs, it seems that generation number is no longer added.

```shell
| 13th Gen Intel(R) Core(TM) i5-13600K | v1.1.2 | Dasharo HCL Report |
| 12th Gen Intel(R) Core(TM) i9-12900T | v1.1.0 | Dasharo HCL Report |
| Intel(R) Core(TM) i7-14700K | v0.9.0 | Dasharo HCL Report |
```

* 15 new combinations of CPU + Dasharo were added.
* CPUs from 12th, 13th and 14th generations are present on the list.
* 12th Gen is most extensive and contain all tiers from i3, through i5, i7 to
i9.
* We decided to connect CPU HCL lists for `PRO Z690 (WIFI) DDR4` and `PRO Z690
(WIFI)` (aka `DDR5`).
  * Both boards are supported by the same silicon initialization code,
  * distinguishing boards cause additional overhead to HCL creation and maintenance,
  * it is confusing for users to differentiate between mainboard versions,

Please check: TBD

---

```diff
+        | 12th Gen Intel(R) Core(TM) i9-12900K | v1.1.1 | Dasharo HCL Report |
+        | 12th Gen Intel(R) Core(TM) i3-12100 | v1.1.1 | Dasharo HCL Report |
+        | 12th Gen Intel(R) Core(TM) i3-12100T | v1.1.1 | Dasharo HCL Report |
+        | 12th Gen Intel(R) Core(TM) i5-12400 | v1.0.0 | Dasharo HCL Report |
         | 12th Gen Intel(R) Core(TM) i5-12400F | - | [Github PR][3] |
         | 12th Gen Intel(R) Core(TM) i5-12400F | v1.1.0 | Dasharo HCL Report |
+        | 12th Gen Intel(R) Core(TM) i5-12400F | v1.1.1 | Dasharo HCL Report |
+        | 12th Gen Intel(R) Core(TM) i5-12400F | v1.1.3 | Dasharo HCL Report |
         | 12th Gen Intel(R) Core(TM) i5-12500T | v1.1.0 | Dasharo HCL Report |
         | 12th Gen Intel(R) Core(TM) i5-12500T | v1.1.0 | Dasharo HCL report |
         | 12th Gen Intel(R) Core(TM) i5-12600 | v1.1.0 | Dasharo HCL Report |
```

---

```diff
         | 12th Gen Intel(R) Core(TM) i5-12600K | v1.1.0 | Dasharo HCL report |
         | 12th Gen Intel(R) Core(TM) i5-12600K | v1.1.1 | Dasharo HCL Report |
         | 12th Gen Intel(R) Core(TM) i5-12600K | v1.1.1-rc4 | Dasharo HCL Report |
+        | 12th Gen Intel(R) Core(TM) i5-12600K | v1.1.2 | Dasharo HCL Report |
+        | 12th Gen Intel(R) Core(TM) i5-12600K | v1.1.3 | Dasharo HCL Report |
         | 12th Gen Intel(R) Core(TM) i7-12700K | v1.0.0 | Dasharo HCL Report |
         | 12th Gen Intel(R) Core(TM) i7-12700K | v1.0.0 | Dasharo HCL report |
         | 12th Gen Intel(R) Core(TM) i7-12700K | v1.0.0 | [Qubes HCL reports][2] |
         | 12th Gen Intel(R) Core(TM) i7-12700K | v1.1.0 | Dasharo HCL Report |
         | 12th Gen Intel(R) Core(TM) i7-12700K | v1.1.1 | Dasharo HCL Report |
+        | 12th Gen Intel(R) Core(TM) i7-12700K | v1.1.3 | Dasharo HCL Report |
+        | 12th Gen Intel(R) Core(TM) i7-12700KF | v1.1.1 | Dasharo HCL Report |
         | 12th Gen Intel(R) Core(TM) i9-12900K | v0.4.0 | [Qubes HCL reports][1] |
         | 12th Gen Intel(R) Core(TM) i9-12900K | v1.1.0 | Dasharo HCL Report |
+        | 12th Gen Intel(R) Core(TM) i9-12900K | v1.1.1 | Dasharo HCL Report |
+        | 12th Gen Intel(R) Core(TM) i9-12900K | v1.1.2 | Dasharo HCL Report |
         | 12th Gen Intel(R) Core(TM) i9-12900KF | v1.1.1 | [Github PR][4] |
         | 12th Gen Intel(R) Core(TM) i9-12900KS | v1.1.1 | Dasharo HCL Report |
         | 12th Gen Intel(R) Core(TM) i9-12900T | v1.1.0 | Dasharo HCL Report |
+        | 13th Gen Intel(R) Core(TM) i5-13600K | v0.9.0 | Dasharo HCL Report |
+        | 13th Gen Intel(R) Core(TM) i5-13600K | v1.1.2 | Dasharo HCL Report |
+        | 14th Gen Intel(R) Core(TM) i7-14700K | v0.9.0 | Dasharo HCL Report |
```

---

## MSI PRO Z690-A Memory HCL results
* 21 new combinations of memory modules + Dasharo were added.
* Modules with various speeds are support from 2133 MT/s to even 3200 MT/s (in
case of Samsung).
* Ranking of reported modules:
  * Kingston - 17 reported combinations
  * Corsair - 11
  * Crucial - 4
* We decided to connect CPU HCL lists for `PRO Z690 (WIFI) DDR4` and `PRO Z690
(WIFI)` (aka `DDR5`).
  * Both boards are supported by the same silicon initialization code,
  * distinguishing boards cause additional overhead to HCL creation and maintenance,
  * it is confusing for users to differentiate between mainboard versions,

Please check: TBD

---

## MSI PRO Z690-A Memory HCL results

```diff
+| Corsair | CMH16GX4M2E3200C16 | 8192 MB | 2133 MT/s (PC4-17000) | -/-/&#10004 | v1.1.1 | Dasharo HCL report |
+| Corsair | CMK16GX4M1D3000C16 | 16384 MB | 2133 MT/s (PC4-17000) | &#10004/-/- | v1.1.1 | Dasharo HCL report |
 | Corsair | CMK16GX4M2B3200C16 | 16384 MB | 2133 MT/s (PC4-17000) | &#10004/-/- | v1.1.1 | Dasharo HCL report |
 | Corsair | CMK16GX4M2B3200C16 | 16384 MB | 2133 MT/s (PC4-17000) | -/-/&#10004 | v1.1.0 | Dasharo HCL report |
 | Corsair | CMK16GX4M2B3200C16 | 32768 MB | 2133 MT/s (PC4-17000) | &#10004/-/- | v1.1.1 | Dasharo HCL report |
+| Corsair | CMK16GX4M2B3200C16 | 8192 MB | 2133 MT/s (PC4-17000) | -/-/&#10004 | v1.1.1 | Dasharo HCL report |
+| Corsair | CMK32GX4M2B3200C16 | 16384 MB | 2133 MT/s (PC4-17000) | &#10004/-/- | v1.0.0 | Dasharo HCL report |
+| Corsair | CMK32GX4M2E3200C16 | 16384 MB | 2133 MT/s (PC4-17000) | &#10004/-/- | v1.1.1 | Dasharo HCL report |
 | Corsair | CMK32GX4M2E3200C16 | 16384 MB | 2133 MT/s (PC4-17000) | -/&#10004/- | v1.1.1 | [Github PR][4] |
+| Corsair | CMK32GX4M2E3200C16 | 16384 MB | 2133 MT/s (PC4-17000) | -/-/&#10004 | v1.1.0 | Dasharo HCL report |
+| Corsair | CMK64GX4M2E3200C16 | 32768 MB | 2133 MT/s (PC4-17000) | &#10004/-/- | v1.1.1 | Dasharo HCL report |
 | Crucial Technology | BL16G32C16U4B.16FE | 16384 MB | 2666 MT/s (PC4-21300) | &#10004/-/- | v1.1.0 | Dasharo HCL report |
 | Crucial Technology | BL16G32C16U4B.16FE | 16384 MB | 2666 MT/s (PC4-21300) | &#10004/-/- | v1.1.1 | Dasharo HCL report |
+| Crucial Technology | BLS16G4D32AESB.M16FE | 16384 MB | 2400 MT/s (PC4-19200) | &#10004/-/- | v1.1.1 | Dasharo HCL report |
 | Crucial Technology | CT8G4DFS8266.C8FJ | 8192 MB | 2666 MT/s (PC4-21300) | &#10004/-/- | v1.1.0 | Dasharo HCL report |
+| Essencore Limited (former ISD Technology Limited) | KD4AGU880-36A180X | 16384 MB | 2666 MT/s (PC4-21300) | -/-/&#10004 | v1.1.1 | Dasharo HCL report |
+| G Skill Intl | F4-3600C18-32GVK | 32768 MB | 2666 MT/s (PC4-21300) | &#10004/-/- | v1.1.2 | Dasharo HCL report |
 | Kingston | KF3200C16D4/16GX | 16384 MB | 2400 MT/s (PC4-19200) | &#10004/-/- | v1.1.1 | Dasharo HCL report |
 | Kingston | KF3200C16D4/16GX | 16384 MB | 2400 MT/s (PC4-19200) | -/-/&#10004 | v1.1.1 | Dasharo HCL report |
+| Kingston | KF3200C16D4/32GX | 32768 MB | 2400 MT/s (PC4-19200) | &#10004/-/- | v1.1.1 | Dasharo HCL report |
 | Kingston | KF3200C16D4/32GX | 32768 MB | 2400 MT/s (PC4-19200) | -/-/&#10004 | v1.1.0 | Dasharo HCL report |
 | Kingston | KF3200C16D4/32GX | 32768 MB | 2400 MT/s (PC4-19200) | -/-/&#10004 | v1.1.1 | Dasharo HCL report |
```

---

## MSI PRO Z690-A Memory HCL results

```diff
+| Kingston | KF3600C16D4/16GX | 16384 MB | 2400 MT/s (PC4-19200) | -/-/&#10004 | v1.1.1 | Dasharo HCL report |
 | Kingston | KF3600C17D4/8GX | 8192 MB | 2400 MT/s (PC4-19200) | &#10004/-/- | v1.0.0 | Dasharo HCL report |
+| Kingston | KF3600C17D4/8GX | 8192 MB | 2400 MT/s (PC4-19200) | -/-/&#10004 | v0.9.0 | Dasharo HCL report |
 | Kingston | KF3600C17D4/8GX | 8192 MB | 2400 MT/s (PC4-19200) | -/-/&#10004 | v1.0.0 | Dasharo HCL report |
 | Kingston | KF3600C17D4/8GX | 8192 MB | 2400 MT/s (PC4-19200) | -/-/&#10004 | v1.1.0 | Dasharo HCL report |
 | Kingston | KF3600C17D4/8GX | 8192 MB | 2400 MT/s (PC4-19200) | -/-/&#10004 | v1.1.1 | Dasharo HCL report |
 | Kingston | KF3600C17D4/8GX | 8192 MB | 2400 MT/s (PC4-19200) | -/-/&#10004 | v1.1.1-rc4 | Dasharo HCL report |
+| Kingston | KF3600C17D4/8GX | 8192 MB | 2400 MT/s (PC4-19200) | -/-/&#10004 | v1.1.2 | Dasharo HCL report |
+| Kingston | KF3600C17D4/8GX | 8192 MB | 2400 MT/s (PC4-19200) | -/-/&#10004 | v1.1.3 | Dasharo HCL report |
+| Kingston | KF3600C18D4/32GX | 32768 MB | 2400 MT/s (PC4-19200) | &#10004/-/- | v1.1.1 | Dasharo HCL report |
+| Kingston | KF3600C18D4/32GX | 32768 MB | 2400 MT/s (PC4-19200) | &#10004/-/- | v1.1.3 | Dasharo HCL report |
+| Kingston | KF3600C18D4/32GX | 32768 MB | 2400 MT/s (PC4-19200) | -/-/&#10004 | v1.1.2 | Dasharo HCL report |
 | Patriot Memory | 4400 C19 Series | 8192 MB | 2133 MT/s (PC4-17000) | &#10004/-/- | v1.0.0 | Dasharo HCL report |
+| Samsung | M378A2G43AB3-CWE | 16384 MB | 3200 MT/s (PC4-25600) | &#10004/-/- | v1.1.1 | Dasharo HCL report |
+| Silicon Power Computer & Communications |  | 16384 MB | 3200 MT/s (PC4-25600) | -/-/&#10004 | v1.1.1 | Dasharo HCL report |
+| Team Group Inc. | TEAMGROUP-UD4-3200 | 16384 MB | 2400 MT/s (PC4-19200) | -/-/&#10004 | v1.1.2 | Dasharo HCL report |
 | Thermaltake Technology Co Ltd | RG26D408GX2-3600C18A | 8192 MB | 2666 MT/s (PC4-21300) | &#10004/-/- | v1.1.0 | Dasharo HCL report |
```
---
layout: two-cols
---

## MSI PRO Z690-A GPU HCL
* Despite [issue #462](https://github.com/Dasharo/dasharo-issues/issues/462)
was not resolved we decide to add GPU HCL automatically generated from Dasharo
HCLs.
* It is very limited and to some extent may be misleading since it is based on
`lspci` output, but we think it is better than nothing.
* It looks like `lspic` see Intel iGPU differently for ADL and RPL:
  - `Intel Corporation AlderLake-S GT1 [8086:4680]`
  - `Intel Corporation Device [8086:4692]`

::right::

<center><img src="/../../img/dug_7/dasharo_gpu_hcl.png" width="750"></center>

---

## MSI PRO Z790-P CPU HCL results

<br>

* 12 uniq CPUs from 12th, 13th and 14th Gen
* 4x 14th Gen CPUs

```diff
+        | 12th Gen Intel(R) Core(TM) i5-12500 | v0.9.0 | Dasharo HCL Report |
+        | 12th Gen Intel(R) Core(TM) i5-12500 | v0.9.1 | Dasharo HCL Report |
+        | 12th Gen Intel(R) Core(TM) i5-12600K | v0.9.0 | Dasharo HCL Report |
+        | 12th Gen Intel(R) Core(TM) i5-12600K | v0.9.1 | Dasharo HCL Report |
+        | 12th Gen Intel(R) Core(TM) i7-12700K | v0.9.0 | Dasharo HCL Report |
+        | 12th Gen Intel(R) Core(TM) i7-12700K | v0.9.1 | Dasharo HCL Report |
+        | 13th Gen Intel(R) Core(TM) i5-13600K | v0.9.0 | Dasharo HCL Report |
+        | 13th Gen Intel(R) Core(TM) i9-13900K | v0.9.0 | Dasharo HCL Report |
+        | 14th Gen Intel(R) Core(TM) i9-14900K | v0.9.0 | Dasharo HCL Report |
+        | 14th Gen Intel(R) Core(TM) i9-14900K | v0.9.1 | Dasharo HCL Report |
+        | 14th Gen Intel(R) Core(TM) i9-14900KF | v0.9.0 | Dasharo HCL Report |
+        | 14th Gen Intel(R) Core(TM) i9-14900KS | v0.9.1 | Dasharo HCL Report |
```

---

## MSI PRO Z690-A and Z790-P GPU HCL results

<br>

* 21 GPU configurations added
  * 12x AMD
  * 9x NVIDIA
* GPU parser still has some glitches but we plan to improve it.

```diff
+    | Advanced Micro Devices, Inc. | AMD/ATI Device  | 1002 | 1002:7480 | No | Dasharo HCL report |
+    | Advanced Micro Devices, Inc. | AMD/ATI Ellesmere  | Radeon RX 470/480/570/570X/580/580X/590  | 1002:67df | No | Dasharo HCL report |
+    | Advanced Micro Devices, Inc. | AMD/ATI Navi 10  | Radeon RX 5600 OEM/5600 XT / 5700/5700 XT  | 1002:731f | No | Dasharo HCL report |
+    | Advanced Micro Devices, Inc. | AMD/ATI Navi 10  | Radeon RX 5600 OEM/5600 XT / 5700/5700 XT  | 1002:731f | Yes (2) | Dasharo HCL report |
+    | Advanced Micro Devices, Inc. | AMD/ATI Navi 21  | Radeon RX 6800/6800 XT / 6900 XT  | 1002:73bf | No | Dasharo HCL report |
+    | Advanced Micro Devices, Inc. | AMD/ATI Navi 22  | Radeon RX 6700/6700 XT/6750 XT / 6800M  | 1002:73df | No | Dasharo HCL report |
+    | Advanced Micro Devices, Inc. | AMD/ATI Navi 22  | Radeon RX 6700/6700 XT/6750 XT / 6800M/6850M XT  | 1002:73df | No | Dasharo HCL report |
+    | Advanced Micro Devices, Inc. | AMD/ATI Navi 23  | Radeon RX 6600/6600 XT/6600M  | 1002:73ff | No | Dasharo HCL report |
+    | Advanced Micro Devices, Inc. | AMD/ATI Navi 23  | Radeon RX 6650 XT  | 1002:73ef | No | Dasharo HCL report |
+    | Advanced Micro Devices, Inc. | AMD/ATI Device  | 1002 | 1002:744c | No | Dasharo HCL report |
+    | Advanced Micro Devices, Inc. | AMD/ATI Device  | 1002 | 1002:744c | Yes (2) | Dasharo HCL report |
+    | Advanced Micro Devices, Inc. | AMD/ATI Device  | 1002 | 1002:7480 | No | Dasharo HCL report |
```

---

## MSI PRO Z690-A and Z790-P GPU HCL results

<br>

```diff
+    | NVIDIA Corporation | GA106 | Geforce RTX 3050 | 10de:2507 | No | Dasharo HCL report |
+    | NVIDIA Corporation | GA106 | RTX A2000 | 10de:2531 | No | Dasharo HCL report |
+    | NVIDIA Corporation | GK104 | GeForce GTX 660 Ti | 10de:1183 | No | Dasharo HCL report |
+    | NVIDIA Corporation | GP106 | GeForce GTX 1060 3GB | 10de:1c02 | No | Dasharo HCL report |
+    | NVIDIA Corporation | GP106 | GeForce GTX 1060 3GB | 10de:1c02 | Yes (2) | Dasharo HCL report |
+    | NVIDIA Corporation | GP108 | GeForce GT 1030 | 10de:1d01 | No | Dasharo HCL report |
+    | NVIDIA Corporation | TU104GL | Quadro RTX 4000 | 10de:1eb1 | Yes (2) | Dasharo HCL report |
+    | NVIDIA Corporation | TU116 | GeForce GTX 1650 SUPER | 10de:2187 | No | Dasharo HCL report |
+    | NVIDIA Corporation | TU117GLM | Quadro T1000 Mobile | 10de:1fb0 | No | Dasharo HCL report |
```

---

## Issues

* Most people run DTS HCL Report before deploying Dasharo, not after. That way
we losing information useful for community.
* Memory configurations could be managed better, right now every combination
tested is reported separately even if those are the same DIMMs, but connected
differently.
* No information about memory for MSI Pro Z790-P most likely parser issue.
* Changes not yet upstream:
  * https://github.com/Dasharo/docs/pull/899

---

# Call for Action

If you run Dasharo on your hardware and you didn't sent HCL yet please
consider doing so.

<center><img src="/../../img/dug_7/dts-hcl-run.png" width="700"></center>

---
layout: cover
background: /intro.png
class: text-center

---

# Questions?

<!--

Comment to satisfy pre-commit

-->
