#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>
#
# SPDX-License-Identifier: Apache-2.0
import matplotlib.pyplot as plt
import numpy as np

# Last checked 11/06/2024

emulation = {}
network_appliance = {}
laptops = {}
desktops = {}
workstation = {}

emulation["Q3'21"] = 0
emulation["Q4'21"] = 0
emulation["Q1'22"] = 0
emulation["Q2'22"] = 0
emulation["Q3'22"] = 0
emulation["Q4'22"] = 0
emulation["Q1'23"] = 0
emulation["Q2'23"] = 0
emulation["Q3'23"] = 0
emulation["Q4'23"] = 1
emulation["Q1'24"] = 0
emulation["Q2'24"] = 1
emulation["Q3'24"] = 0
laptops["Q3'21"] = 3
laptops["Q4'21"] = 3
laptops["Q1'22"] = 5
laptops["Q2'22"] = 4
laptops["Q3'22"] = 1
laptops["Q4'22"] = 3
laptops["Q1'23"] = 2
laptops["Q2'23"] = 2
laptops["Q3'23"] = 0
laptops["Q4'23"] = 4
laptops["Q1'24"] = 5
laptops["Q2'24"] = 1
laptops["Q3'24"] = 2
network_appliance["Q3'21"] = 0
network_appliance["Q4'21"] = 0
network_appliance["Q1'22"] = 1
network_appliance["Q2'22"] = 2
network_appliance["Q3'22"] = 2
network_appliance["Q4'22"] = 3
network_appliance["Q1'23"] = 1
network_appliance["Q2'23"] = 2
network_appliance["Q3'23"] = 0
network_appliance["Q4'23"] = 0
network_appliance["Q1'24"] = 1
network_appliance["Q2'24"] = 4
network_appliance["Q3'24"] = 0
desktops["Q3'21"] = 0
desktops["Q4'21"] = 0
desktops["Q1'22"] = 0
desktops["Q2'22"] = 5
desktops["Q3'22"] = 0
desktops["Q4'22"] = 1
desktops["Q1'23"] = 1
desktops["Q2'23"] = 0
desktops["Q3'23"] = 2
desktops["Q4'23"] = 0
desktops["Q1'24"] = 4
desktops["Q2'24"] = 0
desktops["Q3'24"] = 0
workstation["Q3'21"] = 0
workstation["Q4'21"] = 4
workstation["Q1'22"] = 1
workstation["Q2'22"] = 1
workstation["Q3'22"] = 2
workstation["Q4'22"] = 0
workstation["Q1'23"] = 0
workstation["Q2'23"] = 0
workstation["Q3'23"] = 1
workstation["Q4'23"] = 0
workstation["Q1'24"] = 0
workstation["Q2'24"] = 0
workstation["Q3'24"] = 0

dates = list(laptops.keys())
emulation_values = np.array(list(emulation.values()))
network_appliance_values = np.array(list(network_appliance.values()))
laptop_values = np.array(list(laptops.values()))
desktop_values = np.array(list(desktops.values()))
workstation_values = np.array(list(workstation.values()))

total_releases = (
    sum(emulation_values)
    + sum(network_appliance_values)
    + sum(laptop_values)
    + sum(desktop_values)
    + sum(workstation_values)
)

plt.figure(figsize=(10, 6))

bars_emulation = plt.bar(
    dates,
    emulation_values,
    color="#272727",
    label=f"Emulation ({sum(emulation_values)/total_releases*100:.1f}%)",
)
bars_network_appliance = plt.bar(
    dates,
    network_appliance_values,
    bottom=emulation_values,
    color="#1f77b4",
    label=f"Network Appliance ({sum(network_appliance_values)/total_releases*100:.1f}%)",
)
bars_laptop = plt.bar(
    dates,
    laptop_values,
    bottom=emulation_values + network_appliance_values,
    color="#38d430",
    label=f"Laptop ({sum(laptop_values)/total_releases*100:.1f}%)",
)
bars_desktop = plt.bar(
    dates,
    desktop_values,
    bottom=emulation_values + network_appliance_values + laptop_values,
    color="#ff7f0e",
    label=f"Desktop ({sum(desktop_values)/total_releases*100:.1f}%)",
)
bars_workstation = plt.bar(
    dates,
    workstation_values,
    bottom=emulation_values + network_appliance_values + laptop_values + desktop_values,
    color="#d62728",
    label=f"Workstation ({sum(workstation_values)/total_releases*100:.1f}%)",
)

plt.title(
    "Dasharo Public Releases per market segment",
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


add_labels(bars_emulation)
add_labels(bars_network_appliance)
add_labels(bars_laptop)
add_labels(bars_desktop)
add_labels(bars_workstation)

plt.legend(fontsize=12)

plt.gca().set_facecolor("#f5f5f5")

plt.savefig("public/dug_7/dasharo_per_segment.png", dpi=300)

plt.close()
