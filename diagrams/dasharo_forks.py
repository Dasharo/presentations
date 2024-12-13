#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>
#
# SPDX-License-Identifier: Apache-2.0

import matplotlib.pyplot as plt
import subprocess
import logging

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])


def run_gh_command(command):
    try:
        result = subprocess.run(
            command, shell=True, check=True, text=True, capture_output=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return None


def count_prs(repo, state, date):
    # Construct the GitHub CLI command
    command = f"gh pr list --repo {repo} --state {state} --search 'created:<={date}' -L 10000 --json number --jq '. | length'"

    # Run the command and capture the output
    output = run_gh_command(command)

    # Parse the output to get the count
    if output is not None:
        return int(output)
    else:
        return 0


def count_closed_prs(repo, state, date):
    # Construct the GitHub CLI command
    command = f"gh pr list --repo {repo} --state {state} --search 'closed:<={date}' -L 10000 --json number --jq '. | length'"

    # Run the command and capture the output
    output = run_gh_command(command)

    # Parse the output to get the count
    if output is not None:
        return int(output)
    else:
        return 0


dates = [
    "2023-03-16",
    "2023-07-06",
    "2023-09-28",
    "2023-12-03",
    "2024-03-11",
    "2024-06-10",
    "2024-09-09",
    "2024-12-10",
]
repo = "Dasharo/coreboot"

# Data storage
data = {"Merged": [], "Closed": [], "Open": []}

# Gather data
for date in dates:
    total_prs = count_prs(repo, "all", date)
    merged_prs = count_prs(repo, "merged", date)
    closed_prs = count_closed_prs(repo, "closed", date) - merged_prs
    open_prs = count_prs(repo, "open", date)
    data["Merged"].append(merged_prs)
    data["Closed"].append(closed_prs)
    data["Open"].append(open_prs)

# Plotting
plt.figure(figsize=(10, 6))

# Stacked bar chart
bars_merged = plt.bar(dates, data["Merged"], color="#38d430", label="Merged PRs")
bars_closed = plt.bar(
    dates, data["Closed"], bottom=data["Merged"], color="#272727", label="Closed PRs"
)
bars_open = plt.bar(
    dates,
    data["Open"],
    bottom=[m + c for m, c in zip(data["Merged"], data["Closed"])],
    color="#1E90FF",
    label="Open PRs",
)

# Add titles and labels
plt.title(
    "PR Statistics for Dasharo/coreboot downstream",
    fontsize=18,
    fontweight="bold",
    color="#272727",
)
plt.xlabel("Date", fontsize=16, fontweight="bold", color="#272727")
plt.ylabel("Number of PRs", fontsize=16, fontweight="bold", color="#272727")


def add_labels_merged(bars):
    for bar in bars:
        height = bar.get_height()
        font_s = 14
        plt.annotate(
            f"{height}",
            xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="bottom",
            color="white",
            fontsize=font_s,
            fontweight="bold",
        )


def add_labels_closed(bars, offset=0):
    for bar in bars:
        height = bar.get_height()
        font_s = 14
        logging.info("height:{}, x:{}, y:{}".format(height, bar.get_x(), bar.get_y()))
        plt.annotate(
            f"{height}",
            xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2 - offset),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="bottom",
            color="white",
            fontsize=font_s,
            fontweight="bold",
        )


def add_labels_open(bars, offset=0):
    for bar in bars:
        height = bar.get_height()
        font_s = 14
        logging.info("height:{}, x:{}, y:{}".format(height, bar.get_x(), bar.get_y()))
        plt.annotate(
            f"{height}",
            xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2 - offset),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="bottom",
            color="black",
            fontsize=font_s,
            fontweight="bold",
        )


# Add labels to the bars
add_labels_merged(bars_merged)
add_labels_closed(bars_closed, offset=30)
add_labels_open(bars_open, offset=5)

# Add legend
plt.legend(fontsize=12)

# Set the background color
plt.gca().set_facecolor("#f5f5f5")

# Save the plot as an image file
plt.savefig("public/dug_8/dasharo_coreboot.png")

# Optionally, close the plot to free up memory
plt.close()

repo = "Dasharo/edk2"

# Data storage
data = {"Merged": [], "Closed": [], "Open": []}

# Gather data
for date in dates:
    merged_prs = count_prs(repo, "merged", date)
    closed_prs = count_closed_prs(repo, "closed", date) - merged_prs
    open_prs = count_prs(repo, "open", date)
    data["Merged"].append(merged_prs)
    data["Closed"].append(closed_prs)
    data["Open"].append(open_prs)

# Plotting
plt.figure(figsize=(10, 6))

# Stacked bar chart
bars_merged = plt.bar(dates, data["Merged"], color="#38d430", label="Merged PRs")
bars_closed = plt.bar(
    dates, data["Closed"], bottom=data["Merged"], color="#272727", label="Closed PRs"
)
bars_open = plt.bar(
    dates,
    data["Open"],
    bottom=[m + c for m, c in zip(data["Merged"], data["Closed"])],
    color="#1E90FF",
    label="Open PRs",
)

# Add titles and labels
plt.title(
    "PR Statistics for Dasharo/edk2 fork",
    fontsize=18,
    fontweight="bold",
    color="#272727",
)
plt.xlabel("Date", fontsize=16, fontweight="bold", color="#272727")
plt.ylabel("Number of PRs", fontsize=16, fontweight="bold", color="#272727")

# Add labels to the bars
add_labels_merged(bars_merged)
add_labels_closed(bars_closed, offset=7)
add_labels_open(bars_open, offset=1)

# Add legend
plt.legend(fontsize=12)

# Set the background color
plt.gca().set_facecolor("#f5f5f5")

# Save the plot as an image file
plt.savefig("public/dug_8/dasharo_edk2.png")

# Optionally, close the plot to free up memory
plt.close()
