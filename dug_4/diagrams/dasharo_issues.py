#!/usr/bin/env python3

import matplotlib.pyplot as plt

# Data
quarters = ['Q1\'23', 'Q2\'23', 'Q3\'23', 'Q4\'23']
total_issues = [360, 455, 484, 598]
closed_issues = [125, 166, 195, 245]
open_issues = [total - closed for total, closed in zip(total_issues, closed_issues)]

# Create the plot
plt.figure(figsize=(10, 6))

# Stacked bar chart
bars_closed = plt.bar(quarters, closed_issues, color='#38d430', label='Closed Issues')
bars_open = plt.bar(quarters, open_issues, bottom=closed_issues, color='#272727', label='Open Issues')

# Add titles and labels
plt.title('Dasharo Issues in 2023', fontsize=16, fontweight='bold', color='#272727')
plt.xlabel('Quarter', fontsize=14, fontweight='bold', color='#272727')
plt.ylabel('Number of Issues', fontsize=14, fontweight='bold', color='#272727')

# Function to add labels inside the bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        plt.annotate(f'{height}',
                     xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                     xytext=(0, 3),  # 3 points vertical offset
                     textcoords="offset points",
                     ha='center', va='bottom', color='white', fontsize=10)

# Add labels to the bars
add_labels(bars_closed)
add_labels(bars_open)

# Add legend
plt.legend()

# Set the background color
plt.gca().set_facecolor('#f5f5f5')

# Save the plot as an image file
plt.savefig('dasharo_issues.png')

# Optionally, close the plot to free up memory
plt.close()

