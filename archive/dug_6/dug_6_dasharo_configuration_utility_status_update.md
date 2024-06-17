<!-- markdownlint-disable-next-line first-line-h1 -->
class: center, middle, intro

# Dasharo Configuration Utility Status Update

## Tymoteusz Burak

.center[
    <img
        src="/remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg"
        width="150px"
        style="margin-left:-20px">
    ]

---

# `whoami`

.right-column50[

<img
    src="/remark-templates/3mdeb-presentation-template/images/tymek_burak.png"
    width="200px"
    style="marking-top:-50px; margin-left:50px">
]

.left-column50[

<!-- markdownlint-disable no-inline-html -->

**Tymoteusz Burak**
- _Junior Embedded Systems Developer_
- 1 year an 3mdeb
- Integration of functionalities into Zarhus OS
- <a href="mailto:tymoteusz.burak@3mdeb.com">
  <img
    src="/remark-templates/3mdeb-presentation-template/images/email.png"
    width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
    tymoteusz.burak@3mdeb.com
  </a>
- <a href="https://www.linkedin.com/in/tymoteusz-burak-a108252a0/">
    <img
      src="/remark-templates/3mdeb-presentation-template/images/linkedin.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      linkedin.com/in/tymoteusz-burak-a108252a0
    </a>
  ]

<!-- markdownlint-enable no-inline-html -->

---

# Agenda

- Reminder: What is DCU?
- What we envisioned
- Current Status
- The problem
- Our solution
- What does this mean to Dasharo users
- Example Scenario
- Q&A

???

- Here is the Agenda
- First I'll give you a quick reminder what is dasharo configuration utility
and what was presented on it during the Dasharo Configuration Utility
Introduction by Piotr Król at Dasharo User Group #4
- Then we're gonna go over what we envisioned for this tool and where we are now
- I'll end the presentation with an example scenario how Dasharo Configuration
Utility might help you out in practice

---

# Reminder: What is DCU?

_The Dasharo Configuration Utility is a tool designed to configure Dasharo
firmware binary images._

**Until now there was support for**

- Customizing the boot logo
- Setting unique UUIDs or Serial Numbers in SMBIOS tables

???

- Dasharo Configuration Utility is our dedicated tool that enabled
customization of Dasharo binaries for users
- We needed a more scalable solution
- Published around 7 months ago
- Introduced at Dasharo User Group #4
- Upon release allowed only for customization of the boot splash logo and
  managing the Serial Numbers for devices
- Available as a standalone or a container for easy use

---

# Reminder: What is DCU?

_The Dasharo Configuration Utility is a tool designed to configure Dasharo
firmware binary images._

.left-column50[
.code-15px[

```sh
$ ./dcuc logo coreboot.rom -l bootsplash.bmp
```

]
]

.right-column50[
    .center[
        <img
            src="/img/custom_boot.jpg"
            width="399px">
        ]
]

???

- In practice it allowed you to do stuff like this :)
- This is the container version
    + `dcu` vs `dcuc`

---

# What we envisioned

- Custom Configuration Profiles
- Sane Defaults Verification
- Data Migration Tools
- Enterprise Security Features
- Chipsec and HSI Checks Integration
- Integration with Commercial Tools like Binarly

???

- Of course this was only the first iteration and we had ambitious plans how we
  can expand on the idea and bring more functionality to the users

- **Custom Configuration Profiles**
    + Creation of custom configuration profiles that can be applied
    across multiple systems, ensuring consistency in deployment.

- **Sane Defaults Verification**
    + Verifying and aligning user configurations with established sane defaults,
    ensuring optimal security and performance settings for various hardware
    setups

- **Data Migration Tools**
    + Smooth transition of data and settings from proprietary BIOS to Dasharo
  firmware.

- **Enterprise Security Features**
    + Advanced security features like TPM configuration, secure boot
  customization, and hardware-based encryption support.

- **Integration of tools like Chipsec and Binarly for security audits**

---

# Current Status

- ~~Custom Configuration Profiles~~
- ~~Sane Defaults Verification~~
- ~~Data Migration Tools~~
- ~~Enterprise Security Features~~
- ~~Chipsec and HSI Checks Integration~~
- ~~Integration with Commercial Tools like Binarly~~

<br>

.center.image-35[![](/img/slacking_off.png)]

???

- And here is what we actually delivered.
- But that doesn't mean we've been inactive.

---

# The problem

.center[
    <img
        src="/img/x86_ring_level_arrow.svg"
        height="550px"
        style="margin-top:-70px; margin-left:20px"
    >
]

???

- _SMM is a special operating mode in x86 processors that handles system-wide
functions like:_
    + _power management_
    + _system hardware control_
    + _firmware settings storage_
- To be precise settings are stored on SMM mediated part of SPI memory.
- This separates this funtionality from the userspace protecting it from
  software attacks
- coreboot stores it's firmware settings in the SMM
    + Until recently they could be only modified by hand from the UEFI menu
    + So we made a tool for changing the settings via an util/smmstoretool
- We had to develop a way to access the contents of the dasharo binary without
  manually setting the UEFI variables.

---

# Our solution

.center[

<!-- markdownlint-disable-next-line heading-increment -->
### [smmstoretool](https://github.com/coreboot/coreboot/tree/main/util/smmstoretool)

<img
    src="/img/coreboot_repo_smmstoretool_sc.png"
    height="390px"
    style="margin-left:100px">
]

???

- Here at 3mdeb we've developed and upstreamed the `smmstoretool` utility for
  offline modification of the SMM storage in the coreboot or Dasharo binaries
