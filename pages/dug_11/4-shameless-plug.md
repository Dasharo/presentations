---
theme: ../../slidev-template/theme
layout: cover
background: /intro.png
class: text-center

---

## &#x1F44B; DUG#11 Shameless Plug &#x1F44B;

<center><img src="/../../img/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px"></center>

---

<br>

<center><img src="/../../img/dug_9/shameless_plug.png" width="480"></center>

<br>

- 🌱 **Growth & Transparency:** Showcasing our evolution and commitment to open-source.
- 📚 **Historical Record:** A resource for 3mdeb, future customers, and the privacy/security community.
- 📈 **Explore Business Model:** Learn from our open-source firmware journey, including potential pitfalls.

---

## What we will talk about

<br>

- Hardware,
- Services,
- Pace Enterprise Training,
- Dasharo Pro/Enterprise Package
- Accessories
- Everything available in 3mdeb shop: https://shop.3mdeb.com

---
layout: cover
background: /intro.png
class: text-center

---

# Hardware

---

<center><img src="/../../img/dug_9/shop_sdwire.png" width="700"></center>

<br>

<center>

### [https://shop.3mdeb.com/shop/open-source-hardware/sdwire/](https://shop.3mdeb.com/shop/open-source-hardware/sdwire/)
</center>

<!--

SDWire is our one of best selling products. There are very many interesting use
cases in which it can be used.

Let's talk about couple of those.

-->

---

!!! quote
    Developing firmware for an embedded device requires a lot of testing. (...)
    Some tests can be done on the host machine, but in most cases (especially
    related to specific peripherals), it is best to run tests on actual hardware.

!!! quote
    Physical swap SD card / USB disk is the safest and easiest way for initial flash transfer from the development computer to the device being tested. (...)
    Initially, I contemplated a robot carrying a physical SD card like in the movie Hackers, but there should be an easier way… and it turns out there is! (...)
    They designed SD wrapper with no moving parts and called it SDWire.

<center>

### [https://www.kurokesu.com/main/2022/08/02/ethernet-camera-module-build-log-5-automated-flashing/](https://www.kurokesu.com/main/2022/08/02/ethernet-camera-module-build-log-5-automated-flashing/)

</center>

---

* SDWire as well as other products for DYI can be bought on Tindie.
* We appreciate very nice review and a blog post about usage of SDWire in
Apache NuttX validation from Lup Yuen.

<br>

<center><img src="/../../img/dug_9/sdwire_tindie_review.png" width="700"></center>

<center>

### [https://www.tindie.com/products/3mdeb/sd-wire-sd-card-reader-sd-card-mux/](https://www.tindie.com/products/3mdeb/sd-wire-sd-card-reader-sd-card-mux/)

</center>

---

!!! quote
    *We used Special Hardware: SDWire MicroSD Multiplexer (pic above)
    * Controlled by a Single-Board Computer: Yuzuki Avaota-A1 (Open Hardware)
    *PinePhone Test Bot kinda works!
    * Though PinePhone Battery complicates Hardware Testing
    *We might pivot to another Arm64 Single-Board Computer
    * Maybe we’ll port NuttX to Allwinner A527 SoC

<center>

### [https://lupyuen.org/articles/testbot3.html](https://lupyuen.org/articles/testbot3.html)

</center>

<!--

Article in a lot of details describe hardware setup for testing Apache Nuttx on
PinePhone.

-->

---
layout: cover
background: /intro.png
class: text-center

---

<center><img src="/../../img/dug_9/testbot2-flow.jpg" width="600"></center>

<center>

### [https://lupyuen.org/articles/testbot3.html](https://lupyuen.org/articles/testbot3.html)

</center>

---

<center><img src="/../../img/dug_9/avaota-title.jpg" width="450"></center>

<center>

### [https://lupyuen.org/articles/testbot3.html](https://lupyuen.org/articles/testbot3.html)

</center>

---

<center><img src="/../../img/dug_9/shop_twonkie.png" width="600"></center>

<br>

<center>

### [https://shop.3mdeb.com/shop/open-source-hardware/twonkie-usb-c-sniffer/](https://shop.3mdeb.com/shop/open-source-hardware/twonkie-usb-c-sniffer/)
</center>

<!--

Also community around this project has very interesting use cases.

-->

---

<center><img src="/../../img/dug_9/twonkie_hn.png" width="900"></center>

!!! quote
    (...) they make sniffing the USB-PD messages considerably easier than using an
    amplifier and logic analyzer like I did here. If you’re only interested in the
    protocol layer and above, these seem like excellent choices.

<center>

### [https://www.rbaron.net/blog/2024/06/02/usb-power-delivery-for-makers.html](https://www.rbaron.net/blog/2024/06/02/usb-power-delivery-for-makers.html)
</center>

<!--

Of course there were many more publications about Twonkie like those on Hack A
Day.

-->

---

## <center>Dasharo Supported Hardware</center>

<center><img src="/../../img/dug_11/asrock.png" width="230"></center>

<br>

<center>

### [https://shop.3mdeb.com/product-category/dasharo-supported-hardware/](https://shop.3mdeb.com/product-category/dasharo-supported-hardware/)
</center>

