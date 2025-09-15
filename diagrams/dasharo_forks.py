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


def add_labels(bars_merged, bars_closed, bars_open, min_height_internal=8):
    """
    Smart labeling that avoids overlaps between adjacent segments.
    Processes all bars together to coordinate positioning.
    """
    # Store label information for collision detection
    label_positions = []

    # Process each date column (assuming all bar lists have same length)
    for i in range(len(bars_merged)):
        bars_in_stack = [
            (bars_merged[i], "merged", "white", "#1a5a0f"),
            (bars_closed[i], "closed", "white", "#000000"),
            (bars_open[i], "open", "white", "#0066cc"),
        ]

        # Calculate positions for this stack
        stack_labels = []

        for bar, bar_type, internal_color, external_color in bars_in_stack:
            height = bar.get_height()
            if height <= 0:  # Skip zero height bars completely
                continue

            x_center = bar.get_x() + bar.get_width() / 2

            # Determine initial positioning
            if height >= min_height_internal:
                # Internal label
                y_pos = bar.get_y() + height / 2
                is_external = False
                color = internal_color
                font_size = 13
            else:
                y_pos = bar.get_y() + height + 2
                is_external = True
                color = external_color
                font_size = 11

            stack_labels.append(
                {
                    "bar": bar,
                    "height": height,
                    "x": x_center,
                    "y": y_pos,
                    "is_external": is_external,
                    "color": color,
                    "font_size": font_size,
                    "bar_type": bar_type,
                    "text": str(int(height)),
                }
            )

        # Resolve collisions in this stack
        stack_labels = resolve_stack_collisions(stack_labels)

        # Add the resolved labels to the plot
        for label_info in stack_labels:
            plt.annotate(
                label_info["text"],
                xy=(label_info["x"], label_info["y"]),
                ha="center",
                va="center" if not label_info["is_external"] else "bottom",
                color=label_info["color"],
                fontsize=label_info["font_size"],
                fontweight="bold",
            )


def resolve_stack_collisions(stack_labels):
    """
    Resolve label collisions within a single stack by considering both internal and external labels.
    """
    if len(stack_labels) <= 1:
        return stack_labels

    # Sort labels by their original y position (bottom to top)
    stack_labels.sort(key=lambda x: x["y"])

    # Minimum spacing between any two labels
    min_spacing = 6

    # Check for collisions between ALL adjacent labels (internal and external)
    for i in range(1, len(stack_labels)):
        prev_label = stack_labels[i - 1]
        curr_label = stack_labels[i]

        # Calculate the visual bounds of each label
        prev_top = prev_label["y"] + (
            6 if prev_label["is_external"] else 7
        )  # Approximate label height
        curr_bottom = curr_label["y"] - (
            3 if curr_label["is_external"] else 7
        )  # Approximate label height

        # Check for overlap
        if prev_top > curr_bottom:
            # There's an overlap! We need to resolve it

            # Strategy: if current label is internal and would overlap with external above,
            # move current label to external position
            if not curr_label["is_external"] and prev_label["is_external"]:
                # Move current label outside
                curr_label["y"] = curr_label["bar"].get_y() + curr_label["height"] + 4
                curr_label["is_external"] = True
                # Update color for external positioning
                if curr_label["bar_type"] == "merged":
                    curr_label["color"] = "#1a5a0f"
                elif curr_label["bar_type"] == "closed":
                    curr_label["color"] = "#000000"
                else:  # open
                    curr_label["color"] = "#0066cc"

            # Ensure minimum spacing between external labels
            if curr_label["is_external"] and prev_label["is_external"]:
                if curr_label["y"] - prev_label["y"] < min_spacing:
                    curr_label["y"] = prev_label["y"] + min_spacing

            # If previous is internal and current is external, adjust current position
            elif not prev_label["is_external"] and curr_label["is_external"]:
                # Calculate minimum safe position for external label
                safe_y = prev_label["y"] + 6 + 3
                bar_top = curr_label["bar"].get_y() + curr_label["height"]
                base_external_y = bar_top + 4

                # Use the higher of the two positions
                curr_label["y"] = max(safe_y, base_external_y)

    return stack_labels


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


def plot_pr_statistics(repo, dates, data, title, filename, cap_to_zero=False):
    """
    Plots PR statistics for a given repository.

    Parameters:
        repo (str): Repository name.
        dates (list): List of dates.
        data (dict): Dictionary containing PR data.
        title (str): Title of the plot.
        filename (str): Filename to save the plot.
    """
    plt.figure(figsize=(10, 6))

    # Negative bar values are broken and the differences can be negative
    if cap_to_zero:
        data = {
            "Merged": [max(d, 0) for d in data["Merged"]],
            "Closed": [max(d, 0) for d in data["Closed"]],
            "Open": [max(d, 0) for d in data["Open"]],
        }

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
    add_labels(bars_merged, bars_closed, bars_open)

    # Add legend
    plt.legend(fontsize=12)

    # Set the background color
    plt.gca().set_facecolor("#f5f5f5")

    # Save the plot as an image file
    plt.savefig(filename)

    # Optionally, close the plot to free up memory
    plt.close()


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
    "2025-08",
]

# Plot for Dasharo/coreboot
repo_coreboot = "Dasharo/coreboot"
data_coreboot = gather_data(repo_coreboot, dates)
plot_pr_statistics(
    repo_coreboot,
    dates,
    data_coreboot,
    "PR Statistics for Dasharo/coreboot downstream",
    "img/dug_10/dasharo_coreboot.png",
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
)
data_osfv = gather_data(repo_osfv, dates, differences=True)
plot_pr_statistics(
    repo_osfv,
    dates,
    data_osfv,
    "PR Statistics for OSFV repository - increments",
    "img/dug_10/dasharo_prs_osfv_diff.png",
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
    cap_to_zero=True,
)
data_osfv_cli = gather_data(repo_osfv_cli, dates, differences=True)
plot_pr_statistics(
    repo_osfv_cli,
    dates,
    data_osfv_cli,
    "PR Statistics for osfv_cli repository - increments",
    "img/dug_10/dasharo_prs_osfv_cli_diff.png",
    cap_to_zero=True,
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
)
