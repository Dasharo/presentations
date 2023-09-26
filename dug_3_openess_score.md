class: center, middle, intro

# &#x1F386; Dasharo Openess Score Status &#x1F386;

.center[<img src="/remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">]

???

---

# Agenda

* Short Introduction to Dasharo Openness Score (DTS)
* Exploring Dasharo Openness Score v0.1
* Upcoming Features: Dasharo Openness Score v0.2 and Beyond
* Q&A

???

---

# Dasharo Openess Score

* Dasharo Openness Score is a tool designed to quantify the openness of 
firmware images, providing insights into the ratio of open-source to
closed-source components.
* Python, MIT licensed, https://github.com/Dasharo/Openness-Score
* DRY: https://www.youtube.com/live/ZyctrnJNTPc?si=O_SZPLJgqi2ro_q9&t=5854
* Since last DUG we made some slight progress and we would like to treat this
  presentation as opportunity to provide more details about project status as
  well some knowledge about methodology.
* Unfortunately no new releases, but ...

---

# Documentation Released
 
.center.image-90[![](/img/dos_docs.png)]

* Documentation is in Sphinx at this point, but we will migrate it to Dasharo
  Universe, which use mkdocs in long run.

---

# Methodology

???

@startuml
start

:Identify and Save Region Properties;
:Separate and Classify Regions;
:Extract and Identify Firmware Volumes;
:Calculate Metrics for Firmware Volumes;
:Classify Paddings;
:Summarize Region Sizes;
:Verify Total Size;
if (Mismatch?) then (yes)
  :Adjust Data and Report Error;
else (no)
endif

:Export Data;
stop
@enduml

---

# Integration for NovaCustom 

* Starting from:
  - NS5x/7x ADL v1.7.0
  - NS5x/7x TGL v1.5.0
  All Novacustom releases will contain Dasharo Openess Score.


---

# Release Newsletter integration

.center.image-70[![](/img/dos_newsletterv2.png)]

---

# Dasharo Openess Score v0.2

* ETA: Q3 2023
* Planned features
  * **Improved Visualization**: Enhancing visual representation for
    user-friendliness.
  * **CI/CD Integration**: Including Openness Score script in CI/CD
    processes.
  * **Increased Visibility**: Openness Score updates in newsletters and
    Dasharo User's Guide.
  * **Binary Comparison**: Comparing Dasharo binary with reference binaries.
  * **Documentation Upgrade**: Improving methodology explanation in
    documentation.
  * **Versioning & Wide Application**: Implementing versioning and supporting
    multiple platforms.
  * **Advanced Parsing**: Utilizing ifdtool for improved image parsing.

---
class: center, middle, intro

# Q&A