---

## <center>Dasharo Supported Hardware</center>

<center><img src="/../../img/dug_11/gigabyte-mz33.png" width="230"></center>

<br>

<center>

### [https://shop.3mdeb.com/product-category/dasharo-supported-hardware/](https://shop.3mdeb.com/product-category/dasharo-supported-hardware/)
</center>

---

## <center>Dasharo Supported Hardware</center>

<center><img src="/../../img/dug_9/dell_optiplex.png" width="400"></center>

<br>

<center>

### [https://shop.3mdeb.com/product-category/dasharo-supported-hardware/](https://shop.3mdeb.com/product-category/dasharo-supported-hardware/)
</center>

<!--

No longer under pre-order. Also Dasharo (coreboot+UEFI) v0.1.1 is available.

This is old Ivy Bridge hardware, but still capable and cheap.
What is important there are multiple interesting functions available like:
- ME Neutering - means essesntially cutting off "unneeded" pieces of ME
- Possible TrenchBoot aka AEM for Qubes OS.
- Possible SMI Transfer Monitor.
- UEFI Capsule Update integration
- New Dasharo Measured Boot which cover correctly coreboot and EDKII/UEFI payload.
- NVMe disks support through adapter.
- Qubes OS Certification - Unfortunately not possible due to end of life on Intel side, Intel do not provide microcode fixes, biggest value for that hardware is potential of TrenchBoot.

-->

---

## <center>Dasharo Supported Hardware</center>

<center><img src="/../../img/dug_11/odroid.png" width="230"></center>

<br>

<center>

### [https://shop.3mdeb.com/product-category/dasharo-supported-hardware/](https://shop.3mdeb.com/product-category/dasharo-supported-hardware/)
</center>

<!--

No longer under pre-order. Dasharo (coreboot+UEFI) v0.9.0 was released.

Current release is minimalistic but we already planning new version which will be closer in functionality to closed source firmware.

The goal of this platform is to serve as base line for hardware training which
we provide as part of various conferences, as well as directly to customers. It
will be also very useful for students who want to get through upcoming OST2
UEFI Secure Boot course.

-->

---

<center><img src="/../../img/dug_9/novacustom_laptops.png" width="900"></center>

<br>

<center>

### [https://shop.3mdeb.com/product-category/laptops/](https://shop.3mdeb.com/product-category/laptops/)
</center>

<!--

We also have referral links to Novacustom. Buying through our website you
support us directly.

Please note this is dropshipping.

-->

---

<center><img src="/../../img/dug_9/pcengines.png" width="250"></center>

<br>

<center>

### [https://shop.3mdeb.com/product-category/system-boards/](https://shop.3mdeb.com/product-category/system-boards/)
</center>

<!--

We also provide PC Engines refurbished units. This hardware is no longer
officially available and we can consider it last of its kind.

Setup comes with:
- TPM2.0
- 3 years of Dasharo Pro Package

It is unique old piece of hardware, but still serves as very stable router. If
your goals are more on stability, firmware updates, low TDP this may be option
for you.

We offer apu2e and apu6a and b.

Number of units is very limited.

-->

---

<center><img src="/../../img/dug_8/protectli_firewalls.png" width="500"></center>

<br>

<center>

### [https://shop.3mdeb.com/product-category/vaults/](https://shop.3mdeb.com/product-category/vaults/)
</center>

<!--

Another dopshipping option is for Protectli. All those firewalls support
Dasharo open-source firmware. Those are high quality and well-tested products.

So if you want to buy those and leave some tiny margin for 3mdeb feel free to
use our shop.

-->

---
layout: cover
background: /intro.png
class: text-center

---

# Pace Enterprise Training

---
clicks: 6
---

<center><img src="/../../img/dug_9/pet_cooperation_models.png" width="900"></center>

<!--

[click]
It’s essential to explicitly mention that we provide both **On-Site
Instructor-Led for Individuals** and **Remote Instructor-Led Group** options.
These are significant formats that provide structured guidance and should be
highlighted for clarity.

[click]
Within segments we don't want to create **Business** categories, although from
our experience it is closely related to annual training budget of organization.
Obviously bigger organization typically have bigger budget.

[click]
We can always discuss custom training but those solutions are typically with
higher price tag. Over 10 years of activity in platform security we gathered
information and hand-on experience from many areas of low level security,
because of that we can tackle almost any topic. If in doubt contact us.

[click]
"Extended Direct Support from Instructor" means Instructor is not only
available during training event, but also would respond to questions before and
after training. Of course unless it turns into consulting endeavour, but please
note we are not a lawyers we don't count for every hour.

[click]
Potential discounts for bulk training purchases or long-term contracts, which would be appealing to corporate clients are possible

[click]
Regarding additional features there can be availability of recordings for
Remote sessions or The PET Blueprint and Pace Training Reference Guide
containing extensive editorial version of speaker notes.

-->

---

- x86, Arm and POWER9/10
- All open-source firmware topics for each available framework (coreboot, EDKII, U-Boot, TrustedFirmware, OpenBMC, Yocto etc.)
- Closed source firmware components: ME/CSME/TXE/SPS, PSP/ASP, microcode, Intel ACMs
  - based on publicly available materials
