## <center>Dasharo/coreboot PRs</center>

<center><img src="/slides/img/dug_12/coreboot_prs.png" width="600"></center>
<center><img src="/slides/img/dug_12/dasharo_coreboot.png" width="650"></center>

<!--

* This quarter (Q4 2025) we merged 34 PRs, maintaining steady development pace.
* Open PR backlog grew by 5 PRs this quarter - we need more reviewers!
* We created approximately 39 new PRs this quarter, continuing strong
contribution flow.
* If you want to help with review and validation, feel free to join bug bounty
program.

Recent quarterly merging performance:
- Q1 2025 (2025-03): 50 PRs merged
- Q2 2025 (2025-06): 60 PRs merged
- Q3 2025 (2025-09): 27 PRs merged
- Q4 2025 (2025-12): 34 PRs merged (current quarter)

Modify and run:
./diagrams/dasharo_forks.py

-->

---

## <center>Dasharo/coreboot upstreaming</center>

<center><img src="/slides/img/dug_12/coreboot_upstreaming.png" width="600"></center>
<center><img src="/slides/img/dug_12/dasharo_coreboot_upstraming.png" width="650"></center>

<!--

RECORD BREAKING QUARTER! We upstreamed 7,443 lines of code in Q4 2025!

* This is 51% more than our previous record of 4,923 lines (Q3 2025).
* New historical average: ~3,201 SLOC/quarter (up 16% from 2,770).
* Despite massive downstream backlog, we're accelerating upstreaming efforts.
* At this pace, we're making real progress on closing the gap.
* A lot of those changes were upstream first from our activity in AMD server
market towards Gigabyte MZ33-AR1.

We're seeing more community members picking code from Dasharo branches and
upstreaming independently. Very grateful for this collaboration!

Recent upstreaming performance:
- Q1 2025: 2,751 lines
- Q2 2025: 3,241 lines
- Q3 2025: 4,923 lines (previous record)
- Q4 2025: 7,443 lines (NEW RECORD!)

Historical average calculation:
- Total: 2240+4203+173+2927+3819+3447+50+2751+3241+4923+7443 = 35,217 lines
- Average: 35,217 / 11 quarters = 3,201 SLOC/quarter

Top is total:

```shell
~/src/3mdeb/dasharo/presentations/diagrams/coreboot-upstreaming.sh
```

-->

---

### <center>Top Upstreamers</center>

- **Michał Żygowski (miczyg):** +6650/-96
  - _[soc/amd/turin_poc: Add Turin SoC structure as a copy of genoa_poc](https://review.coreboot.org/c/coreboot/+/88707)_
  - _[util/amdtool: Add utility to dump useful information on AMD CPUs](https://review.coreboot.org/c/coreboot/+/89492)_
  - _[util/amdtool: Add support for Phoenix AM5 CPUs](https://review.coreboot.org/c/coreboot/+/90009)_
- **Sergii Dmytruk:** +491/-5
  - _[drivers/ipmi: add Block Transfer (BT) interface](https://review.coreboot.org/c/coreboot/+/67057)_
  - _[payloads/Kconfig: default to Skiboot payload on PPC64](https://review.coreboot.org/c/coreboot/+/67070)_
  - _[sb/intel/common/firmware/Makefile.mk: fix INTEL_IFD_SET_TOP_SWAP_BOOTBLOCK_SIZE](https://review.coreboot.org/c/coreboot/+/90432)_
- **Filip Lewiński:** +168/-28
  - _[Makefile.mk: separate bootblocks into BOOTBLOCK and TOPSWAP](https://review.coreboot.org/c/coreboot/+/89570)_
  - _[ifittool: allow adding files from a separate region](https://review.coreboot.org/c/coreboot/+/89608)_
  - _[soc/intel/common/block/rtc/rtc.c: Top Swap: add Slot B selection mechanism](https://review.coreboot.org/c/coreboot/+/90147)_

<!--

Delta with upstream no longer make sense unless you are on the same base.

Massive contributions this quarter led by Michał Żygowski with over 6,650 lines!

* Michał Żygowski (miczyg) absolutely dominated Q4 2025 with 6,650 lines:
  - Added initial Turin SoC structure (3,218 lines) - opening new AMD server platform
  - Created comprehensive AMD CPU diagnostic utility amdtool (2,952 lines)
  - Extended amdtool with Phoenix AM5 CPU support (311 lines)
  - Major focus on AMD server platforms and tooling infrastructure

* Sergii Dmytruk contributed 491 lines focused on enterprise features:
  - Implemented IPMI Block Transfer interface for server management
  - Fixed Intel Top Swap bootblock size configuration
  - Added PPC64 Skiboot payload support

* Filip Lewiński added 168 lines for Intel Top Swap feature:
  - Separated bootblock handling for Top Swap/A-B boot
  - Enhanced ifittool for multi-region support
  - Added Slot B selection mechanism for RTC-based boot control

We are grateful for all contributions, big and small!

Generate report with:

```shell
./contribution-stats list -r coreboot -s 09/18/2025 -e 12/11/2025 -o /tmp/dug12.csv
```

-->
