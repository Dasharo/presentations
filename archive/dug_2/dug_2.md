class: center, middle, intro

# &#x1F44B; Dasharo User Group #2 &#x1F389;

## Greetings

.center[<img src="/remark"-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">]

---

# Why we are here?

.center.image-85[![](/img/dug_2_vpub_7.png)]

???

* explain format of the meeting
* meeting is recorded and will be published on Youtube

---

# Agenda

### .center[&#x1F680; Dasharo User Group #2 Meeting Agenda &#x1F680;]

* #### &#x1F44B; 17:00 UTC Greetings, Agenda
* #### &#x1F9ED; 17:10 UTC Nitrokey introduction
* #### &#x1F4BB; 17:20 UTC Dasharo Announcements
* #### &#x1F9F0; 17:50 UTC Dasharo Roadmap
* #### &#x1F9F0; 18:10 UTC Dasharo Tool Suite Roadmap
* #### &#x1F9F0; 18:20 UTC TBD
* #### &#x1F9F0; 18:40 UTC TBD
* #### &#x1F44F; 18:55 UTC Closing remarks &#x27A1;&#xFE0F; &#x1F37A;&#x1F37B; vPub 0x7

???

---

# Community Hearbeat &#x1F493;

.image-100[![](/img/community_heartbeat_dug_2.png)]

???

TBD: look at community status of other projects, news?
  - consider news presentation with Dasharo status about that
	- OpenSIL

* 455 issues reported, 166 closed
  - gh issue list -s all -L 5000
  - gh issue list -s closed -L 5000
* PRs: Dasharo/coreboot 318 PRs merged, Dasharo/edk2 46
  - gh pr list --state all
* We received over 1600 comments from 51 users (including 3mdeb employees)
  - PAGER="less -R" gh issue list -s all -L 5000 --json author,comments --jq '.[].author.login'|sort|uniq|wc -l - users
  - comments - this doesn't look like relibable method
    - contrib_list=$(PAGER="less -R" gh issue list -s all -L 5000 --json author,comments --jq '.[].author.login'|sort|uniq|xargs)
    - ./community-analysis.sh "$contrib_list" > issues_contrib.csv
* 22k+ messages so far (~52msg/day)
  - 104 users in Dasharo Matrix Space (108 in Dasharo General)
  - Most active channels: General,
	- grep -E '^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}, [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2} [AP]M - .*:' log.txt|wc
* matrix comments per user:
	- grep -E "\-.+: " matrix\ -\ Dasharo\ -\ General\ -\ Chat\ Export\ -\ 2023-07-02T22-37-07.435Z.txt |cut -d"-" -f2|cut -d":" -f1|grep -E "^ "|sort|uniq -c|grep -v "banned"|sort -h|grep -v import|grep -v "'"|grep -v "removed"|grep -v coreboot

---

# Dasharo Space on Matrix

* 20 channels
* Most acitve:
  - `Dasharo - General`
  - `#qubes`
  - `Dasharo - Support`
  - `Dashro Developers vPub`
  - `TrenchBoot`
* Dedicated channels
  - `Dasharo - Laptops`
  - we have bridge to IRC (libera.chat) - `#dasharo`
  - there are partner and side projects channels like:
      - `Fiedka the Firmware Editor`,
      - `TwPM`,
      - `Fobnail`,
      - `fwupd for BSD`
      - `core-ec`

???

TBD: which information are really important?

Go to Dasharo Space and copy&paste content from there:

* Dasharo - Support
  - 75 members
  - created: 12/5/2021
  - activity since last measurement:
* Dasharo - Random
  - 68 members
* Dasharo - General
  - 162 members
* Dasharo Developers vPub
  - 124 members
* Dasharo - Announcements
  - 78 members
* core-ec
  - 25 members
* Fiedka the Firmware Editor
  - 55 members
* Dasharo - Fobnail
  - 32 members
* Dasharo - OSF Bootstrappable Toolchain
  - 20 members
* Trenchboot
  - 45 members
* fwupd for BSD
  - 15 members
* qubes-summit
  - 42 members
* Dasharo Tools Suite
  - 37 members
* #qubes
  - 135 members
* Dasharo Premier Support
  - 17 members
* OST2
  - 18 members
* TwPM
  - 18 members
* #dasharo
  - 8 members
* Dasharo - Supermicro X11 LGA1151 Series
  - 19 members
* Dasharo - Laptops
  - 16 members

---
class: center, middle, intro

# Q&A
