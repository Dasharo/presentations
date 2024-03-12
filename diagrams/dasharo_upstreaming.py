#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>
#
# SPDX-License-Identifier: Apache-2.0
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])

added = {}
removed = {}

logging.info('Adding data to dictionaries')
added["2023-07-06"] = 2230
removed["2023-07-06"] = 288
added["2023-09-28"] = 4203
removed["2023-09-28"] = 244
added["2023-12-03"] = 193
removed["2023-12-03"] = 189
added["2024-03-11"] = 2928
removed["2024-03-11"] = 73

logging.info('Creating lists from dictionaries')
dates = list(added.keys())
added_values = list(added.values())
removed_values = list(removed.values())

logging.info('Creating figure')
plt.figure(figsize=(10, 6))

logging.info('Creating bars')
bars_added = plt.bar(dates, added_values, color='#38d430', label='Added lines')
bars_removed = plt.bar(dates, removed_values, bottom=added_values, color='#272727', label='Removed lines')

logging.info('Setting title and labels')
plt.title('Contribution Statistics', fontsize=18, fontweight='bold', color='#272727')
plt.xlabel('Date', fontsize=16, fontweight='bold', color='#272727')
plt.ylabel('Number of Lines', fontsize=16, fontweight='bold', color='#272727')

# Function to add labels inside the bars
def add_labels(bars, color='white', offset=0):
    for bar in bars:
        height = bar.get_height()
        plt.annotate(f'{height}',
                     xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2 + offset),
                     xytext=(0, 3),  # 3 points vertical offset
                     textcoords="offset points",
                     ha='center', va='bottom', color=color, fontsize=14, fontweight='bold')

add_labels(bars_added)
add_labels(bars_removed, color='black', offset=60)

logging.info('Adding legend')
plt.legend(fontsize=12)

logging.info('Setting facecolor')
plt.gca().set_facecolor('#f5f5f5')

logging.info('Saving figure')
plt.savefig('img/dug_5_dasharo_coreboot_upstraming.png', dpi=300)

logging.info('Closing figure')
plt.close()
