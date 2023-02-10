class: center, middle, intro

<img src='remark-templates/3mdeb-trainings-template/images/intro-logo.svg' class='intrologo'>

## Novacustom flashing

---
# Prerequisities

## Hardware
* Novacustom Laptop 
* Power supply
* Ethernet cable
* Flashing tool (in case of bricking the device)

## Software
* Docker installed on host machine
* Source of the coreboot
* edk2 sources
These sources are distributed as submodules for coreboot sources

???
Flashing tool is not absolutely needed, unless laptop is not bricked.  

---

# Documentation 
* Official webpage for documentation:
https://docs.dasharo.com/
* Path to more specific information: 
  - Supported hardware -> Novacustom Laptops -> Building manual

---
# Build Process
*
 
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

copy previously compiled coreboot:
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
# Recovery

TBD:
In case there is problem, computer is bricked there is need to 
reflash using external programmer


---

class: center, middle, outro

# Str 6.
<img src='remark-templates/3mdeb-trainings-template/images/intro-logo.svg' class='intrologo'>

## Thank you for trusting us
