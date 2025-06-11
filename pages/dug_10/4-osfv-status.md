---
theme: /slidev-template/theme
layout: cover
background: /intro.png
class: text-center

---
## Dasharo Open Source Firmware Validation Status

<center><img src="/img/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px"></center>

---

# <center> Agenda </center>

* Short introduction to OSFV
* Stats
* Improvements
* Work in progress & future plans
* Q&A

---
layout: cover
background: /intro.png
class: text-center
---

# <center> Introduction to Open Source Firmware Validation </center>

---

# <center> Introduction to Open Source Firmware Validation </center>

- Open Source Validation of Open Source Firmware
- Based on Robot Framework
- Allows us to perform hundreds of automated tests
  to ensure the quality of Dasharo

For more details check the previous OSFV Status presentations at
DUG #08 and DUG #06 at [vpub.dasharo.com](https:/vpub.dasharo.com).

<img src="/img/dug_10/osfv-status/dug8.png"/>
<img src="/img/dug_10/osfv-status/dug6.png"/>

<!--

-->
---
layout: cover
background: /intro.png
class: text-center
---

# OSFV Stats

---

# <center> Releases? </center>

We have decided on switching to a rolling release for now

<center><img src="/img/dug_10/osfv-status/main-branch.png" width=250/></center>

---

# <center> PR stats </center>
### <center> open-source-firmware-validation </center>
#### <center> Total </center>

<center>
<img src="/img/dug_10/osfv-status/dasharo_prs_osfv_total.png" width=600/>
</center>

---

# <center> PR stats </center>
### <center> open-source-firmware-validation </center>
#### <center> Difference </center>

<center>
<img src="/img/dug_10/osfv-status/dasharo_prs_osfv_diff.png" width=600/>
</center>

---

# <center> PR stats </center>
### <center> osfv-scripts </center>
#### <center> Total </center>

<center>
<img src="/img/dug_10/osfv-status/dasharo_prs_osfv_cli_total.png" width=600/>
</center>

---

# <center> PR stats </center>
### <center> osfv-scripts </center>
#### <center> Difference </center>

<center>
<img src="/img/dug_10/osfv-status/dasharo_prs_osfv_cli_diff.png" width=600/>
</center>

---

# <center> Test modules stats </center>
#### <center> Total </center>

<center>
<img src="/img/dug_10/osfv-status/test_counts.png" width=600/>
</center>

---

# <center> Test modules stats </center>
#### <center> Difference </center>

<center>
<img src="/img/dug_10/osfv-status/test_counts_difference.png" width=600/>
</center>

Total count increased by **415**

---

# <center> New test cases </center>

* Added FBT suite testing the fast boot feature
* Added ACPI suite testing ACPI drivers
* Added USC suite testing the Always On USB feature
* Added multiple benchmark test suites:
  + UPP, CPP, ETHPERF, DIO
  + testing the CPU, Ethernet and disks performance
* Automated the CBO - Custom Boot Order test suite
* Automated most of the AUD tests
* Extended NVM suite with an NVMe on x2 PCIe test
* Extended TPM suite with tests for the TPM Physical Presence Interface and changing the Endorsement Primary Seed
* Extended UTC Docking station tests with variants for every docking station, ME enabled/disabled

<!--
Graph showing differences since the last status presentation.
List which suites were updated and short description, like
"new suite" or "4 new cases"
-->

---

# <center> New platforms </center>

* Protectli VP2440
<!--
Graphs probably won't be necessary.
List new supported platforms if any
-->

---
layout: cover
background: /intro.png
class: text-center
---

# Key changes

---

# <center> Fedora support </center>

