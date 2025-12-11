<center><img src="/slides/img/dug_12/docs_naming_convention.png" width="510">

<br>

#### https://docs.dasharo.com/dasharo-naming-convention/

</center>

<!--

Dasharo Product Naming Convention v2 - Released October 30, 2025

This is a major update to how Dasharo firmware packages are named, following
RFC feedback from the community. The new naming convention helps users quickly
identify the right firmware package for their needs.

Key improvements:
- Clearer framework specification (coreboot, UEFI, Slim Bootloader)
- Optional payload indication (UEFI, SeaBIOS, Heads, U-Boot)
- Edition codes standardized: Community (DCP), Pro (DPP), Enterprise (DEP)
- Release tiers defined: Rapid, Assured, LTS with specific QA scope
- Consistent platform naming following supported hardware list

Examples:
- "Dasharo (coreboot+UEFI) Pro Release for NovaCustom NV4x"
- "Dasharo (UEFI) Community Release for MSI Z690-A"

This makes it much easier for users to understand what's included in each
firmware package and select the appropriate edition and release tier for their
use case.

-->

---

<center><img src="/slides/img/dug_12/docs_hcl_external.png" width="520">

<br>

#### https://docs.dasharo.com/dasharo-tools-suite/documentation/features/#hcl-report-using-an-external-firmware-binary

</center>

<!--

HCL Report Using an External Firmware Binary - Added in DTS v2.7.2+

This innovative feature solves a critical limitation: proprietary firmware
that blocks internal flash reading. Now users can still generate complete
Hardware Compatibility List (HCL) reports!

The Problem:
- Stock/proprietary firmware often prevents internal programmer access
- Without flash dump, HCL reports are incomplete
- Missing firmware backup and automated analysis data
- Limited hardware compatibility validation

The Solution:
- Users provide firmware binary via external programmer or BMC
- Copy to /firmware/external/ directory
- DTS automatically uses it for complete HCL generation
- Works with SCP, flash drive, or network transfer

Why This Matters:
- Enables HCL reports on locked-down systems
- Critical for pre-Dasharo platform evaluation
- Helps assess compatibility before purchasing
- Supports enterprise evaluation workflows
- Works around vendor restrictions

Use Cases:
- Evaluating new hardware before Dasharo port
- Generating HCL on systems with protected firmware
- OEM evaluation and compatibility testing
- Pre-sale hardware validation

This feature demonstrates Dasharo's commitment to hardware compatibility
transparency, even on systems with restrictive firmware.

-->

---

<center><img src="/slides/img/dug_12/docs_ibg_validator.png" width="550">

<br>

#### https://docs.dasharo.com/dasharo-tools-suite/documentation/features/#intel-boot-guard-ibg-key-validator

</center>

<!--

Intel Boot Guard (IBG) Key Validator - Added December 5, 2025

The IBG Key Validator is a security-focused tool added to Dasharo Tools Suite
to help users verify Intel Boot Guard configuration and key integrity.

What it does:
- Validates Intel Boot Guard key material
- Verifies Boot Guard configuration correctness
- Helps detect potential Boot Guard misconfigurations
- Assists with secure boot provisioning
- Supports security auditing and compliance

Why it matters:
- Intel Boot Guard is a critical hardware root of trust
- Misconfigured Boot Guard can brick devices or create security gaps
- Validation before deployment prevents costly mistakes
- Essential for security-conscious deployments
- Helps meet compliance requirements

This tool fills an important gap in Boot Guard deployment workflows, giving
users confidence that their hardware root of trust is properly configured
before production deployment.

-->

---

<figure>
  <img src="/slides/img/dug_12/3mdeb_lite.png" width="450px">
</figure>

<br>

<center>

### https://www.youtube.com/@3mdebLite

</center>
