#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2025 3mdeb <contact@3mdeb.com>
#
# SPDX-License-Identifier: Apache-2.0

import matplotlib.pyplot as plt
import subprocess
import logging
import shutil

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])


def run_gh_command(command):
    if not shutil.which("gh"):
        print("Error: 'gh' command is not available on this system.")
        exit("Please install GitHub CLI (gh) first")

    print(f"Executing command: {command}")
    try:
        print(f"Running command: {command}")
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


dates = [
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


def gather_data(repo, dates, differences=False):
    """
    Gathers PR data for a given repository and dates.
    """
    data = {"Merged": [], "Closed": [], "Open": []}
    for date in dates:
        merged_prs = count_prs(repo, "merged", date)
        closed_prs = count_closed_prs(repo, "closed", date) - merged_prs
        open_prs = count_prs(repo, "open", date)
        data["Merged"].append(merged_prs)
        data["Closed"].append(closed_prs)
        data["Open"].append(open_prs)

    if differences:
        # Calculate differences if required
        for key in data:
            data[key] = [
                data[key][i] - data[key][i - 1] for i in range(1, len(data[key]))
            ]
            data[key].insert(0, 0)
    return data


def plot_pr_statistics(repo, dates, data, title, filename, label_offsets):
    """
    Plots PR statistics for a given repository.

    Parameters:
        repo (str): Repository name.
        dates (list): List of dates.
        data (dict): Dictionary containing PR data.
        title (str): Title of the plot.
        filename (str): Filename to save the plot.
        label_offsets (tuple): Offsets for merged, closed, and open PR labels.
    """
    plt.figure(figsize=(10, 6))

    # Stacked bar chart
    bars_merged = plt.bar(dates, data["Merged"], color="#38d430", label="Merged PRs")
    bars_closed = plt.bar(
        dates,
        data["Closed"],
        bottom=data["Merged"],
        color="#272727",
        label="Closed PRs",
    )
    bars_open = plt.bar(
        dates,
        data["Open"],
        bottom=[m + c for m, c in zip(data["Merged"], data["Closed"])],
        color="#1E90FF",
        label="Open PRs",
    )

    # Add titles and labels
    plt.title(title, fontsize=18, fontweight="bold", color="#272727")
    plt.xlabel("Date", fontsize=16, fontweight="bold", color="#272727")
    plt.ylabel("Number of PRs", fontsize=16, fontweight="bold", color="#272727")

    # Add labels to the bars
    add_labels_merged(bars_merged)
    add_labels_closed(bars_closed, offset=label_offsets[0])
    add_labels_open(bars_open, offset=label_offsets[1])

    # Add legend
    plt.legend(fontsize=12)

    # Set the background color
    plt.gca().set_facecolor("#f5f5f5")

    # Save the plot as an image file
    plt.savefig(filename)

    # Optionally, close the plot to free up memory
    plt.close()


# Plot for Dasharo/coreboot
repo_coreboot = "Dasharo/coreboot"
data_coreboot = gather_data(repo_coreboot, dates)
plot_pr_statistics(
    repo_coreboot,
    dates,
    data_coreboot,
    "PR Statistics for Dasharo/coreboot downstream",
    "img/dug_10/dasharo_coreboot.png",
    label_offsets=(30, 5),
)

# Plot for Dasharo/edk2
repo_edk2 = "Dasharo/edk2"
data_edk2 = gather_data(repo_edk2, dates)
plot_pr_statistics(
    repo_edk2,
    dates,
    data_edk2,
    "PR Statistics for Dasharo/edk2 fork",
    "img/dug_10/dasharo_edk2.png",
    label_offsets=(7, 1),
)

# Plot for Dasharo/open-source-firmware-validation
repo_osfv = "Dasharo/open-source-firmware-validation"
data_osfv = gather_data(repo_osfv, dates, differences=False)
plot_pr_statistics(
    repo_osfv,
    dates,
    data_osfv,
    "PR Statistics for OSFV repository",
    "img/dug_10/dasharo_prs_osfv_total.png",
    label_offsets=(7, 1),
)
data_osfv = gather_data(repo_osfv, dates, differences=True)
plot_pr_statistics(
    repo_osfv,
    dates,
    data_osfv,
    "PR Statistics for OSFV repository - increments",
    "img/dug_10/dasharo_prs_osfv_diff.png",
    label_offsets=(7, 1),
)

# Plot for Dasharo/osfv-scripts
repo_osfv_cli = "Dasharo/osfv-scripts"
data_osfv_cli = gather_data(repo_osfv_cli, dates, differences=False)
plot_pr_statistics(
    repo_osfv_cli,
    dates,
    data_osfv_cli,
    "PR Statistics for osfv_cli repository",
    "img/dug_10/dasharo_prs_osfv_cli_total.png",
    label_offsets=(7, 1),
)
data_osfv_cli = gather_data(repo_osfv_cli, dates, differences=True)
plot_pr_statistics(
    repo_osfv_cli,
    dates,
    data_osfv_cli,
    "PR Statistics for osfv_cli repository - increments",
    "img/dug_10/dasharo_prs_osfv_cli_diff.png",
    label_offsets=(7, 1),
)

# Plot for Dasharo/meta-dts
repo_meta_dts = "Dasharo/meta-dts"
data_meta_dts = gather_data(repo_meta_dts, dates)
plot_pr_statistics(
    repo_meta_dts,
    dates,
    data_meta_dts,
    "PR Statistics for meta-dts repository",
    "img/dug_10/dasharo_prs_meta_dts.png",
    label_offsets=(7, 1),
)

# Plot for Dasharo/meta-dts
repo_dts_scripts = "Dasharo/dts-scripts"
data_dts_scripts = gather_data(repo_dts_scripts, dates)
plot_pr_statistics(
    repo_dts_scripts,
    dates,
    data_dts_scripts,
    "PR Statistics for dts-scripts repository",
    "img/dug_10/dasharo_prs_dts_scripts.png",
    label_offsets=(7, 1),
)
