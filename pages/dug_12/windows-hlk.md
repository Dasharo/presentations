---
theme: slidev-template/theme
layout: cover
background: /intro.png
class: text-center

---

## Windows Hardware Lab Kit
### A new tool at Dasharo testsers arsenal

---

## What's Windows Hardware Lab Kit

<!-- HLK used to use windows sticker as a sign of support-->
<!-- historic names for HLK tool -->
<!-- sticker image -->

---

## Why it's interesting to us

<!-- test coverage, compare to OSFV -->
<!-- maybe list TPM tests and similar -->

---

## HLK Overview #1

<!-- list and shortly describe main components
- studio, controller, client
-->

---

## HLK Overview #2

<!-- lab diagram HLK vs OSFV -->

---

## HLK VM Setup #1

<!-- proxmox VM, allocated resources -->

## HLK VM Setup #2

<!-- other requirements that had to be met -->
<!-- virtio, any settings from setup in blog -->

## Running Tests

<!-- live demo??? -->
<!-- if not, then one slide per point:
 - device group
 - project
 - test selection
 - run tests
 - show results (premade), compare to OSFV
 - show logs (premade), compare to OSFV
 -->

## PoC on Novacustom NV41PZ v1.7.2

<!--
- runtime and estimated runtime for all tests
- pass rate pie chart, run/skipped pie chart
-
- list some interesing ones?
 -->

## Summary & next steps

<!--
- hardware
  - faster server needed even for single DUT. HLK is resource intensive
- automation:
  - wrapping tests in OSFV would be wasteful
  - automation only via .NET programs / powershell
  - clicking in GUI fine for small scale
- presenting results:
  - converting to human readable format
  - promising project should scaling be needed https://github.com/HCK-CI
-->


## Q&A