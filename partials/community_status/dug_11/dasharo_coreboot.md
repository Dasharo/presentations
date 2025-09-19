## <center>Dasharo/coreboot PRs</center>

<center><img src="/@fs/repo/img/dug_10/coreboot_prs.png" width="600"></center>
<center><img src="/@fs/repo/img/dug_11/dasharo_coreboot.png" width="650"></center>

<!--

* Average tempo of margining changes dramatically increased thanks to final
results of Q2 and Q3 so far from 29.3PR/quarter to 33.7PR/quarter, it is over 4
more PRs/quarter on average in whole history of Dasharo, obviously we are a lot
over average with 53 PRs merged.
* Backlog of open PRs classically growing faster and faster. So if you want to
help with review and validation feel free to join bug bounty program.
* We definitely hit record high second quarter in row in opening new PRs, where
our average increased to 46.6PRs/quarter from 41.9PRs and we high 88PRs this
quarter so far.
* This proves how Dasharo accelerates.

* Average mergining tempo per quarter:
  - 26+39+31+21+37+29+29+22+50+53=337/10=33.7
* Average PRs creation:
  - 40+46+40+26+46+38+43+32+67+88=466/10=46.6

Modify and run:
./diagrams/dasharo_forks.py

-->

---

## <center>Dasharo/coreboot upstreaming</center>

<center><img src="/@fs/repo/img/dug_11/coreboot_upstreaming.png" width="600"></center>
<center><img src="/@fs/repo/img/dug_11/dasharo_coreboot_upstraming.png" width="600"></center>

<!--

On average we upstream ~2770SLOC every quarter, what is increase by 10% from
previous quarter, but considering how much code sitting on our branches
downstream it would take us years to deliver everything even if we would stop
doing development. Despite this was record high quarter.

Luckily we see interesting activity that some people pick code from Dasharo and
start upstreaming. We are very grateful for that.

Average added:
- 2240+4203+173+2927+3819+3447+50+2751+3241+4923=22851/10=2770

Top is total:

```shell
~/src/3mdeb/dasharo/presentations/diagrams/coreboot-upstreaming.sh
```

-->

---

### <center>Delta `dasharo` branch vs upstream v24.12 tag</center>

<br>

#### <center>`673 files changed, 2237 insertions(+), 40101 deletions(-)`</center>

<br>

### <center>Top Upstreamers</center>

- **Michał Żygowski (miczyg):** +2511/-48
  - _src/superio/nuvoton: Add HWM initialization code_
  - _mb/msi/\{ms7d25,ms7e06}/devicetree.cb: Add fan control config_
  - _util/amdfwtool: Handle address mode properly for Turin_
- **Michał Kopeć (mkc):** +1071/-4
  - _mb/novacustom/mtl-h/var/dgpu: Add NVIDIA dGPU ASL code_
  - _mb/lenovo/m900_tiny: Put options in CFR cbtable_
- **Krystian Hebel:** +793/-58
  - _soc/power9/rom_media.c: find CBFS in PNOR_
  - _ppc64: Kconfig switch for bootblock in SEEPROM, zero HRMOR_

<!--

We see quite a lot of interesting contribution. First of all massive nuvoton
superio driver landed upstream thanks to Miczyg work. Congratulations. Miczyg
also improve MSI as well as starting to upstream code for Turin. There is also
not visible here statistics which we may consider in future which is OpenSIL
public repository.

Michał Kopeć did great job bringing dGPU code for Novacusom laptops as well as
some improvements for Lenovo M900.

Krystian Hebel finished cooperation with 3mdeb at the end of July, but his
patches with 3mdeb email keeps landing to coreboot. Especially those related to
our POWER9 port.

We are grateful for all effort big and small.

Open file in LibreOffice and sort after lines added, you can limit file by:

```shell
./contribution-stats list -r coreboot -s 03/20/2025 -e 06/10/2025 -o dug10.csv
```

-->
