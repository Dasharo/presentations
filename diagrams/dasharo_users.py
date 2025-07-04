#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>
#
# SPDX-License-Identifier: Apache-2.0

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Data
quarters = [
    "2023-03",
    "2023-07",
    "2023-09",
    "2023-12",
    "2024-03",
    "2024-06",
    "2024-09",
    "2024-12",
    "2025-03",
    "2025-06",
]
# Dasharo Matrix Space counter
users = [104, 162, 201, 234, 257, 311, 358, 401, 430, 458]

# Create the plot
plt.figure(figsize=(12, 7))
plt.plot(
    quarters,
    users,
    marker="o",
    linestyle="-",
    color="#38d430",
    linewidth=2,
    markersize=10,
)

# Add titles and labels
plt.title(
    "Dasharo Matrix Space User Base", fontsize=18, fontweight="bold", color="#272727"
)
plt.xlabel("Date", fontsize=16, fontweight="bold", color="#272727")
plt.ylabel("Number of Users", fontsize=16, fontweight="bold", color="#272727")

# Customize the tick marks
plt.xticks(fontsize=14, color="#272727")
plt.yticks(fontsize=14, color="#272727")
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter("%d"))

# Add a grid with a lighter color and dashed line
plt.grid(color="#a9a9a9", linestyle="--", linewidth=0.5)

# Highlight each data point with annotations
for i, txt in enumerate(users):
    plt.annotate(
        txt,
        (quarters[i], users[i]),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        fontsize=14,
        fontweight="bold",
        color="#38d430",
    )

# Set the background color
plt.gca().set_facecolor("#f5f5f5")

# Save the plot as an image file
plt.savefig("img/dug_10/dasharo_users.png")

# Optionally, close the plot to free up memory
plt.close()
