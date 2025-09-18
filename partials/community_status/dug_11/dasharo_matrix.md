## <center>Dasharo Matrix Community</center>

### <center>Messages and Users</center>

<center><img src="/@fs/repo/img/dug_11/dasharo_general_matrix.png" width="500"></center>

### <center>Top contributors</center>

<center><img src="/@fs/repo/img/dug_11/dasharo_general_matrix_users.png" width="500"></center>

<!--

* We doubled activity in comparison to Q2'25
* No change in Top Contributors, zir_blazer keep distancing everyone.
* We are very sorry that Dasharo becoming ground for political and religious
flamewars. There are some members who coming for gaslighting instead of
contributing to open-source firmware ecosystem.
  - in generate we are free speech enthusiast
  - but Dasharo Community is to some extent reputation based environment, if
someone coming to the channel and first post is political it cannot be received
well by moderators even on Random channel
  - if this will not change we will introduce timely mute and in case of
repeating situation we will have to permanently ban accounts which do not
respect calm and peacful life of our community

Getting number of messages for every user:

```shell
grep -E "\-.+:\s" matrix\ -\ Dasharo\ -\ General\ -\ Chat\ Export\ -\ 2024-03-12T11-16-54.063Z.txt |cut -d"-" -f2|cut -d":" -f1|grep -E "^ "|sort|uniq -c|grep -v "banned"|sort -h|grep -v import|grep -v "'"|grep -v "removed"|grep -v coreboot
```

To count messages add after pipe:

```shell
awk '{sum += $1} END {print sum}'
```

-->

---

# Top Contributors Benefits

* Unlimited access to the Dasharo Pro Package
* Up to 15% discount on hardware sold by 3mdeb (excluding dropshipping)
* How to claim?
  - Write an email to: contact@dasharo.com

<!--

Just want to recall that.

Dasharo Matrix Community and Dasharo Issues Contributors benefits.

-->

---

<center><img src="/@fs/repo/img/dug_11/dasharo_users.png" width="800"></center>

<!--

There is some saturation, but we believe it will change after announcing couple
new platform releases.

-->
---

### <center>Most active Dasharo Community Matrix channels since last DUG</center>

<br>

#### <center>Random (`#dasharo-random:matrix.org`)</center>
<br>

#### <center>Support (`#dasharo-support:matrix.org`)</center>

<br>

#### <center>Laptops (`#dasharo-laptops:matrix.org`)</center>

<!--

* Random: 12888 (+1782) - sometimes gaining bad reputation, so join on your own risk.
* General: 38303 (+1796)
* Support: 6102 (+659)
* OST2: 607 348 (+259)
* TrenchBoot: 2446 (+165)
* vPub: 4575 (+155)
* Laptops: 1532 (+124)
* OSF Bootstrapable Toolchain: 284 (+13)
* Supermicro: 1667 (+8)
* OSFV: 1860 (+1)

-->
