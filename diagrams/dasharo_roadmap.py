#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>
#
# SPDX-License-Identifier: Apache-2.0

from roadmapper.roadmap import Roadmap
from roadmapper.timelinemode import TimelineMode
import sys

version = "v0.6"
date = "June 2024"

""""
Dasharo Community Support Emulation Roadmap
"""
roadmap = Roadmap(1600, 660, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Emulation Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2023-10-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

qemu_q35_v010 = roadmap.add_group("QEMU Q35 UEFI v0.1.0")
qemu_q35_v020 = roadmap.add_group("coreboot+UEFI v0.2.0")

qemu_q35_v010.add_task("Validation", "2023-10-01", "2023-11-15", style="rounded", fill_colour="#34A853", font_size=23)
qemu_q35_v010.add_task("Community Release", "2023-11-16", "2023-12-31", style="rounded", fill_colour="#ADD8E6", font_size=23)
qemu_q35_v020.add_task("Community Release", "2024-04-01", "2024-06-30", style="rounded", fill_colour="#ADD8E6")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"img/dcs_emu_roadmap_{version}.png")

""""
Dasharo Community Support Network Appliance Roadmap
"""
roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Network Appliance Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-01-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

pcengines = roadmap.add_group("PC Engines apu2/3/4/6 coreboot+UEFI v0.9.0", font_size=26)
pcengines_091 = roadmap.add_group("coreboot+UEFI v0.9.1", font_size=26)
pcengines_24020101 = roadmap.add_group("coreboot+SeaBIOS v24.05.00.01", font_size=26)
pcengines_4034 = roadmap.add_group("coreboot+SeaBIOS v4.0.34", font_size=26)

pcengines.add_task("Validation", "2024-01-01", "2024-02-14", style="rounded", fill_colour="#34A853", font_size=23)
pcengines.add_task("DES Release", "2024-02-15", "2024-03-31", style="rounded", fill_colour="#FD7E14", font_size=23)
pcengines_091.add_task("DES Release", "2024-04-01", "2024-06-30", style="rounded", fill_colour="#FD7E14")
pcengines_24020101.add_task("DES Release", "2024-04-01", "2024-06-30", style="rounded", fill_colour="#FD7E14")
pcengines_4034.add_task("DES Release", "2024-07-01", "2024-09-30", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"img/dcs_network_appliance_roadmap_{version}_pt1.png")


roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Network Appliance Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-01-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

protectli = roadmap.add_group("Protectli VP4670\ncoreboot+SeaBIOS\nv0.9.0", font_size=30)
protectli.add_task("Evaluation", "2024-01-01", "2024-02-14", style="rounded", fill_colour="#9B51E0", font_size=23)
protectli.add_task("Porting", "2024-02-15", "2024-03-31", style="rounded", fill_colour="#EA4335")
protectli.add_task("Validation", "2024-04-01", "2024-06-30", style="rounded", fill_colour="#34A853")
protectli.add_task("DES Release", "2024-07-01", "2024-09-30", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"img/dcs_network_appliance_roadmap_{version}_pt2.png")

roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Network Appliance Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-01-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

mb = roadmap.add_group("MinnowBoard Turbot\nDasharo (coreboot+UEFI) v0.9.0")
mb.add_task("Porting", "2024-04-01", "2024-05-15", style="rounded", fill_colour="#EA4335")
mb.add_task("Validation", "2024-05-16", "2024-06-30", style="rounded", fill_colour="#34A853", font_size=23)
mb.add_task("DES Release", "2024-07-01", "2024-09-30", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"img/dcs_network_appliance_roadmap_{version}_pt3.png")

roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Network Appliance Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-07-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

mb = roadmap.add_group("Hardkernel Odroid-H4\nDasharo (coreboot+UEFI) v0.9.0")
mb.add_task("Porting", "2024-07-01", "2024-08-15", style="rounded", fill_colour="#EA4335")
mb.add_task("Validation", "2024-08-16", "2024-09-30", style="rounded", fill_colour="#34A853", font_size=23)
mb.add_task("DES Release", "2024-10-01", "2024-12-31", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"img/dcs_network_appliance_roadmap_{version}_pt4.png")

""""
Dasharo Community Support Laptops Roadmap
"""
roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Laptop Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-01-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

novacustom = roadmap.add_group("Novacustom NV4x v0.9.0")
novacustom.add_task("Validation", "2024-01-01", "2024-02-14", style="rounded", fill_colour="#34A853", font_size=23)
novacustom.add_task("DES Release", "2024-02-15", "2024-03-31", style="rounded", fill_colour="#FD7E14")
novacustom_091 = roadmap.add_group("Novacustom NV4x v0.9.1")
novacustom_091.add_task("DES Release", "2024-07-01", "2024-09-30", style="rounded", fill_colour="#FD7E14")
novacustom_180 = roadmap.add_group("Novacustom NV4x v1.8.0")
novacustom_180.add_task("DES Release", "2024-07-01", "2024-09-30", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"img/dcs_laptop_roadmap_{version}.png")


""""
Dasharo Community Support Desktop Roadmap
"""
roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Desktop Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-01-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

