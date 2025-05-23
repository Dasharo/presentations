<!--
SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>

SPDX-License-Identifier: CC-BY-SA-4.0
-->

class: center, middle, intro

# Dasharo onboarding

### v0.1.0

.center[<img src="/remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">]

---

# Contents

These tasks can be done on two different platforms:
Novacustom Laptop or Remote Testing Environment with Protectli VP2410

Next section is dedicated to Novacustom laptop

---
# Prerequisities

* Hardware
  * Novacustom Laptop
  * Power supply
  * Ethernet cable
  * Flashing tool (optional; in case of bricking the device)

* Software
  * Docker installed on host machine
  * Source of the coreboot
  * edk2 sources

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
* Mainly, process is described in instruction.
* Flashing is performed on target device, itself.
* Before attempting flashing make sure the `BIOS lock` is turned off, otherwise
flashing will fail.
     - make sure the laptop is powered off
     - turn on the device
     - wait for the splash screen
     - press key for `Setup`
        - Alternatively press the key for one-time boot menu and choose `Setup`
     - Select `Dasharo System Features`
     - Select `Dasharo Security Options`
     - Make sure the option `Lock the BIOS boot medium` is unchecked
* To enter flashing mode, device should be booted properly:
 - make sure laptop is powered off
 - turn on the device
 - wait for splash with one-time boot menu
 - press key for one-time boot menu
 - choose option `iPXE Network Boot`
 - choose option `Dasharo Tools Suite`
 - choose option 9 (Shell)

---
# Flash Process - cont.
* check flashrom is available on the laptop
```
flashrom -p internal
```
* connect laptop to Ethernet, get its IP

* copy previously compiled Dasharo firmware:
```
scp build/coreboot.rom root@<here IP of NVC laptop>/tmp
```
* connect with scp
```
ssh root@<here IP of NVC laptop
cd /tmp
flashrom -p internal --ifd -i bios -w /tmp/coreboot.rom
```
* After finishing(still, under ssh):
```
reboot
```
* Test whether flashing correctly
---
# Troubleshooting
* If the build process described in "Build Dasharo BIOS firmware" fails,
  try using the `build.sh` script available in the repository.
  It is recommended to take a look inside and famliarize yourself with
  what the script actually does. In version 1.7.2 you can notice that:
  * The script runs `make clean` every time.
  * The script copies the `.config` configuration file from the selected
    devices default configuration overwriting any changes you could have
    made. Make sure to comment out that line.
  * The device name in variable `BOARD` may be different from the device
    you are building for. Make sure to change it to the correct value.
    You can find the possible values in the `configs` directory where
    you can find files named `config.<BOARD NAME>`.
    You can use the `<BOARD NAME>` part as the value for the `BOARD` variable.

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
Another solution is to manually edit the `known_hosts` file using a text
editor and deleting the lines corresponding to the host. In this example
the message says `/home/coreboot/.ssh/known_hosts:1` which means we
need to delete line number `1` in the `/home/coreboot/.ssh/known_hosts` file.
Generally we should be cautious when receiving this warning, but in this case
it is expected for the warning to appear every time we are network booting.

* After flashing new firmware the `iPXE Network Boot` option may not appear
in the boot menu. In that case make sure that in the `Setup` the option
`Dasharo System Features -> Networking Options -> Enable network boot`
is checked.
---

* When trying to connect via `ssh` or `scp` to the machine an error like
this may appear:
```
ssh: connect to host 192.168.10.152 port 22: Connection refused
```
That means that the ssh server is not running on the machine. To start it type:
```bash
/usr/sbin/sshd
```
If there is no output then the ssh server should now be running fine. If you get:
```
sshd: no hostkeys available -- exiting.
```
Then we need to create the hostkeys. Type:
```bash
cd /etc/ssh; ssh-keygen -A
```

