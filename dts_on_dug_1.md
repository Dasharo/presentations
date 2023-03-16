class: center, middle, intro

# &#x1F386; Dasharo Tools Suite &#x1F386;

## Getting started and roadmap

.center[<img src="remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">]

???

---

# Agenda

* What?
* How?
* Why?
* List of features
* Demo on MSI PRO Z690-A DDR4
* Upcoming release
* Roadmap

???

* What DTS is; set of tools and scripts, swiss army knife for Dasharo users
* How DTS is created with Yocto, how you can run it on your platform
* Why DTS was created, how it can help you check what is on your platform,
  deploy Dasharo, update Dasharo; people bricking their platforms
* Features like HCL report, initial deployment, SBoM
* Demo of deploy, rollback on MSI PRO Z690-A DDR4 with dumping HCL report
* Upcoming release
  - milestone on GH for v1.1.2
  - releases also connected with Dasharo firmware releases (init deploy for more
    and more platforms)
  - DTS Logo
  - DTS UX update
  - Dasharo update from menu
  - Develop builds
* Roadmap
  - device authentication to improve Dasharo firmware update: Q3
  - DTS security features provisioning: Q4
  - DTS zero touch initial deployment for firmware `as is`: Q4

---

# What?

* Dasharo Tools Suite a.k.a. DTS
* Set of tools and scripts running in minimal Linux environment
  - swiss army knife for Dasharo users and open-source firmware community
  - aims to provide a comprehensive solution for firmware flashing, gather
    information about hardware
  - [documentation](https://docs.dasharo.com/dasharo-tools-suite/overview/)
* First publicly available release on 2022-08-09
  - since then four more releases
  - [releases](https://docs.dasharo.com/dasharo-tools-suite/releases/#embedded-firmware)
* Dasharo Tools Suite test cases
  - performed on MSI PRO Z690-A DDR4 and DDR5 also on NovaCustom NV4x and
    NS5x/7x
  - [test cases](https://docs.dasharo.com/unified-test-documentation/dasharo-compatibility/326-dasharo-tools-suite/)

---

# How?

* Build based on Yocto Project
  - compatible with Kirkstone release
  - dependent on minimal set of additional layers
  - kas used to manage the compilation
  - provided documentation about how to build manually
* Meta layer stored on Dasharo GitHub organization
  - two main branches `main` and `develop`
  - [meta-dts](https://github.com/Dasharo/meta-dts)
* Available artifacts
  - iso and compressed images on releases subpage
  - kernel and cpio to boot from iPXE

---

# Why?

TBD Storytell about Bob who saw Dasharo, wanted to test it, check documentation,
made one, small mistake, and... brick his hardware. DTS is here for him.

???

* not only story about bricking, this is only one of DTS functionality
* also HCL report, get to know your hardware
* also latest versions of available tools like flashrom or coreboot utils, helps
  to investigate hardware and flash firmware

---

# Features

* Dasharo zero-touch initial deployment
  - automates Dasharo firmware flashing, while also dumping flash content before
    to create backup
  - supported on ASUS KGPE-D16, Dell OptiPlex 7010/9010, MSI PRO Z690-A DDR4 and
    DDR5, NovaCustom NV4x and NS5x/7x
  - [more information](https://docs.dasharo.com/dasharo-tools-suite/documentation/#dasharo-zero-touch-initial-deployment)
* HCL Report
  - powerful option, allows to get information about your hardware
  - dumped as compressed tarball in rootfs of DTS, also can be send to Dasharo
    Team
  - `results` file in dump
  - [more information](https://docs.dasharo.com/dasharo-tools-suite/documentation/#hcl-report)
* Latest versions of important utilities
  - e.g. `fwupd`, `flashrom`, `coreboot-utils` from Dasharo forks
  - allows to compile, test and upstream
  - in future, we want to provide whole SBoM

---
class: center, top, outro

.center[##DEMO]
.center[###Dasharo Tools Suite - Initial deployment and rollback]

???

Demo link: https://cloud.3mdeb.com/index.php/f/562798

Descibe what happens while demo is playing.

---

# Upcoming release

* DTS v1.1.2
  - ETA: April/May 2023
  - [GitHub Milestone](https://github.com/Dasharo/dasharo-issues/milestone/5)
* Key features
  - add QEMU image with sets of basic tests of the system
  - update UI; make it shiny, beautiful and what more important - user friendly
  - enable Dasharo zero-touch initial deployment on Dell Precision T1650
  - work on DTS logo
  - introduce nightly/develop builds
  - enable Dasharo firmware update already available on develop build

---

# Roadmap

* Device authentication to improve Dasharo firmware update
  - client authentication mechanism working with updates
  - ETA: Q3 2023
  - [GitHub issue](https://github.com/Dasharo/dasharo-issues/issues/55)
* Expanding DTS root file system via NFS or other solution
  - adds posibility to load custom kernel modules
  - protects against endless growth of root file system size
  - ETA: Q3 2023
  - [GitHub issue](https://github.com/Dasharo/dasharo-issues/issues/366)
* DTS zero touch initial deployment for firmware `as is`
  - facilitate entry into the world of open-source firmware
  - ETA: Q4 2023
  - [GitHub issue](https://github.com/Dasharo/dasharo-issues/issues/384)
* DTS security features provisioning
  - improve the trustworthiness of computing device
  - ETA: Q1 2024
  - [GitHub issue](https://github.com/Dasharo/dasharo-issues/issues/385)

---
class: center, middle, outro

.center[##Q&A]
