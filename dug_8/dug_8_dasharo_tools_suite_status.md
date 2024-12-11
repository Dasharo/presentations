class: center, middle, intro

# &#x1F44B; Dasharo User Group #8 &#x1F389;

## DTS - tiny Dasharo OS for hacking, Q3 and Q4 status, future improvements

<img src="/remark-templates/dasharo-presentation-template/images/dasharo-sygnet-white.svg" width="150px" style="margin-left:-20px">

???

- Time for this slid: 10s
- Idea/goal of this slide: Just start it
- What to say: "Hello there! I am going to present you Dasharo Tools Suite
status and future improvements."
- Notes:

---

# Who am I?

.left-column50[.center[
<img
src="/remark-templates/3mdeb-presentation-template/images/daniil_klimuk.webp"
height="250px" style="marking-top:-50px">

Daniil Klimuk

_Junior Embedded Systems Developer_]
- <a href="mailto:daniil.klimuk@3mdeb.com">
  <img
    src="/remark-templates/3mdeb-presentation-template/images/email.png"
    width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
    daniil.klimuk@3mdeb.com
  </a>
- <a href="https://www.linkedin.com/in/daniil-klimuk-9358a1271/">
    <img
      src="/remark-templates/3mdeb-presentation-template/images/linkedin.png"
      width="24px" style="margin-bottom:-5px; margin-left:-15px"/>
      linkedin.com/in/daniil-klimuk-9358a1271/
    </a>
]

.right-column50[.center[<img src="/img/zarhus_logo.png" height="280px">]]

.right-columt50[.center[3mdeb Zarhus team member]]

.right-column50[
- <a href="https://3mdeb.com">https://3mdeb.com</a>
- <a href="https://cloud.3mdeb.com/index.php/apps/calendar/appointment/n7T65toSaD9t">
    Book a call
    </a>
- <a href="https://newsletter.3mdeb.com/subscription/PW6XnCeK6">
      Sign up for the newsletter
    </a>
]

???

- Time for this slide: 25s
- Idea/goal of this slide: Present yourself
- What to say: "My name is Daniil. I am junior embedded system developer
interested in system level programming and security. Currently I am a member of
3mdeb Zarhus team, and responsible, among other, for Dasharo Tools Suite."
- Notes:

---

# Agenda

.left-column50[
* What is DTS?
* DTS statistics Q3-Q4 2024.
  + Issues
  + Contributions.
  + Features.
  + Hardware support.
* DTS current architecture and tests.
* DTS new architecture and tests.
* Roadmap Q1-Q2 2025
* Q&A
]

???

- Time for this slide: 35s
- Idea/goal of this slide: Introduce agenda
- What to say: "Here is the agenda for this meeting. After a brief intro into
DTS we will take a look on DTS latest contribution and features statistics. Then
we will discuss the transition between old and new DTS architecture. After the
architecture a new testsuites will be presented and described. Then we will
finish with questions and answers, where you will be able to ask questions and
share your ideas."
- Notes:

---

# What is DTS?

.center[<img src="/img/solid-and-secure-bridge.png" height="280px">]

.center[<font size="16">Solid and Secure bridge</font>]

???

- Time for this slide: 50s
- Idea/goal of this slide: Present DTS
- What to say: "What is DTS? DTS states for Dasharo Tools Souite and is a tiny
Linux Kernel built for 64-bit x86with goal to make Dasharo user experience
easier. Actually, it could be thought of as a solid and secure bridge between a
user and Dasharo. It has several Dasharo and Coreboot tools built in, as well
as other, firmware related tools for enhanced debugging and programming. But
most importantly, it has a layer of automation and GUI scripts that make DTS
more user-friendly."
- Notes:

---

# DTS statistics

.center[<img src="/img/dts-issues-q3-q4-2024.png" height="380px">]

.center[Two big releases: 2.0.0 and 2.1.0!]

???

- Time for this slide: 45s
- Idea/goal of this slide: Present DTS issues statistics
- What to say: "There have been a lot of changes in DTS since first half of 2024
year. We had several minor releases with hot fixes and, most importantly we had
two big releases 2.0.0 and 2.1.0. Unfortunately, our plan to win in issues fight
met a counterattack, and now we are fighting back. Here I would like to thank
all of users who add issues and participate in discussions, it is really
important for developers. Great thanks to all of you!"
- Notes:

---

# DTS changes

.left-column50[
Updates:
* Linux Kernel to 6.6.21
* Updates for meta layers

New features:
* pre-commit now used everywhere
* Some new tools
* Verbose debugging mode
* New GUI
* DTS extensions feature
* UEFI Capsule Update support
* DTS is now in netboot.xyz official support
]

.right-column50[
Platforms updates:
* Added support for Novacustom MTL
* Added support for Dell Optiplex 7010/9010
* Added support fore ODROID-H4
* New versions for MSI Z690 and Z790

Important changes:
* DTS script moved to a separate repository
* Enhanced debugging and testing
* Qemu is now supported
]

???

- Time for this slide: 2.5m
- Idea/goal of this slide: Present DTS new features and updates
- What to say:
  + "Here is a list of most important changes and updates since Q2. First of
all, all meta layers have been updated to new Yocto long term support release,
therefore all tools have been updated too. A huge list of new features have been added.

  + "Now pre-commit is being used in all DTS-related repositories, so the DTS
  code now is more readable and contribution-friendly."

  + "Some new tools were added into DTS image, including tools for Dasharo
  TrustRoot provisioning for Intel Bay Trail."

  + "Verbose debugging mode has been added for leveraging testing and developing
  processes"

  + "New GUI and DTS extensions were released."

  + "A new way to deploy Dasharo has been added - that is UEFI Capsule Update
  now is supported by some platforms."

  + "Good news for those who love iPXE, DTS is now officially supported in
  netboot.xyz."

  + "A list of supported HW platforms has been extended too. In last two updates
   two families have joined Dasharo: Novacustom Meteorlake laptops and Dell
  Optiplex PCs. MSIs and some other platforms got updates too."

  + "And about more important changes. dts-scripts has moved to another repo,
  and now is being linked to DTS image from a recipe. dts-scripts was modified
  to support new tests, more about this later. And, from update 2.1.0 Qemu
  support has been added for DTS, now we are working to get best of this
  support!"

- Notes:

---

# New GUI

.left-column50[.center[<img src="/img/dts-gui-2.png" height="340px">]]

.right-column45[.center[
<br>
<br>
<br>
<span style="font-size: 40px;">
    More colors!
    More information!
</span>
]]

???

- Time for this slide: 35s
- Idea/goal of this slide: Present new DTS GUI
- What to say: "Here how DTS GUI looks like from update 2.0.0. Now it has more
colors and, most importantly, it has more HW inf. printed out, so user
feedback in form of photos is now easier to analyze for us. Now we are fixing
and polishing all other mesassages and logs that are being printed during
deploy. This clearing could drastically improve user experience."
- Notes:

---

# DTS extensions

.left-column50[.center[<img src="/img/dts-extensions-example-1.png" height="340px">]]
.right-column50[.center[<img src="/img/dts-extensions-example-2.png" height="140px">]]
.right-column50[.center[
<br>
<br>
Adding custom DTS extensions is now possible!
]]

???

- Time for this slide: 50s
- Idea/goal of this slide: Present DTS extensions
- What to say: "A bit about this completely new feature that has been added in
update 2.0.0 and enables per client custom extensions. It is somewhat similar to
private packages. If you
want smth. related to firmware to be installed in DTS but not available
publicly, - you could install it via DTS extensions. Just ask us and we will add
package on our side and give you credentials, that give access to both firmware
and your DTS extension. And then, all you need to do is to provide the
credentials and the package will be downloaded and installed automatically."
- Notes:

---

# DTS architecture

.center[<img src="/img/old-dts-architecture.png" height="380px">]

???

- Time for this slide: 1m (35s~)
- Idea/goal of this slide: Present DTS old architecture
- What to say: "Now about problems that appeared lately. Currently DTS has a
monolitic architecture, we have almost
everything in two files. This was OK until DTS started to grow. Then we faced
several problems related to scalability, stability and testing, that now
result in issues. We, as well, did not have full test coverage for this
architecture, only some unit tests and a few end-to-end regression tests were
implemented."
- Notes:

---

# DTS new architecture