- Low-level security mechanisms with example CVE exploitation (UEFI Secure Boot, Intel Boot Guard, closed source firmware etc.)
  - vulnerability class analysis
* Trusted Computing Technologies
  - BitLocker/LUKS/Heads
  - Measured Boot
  - SRTM/DRTM and other Root of Trust for Measurement
* Firmware development life-cycle from considerations at hardware design stage
  to long term maintenance.
* Your topic not on the list? Feel free to contact us: `contact<at>dasharo<dot>com`

<!--

Our curriculum is fully featured, but we essentially can cover everything in
following areas.

-->
---

<center><img src="/../../img/dug_8/pet_ds01cbi.png" width="550"></center>

<br>

<center>

### [https://paceenterprisetraining.com/](https://paceenterprisetraining.com/)
</center>

<!--

Pace Enterprise Training by 3mdeb helps companies to bridge knowledge gaps and accelerate engineering team readiness, delivered by trainers with years of hands-on experience with collaborative open-source and commercial software development.

We essentially provide training in all areas of our expertise:
- Dasharo: BIOS, boot firmware, ME/PSP, advanced security features, UEFI, coreboot etc.
- Zarhus: Embedded Linux for all major SoC vendors.

We educate about every aspect of platform life cycle in context of open-source
ecosystem. Start from input at design stage, component selection to match best
possible support or easily develop it, through bring up, initial deployment,
update and long term maintenance.

-->

---

<center><img src="/../../img/dug_8/pet_ds02rta.png" width="750"></center>

<br>

<center>

### [https://paceenterprisetraining.com/](https://paceenterprisetraining.com/)
</center>

---

<center><img src="/../../img/dug_8/pet_ds03ssi.png" width="650"></center>

<br>

<center>

### [https://paceenterprisetraining.com/](https://paceenterprisetraining.com/)
</center>

---

<center><img src="/../../img/dug_8/pet_zh01eli.png" width="550"></center>

<br>

<center>

### [https://paceenterprisetraining.com/](https://paceenterprisetraining.com/)
</center>

---

<center><img src="/../../img/dug_8/pet_zh02ypi.png" width="650"></center>

<br>

<center>

### [https://paceenterprisetraining.com/](https://paceenterprisetraining.com/)
</center>

---

<center><img src="/../../img/dug_11/pet_ds08msa.png" width="650"></center>

<br>

<center>

### [https://paceenterprisetraining.com/](https://paceenterprisetraining.com/)
</center>

---

<center><img src="/../../img/dug_11/pet_ds09sbl.png" width="650"></center>

<br>

<center>

### [https://paceenterprisetraining.com/](https://paceenterprisetraining.com/)
</center>

---

<center><img src="/../../img/dug_1/hwio.jpg" width="400"></center>

<br>

<center>

### [https://hardwear.io/netherlands-2025/training/mastering-uefi-secure-boot-and-intel-root-of-trust-technologies.php](https://hardwear.io/netherlands-2025/training/mastering-uefi-secure-boot-and-intel-root-of-trust-technologies.php)
</center>

<!--

Feel free to contact us if you need discount code.

-->
---
layout: cover
background: /intro.png
class: text-center

---

# https://shop.3mdeb.com

<!--

Everything else you will buy on 3mdeb.com

-->

---
layout: cover
background: /intro.png
class: text-center

---

# Backlog

---
layout: cover
background: /intro.png
class: text-center

---

# Services

---

## <center>Zarhus Services</center>

<br>

<center><img src="/../../img/dug_8/zarhus_services.png" width="900"></center>

<br>

<center>

### [https://shop.3mdeb.com/shop/zarhus-services/](https://shop.3mdeb.com/shop/zarhus-services/)
</center>

---
layout: cover
background: /intro.png
class: text-center

---

# Dasharo Pro/Enterprise Package
## (formerly Dasharo Entry Subscription)

---

## <center>Dasharo Pro/Enterprise Package</center>

<br>

<div style="display: flex; justify-content: center; align-items: center;">
  <img src="/../../img/dug_7/des.png" width="220"/>
  <img src="/../../img/dug_7/des2.png" width="220" style="margin-left: 50px"/>
  <img src="/../../img/dug_7/des3.png" width="220" style="margin-left: 50px"/>
</div>

<br>

<center>

### [https://shop.3mdeb.com/product-category/dasharo-pro-package](https://shop.3mdeb.com/product-category/dasharo-pro-package)
</center>

---

## <center>Dasharo Pro/Enterprise Package</center>

<br>

<div style="display: flex; justify-content: center; align-items: center;">
  <img src="/../../img/dug_7/des5.png" width="220"/>
  <img src="/../../img/dug_7/des4.png" width="220" style="margin-left: 50px"/>
  <img src="/../../img/dug_7/des6.png" width="220" style="margin-left: 50px"/>
</div>

<br>

<center>

### [https://shop.3mdeb.com/product-category/dasharo-pro-package](https://shop.3mdeb.com/product-category/dasharo-pro-package)
</center>
