#!/usr/bin/env python3

from roadmapper.roadmap import Roadmap
from roadmapper.timelinemode import TimelineMode

roadmap = Roadmap(1200, 400, colour_theme="dasharo.json")
roadmap.set_title("Dasharo Emulation Roadmap")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2023-01-01", number_of_items=5)
roadmap.add_logo("../../img/dasharo_logo.png", "top-right", 50, 50)

qemu_q35_v010 = roadmap.add_group("QEMU Q35 v0.1.0")

qemu_q35_v010.add_task("Porting", "2023-01-01", "2023-03-31")
qemu_q35_v010.add_task("Validation", "2023-10-01", "2023-11-15")
q35_cr_v01 = qemu_q35_v010.add_task("Community Release", "2023-11-16", "2023-12-31")
q35_cr_v01.add_milestone("v0.1.0", "2023-12-06")

qemu_q35_v020 = roadmap.add_group("QEMU Q35 v0.2.0")
qemu_q35_v020.add_task("Validation", "2024-01-01", "2024-02-14")
q35_cr_v02 = qemu_q35_v020.add_task("Community Release", "2024-02-14", "2024-03-30")
q35_cr_v02.add_milestone("v0.2.0", "2024-03-30")

roadmap.set_footer("Dasharo Community Support Roadmap | December 2023 (v0.4) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save("demo01.png")
