---
theme: slidev-template/theme
layout: cover
background: /intro.png
class: text-center

---

# Porting Dasharo to the ASRock Rack SPC741D8

## A Journey into Modern Intel Server Firmware

---

### Introduction & Context

**The Mission:**

* Porting Dasharo (coreboot-based) to a modern Intel Server Platform.
* **Target:** ASRock Rack SPC741D8 (Intel Sapphire Rapids).
* **Collaboration:** Based on initial work by the KIT Operating Systems Group.
* **Goal:** A production-ready, secure, open-source firmware release.

<!--
Today I'm going to walk you through the engineering challenges we faced porting
Dasharo to the ASRock Rack SPC741D8.

This task required deep-diving into hardware analysis, bus topologies, and ACPI
tables. We took a port initiated by the KIT Operating Systems Group and hardened
it into a production-grade product ready for enterprise deployment.
-->

---
layout: two-cols-header
---

### The Hardware Overview

::left::

**ASRock Rack SPC741D8-2L2T/BCM**

* **Processor:** Single Socket E (LGA 4677), supporting Intel Sapphire &
  Emerald Rapids.
* **Form Factor:** CEB (12" x 10.5").
* **Memory:** 8 DIMM slots (DDR5).
* **Expansion:** 4x PCIe 5.0 / CXL 1.1 slots.
* **Network:** 2x 10GbE (Broadcom) + 2x 1GbE.
* **Storage:** 64 MB SOIC-16 SPI Flash (Shared by BIOS + Intel SPS).

::right::

<center><img src="/slides/img/vpub_0x11/asrock_spc741d8.jpg" width="650"></center>

<!--
First, let's look at the beast. It's a CEB form-factor server board designed
for high-performance computing.

Crucially for us firmware engineers, the firmware resides on a single 64MB SPI
flash chip. This chip houses both the BIOS (where Dasharo lives) and the Intel
Server Platform Services—which is the server equivalent of the Management
Engine.
-->

---

### The BMC Landscape

**Current vs. Future State**

* **The Chip:** ASPEED AST2600.
* **Current State:** Proprietary AMI MegaRAC.
  * _Pros:_ Industry standard, stable.
  * _Cons:_ Closed source, "Black Box."
* **The Challenge:** Dasharo must coexist and communicate with this
  proprietary stack.
* **Future Roadmap:** Evaluating an OpenBMC port for a 100% open-source server
  stack.

<!--
A server isn't just a CPU; it's also the Baseboard Management Controller, or
BMC. Currently, this board runs AMI MegaRAC on the AST2600 chip.

While our BIOS is open-source, the BMC is still proprietary. This creates an
environment where our open firmware must talk to a closed-source management
controller. A major item on our roadmap is replacing this with OpenBMC to
achieve the 'holy grail' of a fully open-source server stack.
-->

---

### Dasharo Features Implementation

**From "Booting" to "Feature Complete"**

* **Base:** Backported KIT's coreboot work to Dasharo (v24.12 base).
* **Usability Enhancements:**
  * Setup Menu Password.
  * PCIe Configuration Menu.
  * Firmware Update Mode.
  * USB & Network Stack toggle.
* **Networking:** Full iPXE network boot integration.

<!--
We took the initial port and fortified it. We didn't just want it to boot; we
wanted it to be usable by administrators.

We integrated features like a proper setup menu for PCIe configuration, password
protection for the BIOS menu, and iPXE for advanced network booting. This
transforms the firmware from a research project into a deployable tool.
-->

---

### Security Deep Dive

**Hardening the Platform**

1. **SMM BIOS Write Protection (BWP):**
      * Locks SPI flash hardware.
      * Prevents Ring 0 (OS-level) rootkits from overwriting firmware.
2. **UEFI Secure Boot:**
      * Cryptographically verifies the boot chain (Firmware $\rightarrow$
        Bootloader $\rightarrow$ Kernel).
3. **CBFS Verification:**
      * Ensures integrity of files inside the firmware filesystem.

<!--
Security is paramount in the server space. We enabled SMM BIOS Write
Protection, which locks the SPI flash hardware so that even if an attacker gets
root access to the operating system, they cannot overwrite the firmware to
install a persistent implant.

We also integrated standard UEFI Secure Boot to ensure the chain of trust is
extended from firmware to the OS.
-->

---

### Challenge \#1 - The Flashing Hurdle

**The Roadblock**

