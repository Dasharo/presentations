#!/usr/bin/env bash

# SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>
#
# SPDX-License-Identifier: Apache-2.0

grep -En '"remark|"images|\(images|\(img|"img' "$1"

GREP_EC=$?

if [ $GREP_EC -eq 0 ]; then
  echo "Found problematic lines in: $1"
  echo "See above for line numbers"
  exit 1
else
  echo "No problematic lines found in: $1"
  exit 0
fi
