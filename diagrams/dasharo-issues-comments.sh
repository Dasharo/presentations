#!/bin/bash

echo "number of unique users active in Dasharo community: "

PAGER="less -R" gh issue list --repo "Dasharo/dasharo-issues" -s all -L 10000 --json author,comments --jq '.[].author.login'|sort|uniq|wc -l

echo "count all comments: "

PAGER="less -R" gh issue list --repo "Dasharo/dasharo-issues" -s all -L 10000 --json comments --jq '.[].[].[].createdAt'|wc -l

echo "count how many comments each user posted: "

PAGER="less -R" gh issue list --repo "Dasharo/dasharo-issues" -s all -L 10000 --json comments --jq '.[].[].[].author.login'|sort|uniq -c|sort -h
