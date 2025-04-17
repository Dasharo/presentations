#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>
#
# SPDX-License-Identifier: Apache-2.0

from roadmapper.roadmap import Roadmap
from roadmapper.timelinemode import TimelineMode

""""
Dasharo Team Events Roadmap Q1-Q2'25
"""
roadmap = Roadmap(1900, 1100, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Team Events Roadmap Q1'25")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.MONTHLY, start="2025-01-01", number_of_items=6)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

dasharo = roadmap.add_group("Dasharo")
zarhus = roadmap.add_group("Zarhus")
pet = roadmap.add_group("Pace Enterprise Training")

dasharo.add_task(
    "DUG#9 &\nvPub 0xE",
    "2025-02-20",
    "2025-03-20",
    style="rounded",
    fill_colour="#38d430",
)
fosdem = dasharo.add_task(
    "FOSDEM 2025", "2025-01-04", "2025-02-04", style="rounded", fill_colour="#38d430"
)
fosdem.add_milestone(
    "Open-source firmware\ndevroom",
    "2025-02-04",
    font_size=30,
    text_alignment="right:35%",
)
xen = dasharo.add_task(
    "Xen Winter Meetup",
    "2024-12-31",
    "2025-01-31",
    style="rounded",
    fill_colour="#38d430",
)
xen.add_milestone(
    "Enabling UEFI Secure Boot\nin XCP-ng: Establishing\na Robust Chain of Trust",
    "2025-01-31",
    font_size=30,
    text_alignment="right:35%",
)

yocto = zarhus.add_task(
    "Zarhus Dev Meetup",
    "2025-04-06",
    "2025-05-06",
    style="rounded",
    fill_colour="#ff8c00",
)

hwio = pet.add_task(
    "HWIO US", "2025-04-27", "2025-05-27", style="rounded", fill_colour="#9370db"
)
hwio.add_milestone(
    "Mastering\nUEFI Secure Boot\nand Intel Root of\nTrust Technologies",
    "2025-05-27",
    font_size=30,
    text_alignment="right:35%",
)

dasharo.add_task(
    "DUG#10 &\nvPub 0xF",
    "2025-05-13",
    "2025-06-12",
    style="rounded",
    fill_colour="#38d430",
)

roadmap.set_footer("Dasharo Team Events Roadmap | March 2025 | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save("public/dug_9/dasharo_team_roadmap.png")

""""
Dasharo Team Events Roadmap Q3-Q4'25
"""
roadmap2 = Roadmap(1900, 1100, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap2.set_title("Dasharo Team Events Roadmap Q3-Q4'25")
roadmap2.set_subtitle("subject to change")
roadmap2.set_timeline(TimelineMode.MONTHLY, start="2025-07-01", number_of_items=6)
roadmap2.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

dasharo = roadmap2.add_group("Dasharo")

dasharo.add_task(
    "DUG#11 &\nvPub 0x10",
    "2025-08-18",
    "2025-09-18",
    style="rounded",
    fill_colour="#38d430",
)
dasharo.add_task(
    "Qubes OS Summit 2025",
    "2025-09-01",
    "2025-09-30",
    style="rounded",
    fill_colour="#38d430",
)

roadmap2.set_footer("Dasharo Team Events Roadmap | March 2025 | CC-BY-SA-4.0")
roadmap2.draw()
roadmap2.save("public/dug_9/dasharo_team_roadmap2.png")