.center[<img src="/img/dts-refactoring.svg" height="400px">]
.center[More inf.: https://github.com/Dasharo/dasharo-issues/issues/1067]

???

- Time for this slide: 2m (50s~)
- Idea/goal of this slide: Present DTS new architecture
- What to say: "But now we are thinking about redesigning DTS so it will have a
clear and consice structure. As you can see it will be divided into modules with
a defined interfaces between each other, enhancing developing and debugging
processes. All configuration, that is now stored in bare Bash code will be
stored directly in Linux FS in files in human-readable format. Hardware-depended
code will be separated into a module, named HAL that states for Hardware
Abstraction Layer where it will reside alongise with mocking functions, named
HAL for tests on the diagram, that will make running DTS on Qemu possible. We
have decided to change DTS language as well, new architecture will be
implemented mostly in GO language."
- Notes:

---

# DTS new tests

.center[<img src="/img/dts-new-tests.svg" height="400px">]
.center[More inf.: https://github.com/Dasharo/dasharo-issues/issues/1067]

???

- Time for this slide: 2m (1m~)
- Idea/goal of this slide: Present  DTS new tests
- What to say: "At the same time, we want to develop a test suite that will
cover entire DTS. As you can see, we are planning two types of tests: end-to-end
tests and unit tests, and we would like to do as many testing as possible using
OSFV on Qemu. Therefore end-to-end tests will be intirely hardware-independed
and automated. As you can see these tests cover most of DTS
structure. The goal of this tests is to keep large and crucial parts of DTS
stable and secure. On the other hand, unit tests, will cover all
hardware-depended code, that could not be tested on Qemu. These tests will be
mostly automated utilizing OSFV functionalities and devices in our lab. But some
of them may require manual steps, which is ok for some systems."
- Notes:

---

# DTS new tests

.left-column50[
<b>End-to-end tests</b>:
* Will be launched by OSFV
* Will be launched on Qemu
* Will test DTS logic as well as user experience
* Some of them will be used in CIs
* First version of it is already in integration (check `open-source-firmware-validation/dts`)

<b>What we will get</b>:
* More stable and secure DTS
* Strictly defined and tracked user experience features
* Less time wasted on SW tests
]

.right-column30[.center[<img src="/img/end-to-end-tests.svg" height="440px" style="margin-right:-120px">]]

???

- Time for this slide: 1.5m (40s~)
- Idea/goal of this slide: DTS new features and updates
- What to say: "Here you can se an example of end-to-end test workflow. It will
start from booting DTS and choosing an option from a list of options that a user
can see when he boots DTS. After choosing an option, test will read output and
check whether DTS went through all point of a choosen options.  These point
could be called anchors. These anchors are simple prints for user, that inform
where DTS is now and what it is doing. In case of a fail a simple error will be
printed, informing test about some issue. This will trigger the test to fail. If
there will be no fails, DTS will go down to rebooting message, which will signal
to the test, that everything passed with success. This tests, as was said, will
cover most of the DTS logic. It may seem that there is a lot to implement. But
it is not true, because these tests will utilize all exeisting functionalities
from Dasharo OSFV. Nad even if it will take some time to integrate, the long
term outcome is worth it. Because with these tests we will be able to easily
verify entire DTS during merging of every PR. Ability to run on Qemu will allow
us to run these tests implicitely in every PR. As was said, these tests will use
GUI interface, which is used by users. We will take this apportunity to make our
GUI more strict and user-friendly. First version of these test is already being
integrated, and a PR workflow is being tested."
- Notes:

---

# DTS new tests

.left-column50[
<b>Unit tests</b>:
* Will be launched by OSFV
* Will be launched on real HW
* Will test HW-specific logic
* Will be used in every HW-related release

<b>What we will get</b>:
* Separate HW tests from SF tests
* More stable and secure DTS
* Less time wasted on HW releases
]

.right-column30[.center[<img src="/img/unit-tests.svg" height="360px">]]

???

- Time for this slide: 1.5m (40s~)
- Idea/goal of this slide: DTS new features and updates
- What to say: WIP 
- Notes:

---

# Roadmap

.center[<img src="/img/dts-roadmap.svg" height="310px">]

.center[Some simultaneous development]

???

- Time for this slide:
- Idea/goal of this slide: Present roadmap
- What to say: WIP
- Notes:

---

<br>
<br>

## .center[Q&A]

???

- Time for this slide:
- Idea/goal of this slide: Q&A
- What to say:
- Notes:
