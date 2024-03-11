#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>
#
# SPDX-License-Identifier: Apache-2.0

from roadmapper.roadmap import Roadmap
from roadmapper.timelinemode import TimelineMode

""""
Dasharo Team Events Roadmap Q1-Q2'24
"""
roadmap = Roadmap(1600, 900, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Team Events Roadmap Q1-Q2'24")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.MONTHLY, start="2024-01-01", number_of_items=8)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

dasharo = roadmap.add_group("Dasharo")
zarhus = roadmap.add_group("Zarhus")

fosdem = dasharo.add_task("FOSSDEM 2024", "2024-01-04", "2024-02-04", style="rounded", fill_colour="#38d430")
fosdem.add_milestone("Open-source firmware devroom", "2024-02-04", font_size=30, text_alignment="right:35%")
dasharo.add_task("DUG#5 & vPub 0xA", "2024-02-14", "2024-03-14", style="rounded", fill_colour="#38d430")
fossasia = dasharo.add_task("FOSSASIA 2024", "2024-03-10", "2024-04-10", style="rounded", fill_colour="#38d430")
fossasia.add_milestone("Dasharo, open-source firmware", "2024-04-10", font_size=30, text_alignment="right:35%")
xds = dasharo.add_task("Xen Dev Summit", "2024-05-06", "2024-06-06", style="rounded", fill_colour="#38d430")
xds.add_milestone("Challenges and status of\nenabling TrenchBoot\nin Xen hypervisor", "2024-06-06", font_size=30, text_alignment="right:35%")
dasharo.add_task("DUG#6 & vPub 0xB", "2024-05-13", "2024-06-13", style="rounded", fill_colour="#38d430")

z_fosdem = zarhus.add_task("FOSSDEM 2024", "2024-01-04", "2024-02-04", style="rounded", fill_colour="#ff8c00")
z_fosdem.add_milestone("Securing Embedded Systems with\nfTPM implemented as Trusted Application\nin TEE", "2024-02-04", font_size=30, text_alignment="right:35%")

roadmap.set_footer("Dasharo Team Events Roadmap | March 2024 (v0.1) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save("img/dasharo_team_roadmap.png")

""""
Dasharo Team Events Roadmap Q3-Q4'24
"""
roadmap = Roadmap(1600, 900, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Team Events Roadmap Q3-Q4'24")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.MONTHLY, start="2024-08-01", number_of_items=5)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

dasharo = roadmap.add_group("Dasharo")
zarhus = roadmap.add_group("Zarhus")
pet = roadmap.add_group("Pace Enterprise Training")

osfc = dasharo.add_task("OSFC", "2024-08-03", "2024-09-03", style="rounded", fill_colour="#38d430")
dasharo.add_task("DUG#7 & vPub 0xC", "2024-08-12", "2024-09-12", style="rounded", fill_colour="#38d430")
lpc = dasharo.add_task("Linux Plumbers", "2024-08-18", "2024-09-18", style="rounded", fill_colour="#38d430")
qos = dasharo.add_task("Qubes OS Summit", "2024-08-22", "2024-09-22", style="rounded", fill_colour="#38d430")
dasharo.add_task("DUG#8 & vPub 0xC", "2024-11-12", "2024-12-12", style="rounded", fill_colour="#38d430")

pet.add_task("Hardwear.io", "2024-10-12", "2024-11-12", style="rounded", fill_colour="#9370db")

yocto = zarhus.add_task("Yocto Summit 2024.11", "2024-10-30", "2024-11-30", style="rounded", fill_colour="#ff8c00")

# FIXME: footer doesn not display
roadmap.set_footer("Dasharo Team Events Roadmap | March 2024 (v0.1) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save("img/dasharo_team_roadmap2.png")
