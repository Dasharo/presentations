class: center, middle, intro

# &#x1F44B; Dasharo User Group #1 &#x1F389;

## Greetings

.center[<img src="/remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">]

---

# Why we are here?

.center.image-85[![](/img/dug_1_vpub_6.png)]

???

* explain format of the meeting
* meeting is recorded and will be published on Youtube

---

# Agenda

### .center[&#x1F680; Dasharo User Group #1 Meeting Agenda &#x1F680;]

* #### &#x1F44B; 17:00 UTC Greetings, Agenda
* #### &#x1F9ED; 17:10 UTC Dasharo Roadmap
* #### &#x1F4BB; 17:30 UTC Revolutionize Your Laptop Experience with NovaCustom's Hardware and Open-Source Firmware
* #### &#x1F9F0; 17:50 UTC Dasharo Tool Suite Roadmap
* #### &#x1FA84; 18:10 UTC Dasharo Features (X11, RPL-S CPU support, T1650)
* #### &#x1F4CB; 18:30 UTC PC Engines survey summary
* #### &#x1F44F; 18:55 UTC Closing remarks &#x27A1;&#xFE0F; &#x1F37A;&#x1F37B; vPub 0x6

???

* each block will take ~15min and we will have 5min to answer some questions
  and switch to next presenter
* we will take one or two selected questions because of limited time
* Wessel klein Snakenborg

---

# Today

.center.image-80[![](/img/dasharo_vision_before.png)]

???

1. Thoughtful computer user heard about problem in firmware (aka BIOS) and have
   concerns about various aspects of the firmware on use computing device.
   Like:
   - when will my favouring computer supplier/vendor will stop deliver firmare
     updates?
   - wouldn't my total cost of ownership largely increase when vendor decide to
     sell me new hardawre and abandon my device?
   - what would be the time needed to respond to recent threats in firmware?
   - is my computing system trustworthy?
   - can I attest what my computer system running?
   - does my computing device is privacy respecting?
   - finally user realize that that one possible solution could be open-source
     firmware
2. User calls favourite compting device supplier and ask for open-source
   firmware support in their devices
   - with some expceptions most suppliers with say, they have no idea
3. (Optional) Hipothethically, user gathers community to convinve supplier it
   makes sense
4. Supplier convinced that open-source firmware brings value for users calls
   Silicon Vendor before planning new design
5. Silicon Vendor support send Supplier to fixed list of Independent BIOS
   Vendors
   - shady, secret oligopoly
6. Supplier contact IBV, but gets answer BIOS cannot be open-source and
   transparent because it is against IBV business model built for tens of years
7. Dasharo apeared on the market and slowlych changed things in way that
   Silicon Vendor no longer recommend fixed set of Independent BIOS Vendors,
   but in transparent way prose to customers various abvailable options. Thanks
   to that users have ability to buy trystworthy computing device directly from
   the favourite supplier.

---

# Vision of tomorrow

.center.image-99[![](/img/dasharo_vision_after.png)]

---

# Community Hearbeat &#x1F493;

.image-100[![](/img/community_heartbeat_dug_1.png)]

???

* Dasharo Github repository was created on 27th Nov 2020
* Dasharo Matrix space was created on 5th Dec 2020
* 360 issues reported, 125 closed
  - gh issue list -s all -L 5000
  - gh issue list -s open -L 5000
  - gh issue list -s closed -L 5000
* We received over 1600 comments from 51 users
  - PAGER="less -R" gh issue list -s all -L 5000 --json author,comments --jq '.[].author.login'|sort|uniq|wc -l
* PRs: Dasharo/coreboot 318 PRs merged, Dasharo/edk2 46
  - gh pr list --state all
* Top contributors on github
* 20k+ messages so far (~50msg/day)
  - 104 users in Dasharo Matrix Space (108 in Dasharo General)
  - Most active channels: General,

---

# Dasharo Space on Matrix

* 20 channels
* Most acitve:
  - `Dasharo - General`
  - `#qubes`
  - `Dasharo - Support`
  - `Dashro Developers vPub`
  - `TrenchBoot`
* Interesting facts:
  - we have bridge to IRC (libera.chat) - `#dasharo`
  - there are partner and side projects channels like:
      - `Fiedka the Firmware Editor`,
      - `TwPM`,
      - `Fobnail`,
      - `fwupd for BSD`
      - `core-ec`

---
class: center, middle, intro

# Q&A