* When trying to send the `coreboot.rom` via scp an error may appear despite
being able to connect via ssh:
```
scp: Connection closed
```
That may mean that the OpenSSH version installed on the machine doesn't support
`sftp` protocol which is used by scp. To overcome this you can tell `scp`
to use a legacy protocol by providing the option `-O` like so:
```bash
scp -O coreboot.rom root@<IP of the machine>/tmp/coreboot.rom
```
instead of:
```bash
scp coreboot.rom root@<IP of the machine>/tmp/coreboot.rom
```
---
# Recovery

After bricking the device there is need to perform the same action, as with
brand new device.

???
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
`Payload->TianoCore setup menu key`, press button Help.
---
# Exercise 1

* Change boot option key
* Find in configuration key: `EDK2_BOOT_MENU_KEY`/"TianoCore boot menu key"
* Change value (button Help will show possible options)
* Check changes (build, reflash laptop)

--
* Result in next slide:

???
Comment

---
# Exercise 1-solution

.center[.image-65[![](/img/Boot_Setup_key_modified.jpg)]]

---
# Exercise 2
* Change option for booting option `iPXE Network Boot` to add own string
* Recompile, flash
* Test changes
* Solve results in next slide

---
# Exercise 2-solution
* Find string in `.config` file: `CONFIG_EDK2_IPXE_OPTION_NAME`
* Change value (here: change to `iPXE Network Boot-moj tekst`)
.center[.image-45[![](/img/Boot_option-custom.jpg)]]

---
# Excercise 3
* Change SMBIOS variable, SKU Number
* String is set up in mainboard's code
* Find in directory, in `src/mainboard` proper file, function, change phrase
* Compile, burn to the flash
* Check value using `dmidecode` (run on target device)
--
.column-1[
.middle-1[Result on next slide...]
]

---
# Exercise 3-solution

* Source:

```
coreboot/src/mainboard/clevo/adl-p/ramstage.c
```

function:
```
const char *smbios_system_sku(void);
```

--
.center[.image-45[![](/img/SKU_String_modified.jpg)]]

---
# Remote Protectli VP2410 platform

