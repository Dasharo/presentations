#!/usr/bin/env python3

import yaml
import pytz
import os
from github import Github
import datetime
import matplotlib.pyplot as plt
import requests
from datetime import datetime
import subprocess

def get_github_token():
    # Path to the GitHub hosts.yml file
    config_path = os.path.expanduser('~/.config/gh/hosts.yml')

    # Read the YAML file
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    # Extract the OAuth token
    return config['github.com']['oauth_token']

def run_gh_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
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

repo = "Dasharo/coreboot"
dates = ["2023-03-16", "2023-07-06", "2023-09-28", "2023-12-03"]

# Data storage
data = {"Total": [], "Merged": [], "Closed": [], "Open": []}

# Gather data
for date in dates:
    total_prs = count_prs(repo, 'all', date)
    merged_prs = count_prs(repo, 'merged', date)
    closed_prs = count_prs(repo, 'closed', date) - merged_prs
    open_prs = count_prs(repo, 'open', date)
    data["Total"].append(total_prs)
    data["Merged"].append(merged_prs)
    data["Closed"].append(closed_prs)
    data["Open"].append(open_prs)

# Plotting
plt.figure(figsize=(10, 6))

# Stacked bar chart
bars_merged = plt.bar(dates, data["Merged"], color='#38d430', label='Merged PRs')
bars_closed = plt.bar(dates, data["Closed"], bottom=data["Merged"], color='#272727', label='Closed PRs')
bars_open = plt.bar(dates, data["Open"], bottom=[m+c for m, c in zip(data["Merged"], data["Closed"])], color='#1E90FF', label='Open PRs')

# Add titles and labels
plt.title('PR Statistics for Dasharo/coreboot fork', fontsize=18, fontweight='bold', color='#272727')
plt.xlabel('Date', fontsize=16, fontweight='bold', color='#272727')
plt.ylabel('Number of PRs', fontsize=16, fontweight='bold', color='#272727')

# Function to add labels inside the bars
def add_labels(bars, color='white'):
    for bar in bars:
        height = bar.get_height()
        plt.annotate(f'{height}',
                     xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                     xytext=(0, 3),  # 3 points vertical offset
                     textcoords="offset points",
                     ha='center', va='bottom', color=color, fontsize=14, fontweight='bold')

# Add labels to the bars
add_labels(bars_merged)
add_labels(bars_closed)
add_labels(bars_open, color='black')

# Add legend
plt.legend(fontsize=12)

# Set the background color
plt.gca().set_facecolor('#f5f5f5')

# Save the plot as an image file
plt.savefig('dasharo_coreboot.png')

# Optionally, close the plot to free up memory
plt.close()

repo = "Dasharo/edk2"
dates = ["2023-03-16", "2023-07-06", "2023-09-28", "2023-12-03"]

# Data storage
data = {"Total": [], "Merged": [], "Closed": [], "Open": []}

# Gather data
for date in dates:
    total_prs = count_prs(repo, 'all', date)
    merged_prs = count_prs(repo, 'merged', date)
    closed_prs = count_prs(repo, 'closed', date) - merged_prs
    open_prs = count_prs(repo, 'open', date)
    data["Total"].append(total_prs)
    data["Merged"].append(merged_prs)
    data["Closed"].append(closed_prs)
    data["Open"].append(open_prs)

# Plotting
plt.figure(figsize=(10, 6))

# Stacked bar chart
bars_merged = plt.bar(dates, data["Merged"], color='#38d430', label='Merged PRs')
bars_closed = plt.bar(dates, data["Closed"], bottom=data["Merged"], color='#272727', label='Closed PRs')
bars_open = plt.bar(dates, data["Open"], bottom=[m+c for m, c in zip(data["Merged"], data["Closed"])], color='#1E90FF', label='Open PRs')

# Add titles and labels
plt.title('PR Statistics for Dasharo/coreboot fork', fontsize=18, fontweight='bold', color='#272727')
plt.xlabel('Date', fontsize=16, fontweight='bold', color='#272727')
plt.ylabel('Number of PRs', fontsize=16, fontweight='bold', color='#272727')

# Add labels to the bars
add_labels(bars_merged)
add_labels(bars_closed)
add_labels(bars_open, color='black')

# Add legend
plt.legend(fontsize=12)

# Set the background color
plt.gca().set_facecolor('#f5f5f5')

# Save the plot as an image file
plt.savefig('dasharo_edk2.png')

# Optionally, close the plot to free up memory
plt.close()
