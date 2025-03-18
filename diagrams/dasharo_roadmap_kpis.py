#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>
#
# SPDX-License-Identifier: Apache-2.0
import matplotlib.pyplot as plt

dcr = {}
dspr = {}

# Dasharo Community Releases
dcr["Q3'21"] = 0
dcr["Q4'21"] = 4
dcr["Q1'22"] = 1
dcr["Q2'22"] = 6
dcr["Q3'22"] = 2
dcr["Q4'22"] = 1
dcr["Q1'23"] = 1
dcr["Q2'23"] = 0
dcr["Q3'23"] = 3
dcr["Q4'23"] = 1
dcr["Q1'24"] = 4
dcr["Q2'24"] = 4
dcr["Q3'24"] = 0
dcr["Q4'24"] = 3
dcr["Q1'25"] = 2
# Dasharo Supporter Package Releases (DSPR)
dspr["Q3'21"] = 3
dspr["Q4'21"] = 3
dspr["Q1'22"] = 6
dspr["Q2'22"] = 6
dspr["Q3'22"] = 3
dspr["Q4'22"] = 6
dspr["Q1'23"] = 3
dspr["Q2'23"] = 4
dspr["Q3'23"] = 0
dspr["Q4'23"] = 4
dspr["Q1'24"] = 6
dspr["Q2'24"] = 2
dspr["Q3'24"] = 4
dspr["Q4'24"] = 4
dspr["Q1'25"] = 3

dates = list(dcr.keys())
dcr_values = list(dcr.values())
dspr_values = list(dspr.values())

plt.figure(figsize=(10, 6))

bars_dspr = plt.bar(
    dates, dspr_values, color="#272727", label="Dasharo Support Package Releases"
)
bars_dcr = plt.bar(
    dates,
    dcr_values,
    bottom=dspr_values,
    color="#38d430",
    label="Dasharo Community Releases",
)

plt.title(
    "Number of Dasharo Public Releases in time",
    fontsize=18,
    fontweight="bold",
    color="#272727",
)
plt.xlabel("Date", fontsize=16, fontweight="bold", color="#272727")
plt.ylabel("Number of Releases", fontsize=16, fontweight="bold", color="#272727")


# Function to add labels inside the bars
def add_labels(bars, color="white", offset=0):
    for bar in bars:
        height = bar.get_height()
        if height != 0:
            plt.annotate(
                f"{height}",
                xy=(bar.get_x() + bar.get_width() / 2, bar.get_y()),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha="center",
                va="bottom",
                color=color,
                fontsize=14,
                fontweight="bold",
            )


add_labels(bars_dcr)
add_labels(bars_dspr)

# Add sum on top of stacked bars
for i in range(len(dates)):
    if dcr_values[i] != 0 and dspr_values[i] != 0:
        total = dcr_values[i] + dspr_values[i]
        plt.annotate(
            f"{total}",
            xy=(
                bars_dcr[i].get_x() + bars_dcr[i].get_width() / 2,
                bars_dcr[i].get_y() + bars_dcr[i].get_height(),
            ),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="bottom",
            color="black",
            fontsize=14,
            fontweight="bold",
        )

plt.legend(fontsize=12)

plt.gca().set_facecolor("#f5f5f5")

plt.savefig("public/dug_9/dasharo_releases_kpis.png", dpi=300)

plt.close()