- In other words we can now set our firmware settings without booting it up

---

# What does this mean to Dasharo users

<!-- Accepted values are slanted so they appear correctly on the presentation -->

.code-15px[
- **Get a list of settings in a binary**:

```sh
$ ./dcuc variable --list coreboot.rom
Settings in coreboot.rom:
NAME		VALUE		    ACCEPTED VALUES
MeMode	  Enabled          Enabled / Disabled (Soft) / Disabled (HAP)
```

- **Change a setting**:

```sh
$ ./dcuc variable coreboot.rom --set "MeMode" --value "Disabled (Soft)"
```

```sh
$ ./dcuc variable --list coreboot.rom
Settings in coreboot.rom:
NAME		VALUE			ACCEPTED VALUES
MeMode	  Disabled (Soft)  Enabled / Disabled (Soft) / Disabled (HAP)
```

]

???

- We expanded the DCU with additional utilities based on the smmstoretool
- This allows for easy modification of binaries and the firmware settings

**Use Cases**

- Turning on serial support from the start for headless platforms
or for automatic testing
- Set power state after failure so the board boots automatically when the power
to supply unit is delivered - also useful for some test cases.
- Set the network boot to enabeld (defaults to disabled). So after flashing we
can readily boot from network (useful in manufacturing, testing,
OS installation).
- Change any setting you want from the OS rather than from firmware menu.
    + It can be done as long as the SMM Bios Write Protection is not locked.
    + It is more of a development/hacking/manufacturing feature, as in final
    products we advise to turn the SMM protection ON.

---

# What does this mean to Dasharo users

<!-- Accepted values are slanted so they appear correctly
on the presentation-->

.code-15px[
- **Get a list of settings supported by this tool**:

```sh
$ ./dcuc variable --list-supported coreboot.rom
Settings that can be modified using this tool:
NAME				        ACCEPTED VALUES
LockBios			        Disabled / Enabled
NetworkBoot			     Disabled / Enabled
UsbDriverStack			  Disabled / Enabled
SmmBwp				      Disabled / Enabled
Ps2Controller			   Disabled / Enabled
BootManagerEnabled		  Disabled / Enabled
PCIeResizeableBarsEnabled   Disabled / Enabled
EnableCamera			    Disabled / Enabled
EnableWifiBt			    Disabled / Enabled
SerialRedirection		   Disabled / Enabled
SerialRedirection2		  Disabled / Enabled
MeMode				      Enabled / Disabled (Soft) / Disabled (HAP)
FanCurveOption			  Silent / Performance
CpuThrottlingThreshold	  0-255 (Actual supported values may vary)
```

]

???

- You can also view supported settings with this command
- Actual implemented values may vary between devices.
    + For example, CPU throttling temperature is adjustable from TjMax to
    TjMax-63.
    + To see what values are implemented in a given build, check the UEFI setup
    menu.

**Closing remarks**

- We'd love to hear your feedback what features you're most excited about and
what you'd want to see bringed to life first so we know where to prioritize our
efforts.

---

<br>
<br>
<br>

## .center[Example Scenario]

---

# Example Scenario

<br>
<br>
<br>
<br>

.code-15px[

```sh
$ git clone https://github.com/Dasharo/dcu.git
$ cd dcu
```

]

---

# Example Scenario

<br>

.code-15px[

```sh
$ ./dcuc variable --list-supported msi_ms7d25_v1.1.3_ddr4.rom
Settings that can be modified using this tool:
NAME                          ACCEPTED VALUES                                  
LockBios			        Disabled / Enabled
NetworkBoot			     Disabled / Enabled
UsbDriverStack			  Disabled / Enabled
SmmBwp				      Disabled / Enabled
Ps2Controller			   Disabled / Enabled
BootManagerEnabled		  Disabled / Enabled
PCIeResizeableBarsEnabled   Disabled / Enabled
EnableCamera			    Disabled / Enabled
EnableWifiBt			    Disabled / Enabled
SerialRedirection		   Disabled / Enabled
SerialRedirection2		  Disabled / Enabled
MeMode				      Enabled / Disabled (Soft) / Disabled (HAP)
FanCurveOption			  Silent / Performance
CpuThrottlingThreshold	  0-255 (Actual supported values may vary)
```

]

---

# Example Scenario

<br>
<br>
<br>

.code-15px[

```sh
$ ./dcuc variable --list msi_ms7d25_v1.1.3_ddr4.rom
Settings in msi_ms7d25_v1.1.3_ddr4.rom:
No firmware volume header present
No valid firmware volume was found
Failed to find variable store in "msi_ms7d25_v1.1.3_ddr4.rom"
NAME                          VALUE                         ACCEPTED VALUES
```

]

---

# Example Scenario

<br>
<br>

.code-15px[

```sh
$ ./dcuc variable msi_ms7d25_v1.1.3_ddr4.rom --set "SerialRedirection" --value "Enabled"
No firmware volume header present
No valid firmware volume was found

The variable store has not been found in the ROM image
and is about to be initialized. This situation is normal
for a release image, as the variable store is usually
initialized on the first boot of the platform.

Successfully created variable store in "msi_ms7d25_v1.1.3_ddr4.rom"
Successfully set variable SerialRedirection in the variable store.
```

]

---

# Example Scenario

.center[
<img
    src="/img/dcu_serialredirection_enabled.png"
    height="390px"
    style="margin-left:150px">
]

---

<br>
<br>
<br>

## .center[Q&A]
