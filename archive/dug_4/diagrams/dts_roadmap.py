#!/usr/bin/env python3

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

dts_1213 = roadmap.add_group("DTS v1.2.13")

dts_1213.add_task("Porting", "2024-01-01", "2024-02-14", style="rounded", fill_colour="#EA4335")
dts_1213.add_task("Validation", "2024-02-15", "2024-03-06", style="rounded", fill_colour="#34A853")
dts_1213.add_task("Community Release", "2024-03-07", "2024-03-31", style="rounded", fill_colour="#ADD8E6")

dts_200 = roadmap.add_group("DTS v2.0.0")
dts_200.add_task("Porting", "2024-01-01", "2024-03-31", style="rounded", fill_colour="#EA4335")
dts_200.add_task("Validation", "2024-04-01", "2024-05-15", style="rounded", fill_colour="#34A853")
dts_200.add_task("Community Release", "2024-05-16", "2024-06-30", style="rounded", fill_colour="#ADD8E6")

roadmap.set_footer("Dasharo Community Support Roadmap | December 2023 (v0.4) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save("dts_roadmap_v0.4.png")