---
# Prerequisities:
- python
- telnet
- ready to use SnipeIT account ([instructions](https://gitlab.com/3mdeb/rte/docs/-/blob/master/docs/snipeIT_theory_of_operation.md))

---

## Setup
Clone [osfv-scripts](https://github.com/Dasharo/osfv-scripts) repository:

```bash
git clone https://github.com/Dasharo/osfv-scripts.git

```
Create virtual environment and activate it:

```bash
virtualenv venv
```

```bash
source venv/bin/activate
```

Navigate to the cloned repository:

```bash
cd osfv-scripts/osfv_cli
```

Install poetry:

```bash
pip install poetry
```

Build and install utility:

```bash
make install
```

Test if script works (you should get the list of possible subcommands):

```bash
osfv_cli snipeit -h
```

---

### Connecting and basic operations
First of all make sure that the platform is available for checking out:

```
osfv_cli snipeit list_unused | grep VP2410 -A 8
```

If platform is available you should get this entry in output:

```

Asset Tag: Protectli VP2410_1, Asset ID: 317, Name: , Serial:
Lab location:
RTE IP: 192.168.10.233
RTE cpuid:
RTE Rev:
RTE MAC address: 02:42:66:1f:90:13
Sonoff IP:
PiKVM IP:
PiKVM HW Base:
```

Checkout the platform:

```
osfv_cli snipeit check_out --rte_ip 192.168.10.233
```

---

### Connecting and basic operations - cont.

Now if you run `osfv_cli snipeit list_used | grep VP2410 -A 8` you should get the same entry of Protectli as above.

You can get list of possible operations by running

```
osfv_cli rte --rte_ip 192.168.10.233 -h
```

For example you can check the state of the GPIO pin 0:

```
osfv_cli rte --rte_ip 192.168.10.233 gpio get 0
```

Access the platform by serial interface:

```
osfv_cli rte --rte_ip 192.168.10.233 serial
```

Fetch current ROM image:

```
osfv_cli rte --rte_ip 192.168.10.233 flash read --rom vp2410-read.rom
```

---

### Connecting and basic operations - cont.

Writing new ROM image:

```
osfv_cli rte --rte_ip 192.168.10.233 flash write --rom ~/coreboot/protectli_vault_glk_v1.0.15.rom
```

Switching power on relay:
```
osfv_cli rte --rte_ip 192.168.10.233 rel tgl
```

---

# Building firmware

This can be done as shown in [building manual](https://docs.dasharo.com/variants/protectli_vp2410/building-manual/).

Tips:
- In protectli blobs repository make sure you are on the branch with the same name as in coreboot repository
- Instead of creating symbolic link you can simply copy Geminilake (inside root coreboot directory):

    ```
    cp -r 3rdparty/blobs/mainboard/protectli/vault_glk/GeminilakeFspBinPkg 3rdparty/fsp/GeminilakeFspBinPkg
    ```

---
## Exercises

1. Change boot menu key
    - Find how to change boot menu key, find `CONFIG_TIANOCORE_BOOT_MENU_KEY`
    - You can use values between `0x0001` (UP) and `0x0017` (ESC)

---

### Excercise 1 - solution

Modify file `coreboot/configs/config.protectli_vp2410`

.center[.image-45[![](/img/boot_key_modified.png)]]

---

### Exercise 2

Change bios information - "Vendor", it can be checked using `dmidecode`:

.center[.image-45[![](/img/dmidecode_original.png)]]

---

### Exercise 2 - solution

Edit file `coreboot/src/arch/x86/smbios.c`, function `smbios_write_type0`, variable `t->vendor`

.center[.image-45[![](/img/dmidecode_changed.png)]]

---

# Remote Protectli VP4630 platform

## Prerequisities

* python
* telnet
* ready to use SnipeIT account ([instructions](https://gitlab.com/3mdeb/rte/docs/-/blob/master/docs/snipeIT_theory_of_operation.md))

---
The following steps will be nearly identical to the VP2410 process described
above. The key difference will be substituting the asset ID and RTE IP in
snipeit to those corresponding to our device. Also, we will use the
 [`protectli_root/build_coreboot`](https://github.com/protectli-root/build_coreboot)
  github repository branch dedicated to our device -
  namely `protectli_vp4630_v1.0.17`.

---

## Setup
Identically as demonstrated for VP2410 above, clone
 [osfv-scripts](https://github.com/Dasharo/osfv-scripts) repository:

```bash
git clone https://github.com/Dasharo/osfv-scripts.git

```
Create virtual environment and activate it:

```bash
virtualenv venv
```

```bash
source venv/bin/activate
```

Navigate to the cloned repository:

```bash
cd osfv-scripts/osfv_cli
```

Install poetry:

```bash
pip install poetry
```

Build and install utility:

```bash
make install
```

Test if script works (you should get the list of possible subcommands):

```bash
osfv_cli snipeit -h
```

---

### Connecting and basic operations

First, let's try to find our desired platform on the unused device list. Same
process as for VP2410, we'll just substitute our model name and receive a
different RTE IP and Asset ID.

```bash
osfv_cli snipeit list_unused | grep VP4630 -A 8
```

If you see the following result, it means the platform is free and available
for use. Make note of the RTE IP address, we will need it to work with our
device.

```bash

Asset Tag: Protectli VP4630, Asset ID: 291, Name: , Serial:
Lab location:
RTE IP: 192.168.10.244
RTE cpuid:
RTE Rev: v1.1.0
RTE MAC address: 02:42:48:d5:bf:fc
Sonoff IP:
PiKVM IP:
PiKVM HW Base:

```

Checkout the platform to mark it as used:

```bash
osfv_cli snipeit check_out --rte_ip 192.168.10.244
```

---

### Connecting and basic operations - continued

Now, if you run `osfv_cli snipeit list_used | grep VP4630 -A 8`
you should get the same entry of Protectli VP4630 as above. This means we've
successfully marked our platform as in-use.

We can access the VP4630 via RTE in the exact same manner as the VP2410.
You can get a list of possible operations by running:

```bash
osfv_cli rte --rte_ip 192.168.10.244 -h
```

For example you can check the state of the GPIO pin 0:

```bash
osfv_cli rte --rte_ip 192.168.10.244 gpio get 0
```

Access the platform by serial interface:

```bash
osfv_cli rte --rte_ip 192.168.10.244 serial
```

Toggle power on relay:

```bash
osfv_cli rte --rte_ip 192.168.10.233 rel tgl
```

---

## Building firmware

This can be done as shown in this
[building manual](https://docs.dasharo.com/variants/protectli_vp46xx/building-manual/).

**NOTE:** When instructed to obtain the proprietary Intel blobs, please use
[our repository](https://github.com/Dasharo/protectli-blobs).

---

## Flashing the firmware ROM onto the VP4630

To do so, we will use the exact same commands as for the VP2410, substituting
our device's RTE IP address. First, I recommend you read the currently flashed
.rom from the platform as a backup file. Please go back to the `osfv_cli`
branch in your `osfv-scripts/snipeit` directory and fetch the current ROM image:

```bash
osfv_cli rte --rte_ip 192.168.10.244 flash read --rom vp4630-read.rom
```

Now, we can attempt to flash our own firmware onto the device, same as for the
VP2410. Adjust the path to your newly built ROM if necessary. This command
should be accurate, provided you followed the building manual above:

```bash

osfv_cli rte --rte_ip 192.168.10.244 flash write --rom ~/coreboot/protectli_vault_cml_v1.0.19_vp4630_vp4650.rom
```

---

### Exercise 1

1. Change the boot menu key
    - Try to figure out how to change the boot menu key, similarly as for the VP2410.
    **HINT**: find `CONFIG_EDK2_BOOT_MENU_KEY` - _slightly different than the
    TianoCore option for VP2410!_
    - You can use values between `0x0001` (UP) and `0x0017` (ESC)

---

### Excercise 1 - solution

Similarly to the VP2410 solution, we need to modify our coresponding coreboot
config file. For our device, it's called
`coreboot/configs/config.protectli_cml_vp4630_vp4650`.

I'll modify it so that the boot menu key is Esc:

![](/img/vp4630_boot_key_config.png)

...and it works!

![](/img/vp4630_boot_key_changed.png)

---

### Exercise 2

Change the BIOS information - "Vendor", it can be checked using `dmidecode`.

---

### Exercise 2 - solution

Same as for the VP2410, edit file `coreboot/src/arch/x86/smbios.c`, function
`smbios_write_type0`, variable `t->vendor`:

![](/img/vp4630_bios_vendor_config.png)

...and it works!:

![](/img/vp4630_bios_vendor_changed.png)

---
## Flashing the firmware ROM onto protectli V1410

Before V1410 got flashed, a backup rom file has been created containing
whatever was on this device before intervention:

```bash
osfv_cli rte --rte_ip 192.168.10.198 flash read --rom dump.rom
```

Now, we follow the exact same procedure as for other devices to flash via RTE:

```bash

osfv_cli rte --rte_ip 192.168.10.198 flash write --rom ~/coreboot/protectli_v1410_v0.9.2.rom
```
Expected output indicating a success:

```
Reading old flash chip contents...
done.
Erasing and writing flash chip...
Erase/write done.
Verifying flash...
VERIFIED.


Flash written
```
---

### Exercise 1

1. Change the boot menu key
    - Try to figure out how to change the boot menu key, similarly as for the VP2410.
    **HINT**: find `CONFIG_EDK2_BOOT_MENU_KEY` - _slightly different than the
    TianoCore option for VP2410!_
    - You can use values between `0x0001` (UP) and `0x0017` (ESC)

---

### Excercise 1 - solution

Inside config:
`coreboot/configs/config.protectli_vault_jsl_v1410`.

the part responsible for boot menu and boot setup keys with applied changes:

![](/img/dasharo_1410_Ex1.png)

---

### Exercise 2

Change the BIOS information - "Vendor", it can be checked using `dmidecode`.

---

### Exercise 2 - solution
Access file `coreboot/src/lib/smbios.c`, and change in function
`smbios_write_type0`, variable `t->vendor`:

![](/img/dasharo_1410_Ex2.png)
