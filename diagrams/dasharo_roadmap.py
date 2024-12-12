#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>
#
# SPDX-License-Identifier: Apache-2.0

from roadmapper.roadmap import Roadmap
from roadmapper.timelinemode import TimelineMode
import sys

version = "v0.8"
date = "December 2024"
dug_id = "dug_8"

""""
Dasharo Sample Roadmap v0.8
"""
roadmap = Roadmap(1600, 900, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo [Segment] [Vendor] [Model] Roadmap ")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-10-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

sample_1 = roadmap.add_group("coreboot+UEFI\nv0.9.0")

sample_1.add_task("Validation", "2024-10-01", "2024-12-31", style="rounded", fill_colour="#34A853")
sample_1.add_task("DPP Release", "2025-01-01", "2025-03-31", style="rounded", fill_colour="#FD7E14")

sample_2 = roadmap.add_group("coreboot+SeaBIOS\nv24.08.00.01", font_size=31)

sample_2.add_task("Validation", "2025-04-01", "2025-06-30", style="rounded", fill_colour="#34A853")
sample_2.add_task("DPP Release", "2025-07-01", "2025-09-30", style="rounded", fill_colour="#FD7E14")

sample_3 = roadmap.add_group("coreboot+Heads\nv0.9.0")

sample_3.add_task("Release Candidate", "2025-01-01", "2025-03-31", style="rounded", fill_colour="#7E14FD")
sample_3.add_task("Community Release", "2025-04-01", "2025-06-30", style="rounded", fill_colour="#ADD8E6")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"public/{dug_id}/dcs_sample_roadmap_{version}.png")

""""
Dasharo Community Support Emulation Roadmap
"""
roadmap = Roadmap(1600, 660, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Emulation QEMU Q35 Roadmap ")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-10-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

qemu_q35_v24080001 = roadmap.add_group("coreboot+UEFI\nv24.08.00.01")

qemu_q35_v24080001.add_task("Release Candidate", "2024-10-01", "2024-12-31", style="rounded", fill_colour="#7E14FD")
qemu_q35_v24080001.add_task("Community Release", "2025-01-01", "2025-03-31", style="rounded", fill_colour="#ADD8E6")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"public/{dug_id}/dcs_emu_roadmap_{version}.png")

""""
Dasharo Community Support Network Appliance Roadmap
"""
roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Network Appliance PC Engines apu2/3/4/6 Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-10-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

pcengines_24080001 = roadmap.add_group("coreboot+SeaBIOS\nv24.08.00.01", font_size=28)
pcengines_24110001 = roadmap.add_group("coreboot+SeaBIOS\nv24.11.00.01", font_size=28)
pcengines_091 = roadmap.add_group("coreboot+UEFI\nv0.9.1", font_size=28)

pcengines_091.add_task("DPP\nRelease", "2025-01-01", "2025-03-31", style="rounded", fill_colour="#FD7E14")
pcengines_24080001.add_task("DPP\nRelease", "2024-10-01", "2024-12-31", style="rounded", fill_colour="#FD7E14")
pcengines_24110001.add_task("DPP\nRelease", "2024-10-01", "2024-12-31", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"public/{dug_id}/dcs_network_appliance_roadmap_{version}_pt1.png")


roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Network Appliance Protectli VP4670 Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-10-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

protectli = roadmap.add_group("coreboot+SeaBIOS\nv0.9.0", font_size=30)
protectli.add_task("DPP\nRelease", "2025-01-01", "2025-03-31", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"public/{dug_id}/dcs_network_appliance_roadmap_{version}_pt2.png")

roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Network Appliance MinnowBoard Turbot Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-01-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

mb = roadmap.add_group("Dasharo (coreboot+UEFI)\nv0.9.0\n")
mb.add_task("DPP\nRelease", "2024-10-01", "2024-12-31", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"public/{dug_id}/dcs_network_appliance_roadmap_{version}_pt3.png")

roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Network Appliance Hardkernel Odroid-H4+ Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-07-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

mb = roadmap.add_group("coreboot+UEFI\nv0.9.0")
mb.add_task("Porting", "2024-07-01", "2024-08-15", style="rounded", fill_colour="#EA4335")
mb.add_task("Validation", "2024-08-16", "2024-09-30", style="rounded", fill_colour="#34A853", font_size=23)
mb.add_task("DPP Release", "2024-10-01", "2024-12-31", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"public/{dug_id}/dcs_network_appliance_roadmap_{version}_pt4.png")

""""
Dasharo Community Support Laptops Roadmap
"""
roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Laptop Novacustom Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-10-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

