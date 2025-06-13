#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>
#
# SPDX-License-Identifier: Apache-2.0
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])

added = {}
removed = {}

logging.info("Adding data to dictionaries")
added["2023-07"] = 2240
removed["2023-07"] = 298
added["2023-09"] = 4203
removed["2023-09"] = 244
added["2023-12"] = 173
removed["2023-12"] = 169
added["2024-03"] = 2927
removed["2024-03"] = 72
added["2024-06"] = 3819
removed["2024-06"] = 1360
added["2024-09"] = 3447
removed["2024-09"] = 272
added["2024-12"] = 50
removed["2024-12"] = 10
added["2025-03"] = 2751
removed["2025-03"] = 460
added["2025-06"] = 3241
removed["2025-06"] = 23

logging.info("Creating lists from dictionaries")
dates = list(added.keys())
added_values = list(added.values())
removed_values = list(removed.values())

logging.info("Creating figure")
plt.figure(figsize=(10, 6))

logging.info("Creating bars")
bars_added = plt.bar(dates, added_values, color="#38d430", label="Added lines")
bars_removed = plt.bar(
    dates, removed_values, bottom=added_values, color="#272727", label="Removed lines"
)

logging.info("Setting title and labels")
plt.title("Contribution Statistics", fontsize=18, fontweight="bold", color="#272727")
plt.xlabel("Date", fontsize=16, fontweight="bold", color="#272727")
plt.ylabel("Number of Lines", fontsize=16, fontweight="bold", color="#272727")


def add_labels_added(bars):
    for bar in bars:
        height = bar.get_height()
        font_s = 14
        plt.annotate(
            f"{height}",
            xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2 - 90),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="bottom",
            color="white",
            fontsize=font_s,
            fontweight="bold",
        )


def add_labels_removed(bars):
    for bar in bars:
        height = bar.get_height()
        font_s = 14
        logging.info("height:{}, x:{}, y:{}".format(height, bar.get_x(), bar.get_y()))
        plt.annotate(
            f"{height}",
            xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height - 60),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="bottom",
            color="black",
            fontsize=font_s,
            fontweight="bold",
        )


add_labels_added(bars_added)
add_labels_removed(bars_removed)

logging.info("Adding legend")
plt.legend(fontsize=12)

logging.info("Setting facecolor")
plt.gca().set_facecolor("#f5f5f5")

logging.info("Saving figure")
plt.savefig("img/dug_10/dasharo_coreboot_upstraming.png", dpi=300)

logging.info("Closing figure")
plt.close()
