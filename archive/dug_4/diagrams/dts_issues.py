#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>
#
# SPDX-License-Identifier: Apache-2.0

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

def count_issues(repo, state, date):
    # Construct the GitHub CLI command
    command = f"gh issue list --label DasharoToolsSuite --repo {repo} --state {state} --search 'created:<={date}' -L 10000 --json number --jq '. | length'"

    # Run the command and capture the output
    output = run_gh_command(command)

    # Parse the output to get the count
    if output is not None:
        return int(output)
    else:
        return 0

repo = "Dasharo/dasharo-issues"
dates = ["2023-03-16", "2023-07-06", "2023-09-28", "2023-12-03"]

# Data storage
data = {"Total": [], "Closed": [], "Open": []}

# Gather data
for date in dates:
    total_issues = count_issues(repo, 'all', date)
    closed_issues = count_issues(repo, 'closed', date)
    open_issues = count_issues(repo, 'open', date)
    data["Total"].append(total_issues)
    data["Closed"].append(closed_issues)
    data["Open"].append(open_issues)

# Plotting
plt.figure(figsize=(10, 6))

# Stacked bar chart
bars_closed = plt.bar(dates, data["Closed"], color='#38d430', label='Closed issues')
bars_open = plt.bar(dates, data["Open"], bottom=data["Closed"], color='#272727', label='Open issues')

# Add titles and labels
plt.title('Dasharo Issues Statistics', fontsize=18, fontweight='bold', color='#272727')
plt.xlabel('Date', fontsize=16, fontweight='bold', color='#272727')
plt.ylabel('Number of Issues', fontsize=16, fontweight='bold', color='#272727')

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
add_labels(bars_closed)
add_labels(bars_open)

# Add legend
plt.legend(fontsize=12)

# Set the background color
plt.gca().set_facecolor('#f5f5f5')

# Save the plot as an image file
plt.savefig('dts_issues_2023q4.png')

# Optionally, close the plot to free up memory
plt.close()