novacustom_v56tu = roadmap.add_group("V56TU\ncoreboot+Heads\nv0.9.0")
novacustom_v56tu.add_task("Validation", "2024-10-01", "2024-12-31", style="rounded", fill_colour="#34A853")
novacustom_v56tu.add_task("DPP Release", "2024-10-01", "2024-12-31", style="rounded", fill_colour="#FD7E14")
novacustom_nv4x = roadmap.add_group("NV4x\ncoreboot+Heads\nv0.9.2")
novacustom_nv4x.add_task("Validation", "2025-01-01", "2025-03-31", style="rounded", fill_colour="#34A853")
novacustom_nv4x.add_task("DPP Release", "2025-01-01", "2025-03-31", style="rounded", fill_colour="#FD7E14")
novacustom_172x = roadmap.add_group("NV4x\ncoreboot+SeaBIOS\nv1.7.2.x", font_size=31)
novacustom_172x.add_task("Validation", "2025-01-01", "2025-03-31", style="rounded", fill_colour="#34A853")
novacustom_172x.add_task("DPP Release", "2025-01-01", "2025-03-31", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"public/{dug_id}/dcs_laptop_roadmap_{version}.png")


""""
Dasharo Community Support Desktop Roadmap
"""
roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Desktop Dell OptiPlex 7010/9010 Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-10-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

dell_optiplex = roadmap.add_group("coreboot+SeaBIOS\nv0.1.1", font_size=31)
dell_optiplex.add_task("Validation", "2024-10-01", "2024-12-31", style="rounded", fill_colour="#34A853")
dell_optiplex.add_task("DPP Release", "2024-10-01", "2024-12-31", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"public/{dug_id}/dcs_desktop_dell_roadmap_{version}.png")


roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Desktop MSI PRO Z690-A Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-10-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

msi_z690_114 = roadmap.add_group("coreboot+UEFI\nv1.1.4")
msi_z690_114.add_task("Validation", "2024-10-01", "2024-12-31", style="rounded", fill_colour="#34A853")
msi_z690_114.add_task("DPP Release", "2024-10-01", "2024-12-31", style="rounded", fill_colour="#FD7E14")

msi_z690_dcr = roadmap.add_group("coreboot+UEFI\nv1.2.0")
msi_z690_dcr.add_task("Validation", "2025-01-01", "2025-03-31", style="rounded", fill_colour="#34A853")
msi_z690_dcr.add_task("Community Release", "2025-01-01", "2025-03-31", style="rounded", fill_colour="#ADD8E6")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"public/{dug_id}/dcs_desktop_msi_z690_roadmap_{version}.png")


roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Desktop MSI PRO Z790-P Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-10-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

msi_z790_092 = roadmap.add_group("coreboot+UEFI\nv0.9.2")
msi_z790_092.add_task("DPP Release", "2024-10-01", "2024-12-31", style="rounded", fill_colour="#FD7E14")

msi_z790_dcr = roadmap.add_group("coreboot+UEFI\nv1.0.0")
msi_z790_dcr.add_task("Validation", "2025-01-01", "2025-03-31", style="rounded", fill_colour="#34A853")
msi_z790_dcr.add_task("Community Release", "2025-01-01", "2025-03-31", style="rounded", fill_colour="#ADD8E6")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"public/{dug_id}/dcs_desktop_msi_z790_roadmap_{version}.png")


roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Desktop Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2023-10-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

msi_z790 = roadmap.add_group("MSI PRO Z790-P v0.9.0\n coreboot+Heads")
msi_z790.add_task("Porting", "2023-11-16", "2023-12-31", style="rounded", fill_colour="#EA4335")
msi_z790.add_task("Validation", "2024-01-01", "2024-02-14", style="rounded", fill_colour="#34A853", font_size=23)
msi_z790.add_task("DPP Release", "2024-02-15", "2024-03-31", style="rounded", fill_colour="#FD7E14")

msi_z690 = roadmap.add_group("MSI PRO Z690-A v0.9.0\n coreboot+Heads")
msi_z690.add_task("Porting", "2023-11-16", "2023-12-31", style="rounded", fill_colour="#EA4335")
msi_z690.add_task("Validation", "2024-01-01", "2024-02-14", style="rounded", fill_colour="#34A853", font_size=23)
msi_z690.add_task("DPP Release", "2024-02-15", "2024-03-31", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"public/{dug_id}/dcs_desktop_msi_heads_roadmap_{version}.png")

roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Desktop Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2023-10-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

asrock = roadmap.add_group("ASRock X370 Killer SLI/ac")
asrock.add_task("Porting", "2023-10-01", "2024-02-14", style="rounded", fill_colour="#EA4335")
asrock.add_task("Validation", "2024-02-15", "2024-03-31", style="rounded", fill_colour="#34A853", font_size=23)
asrock.add_task("DPP Release", "2024-04-01", "2024-06-30", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"public/{dug_id}/dcs_desktop_asrock_roadmap_{version}.png")

""""
Dasharo Community Support Workstation Roadmap
"""
roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Workstation Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2023-10-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"public/{dug_id}/dcs_workstation_roadmap_{version}.png")

""""
Dasharo Community Support Server Roadmap
"""
roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Server Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2023-10-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"public/{dug_id}/dcs_server_roadmap_{version}.png")

sys.exit()
