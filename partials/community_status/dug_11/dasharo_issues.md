## <center>Dasharo Issues</center>

<center><img src="/@fs/repo/img/dug_10/issues.png" width="500"></center>
<center><img src="/@fs/repo/img/dug_10/dasharo_issues.png" width="650"></center>

<!--

* Number of reported bugs was 20 smaller than last quarter. So we definitely
see some slowdown. Hopefully this is silent before storm and during vacation
period when we should have little bit more time to tinker we will get back on
track.
* We fixed 16 bugs less than in last quarter. Slowdown in adding bugs is bigger
than in fixing, at least in absolute terms. Percentage-wise things does not
look so shiny.

Modify and run:
./diagrams/dasharo_issues.py

-->

---

## <center>Dasharo Issues</center>

<br>

### <center>Comments</center>

<center><img src="/@fs/repo/img/dug_10/issue_comments.png" width="500"></center>

### <center>Top Contributors</center>

<center><img src="/@fs/repo/img/dug_10/issue_comments_users.png" width="550"></center>

<!--

Not much growth here. It is definitely one of the calmest quarters in Dasharo
history. We have to change that.

Following should be run in dasharo-issues repo, gh command should be installed:

- number of unique users active in Dasharo community

```shell
PAGER="less -R" gh issue list --repo "Dasharo/dasharo-issues" -s all -L 10000 --json author,comments --jq '.[].author.login'|sort|uniq|wc -l
```

- count all comments

```shell
PAGER="less -R" gh issue list --repo "Dasharo/dasharo-issues" -s all -L 10000 --json comments --jq '.[].[].[].createdAt'|wc -l
```

- count how many comments each user posted

```shell
PAGER="less -R" gh issue list --repo "Dasharo/dasharo-issues" -s all -L 10000 --json comments --jq '.[].[].[].author.login'|sort|uniq -c|sort -h
```

-->
