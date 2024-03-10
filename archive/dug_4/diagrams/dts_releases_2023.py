#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>
#
# SPDX-License-Identifier: Apache-2.0

from roadmapper.roadmap import Roadmap
from roadmapper.timelinemode import TimelineMode

""""
Dasharo Tools Suite Roadmap
"""
roadmap = Roadmap(1600, 1000, colour_theme="dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Tools Suite Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-01-01", number_of_items=2)
roadmap.add_logo("../../img/dasharo_logo_white.png", "top-right", 140, 140)

dts_1213 = roadmap.add_group("DTS")

dts_1213.add_milestone("Porting", "2024-01-01", "2024-02-14", style="rounded", fill_colour="#EA4335")

roadmap.set_footer("Dasharo Community Support Roadmap | December 2023 (v0.4) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save("dts_releases_2023.png")
