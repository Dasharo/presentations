#!/usr/bin/env python3

from roadmapper.roadmap import Roadmap
from roadmapper.timelinemode import TimelineMode

""""
Dasharo Community Support Emulation Roadmap
"""
roadmap = Roadmap(1600, 660, colour_theme="dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Emulation Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2023-01-01", number_of_items=4)
roadmap.add_logo("../../img/dasharo_logo_white.png", "top-right", 140, 140)

qemu_q35_v010 = roadmap.add_group("QEMU Q35 v0.1.0")

qemu_q35_v010.add_task("Porting", "2023-01-01", "2023-03-31", style="rounded", fill_colour="#EA4335")
qemu_q35_v010.add_task("Validation", "2023-10-01", "2023-11-15", style="rounded", fill_colour="#34A853")
qemu_q35_v010.add_task("Community Release", "2023-11-16", "2023-12-31", style="rounded", fill_colour="#ADD8E6")

roadmap.set_footer("Dasharo Community Support Roadmap | December 2023 (v0.4) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save("dcs_emu_roadmap_v0.4.png")

""""
Dasharo Community Support Network Appliance Roadmap
"""
roadmap = Roadmap(1600, 1000, colour_theme="dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Network Appliance Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-01-01", number_of_items=4)
roadmap.add_logo("../../img/dasharo_logo_white.png", "top-right", 140, 140)

pcengines = roadmap.add_group("PC Engines apu2/apu3/apu6 v0.9.0")

pcengines.add_task("Validation", "2024-01-01", "2024-02-14", style="rounded", fill_colour="#34A853")
pcengines.add_task("DES Release", "2024-02-15", "2024-03-31", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer("Dasharo Community Support Roadmap | December 2023 (v0.4) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save("dcs_network_appliance_roadmap_v0.4_pt1.png")

roadmap = Roadmap(1600, 1000, colour_theme="dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Network Appliance Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-01-01", number_of_items=4)
roadmap.add_logo("../../img/dasharo_logo_white.png", "top-right", 140, 140)

protectli = roadmap.add_group("Protectli VP4670 v0.9.0")
protectli.add_task("Evaluation", "2024-01-01", "2024-02-14", style="rounded", fill_colour="#9B51E0")
protectli.add_task("Porting", "2024-02-15", "2024-03-31", style="rounded", fill_colour="#EA4335")
protectli.add_task("Validation", "2024-04-01", "2024-06-30", style="rounded", fill_colour="#34A853")
protectli.add_task("DES Release", "2024-07-01", "2024-09-30", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer("Dasharo Community Support Roadmap | December 2023 (v0.4) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save("dcs_network_appliance_roadmap_v0.4_pt2.png")

""""
Dasharo Community Support Laptops Roadmap
"""
roadmap = Roadmap(1600, 1000, colour_theme="dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Laptop Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-01-01", number_of_items=4)
roadmap.add_logo("../../img/dasharo_logo_white.png", "top-right", 140, 140)

novacustom = roadmap.add_group("Novacustom NV4x v0.9.0")
novacustom.add_task("Validation", "2024-01-01", "2024-02-14", style="rounded", fill_colour="#34A853")
novacustom.add_task("DES Release", "2024-02-15", "2024-03-31", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer("Dasharo Community Support Roadmap | December 2023 (v0.4) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save("dcs_laptop_roadmap_v0.4.png")

""""
Dasharo Community Support Desktop Roadmap
"""
roadmap = Roadmap(1600, 1000, colour_theme="dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Desktop Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-01-01", number_of_items=4)
roadmap.add_logo("../../img/dasharo_logo_white.png", "top-right", 140, 140)

lenovo = roadmap.add_group("Lenovo M920Q v0.9.0")
lenovo.add_task("Evaluation", "2024-01-01", "2024-02-14", style="rounded", fill_colour="#9B51E0")
lenovo.add_task("Porting", "2024-02-15", "2024-03-31", style="rounded", fill_colour="#EA4335")
lenovo.add_task("Validation", "2024-04-01", "2024-06-30", style="rounded", fill_colour="#34A853")
lenovo.add_task("DES Release", "2024-07-01", "2024-09-30", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer("Dasharo Community Support Roadmap | December 2023 (v0.4) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save("dcs_desktop_lenovo_roadmap_v0.4.png")

roadmap = Roadmap(1600, 1000, colour_theme="dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Desktop Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2024-01-01", number_of_items=4)
roadmap.add_logo("../../img/dasharo_logo_white.png", "top-right", 140, 140)

dell_optiplex = roadmap.add_group("Dell OptiPlex 7010/9010")
dell_optiplex.add_task("Validation", "2024-01-01", "2024-02-14", style="rounded", fill_colour="#34A853")
dell_optiplex.add_task("DES Release", "2024-02-15", "2024-03-31", style="rounded", fill_colour="#FD7E14")

dell_precision = roadmap.add_group("Dell Precision T1650")
dell_precision.add_task("Porting", "2024-01-01", "2024-03-31", style="rounded", fill_colour="#EA4335")
dell_precision.add_task("Validation", "2024-04-01", "2024-06-30", style="rounded", fill_colour="#34A853")
dell_precision.add_task("DES Release", "2024-07-01", "2024-09-30", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer("Dasharo Community Support Roadmap | December 2023 (v0.4) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save("dcs_desktop_dell_roadmap_v0.4.png")

roadmap = Roadmap(1600, 1000, colour_theme="dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Desktop Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2023-10-01", number_of_items=4)
roadmap.add_logo("../../img/dasharo_logo_white.png", "top-right", 140, 140)

msi_z690 = roadmap.add_group("MSI PRO Z690-A v1.1.3")
msi_z690.add_task("Validation", "2023-10-01", "2023-11-15", style="rounded", fill_colour="#34A853")
msi_z690.add_task("DES Release", "2023-11-16", "2023-12-31", style="rounded", fill_colour="#FD7E14")

msi_z690_dcr = roadmap.add_group("MSI PRO Z690-A v1.2.0")
msi_z690_dcr.add_task("Validation", "2024-01-01", "2024-03-31", style="rounded", fill_colour="#34A853")
msi_z690_dcr.add_task("Community Release", "2024-04-01", "2024-06-30", style="rounded", fill_colour="#ADD8E6")

roadmap.set_footer("Dasharo Community Support Roadmap | December 2023 (v0.4) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save("dcs_desktop_msi_z690_roadmap_v0.4.png")

roadmap = Roadmap(1600, 1000, colour_theme="dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Desktop Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2023-10-01", number_of_items=4)
roadmap.add_logo("../../img/dasharo_logo_white.png", "top-right", 140, 140)

msi_z790 = roadmap.add_group("MSI PRO Z790-P v0.9.1")
msi_z790.add_task("Validation", "2023-10-01", "2023-11-15", style="rounded", fill_colour="#34A853")
msi_z790.add_task("DES Release", "2023-11-16", "2023-12-31", style="rounded", fill_colour="#FD7E14")

msi_z790_dcr = roadmap.add_group("MSI PRO Z790-P v1.0.0")
msi_z790_dcr.add_task("Validation", "2024-01-01", "2024-03-31", style="rounded", fill_colour="#34A853")
msi_z790_dcr.add_task("Community Release", "2024-04-01", "2024-06-30", style="rounded", fill_colour="#ADD8E6")

roadmap.set_footer("Dasharo Community Support Roadmap | December 2023 (v0.4) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save("dcs_desktop_msi_z790_roadmap_v0.4.png")

roadmap = Roadmap(1600, 1000, colour_theme="dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Desktop Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2023-10-01", number_of_items=4)
roadmap.add_logo("../../img/dasharo_logo_white.png", "top-right", 140, 140)

msi_z790 = roadmap.add_group("MSI PRO Z790-P v0.9.0\n coreboot+Heads")
msi_z790.add_task("Porting", "2023-11-16", "2023-12-31", style="rounded", fill_colour="#EA4335")
msi_z790.add_task("Validation", "2024-01-01", "2024-02-14", style="rounded", fill_colour="#34A853")
msi_z790.add_task("DES Release", "2024-02-15", "2024-03-31", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer("Dasharo Community Support Roadmap | December 2023 (v0.4) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save("dcs_desktop_msi_z790_heads_roadmap_v0.4.png")

roadmap = Roadmap(1600, 1000, colour_theme="dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Desktop Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2023-10-01", number_of_items=4)
roadmap.add_logo("../../img/dasharo_logo_white.png", "top-right", 140, 140)

asrock = roadmap.add_group("ASRock X370 Killer SLI/ac")
asrock.add_task("Porting", "2023-10-01", "2024-02-14", style="rounded", fill_colour="#EA4335")
asrock.add_task("Validation", "2024-02-15", "2024-03-31", style="rounded", fill_colour="#34A853")
asrock.add_task("DES Release", "2024-04-01", "2024-06-30", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer("Dasharo Community Support Roadmap | December 2023 (v0.4) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save("dcs_desktop_asrock_roadmap_v0.4.png")

roadmap = Roadmap(1600, 1000, colour_theme="dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Workstation Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2023-10-01", number_of_items=4)
roadmap.add_logo("../../img/dasharo_logo_white.png", "top-right", 140, 140)

asus = roadmap.add_group("ASUS KGPE-D16 v0.5.0")
asus.add_task("Validation", "2024-04-01", "2024-06-30", style="rounded", fill_colour="#34A853")
asus.add_task("DES Release", "2024-07-01", "2024-09-30", style="rounded", fill_colour="#FD7E14")

rcs = roadmap.add_group("Raptor CS Talos II v0.8.0")
rcs.add_task("Validation", "2024-01-01", "2024-02-14", style="rounded", fill_colour="#34A853")
rcs.add_task("DES Release", "2024-02-15", "2024-03-30", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer("Dasharo Community Support Roadmap | December 2023 (v0.4) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save("dcs_workstation_roadmap_v0.4.png")

roadmap = Roadmap(1600, 1000, colour_theme="dasharo.json", show_marker=False)
roadmap.set_title("Dasharo Server Roadmap")
roadmap.set_subtitle("subject to change")
roadmap.set_timeline(TimelineMode.QUARTERLY, start="2023-10-01", number_of_items=4)
roadmap.add_logo("../../img/dasharo_logo_white.png", "top-right", 140, 140)

smc = roadmap.add_group("Supermicro X11SSH-TF v0.1.0")
smc.add_task("Validation", "2024-01-01", "2024-03-31", style="rounded", fill_colour="#34A853")
smc.add_task("DES Release", "2024-04-01", "2024-06-30", style="rounded", fill_colour="#FD7E14")

roadmap.set_footer("Dasharo Community Support Roadmap | December 2023 (v0.4) | CC-BY-SA-4.0")
roadmap.draw()
roadmap.save("dcs_server_roadmap_v0.4.png")
