class: center, middle, intro

<img src='remark-templates/3mdeb-trainings-template/images/intro-logo.svg' class='intrologo'>

## Novacustom flashing

---
# Prerequisities

## Hardware
* Novacustom Laptop 
* Power supply
* Ethernet cable
* Flashing tool (optional; in case of bricking the device)

## Software
* Docker installed on host machine
* Source of the coreboot
* edk2 sources
These sources are distributed as submodules for coreboot tree.

???
Flashing tool is not absolutely needed, unless laptop is not bricked.  

---
# Types and sources

* There is need to properly identify model and version of the supported
hardware. 
  - NS5* series - model with bigger screen, additional numeric keypad
various minor properties
  - NV4* series - 14" laptop without numeric keypad, monochromatic keyboard
backlight
* Sources:
  - ADL - Alder Lake processor used(Intel 12.gen)
  - TGL - Tiger Lake processor used(Intel 11.gen)
---

# Documentation 
* Official webpage for documentation:
https://docs.dasharo.com/
* Path to more specific information: 
  - Supported hardware -> Novacustom Laptops -> Building manual

---
# Build Process
* Described in "Build Dasharo BIOS firmware"
https://docs.dasharo.com/unified/novacustom/building-manual/
* Make sure testing model and platform
* Chooose proper sources, depending on processor type and Novacustom laptop
model (compilation for Novacustom NV41PZ checkout `clevo/develop`) 
* First time build:
```
make olddefconfig && make
```
further, there is need for only `make` command.

---

# Flash Process
Mainly, process is described in instruction.

TODO: Describe process
F12-> choose option 9 (Shell)

check flashrom is available on the laptop
```
flashrom -p internal
```

connect laptop to Ethernet, get its IP

copy previously compiled Dasharo firmware:
```
scp build/coreboot.rom root@<here IP of NVC laptop>/tmp
```


connect with scp
```
ssh root@<here IP of NVC laptop
cd /tmp
flashrom -p internal -i RW_SECTION_A --fmap -w /tmp/coreboot.rom
```
After finishing(still, under ssh):

```
reboot
```

Test whether flashing correctly

---
# Troubleshooting
* During SSHing process the following message can occur:
```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ECDSA key sent by the remote host is
SHA256:uBHMBbOlesrKFIwafxOTfk0sVoL59tmbnWqKQm08pA4.
Please contact your system administrator.
Add correct host key in /home/coreboot/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in /home/coreboot/.ssh/known_hosts:1
  remove with:
  ssh-keygen -f "/home/coreboot/.ssh/known_hosts" -R "192.168.4.236"
ECDSA host key for 192.168.4.236 has changed and you have requested strict checking.
Host key verification failed.
lost connection
```
Solution is in the line:
```
ssh-keygen -f "/home/coreboot/.ssh/known_hosts" -R "192.168.4.236"
```
---
# Recovery

TBD:
In case there is problem, computer is bricked there is need to 
reflash using external programmer

---
# Change key
* Config option responsible for entering the SETUP is:
```
CONFIG_EDK2_SETUP_MENU_KEY
```
* Config option responsible for one-time boot option is:
```
CONFIG_EDK_BOOT_MENU_KEY
```
Proper values can be found issuing command:
```
make menuconfig
```
Section `Payload->TianoCore boot menu key` and 
`Payload->TianoCore setup menu key`, press button Help

---

class: center, middle, outro

# Str 6.
<img src='remark-templates/3mdeb-trainings-template/images/intro-logo.svg' class='intrologo'>

## Thank you for trusting us