Most test cases are also possible run on Fedora.
The test ID naming convention has changed
[Tests naming convention](https://github.com/Dasharo/open-source-firmware-validation/blob/develop/docs/tests-naming-convention.md)

`<suite_id><case_id>.<environment_id>`
* `suite_id` - It's typically 3 to 4 letters, uppercase, identifies the test suite. Should be related to what the test suite accomplishes.
* `case_id` - It's a three digit number with leading zeros. Identifies test cases in a test suite. Typically test cases are numbered incrementally starting from 001
* `environment_id` - A three digit number, unambiguously identifies the environment in which the test case is performed. The IDs of environments are separated into groups based on the leading digit:
  * `1xx` - Firmware,  Example: 101 - EDK2 UEFI
  * `2xx` - Linux,  Example: 201 - Ubuntu
  * `3xx` - Windows

---

# <center> Fedora support </center>

<center><img src="/img/dug_10/osfv-status/fedora_percent.png" width=700></center>

<!--
many test cases can also be performed on Fedora
every test case *Will* be possible to be performed on Fedora

graphs? stats? % per module?

-->

---

# <center> DeGoogle </center>

Dasharo Test & Feature Matrix at Google Docs deprecated

<img src="/img/dug_10/osfv-status/dtfm.png"/>
<!--
Dasharo Test & Feature matrix going deprecated and is no longer used.
Test results published at osfv-results
-->

---

# <center> OSFV results </center>

The test results are now being published on the [OSFV Results repo](https://github.com/Dasharo/osfv-results/)

<center><img src="/img/dug_10/osfv-status/osfv-results-readme.png" width=700/></center>
<!--
- show how to find results on osfv-results
- how to find a device, a test case, a feature
- preferably live, not on slides, but maybe lets prepare some for a backup
    if something goes wrong
-->

---

# <center> OSFV results </center>

<center><img src="/img/dug_10/osfv-status/osfv-results-vp66xx.png" width=700/></center>

---

# <center> OSFV results </center>

<center><img src="/img/dug_10/osfv-status/osfv-results-result.png" width=700/></center>

---

# <center> OSFV results </center>

<center><img src="/img/dug_10/osfv-status/osfv-results-results2.png" width=700/></center>

---

# <center> OSFV Dashboard </center>

Working on our own tool for documenting and publishing test results
<center><img src="/img/dug_10/osfv-status/dashboard-viewer.png" width=700/></center>
<!--
A new tool is WiP
Will allow for better documentation and repeatability of the testing process
- show some screenshots as a teaser?
- maybe live presentation on localhost of the viewer?
-->

---

# <center> OSFV Dashboard </center>

Will include details of manual tests, causes of fails and links to issues and
logs from the tests.

A large step towards the best documentation and repeatibility of the testing process

<center><img src="/img/dug_10/osfv-status/dashboard-comment.png" width=700/></center>

---

# <center> Manual test documentation deprecated </center>

[docs.dasharo/unified-test-documentation](https://docs.dasharo.com/unified-test-documentation/overview/)

Manual tests will be slowly transferred to OSFV to reduce redundancy and improve coherence

<center><img src="/img/dug_10/osfv-status/manual-test-1.png" width=500/></center>
<center><img src="/img/dug_10/osfv-status/manual-test-2.png" width=500/></center>

---

# <center> Adding HW tests to OSFV CI </center>

</br>
Performing CI tests on real hardware will greatly improve the reliability of OSFV

- The work is in progress
- Two representatives prepared as a start
    <center><table>
    <tr>
    <td>MSI Z690 DDR4 i5 14600k</td><td>PC Engines APU3C AMD GX-412TC</td>
    </tr>
    <tr>
    <td><img src="/img/dug_10/osfv-status/z690.jpeg" width=300/></td>
    <td><img src="/img/dug_10/osfv-status/apu3c.png" width=300/></td>
    </tr>
    </table></center>

# <center> Adding HW test to CI </center>
## <center> Test scope determining </center>

<!--
diagram for choosing the test scope
depending on the changes
-->
---

# <center> Priorities for the future </center>

<!--
seabios still on the roadmap

Todo?
-->

---

# <center> Questions </center>
<!--
Current state
Changes:
- Enforcing the test naming convention
  - the bulk amount of tests we perform
  - how to look for the results, how to find the features you are
    interested in
- A summary of improvements and additions regarding the test cases and supported platforms
- Deprecation of Dasharo Test Specification at docs.dasharo.com
- FTDI converters for laptops

Future plans:
- Development of a new tool for managing Dasharo releases and the testing process
  - still in progress, but can do a little highlight

-->
