#!/bin/bash

./contribution-stats sync -d dasharo
./contribution-stats list -d dasharo -r coreboot -s 01/01/2000 -e $(date +"%m/%d/%Y") -o /tmp/coreboot_stat.csv

echo "coreboot lines added:"
awk -F';' '{sum += $6} END {print sum}' /tmp/coreboot_stat.csv
echo "coreboot lines removed:"
awk -F';' '{sum += $7} END {print sum}' /tmp/coreboot_stat.csv
