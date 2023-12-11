class: center, middle, intro

# PC Engines post-EoL firmware

## Survey summary and next steps

.center[<img src="/remark"-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">]

---

# What is it about?

.center.image-30[![](/img/coreboot.png) ![](/img/pcengines.png)]

* In September 2022 PC Engines decided to discontinue sponsorship for
  open-source firmware on their devices.
* We announced that recently after v4.19.0.1 release (Feb 2023).
* We sent survey to community to ask, if there is interest in continuation of
  open-source firmware support through potential subscription model.
* In following presentation we want to share summary and next steps regarding
  PC Engines open-source firmware support future.

---

# Summary

* We would like to thank all of the respondents for taking the time and
  providing valuable feedback.
* Some questions in survey could be explained better, maybe with example.
* We received 100+ answers.
* Respondents report over 600 PC Engines hardware units for update.
* Most valuable features:
  - ECC,
  - OpenBSD, FreeBSD, OPNsense and pfSense support,
  - Core Preformance Boost,
  - TPM support,
  - Stability and security,
  - Debian and NetBSD support.


???

- `How many PC Engines apuX platforms would you like to support with regular firmware updates?`
- was interpreted as question about which PC Engines platforms apu1,apu2 and so
  on, should get updates
- what we intended to ask was how for how many hardware devices/units, given
  respondent would like to get updates

---

# Summary

.center.image-100[![](/img/pce_num_of_updates.svg)]

???

* 3 updates - 5.5%
* 6 updates - 7.8%
* 7 updates - 0.8%
* 8 updates - 0.8%
* 12 updates - 3.1%

---

# Summary

.center.image-100[![](/img/pce_hw_usage.svg)]

---

# Summary

.center.image-65[![](/img/pce_sub.svg)]

* Over 50% of respondents are interested in paid model.
  - Many respondents requested yearly subscription instead of monthly.
  - Subscription-interested respondents represent 66% of all devices reported
    in survey.

---

# Community suggestions

* Use donation-driven development instead of subscription.
* On-demand custom firmware builds.
  - We will add that to 3mdeb offer.
* Charging for each release.
  - We don't think it is economically feasible,
    - Payment would be **maybe** after release (investment from our side),
    - Not enough market demand right now to take this risk.
* One-off upgrades.
  - Similar as above.
* Paid Technical Assistant Center (TAC) support.
  - We already deliver such services through Dasharo Support Package using JIRA
    Service Desk and we would be glad to extend it to support PC Engines
    customers.
* Provide roadmap you are planning to implement.
  - We will do that quarterly during DUGs.

???

We are doing release and if release contains interesting things people can buy,
and if not they will skip. From our perspective it is way more work since we
have to evaluate market.
We did that little bit in survey, but still we have to trust that respondents
would really buy features they claim they will buy. We are not prepared for
taking risk of building firmware and hoping there will be enough customers to
buy it. Of course I would prefer such situation, but we are far from that.
With such high risk it is better to no do any release unless we have huge,
clear market demand, but with that we would probably take payment upfront
as with donation or subscription yearly payment.

---

# Decision

* Because of feedback we received we opt for donation-only model for now.
  - Subscription model with expressed interest is not economically feasible.
* What may change our decision in future?
  - More business customers interested in supporting open-source firmware
    updates.
  - Critical mass of users who want to see subscription model.

---

# Feature requests

.center.image-99[![](/img/pce_features.svg)]

---

# Roadmap

.center.image-99[![](/img/dcs_pce_roadmap_v0.1.png)]

---

# How to donate

* LiberaPay: https://liberapay.com/dasharo
  - There is only one goal and it is donation for PC Engines firmware release.
* OpenCollective: https://opencollective.com/3mdeb_com
  - Thre are two goals here, one dedicated to PC engines.
  - We plan to enable cryptocurrencies donations before DUG#2.
* Other methods including cryptocurrencies:
  - https://docs.dasharo.com/ways-you-can-help-us/#donate-money
  - If you make crypto donation please send us transaction link, since crypto
    wallets are owned by NLNet.
  - For other form of donations please leave a note, which describes the
    purpose, while making donation.

---
class: center, middle, intro

# Q&A
