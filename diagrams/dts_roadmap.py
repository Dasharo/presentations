#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>
#
# SPDX-License-Identifier: Apache-2.0

from roadmapper.roadmap import Roadmap
from roadmapper.timelinemode import TimelineMode

""""
Dasharo Tools Suite Roadmap
"""
roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Tools Suite Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2025-07-01", number_of_items=2)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

dts_260 = roadmap.add_group("DTS v2.6.0")

dts_260.add_task(
    "E2E testing improvements",
    "2025-07-01",
    "2025-08-04",
    style="rounded",
    fill_colour="#EA4335",
)

dts_261 = roadmap.add_group("DTS v2.6.1")

dts_261.add_task(
    "NovaCustom MTL v1.0.0",
    "2025-08-01",
    "2025-08-28",
    style="rounded",
    fill_colour="#EA4335",
)

dts_261.add_task(
    "Odroid-H4 v0.9.1",
    "2025-08-01",
    "2025-08-28",
    style="rounded",
    fill_colour="#EA4335",
)

dts_270 = roadmap.add_group("DTS v2.7.0")

dts_270.add_task(
    "ASRock server v0.9.0",
    "2025-08-07",
    "2025-09-11",
    style="rounded",
    fill_colour="#EA4335",
)

future = roadmap.add_group("Future")

future.add_task(
    "MSI Z690/Z790", "2025-09-11", "2025-10-31", style="rounded", fill_colour="#EA4335"
)

future.add_task(
    "PC Engines APU (UEFI, SeaBIOS)",
    "2025-09-11",
    "2025-10-31",
    style="rounded",
    fill_colour="#EA4335",
)

roadmap.set_footer("Dasharo Tools Suite Roadmap |  August 2025 (v0.1) | CC-BY-SA-4.0")

roadmap.draw()
roadmap.save("dts_roadmap_v0.1.png")
