#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>
#
# SPDX-License-Identifier: Apache-2.0
import matplotlib.pyplot as plt
import numpy as np

# Last checked 13/03/2024

new = {}
changed = {}
ontrack = {}
released = {}
removed = {}

new["2023-03"] = 9
changed["2023-03"] = 0
ontrack["2023-03"] = 0
released["2023-03"] = 0
removed["2023-03"] = 0
new["2023-07"] = 3
changed["2023-07"] = 6
ontrack["2023-07"] = 3
released["2023-07"] = 0
removed["2023-07"] = 0
new["2023-09"] = 5
changed["2023-09"] = 4
ontrack["2023-09"] = 5
released["2023-09"] = 3
removed["2023-09"] = 0
new["2023-12"] = 1
changed["2023-12"] = 11
ontrack["2023-12"] = 1
released["2023-12"] = 1
removed["2023-12"] = 0
new["2024-03"] = 9
changed["2024-03"] = 7
ontrack["2024-03"] = 2
released["2024-03"] = 3
removed["2024-03"] = 2
new["2024-06"] = 2
changed["2024-06"] = 7
ontrack["2024-06"] = 5
released["2024-06"] = 3
removed["2024-06"] = 1
new["2024-09"] = 1
changed["2024-09"] = 7
ontrack["2024-09"] = 4
removed["2024-09"] = 2
released["2024-09"] = 3
new["2024-12"] = 3
changed["2024-12"] = 8
ontrack["2024-12"] = 0
removed["2024-12"] = 2
released["2024-12"] = 2
new["2025-03"] = 3
changed["2025-03"] = 7
ontrack["2025-03"] = 0
removed["2025-03"] = 1
released["2025-03"] = 3

dates = list(new.keys())
new_values = np.array(list(new.values()))
changed_values = np.array(list(changed.values()))
ontrack_values = np.array(list(ontrack.values()))
released_values = np.array(list(released.values()))
removed_values = np.array(list(removed.values()))

total_releases = (
    sum(new_values)
    + sum(changed_values)
    + sum(ontrack_values)
    + sum(released_values)
    + sum(removed_values)
)

plt.figure(figsize=(10, 6))

bars_new = plt.bar(
    dates,
    new_values,
    color="#4CAF50",
    label=f"New ({sum(new_values)/total_releases*100:.1f}%)",
)
bars_changed = plt.bar(
    dates,
    changed_values,
    bottom=new_values,
    color="#FFC107",
    label=f"Changed ({sum(changed_values)/total_releases*100:.1f}%)",
)
bars_ontrack = plt.bar(
    dates,
    ontrack_values,
    bottom=new_values + changed_values,
    color="#2196F3",
    label=f"On Track ({sum(ontrack_values)/total_releases*100:.1f}%)",
)
bars_released = plt.bar(
    dates,
    released_values,
    bottom=new_values + changed_values + ontrack_values,
    color="#9E9E9E",
    label=f"Released ({sum(released_values)/total_releases*100:.1f}%)",
)
bars_removed = plt.bar(
    dates,
    removed_values,
    bottom=new_values + changed_values + ontrack_values + released_values,
    color="#F44336",
    label=f"Removed ({sum(removed_values)/total_releases*100:.1f}%)",
)

plt.title(
    "Dasharo Roadmap Status Overview ", fontsize=18, fontweight="bold", color="#272727"
)
plt.xlabel("Date", fontsize=16, fontweight="bold", color="#272727")
plt.ylabel("Number of Releases", fontsize=16, fontweight="bold", color="#272727")


# Function to add labels inside the bars
def add_labels(bars, color="white", offset=0):
    for bar in bars:
        height = bar.get_height()
        if height != 0:
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_y() + height / 2,
                f"{height}",
                ha="center",
                va="center",
                color=color,
                fontsize=14,
                fontweight="bold",
            )


add_labels(bars_new)
add_labels(bars_changed)
add_labels(bars_ontrack)
add_labels(bars_released)
add_labels(bars_removed)


# Function to add sum on top of stacked bars
def add_sum_labels(bars1, bars2, bars3, bars4, bars5, color="black"):
    for bar1, bar2, bar3, bar4, bar5 in zip(bars1, bars2, bars3, bars4, bars5):
        total_height = (
            bar1.get_height()
            + bar2.get_height()
            + bar3.get_height()
            + bar4.get_height()
            + bar5.get_height()
        )
        plt.text(
            bar1.get_x() + bar1.get_width() / 2,
            total_height,
            f"{total_height}",
            ha="center",
            va="bottom",
            color=color,
            fontsize=14,
            fontweight="bold",
        )


add_sum_labels(bars_new, bars_changed, bars_ontrack, bars_released, bars_removed)

plt.legend(fontsize=12)

plt.gca().set_facecolor("#f5f5f5")

plt.savefig("public/dug_9/dasharo_roadmap_states.png", dpi=300)

plt.close()
