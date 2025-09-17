## <center>Dasharo/coreboot PRs</center>

<center><img src="/@fs/repo/img/dug_10/coreboot_prs.png" width="600"></center>
<center><img src="/@fs/repo/img/dug_10/dasharo_coreboot.png" width="650"></center>

<!--

* Our average tempo of margining changes is 29.3PR/quarter, we are slightly above with 31PRs merged.
* Backlog of open PRs classically growing faster and faster. So if you want to help with review and validation feel free to join.
* We definitely hit record high in opening new PRs, where our average is 41.9PRs and we high 62PRs this quarter. And it is not yet end.

* Average margining tempo per quarter:
  - 26+39+31+21+37+29+29+21+31=264/9=29.3
* Average PRs creation:
  - 40+46+40+26+46+38+43+34+62=375/9=41.9

Modify and run:
./diagrams/dasharo_forks.py

-->

---

## <center>Dasharo/coreboot upstreaming</center>

<center><img src="/@fs/repo/img/dug_10/coreboot_upstreaming.png" width="600"></center>
<center><img src="/@fs/repo/img/dug_10/dasharo_coreboot_upstraming.png" width="600"></center>

<!--

On average we upstream ~2500SLOC every quarter. This quarter we are so far
already above the average. So maybe we don't work on issues much, but we definitely opened more PRs and upstreamed more code than average.

Average added:
- 2240+4203+173+2927+3819+3447+50+2751+3241=22851/9=2539

Top is total:

```shell
./contribution-stats list -r coreboot -s 01/01/2000 -e 06/10/2024 -o dug6.csv
```

```shell
awk -F';' '{sum += $6} END {print sum}' dug6.csv #added lines
awk -F';' '{sum += $7} END {print sum}' dug6.csv #removed lines
```

-->

---

### <center>Delta `dasharo` branch vs upstream v24.12 tag</center>

<br>

#### <center>`673 files changed, 2237 insertions(+), 40101 deletions(-)`</center>

<br>

### <center>Top Upstreamers</center>

- **Michał Kopeć (mkc):** +3121/-6
  - _mb/novacustom/mtl-h: Add discrete graphics variant_
  - _Documentation/mainboard/lenovo: Add ThinkCentre M700/M900 Tiny_
  - _ec/dasharo/ec: Add DTT power and battery participants_
- **Krystian Hebel (khebel):** +104/-1
  - _drivers/smmstore: allow full flash access for capsule updates_
- **Michał Żygowski (miczyg):** +16/-16
  - _soc/intel/elkhartlake/pmc,gpio: Fix PMC GPE GPIO routes_
  - _mainboard/protectli/vault_ehl/Kconfig: Configure TPM PIRQ_
  - _mb/protectli/vault_ehl/devicetree.cb: Fix assertion in soc/pmutil_

<!--

As said last time our statistics improved thanks to rebasing some platforms to
24.12 coreboot release. Still not all platforms received releases, but we
already working on 25.03 rebase. So it would be harder and harder to track
things.

Some platforms stay on older base and we will not change that unless there will
be new release coming.

We see that Michał Kopeć is definitely the leader of upstreaming with his work
around laptops being top contribution. We also would like to thank Krystian and
Michał Żygowski for their effort to upstream code.

Open file in LibreOffice and sort after lines added, you can limit file by:

```shell
./contribution-stats list -r coreboot -s 03/20/2025 -e 06/10/2025 -o dug10.csv
```

-->