* **Goal:** Flash the initial Dasharo binary.
* **Attempt:** Use BMC's built-in web update tool.
* **Failure:** BMC rejected the image.
  * _Reason:_ Signature/Structure mismatch (Not an "Official" OEM binary).
* **Constraint:** Board needed for the Automated Lab (Remote access only).
* **Problem:** Cannot rely on manual clipping for daily development.

<!--
Our first roadmap block was simply getting the code onto the board. We tried the
easy route—using the BMC's built-in web update tool—but it rejected our
open-source binary because it wasn't structured properly or signed by the OEM.

Since we intended to put this board in our automated certification lab, we
couldn't rely on manually clipping onto the chip every time we broke the build.
We needed a reliable, hardware-level flashing solution.
-->

---
layout: two-cols
---

### Solution \#1 - Physical Hardware Analysis

**The Hardware Hack**

* **Discovery:** Undocumented `BIOS_PH1` header near the flash chip.
* **Action:** Multimeter probing against standard SOIC-16 pinout.
* **Mapping:** Identified CS\#, SCK, MOSI, MISO, and VCC.
* **Result:** Custom adapter cable will be created.
  * Connects `BIOS_PH1` $\rightarrow$ RTE (Flasher).
  * Bypasses BMC restrictions entirely.

::right::

<center><img src="/slides/img/vpub_0x11/asrock_spc741d8_bios_chip.jpg" width="300"></center>

<!--
We found an undocumented header on the motherboard labeled `BIOS_PH1`. By
grabbing a multimeter and probing the pins against the standard SOIC-16 flash
chip legs, we successfully mapped the header.

We are building a custom cable connecting this header to our external flasher.
This gave us direct, physical access to the SPI bus, allowing us to bypass the
BMC's restrictions entirely and flash whatever we wanted.
-->

---
layout: two-cols
---

### Lab Automation & RTE Setup

**Continuous Integration / Continuous Deployment (CI/CD)**

* **RTE (Remote Testing Environment):** An external control board connected to
  the server.
* **Capabilities:**
  * **SPI:** External flashing via `BIOS_PH1`.
  * **GPIO:** Control power/reset buttons.
  * **Serial:** Captures logs via UART.
* **Benefit:** Developers can "brick" the board and automatically "unbrick" it
  remotely.
* **Check it out:**: Available on our shop: https://shop.3mdeb.com/product/rte/

::right::

<center><img src="/slides/img/vpub_0x11/rte-v1.1.0-interface-desc.png" width="400"></center>

<!--
To maintain this firmware efficiently, we integrated the server into our Dasharo
Certification Lab. We use a Remote Testing Environment—or RTE.

Think of the RTE as a 'puppet master.' It controls the server's power button and
flash chip. This allows our developers to push dangerous code updates; if the
update breaks the boot, the RTE can be used to reflash a working build, as well
as capture logs from the serial console. This loop is essential for rapid
development.
-->

---
layout: two-cols-header
---

### Challenge \#2 - The Silent Serial Port

::left::

**The Mystery of the Dead Console**

* **Symptom:** Physical COM header and Serial-over-LAN were dead.
* **Impact:** No early boot logs (critical for debugging before video init).
* **Architecture:**
  * Serial ports are managed by the **AST2600 BMC**.
  * BMC connects to PCH via **eSPI**.
