#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>
#
# SPDX-License-Identifier: Apache-2.0

from roadmapper.roadmap import Roadmap
from roadmapper.timelinemode import TimelineMode

""""
Dasharo Team Events Roadmap Q3-Q4'24
"""
roadmap = Roadmap(1900,1100, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Team Events Roadmap Q3-Q4'24")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.MONTHLY, start="2024-08-01", number_of_items=5)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

dasharo = roadmap.add_group("Dasharo")
zarhus = roadmap.add_group("Zarhus")
pet = roadmap.add_group("Pace Enterprise Training")

osfc = dasharo.add_task("OSFC", "2024-08-03", "2024-09-03", style="rounded", fill_colour="#38d430")
osfc.add_milestone("Enabling coreboot on Talos II Platform", "2024-09-04", font_size=30, text_alignment="right:35%")
dasharo.add_task("DUG#7 & vPub 0xC", "2024-08-12", "2024-09-12", style="rounded", fill_colour="#38d430")
lpc = dasharo.add_task("Linux Plumbers", "2024-08-18", "2024-09-18", style="rounded", fill_colour="#38d430")
lpc.add_milestone("Challenges in developing trustworthy Linux-based\nsystems in an open-source way", "2024-09-18", font_size=30, text_alignment="right:35%")
qos = dasharo.add_task("Qubes OS Summit", "2024-08-22", "2024-09-22", style="rounded", fill_colour="#38d430")
dasharo.add_task("DUG#8 & vPub 0xD", "2024-11-12", "2024-12-12", style="rounded", fill_colour="#38d430")

yocto = zarhus.add_task("Yocto Project Dev Day 2024", "2024-09-19", "2024-10-19", style="rounded", fill_colour="#ff8c00")
yocto.add_milestone("Practical Security for Embedded Systems:\nImplementing TEE and Secure Storage", "2024-10-19", font_size=30, text_alignment="right:35%")

hwio = pet.add_task("Hardwear.io", "2024-09-21", "2024-10-21", style="rounded", fill_colour="#9370db")
hwio.add_milestone("Mastering UEFI Secure Boot\nand Intel Root of Trust Technologies", "2024-10-21", font_size=30, text_alignment="right:35%")

roadmap.set_footer("Dasharo Team Events Roadmap | September 2024 | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save("public/dug_7/dasharo_team_roadmap.png")

""""
Dasharo Team Events Roadmap Q1-Q2'25
"""
roadmap = Roadmap(1800,1100, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Team Events Roadmap Q1-Q2'25")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.MONTHLY, start="2025-01-01", number_of_items=6)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

dasharo = roadmap.add_group("Dasharo")
zarhus = roadmap.add_group("Zarhus")
pet = roadmap.add_group("Pace Enterprise Training")

fosdem = dasharo.add_task("FOSDEM 2025", "2025-01-04", "2025-02-04", style="rounded", fill_colour="#808080")
fosdem.add_milestone("Open-source firmware devroom", "2025-02-04", font_size=30, text_alignment="right:35%")
dasharo.add_task("DUG#9 & vPub 0xE", "2025-02-14", "2025-03-13", style="rounded", fill_colour="#38d430")
dasharo.add_task("Xen Dev Summit", "2025-05-06", "2025-06-06", style="rounded", fill_colour="#808080")
dasharo.add_task("DUG#10 & vPub 0xF", "2025-05-13", "2025-06-12", style="rounded", fill_colour="#38d430")

zarhus.add_task("TBD", "2025-01-01", "2025-12-31", style="rounded", fill_colour="#808080")
pet.add_task("TBD", "2025-01-01", "2025-12-31", style="rounded", fill_colour="#808080")

roadmap.set_footer("Dasharo Team Events Roadmap | September 2024 | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save("public/dug_7/dasharo_team_roadmap2.png")