lenovo = roadmap.add_group("Lenovo ThinkCentre M700/M900 Tiny v0.9.0")
lenovo.add_task("Evaluation", "2024-01-01", "2024-02-14", style="rounded", fill_colour="#9B51E0", font_size=23)
lenovo.add_task("Porting", "2024-02-15", "2024-03-31", style="rounded", fill_colour="#EA4335")
lenovo.add_task("Validation", "2024-04-01", "2024-06-30", style="rounded", fill_colour="#34A853")
lenovo.add_task("DES Release", "2024-07-01", "2024-09-30", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"img/dcs_desktop_lenovo_roadmap_{version}.png")


roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Desktop Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-01-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

dell_optiplex = roadmap.add_group("Dell OptiPlex 7010/9010 v0.1.0")
dell_optiplex.add_task("Validation", "2024-07-01", "2024-08-15", style="rounded", fill_colour="#34A853", font_size=23)
dell_optiplex.add_task("DES Release", "2024-08-16", "2024-09-30", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"img/dcs_desktop_dell_roadmap_{version}.png")


roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Desktop Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-01-01", number_of_items=5)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

msi_z690 = roadmap.add_group("MSI PRO Z690-A v1.1.3")
msi_z690.add_task("Validation", "2023-10-01", "2023-12-31", style="rounded", fill_colour="#34A853", font_size=23)
msi_z690.add_task("DES Release", "2024-01-01", "2024-03-31", style="rounded", fill_colour="#FD7E14")
msi_z690_114 = roadmap.add_group("MSI PRO Z690-A v1.1.4")
msi_z690_114.add_task("DES Release", "2024-07-01", "2024-09-30", style="rounded", fill_colour="#FD7E14")

msi_z690_dcr = roadmap.add_group("MSI PRO Z690-A v1.2.0")
msi_z690_dcr.add_task("Validation", "2024-07-01", "2024-09-30", style="rounded", fill_colour="#34A853")
msi_z690_dcr.add_task("Community Release", "2024-10-01", "2024-12-30", style="rounded", fill_colour="#ADD8E6")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"img/dcs_desktop_msi_z690_roadmap_{version}.png")


roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Desktop Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2023-10-01", number_of_items=5)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

msi_z790 = roadmap.add_group("MSI PRO Z790-P v0.9.1")
msi_z790.add_task("Validation", "2023-10-01", "2023-12-31", style="rounded", fill_colour="#34A853", font_size=23)
msi_z790.add_task("DES Release", "2024-01-01", "2024-03-31", style="rounded", fill_colour="#FD7E14")
msi_z790_092 = roadmap.add_group("MSI PRO Z790-P v0.9.2")
msi_z790_092.add_task("DES Release", "2024-07-01", "2024-09-30", style="rounded", fill_colour="#FD7E14")

msi_z790_dcr = roadmap.add_group("MSI PRO Z790-P v1.0.0")
msi_z790_dcr.add_task("Validation", "2024-07-01", "2024-09-30", style="rounded", fill_colour="#34A853", font_size=23)
msi_z790_dcr.add_task("Community Release", "2024-10-01", "2024-12-30", style="rounded", fill_colour="#ADD8E6")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"img/dcs_desktop_msi_z790_roadmap_{version}.png")


roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Desktop Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2023-10-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

msi_z790 = roadmap.add_group("MSI PRO Z790-P v0.9.0\n coreboot+Heads")
msi_z790.add_task("Porting", "2023-11-16", "2023-12-31", style="rounded", fill_colour="#EA4335")
msi_z790.add_task("Validation", "2024-01-01", "2024-02-14", style="rounded", fill_colour="#34A853", font_size=23)
msi_z790.add_task("DES Release", "2024-02-15", "2024-03-31", style="rounded", fill_colour="#FD7E14")

msi_z690 = roadmap.add_group("MSI PRO Z690-A v0.9.0\n coreboot+Heads")
msi_z690.add_task("Porting", "2023-11-16", "2023-12-31", style="rounded", fill_colour="#EA4335")
msi_z690.add_task("Validation", "2024-01-01", "2024-02-14", style="rounded", fill_colour="#34A853", font_size=23)
msi_z690.add_task("DES Release", "2024-02-15", "2024-03-31", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"img/dcs_desktop_msi_heads_roadmap_{version}.png")

roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Desktop Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2023-10-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

asrock = roadmap.add_group("ASRock X370 Killer SLI/ac")
asrock.add_task("Porting", "2023-10-01", "2024-02-14", style="rounded", fill_colour="#EA4335")
asrock.add_task("Validation", "2024-02-15", "2024-03-31", style="rounded", fill_colour="#34A853", font_size=23)
asrock.add_task("DES Release", "2024-04-01", "2024-06-30", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"img/dcs_desktop_asrock_roadmap_{version}.png")

roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Workstation Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2023-10-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

rcs = roadmap.add_group("Raptor CS Talos II v0.8.0")
rcs.add_task("Validation", "2024-04-01", "2024-05-15", style="rounded", fill_colour="#34A853", font_size=23)
rcs.add_task("DES Release", "2024-05-16", "2024-06-30", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"img/dcs_workstation_roadmap_{version}.png")

roadmap = Roadmap(1600, 1000, colour_theme="diagrams/dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Server Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2023-10-01", number_of_items=4)
roadmap.add_logo("img/dasharo_logo_white.png", "top-right", 140, 140)

roadmap.set_footer(f"Dasharo Community Support Roadmap | {date} ({version}) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save(f"img/dcs_server_roadmap_{version}.png")

sys.exit()
