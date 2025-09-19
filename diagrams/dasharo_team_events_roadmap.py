#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>
#
# SPDX-License-Identifier: Apache-2.0

from roadmapper.roadmap import Roadmap
from roadmapper.timelinemode import TimelineMode

""""
Dasharo Team Events Roadmap Q3-Q4'25
"""
roadmap = Roadmap(1900, 1100, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Team Events Roadmap Q3'25")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.MONTHLY, start="2025-07-01", number_of_items=6)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

dasharo = roadmap.add_group("Dasharo")
zarhus = roadmap.add_group("Zarhus")
pet = roadmap.add_group("Pace Enterprise Training")

zdm02 = zarhus.add_task(
    "Zarhus Dev Meetup #2",
    "2025-07-05",
    "2025-08-05",
    style="rounded",
    fill_colour="#ff8c00",
)

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

zdm03 = zarhus.add_task(
    "Zarhus Dev Meetup #3",
    "2025-10-04",
    "2025-11-04",
    style="rounded",
    fill_colour="#ff8c00",
)

dasharo.add_task(
    "DUG#12 &\nvPub 0x11",
    "2025-11-18",
    "2025-12-18",
    style="rounded",
    fill_colour="#38d430",
)

hwio = pet.add_task(
    "HWIO NL", "2025-10-17", "2025-11-21", style="rounded", fill_colour="#9370db"
)
hwio.add_milestone(
    "Mastering\nUEFI Secure Boot\nand Intel Root of\nTrust Technologies",
    "2025-11-21",
    font_size=30,
    text_alignment="right:35%",
)

dasharo.add_task(
    "Linux Plumbers Conference",
    "2025-11-12",
    "2025-12-12",
    style="rounded",
    fill_colour="#38d430",
)

roadmap.set_footer("Dasharo Team Events Roadmap | September 2025 | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save("img/dug_11/dasharo_team_roadmap.png")

""""
Dasharo Team Events Roadmap Q1'26-Q2'26
"""
roadmap2 = Roadmap(1900, 1100, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap2.set_title("Dasharo Team Events Roadmap Q1'26-Q2'26")
roadmap2.set_subtitle("subject to change")
roadmap2.set_timeline(TimelineMode.MONTHLY, start="2026-01-01", number_of_items=6)
roadmap2.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

dasharo = roadmap2.add_group("Dasharo")
zarhus = roadmap2.add_group("Zarhus")

fosdem = dasharo.add_task(
    "FOSDEM 2026", "2026-01-04", "2026-02-04", style="rounded", fill_colour="#38d430"
)
fosdem.add_milestone(
    "Open-source firmware\ndevroom",
    "2026-02-04",
    font_size=30,
    text_alignment="right:35%",
)

zdm04 = zarhus.add_task(
    "Zarhus Dev Meetup #4",
    "2026-01-10",
    "2026-02-10",
    style="rounded",
    fill_colour="#ff8c00",
)

dasharo.add_task(
    "DUG#13 &\nvPub 0x12",
    "2026-02-12",
    "2026-03-12",
    style="rounded",
    fill_colour="#38d430",
)

zdm04 = zarhus.add_task(
    "Zarhus Dev Meetup #5",
    "2026-04-12",
    "2026-05-12",
    style="rounded",
    fill_colour="#ff8c00",
)

dasharo.add_task(
    "DUG#14 &\nvPub 0x13",
    "2026-05-11",
    "2026-06-11",
    style="rounded",
    fill_colour="#38d430",
)

roadmap2.set_footer("Dasharo Team Events Roadmap | September 2025 | CC-BY-SA-4.0")
roadmap2.draw()
roadmap2.save("img/dug_11/dasharo_team_roadmap2.png")