* **Root Cause:**
  * BMC listening on **Secondary eSPI (CS1\#)**.
  * coreboot: Only enabled Primary eSPI (CS0\#).

::right::

<center><img src="/slides/img/vpub_0x11/asrock_spc741d8_com.jpeg" width="650"></center>

<!--
Once we could flash, we booted... into silence. The serial ports weren't
working. On modern boards, legacy serial ports are emulated by the BMC and
communicated over the eSPI bus.

We discovered that while coreboot was talking to the primary eSPI channel (Chip
Select 0), this specific board had the BMC wired to the *Secondary* channel
(Chip Select 1). The PCH was effectively shouting into the void.
-->

---

### Solution \#2 - The One-Line Fix

**Configuring the PCH**

* **The Fix:** Instruct the PCH to route UART I/O traffic to CS1\#.
* **The Code:**
    ```c
    /* AST2600 is on eSPI CS1# */
    pci_write_config16(PCH_DEV_LPC, ESPI_CS1_ENABLE, lpcioe);
    ```
* **Outcome:**
  * 0x3F8 (COM1) traffic routing enabled.
  * Full Serial-over-LAN and physical UART access restored.

<!--
The fix was surprisingly elegant. We had to flip a specific bit in the PCH
configuration registers—specifically `ESPI_CS1_ENABLE`.

This single line of code told the chipset: 'Hey, send that serial port traffic
to the second chip select too.' Immediately, our logs lit up. We had full serial
debugging and Serial-over-LAN.
-->

---

### Challenge \#3 - The Windows 11 TPM Error

**"This PC can't run Windows 11"**

* **Anomaly:**
  * **Linux:** Detected TPM 2.0 perfectly.
  * **Windows 11:** Installer claimed no TPM present.
* **Investigation:** Windows relies strictly on ACPI tables for device
  discovery.
* **The Bug:** Hardcoded ACPI path in coreboot: `\_SB_.PCI0`.
  * _Assumptions:_ Assumes single domain (consumer/laptop architecture).
* **Reality:** Server platforms (Sapphire Rapids) have multiple PCIe root
  domains.

<!--
Next, we tried installing Windows 11. It failed, claiming no TPM was present.
This was baffling because Linux saw the TPM just fine.

The issue turned out to be how the firmware 'introduced' the hardware to the OS
via ACPI tables. The code had a hardcoded path assuming the TPM was on `PCI0`.
This is true for laptops, but on a massive server chip with multiple domains,
the TPM wasn't there.
-->

---

### Solution \#3 - Dynamic ACPI Paths

**Intelligent Discovery**

* **The Fix:** Replace static string with dynamic generation.
* **New Logic:**
    ```c
    const struct device *domain = dev_get_domain(dev);
    const char *path = acpi_device_path(domain);
    ```
* **Result:** Firmware dynamically finds the correct root bridge and reports it
  to the OS.
* **Outcome:** Windows 11 installs successfully.

<!--
We refactored the code to stop guessing. We used a function to dynamically
check which domain the TPM was actually attached to, and then generated the ACPI
path based on that reality.

This makes the code robust for both single-socket and multi-socket systems. With
this change, Windows 11 immediately recognized the security module and installed
without issue.
-->

---

### The Dasharo Certification Process

**Ensuring Enterprise Reliability**

* **Why Certify?** Open source must match proprietary reliability.
* **The Routine:**
  * **Automated Tests:** Boot speed, memory training stability, S3/S4 cycles.
  * **OS Validation:** Ubuntu, Windows 11.
  * **Security Validation:** Verifying Secure Boot enforcement and TPM
    measurements.
* **Result:** The SPC741D8 is now officially **Dasharo Certified**.

<!--
Before we release, the firmware goes through the Dasharo Certification Process.

We validate against multiple operating systems, including Windows 11 and Ubuntu.
We run automated suites to verify that security features like Secure Boot aren't
just present in the menu, but are actually enforcing signatures. This
certification gives our users confidence that the firmware is stable.
-->

---
layout: two-cols
---

### Commercial Ecosystem & Availability

**Turnkey Open Source**

* **Dasharo Pro Package**.
  * Pre-built reference systems available (3mdeb shop).
  * Pre-flashed, validated, and ready to deploy.
  * Includes professional support.
* **Value:** Bridges the gap between open-source flexibility and
  enterprise-grade ease of use.

::right::

<center><img src="/slides/img/vpub_0x11/asrock_spc741d8_setup_menu.png" width="650"></center>

<!--
We know not everyone wants to compile their firmware. That's why we offer this
as a turnkey solution.

You can buy the ASRock server pre-flashed with Dasharo directly from our shop.
It comes validated and ready to deploy. This approach bridges the gap between
the flexibility of open source and the ease of use required by enterprise IT
departments.
-->

---

### Summary & Roadmap

**The Path Forward**

* **Achievement:** A stable, secure, open-source firmware for Sapphire Rapids
  servers.
* **Immediate Next Steps:**
  * Upstreaming all patches to coreboot main.
  * Continued maintenance (Dasharo v0.9.1 release).
* **Long Term:**
  * OpenBMC integration for the AST2600.
* **Check it out:** Check out the shop, subscribe to the newsletter, and try
  Dasharo.

<!--
To summarize: We overcame proprietary flashing blocks, complex bus routing, and
ACPI definitions to bring Dasharo to the ASRock SPC741D8.

The board is now certified and available. Our next big focus is getting OpenBMC
running on this board to complete the open ecosystem. Thank you for your time,
and I'm happy to take any questions.
-->
