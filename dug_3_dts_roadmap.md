class: center, middle, intro

# &#x1F386; Dasharo Tools Suite Roadmap &#x1F386;

.center[<img src="/remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">]

???

---

# Agenda

* Short Introduction to Dasharo Tools Suite (DTS)
* Overview of DTS v1.2.1 to v1.2.8
* Future Plans: DTS v2.0.0 and Beyond
* Q&A

???

---

# Dasharo Tools Suite a.k.a. DTS

.center.image-99[![](/img/dts-logo.jpg)]

* Set of tools and scripts running in minimal Linux environment
  - https://docs.dasharo.com/dasharo-tools-suite/overview
* DRY: https://www.youtube.com/watch?v=ZyctrnJNTPc&t=5162s
* Since last DUG we had quite a lot of silent releases and one public:
  - by silent we mean not announced in Dasharo Universe documentation,
  - v1.2.6 - beta/preview release, not recommended for wider use,
  - v1.2.8 - fully featured, validated release into which we will dive on
    next slides,

---

# DTS silent releases

* **v1.2.1 - 2023-06-16**
  - Updated coreboot-utils to support Jasper Lake.
* **v1.2.2 - 2023-06-16**
  - Updated coreboot-utils to support Alder Lake.
* **v1.2.3 - 2023-06-16** (no mistake three releases in one day)
  - Enabled devmem applet for buxybox, which helps in gathering important data
    for porting and debugging.
* **v1.2.4 - 2023-07-12**
  - me_cleaner was added
* **v1.2.5 - 2023-08-07**
  - we realize we have bug in Dell BIOS Update downloading which is important
    for deployment of Dasharo for Dell OptiPlex 7010/9010, that problem was
    fixed,
* **v1.2.6 - 2023-08-31**
  - we added 9elements/txt-suite which is useful in validating and diagnosing
    issues we face while integrating TrenchBoot as AEM for Qubes OS

---

# DTS v1.2.7 and v1.2.8

* **v1.2.7 - 2023-09-05**
  - Added Dasharo zero-touch initial deployment on MSI PRO Z790-A for DES
    users.
  - Added Dasharo firmware update to version v1.1.2 on MSI PRO Z690-A for DES
    users.
  - Updated coreboot-utils to support Raptor Lake.
  - Added couple UX improvements for DTS scripts, specially in the context of
    DES users.
  - One more time fix downloading Dell BIOS Update packages.
* **v1.2.8 - 2023-09-06**
  - Check for SMM protection before trying to flash.

---

# 🐛 Bugs everywhere 🐛

* We are aware of feature requests and bugs related to DTS.
  - It works for most use cases, but still need improvements.
* We have to improve hardware checks before flashing.
  - There are reports of people flashing MSI Z690-A v1.1.1 on platforms with
    Intel Raptor Lake, which is not supported by that release and DTS should
    detect and prevent sych lockout.
* As of 26/09/2023 there are 31 bugs, enhancements and other reports open in
  dasharo-issues repository, and 17 clossed.
* If you feel you found some problem please report it:
  - https://github.com/Dasharo/dasharo-issues/issues

---

# DTS v1.2.8 menu

.center.image-99[![](/img/dts-v1.2.8.png)]

* If you want to try DTS in QEMU please check: https://github.com/Dasharo/dasharo-issues/issues/338#issuecomment-1734578527

---

# DTS v2.0.0

.center.image-90[![](/img/dts_v2.0.0.png)]

* https://github.com/Dasharo/dasharo-issues/milestone/5

---

# DTS Roadmap (no changes)

* Device authentication to improve Dasharo firmware update
  - client authentication mechanism working with updates
  - ETA: Q4 2023
  - [GitHub issue #55](https://github.com/Dasharo/dasharo-issues/issues/55)
* Expanding DTS root file system via NFS or other solution
  - adds posibility to load custom kernel modules
  - protects against endless growth of root file system size
  - ETA: Q4 2023
  - [GitHub issue #366](https://github.com/Dasharo/dasharo-issues/issues/366)
* DTS zero touch initial deployment for firmware `as is`
  - multistage approach to improve open-source firmware adoptability
  - ETA: Q1 2024
  - [GitHub issue #384](https://github.com/Dasharo/dasharo-issues/issues/384)
* DTS security features provisioning and attestation
  - improve the trustworthiness of computing device
  - ETA: Q2 2024
  - [GitHub issue #385](https://github.com/Dasharo/dasharo-issues/issues/385)

???

* all dealines shifted by 1Q
* Other ideas
	- automatic bug reporting from DTS

---
class: center, middle, intro

# Q&A
