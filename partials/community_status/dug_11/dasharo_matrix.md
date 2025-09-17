## <center>Dasharo Matrix Community</center>

### <center>Messages and Users</center>

<center><img src="/@fs/repo/img/dug_10/dasharo_general_matrix.png" width="500"></center>

### <center>Top contributors</center>

<center><img src="/@fs/repo/img/dug_10/dasharo_general_matrix_users.png" width="500"></center>

<!--

* Not much activity recently, it is definitely part of our lack of time from
  our side to deliver new shiny stuff.
* tlaurion advanced to top4, so huge thanks to him for engaging in Dasharo Community

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
Dasharo Matrix Community and Dasharo Issues Contributors benefits.
-->

---

<center><img src="/@fs/repo/img/dug_10/dasharo_users.png" width="800"></center>

---

### <center>Most active Dasharo Community Matrix channels since last DUG</center>

<br>

#### <center>Random (`#dasharo-random:matrix.org`)</center>
<br>

#### <center>Support (`#dasharo-support:matrix.org`)</center>

<br>

#### <center>Laptops (`#dasharo-laptops:matrix.org`)</center>

<!--

* Random: 11006 (+1502)
* General: 36607 (+1411)
* Support: 6027 (+659)
* Laptops: 1408 (+217)
* OSFV: 1860 (+119)
* vPub: 4420 (+112)
* TrenchBoot: 2281 (+61)
* OST2: 348 (+12)
* Supermicro: 1667 (+8)
* OSF Bootstrapable Toolchain: 271

-->
