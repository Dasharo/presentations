---
theme: slides/slidev-template/theme
layout: cover
background: /intro.png
class: text-center

---

## &#x1F44B; DUG#12 Shameless Plug &#x1F44B;

<center><img src="/slides/img/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px"></center>

---

<center><img src="/slides/img/dug_12/shameless_plug.png" width="430"></center>

<!--

- 🌱 **Growth & Transparency:** Showcasing our evolution and commitment to open-source.
- 📚 **Historical Record:** A resource for 3mdeb, future customers, and the privacy/security community.
- 📈 **Explore Business Model:** Learn from our open-source firmware journey, including potential pitfalls.

-->

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

<center><img src="/slides/img/dug_9/shop_sdwire.png" width="700"></center>

<br>

<center>

### [https://shop.3mdeb.com/shop/open-source-hardware/sdwire/](https://shop.3mdeb.com/shop/open-source-hardware/sdwire/)
</center>

<!--

After being unavailable for two weeks, SDWire is again available in our shop.
At the beginning of December 2025, we restocked this product. We are shipping orders on an ongoing basis.

-->

---

<center><img src="/slides/img/dug_9/shop_twonkie.png" width="600"></center>

<br>

<center>

### [https://shop.3mdeb.com/shop/open-source-hardware/twonkie-usb-c-sniffer/](https://shop.3mdeb.com/shop/open-source-hardware/twonkie-usb-c-sniffer/)
</center>

<!--

Around 30 remain in stock.

-->

---

<center><img src="/slides/img/dug_12/shop_usbsniffer.png" width="900"></center>

<br>

<center>

### [https://shop.3mdeb.com/product/usb-sniffer-ls-fs-hs-with-wireshark-interface/](https://shop.3mdeb.com/product/usb-sniffer-ls-fs-hs-with-wireshark-interface/)
</center>

---

<center><img src="/slides/img/dug_12/shop_usbarmory.png" width="900"></center>

<br>

<center>

### [https://shop.3mdeb.com/product/usb-armory-mk-ii/](https://shop.3mdeb.com/product/usb-armory-mk-ii/)
</center>

<!--

1st half of 2026.
The redesign of this OSHW is ongoing and we will only commission production once it is complete. We will write a blog post about our adventures with this OSHW, which only appeared to be suitable for production.

-->

---

<center>

### PCI USB controller that enables device certification for Qubes OS

  <center><img src="/slides/img/dug_12/pci_to_usb_converter.excalidraw.png"
    width="400"></center>

</center>

<!--

A custom PCB featuring a PCI-to-USB converter designed to expose an external
USB port in a NucBox enclosure. The project involves selecting an appropriate
conversion chip and creating a PCB layout that fits the NucBox’s dimensional
requirements. The design should not be limited to a single device; ensuring
compatibility with a wide range of systems would increase the product’s
potential reach. Comparable multi-device adapter boards already exist, such as
those shown in example listings.

-->

---
layout: cover
background: /intro.png
class: text-center
---

# Dasharo Supported Hardware

---

<center><img src="/slides/img/dug_12/shop_asrock.png" width="820"></center>

<!--

* 1 - this is currently the only configuration we have tested
* 2 - we plan to expand the list of components with those suggested by
contributors from the Dasharo community. We will purchase and test such
components beforehand.
* 3 - we are considering selling the motherboard itself, in case someone
already has compatible components or wants to purchase them separately.
* 4 - we are also considering selling the DPP package on its own.

-->

<br>

<center>

#### [https://shop.3mdeb.com/product/asrock-spc741d8-2l2t-bcm-dasharo-pro-full-build/](https://shop.3mdeb.com/product/asrock-spc741d8-2l2t-bcm-dasharo-pro-full-build/)
</center>

---

<center><img src="/slides/img/dug_12/shop_gigabyte-mz33.png" width="820"></center>

<br>

<center>

#### [https://shop.3mdeb.com/product/full-build-gigabyte-mz33-ar1-with-dasharo-corebootuefi-pro-package-for-servers/](https://shop.3mdeb.com/product/full-build-gigabyte-mz33-ar1-with-dasharo-corebootuefi-pro-package-for-servers/)
</center>

<!--

1. The product will be released to the shop in Q1'26
2. Initially, it will be a version with one set of components – exactly the
   ones we tested, because we take responsibility for their compatibility.
3. Over time, the product will be developed, as discussed with ASRock.

-->

---

<center><img src="/slides/img/dug_12/shop_msi.png" width="600"></center>

<br>

<center>

### [Link to MSI products in our shop](https://shop.3mdeb.com/?s=MSI&post_type=product&dgwt_wcas=1)

</center>

<!--

We are working on a new platform - MSI PRO B850. It will be available in the
shop in Q1 or Q2 (1H'26).

-->

---

<center><img src="/slides/img/dug_9/dell_optiplex.png" width="450"></center>

<br>

<center>

### [Link to Optiplex products in our shop](https://shop.3mdeb.com/?s=Optiplex&post_type=product&dgwt_wcas=1)
</center>

<!--

Dasharo (coreboot+UEFI) v0.1.1 is available.

Release date: 2024-12-17

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

<center><img src="/slides/img/dug_11/odroid.png" width="700"></center>

<br>

<center>

### [Link to Odroid products in our shop](https://shop.3mdeb.com/?s=Odroid&post_type=product&dgwt_wcas=1)
</center>

<!--

Dasharo (coreboot+UEFI) v0.9.1 was released on 2025-09-03.

Changed
  - VBT file to fix graphical output in firmware
  - Flash descriptor updated to v1.1 (see SBOM)
  - Owner GUID of Secure Boot DB and KEK to Microsoft recommended values
  - Updated DBX to 2025-06-13

-->

---

<center><img src="/slides/img/dug_9/novacustom_laptops.png" width="900"></center>

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

<center><img src="/slides/img/dug_9/pcengines.png" width="250"></center>

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

<center><img src="/slides/img/dug_8/protectli_firewalls.png" width="500"></center>

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

# Dasharo Pro/Enterprise Package

---

<br>

<div style="display: flex; justify-content: center; align-items: center;">
  <img src="/slides/img/dug_11/dpp.png" width="220"/>
  <img src="/slides/img/dug_11/dpp2.png" width="220" style="margin-left: 50px"/>
  <img src="/slides/img/dug_11/dpp3.png" width="220" style="margin-left: 50px"/>
</div>

<br>

<center>

### [https://shop.3mdeb.com/product-category/dasharo-pro-package](https://shop.3mdeb.com/product-category/dasharo-pro-package)
</center>

---

<br>

<div style="display: flex; justify-content: center; align-items: center;">
  <img src="/slides/img/dug_11/dpp4.png" width="220"/>
  <img src="/slides/img/dug_11/dpp5.png" width="220" style="margin-left: 50px"/>
</div>

<br>

<center>

### [https://shop.3mdeb.com/product-category/dasharo-pro-package](https://shop.3mdeb.com/product-category/dasharo-pro-package)
</center>

---
layout: cover
background: /intro.png
class: text-center
---

# Accessories

---

<center><img src="/slides/img/dug_11/privacy-screen.png" width="280"></center>

<br>

<center>

### [https://shop.3mdeb.com/product-category/accessories/](https://shop.3mdeb.com/product-category/accessories/)
</center>

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

# Services

---

## <center>Dasharo Services</center>

<br>

<center><img src="/slides/img/dug_12/dasharo_services.png" width="900"></center>

<br>

<center>

### [https://shop.3mdeb.com/product-category/dasharo-services/](https://shop.3mdeb.com/product-category/dasharo-services/)
</center>

---

## <center>Zarhus Services</center>

<br>

<center><img src="/slides/img/dug_8/zarhus_services.png" width="900"></center>

<br>

<center>

### [https://shop.3mdeb.com/shop/zarhus-services/](https://shop.3mdeb.com/shop/zarhus-services/)
</center>

---

## <center>Services</center>

<br>

<center><img src="/slides/img/dug_12/services1.png" width="900"></center>

<br>

<center>

### [https://shop.3mdeb.com/product-category/services/](https://shop.3mdeb.com/product-category/services/)
</center>

---

## <center>Services</center>

<br>

<center><img src="/slides/img/dug_12/services2.png" width="800"></center>

<br>

<center>

### [https://shop.3mdeb.com/product-category/services/](https://shop.3mdeb.com/product-category/services/)
</center>

---
layout: cover
background: /intro.png
class: text-center

---

# Highlighting HCL Reports

---

<center><img src="/slides/img/dug_12/hcl_highlights_01.png" width="600"></center>

<br>

<center><img src="/slides/img/dug_12/hcl_highlights_02.png" width="600"></center>

<center>

### [https://docs.dasharo.com/unified/msi/hcl/](https://docs.dasharo.com/unified/msi/hcl/)
</center>

<!--

Add: Here are the configurations confirmed compatible, the newly verified ones,
and those you can already purchase from us (listed on each product’s page).

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
