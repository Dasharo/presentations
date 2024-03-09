class: center, middle, intro

# &#x1F386; Dasharo Tools Suite Status &#x1F386;

.center[<img src="/remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">]

???

---

# Agenda

* Short Introduction to Dasharo Tools Suite (DTS)
* Overview of DTS v1.2.9 to v1.2.12
* Future Plans: DTS v2.0.0 and Beyond
* Q&A

???

---

# Dasharo Tools Suite a.k.a. DTS

.center.image-99[![](/img/dts-logo.jpg)]

* Set of tools and scripts running in minimal Linux environment
    - https://docs.dasharo.com/dasharo-tools-suite/overview
* DRY: https://bit.ly/dasharo-tools-suite
* We continue silent releases:
    - by silent we mean not announced in Dasharo Universe documentation,
    - v1.2.8 - last stable release recommended for community, published on
    docs.dasharo.com,
    - v1.2.9-v1.2.12 silent releases made as part of Dasharo Support Package

???

- Frequency of releases chart, sice of releases?
* make sure this presentation will be linked in DTS documentation

---

# DTS silent releases

* **v1.2.9 - 2023-09-29**
    * Added [Firmware Update
    Mode](https://docs.dasharo.com/guides/firmware-update/#firmware-update-mode)
    integration, which speed up the process of Dasharo firmware update.
    * Added efivars support and efivar utility to support FUM.
    * Improved logging of DTS menu options to not throw redundant and confusing
    logs e.g. from flashrom.
    * Fixed problem with EC firmware using incorrect link.
* **v1.2.10 - 2023-10-17**
    * Added [Dasharo Configuration Utility](https://github.com/Dasharo/dcu) which
    allow to change logo displayed on boot and many more. More about that in
    dedicated presentation.
    * Added SMMSTORE migration for NovaCustom laptops, so the Dasharo Setup settings
    are preserved after firmware update.
    * Added CI/CD pipeline to generate signatures.

---

# DTS silent releases

* **v1.2.11 - 2023-10-31**
    * Bumped supported firmware versions of NovaCustom to 1.5.1/1.7.1
* **v1.2.12 - 2023-11-03**
    * Fix updating boards without Vboot slot B
* So far in 2023 we released seven DTS versions from v1.1.1 to v1.2.12.
* We plan to continue improving DTS in 2024.

---

# 🐛 Bugs everywhere 🐛

.center.image-80[![](/img/dts_issues_2023q4.png)]

* We have to improve issues tracking and resolution.
* If you feel you found some problem please report it:
    - https://github.com/Dasharo/dasharo-issues/issues

---

# DTS v1.2.11 menu

.center.image-99[![](/img/dts-v1.2.11.png)]

* v1.2.12 is not yet on https://boot.3mdeb.com
* If you want to try DTS in QEMU please check: https://github.com/Dasharo/dasharo-issues/issues/338#issuecomment-1734578527

---

# DTS v1.2.13

.center.image-99[![](/img/dts-milestone-v1.2.13.png)]

* https://github.com/Dasharo/dasharo-issues/milestone/5

---

# DTS v2.0.0

.center.image-99[![](/img/dts-milestone-v2.0.0.png)]

* https://github.com/Dasharo/dasharo-issues/milestone/5

???

* Other ideas
    - automatic bug reporting from DTS

---

# DTS Future Roadmap

.center.image-99[![](/img/dts_roadmap_v0.4.png)]

---
class: center, middle, intro

# Q&A
