# Amphibious Hybrid Hexacopter CAD Package

Primary file for Fusion 360:

- `amphibious_hybrid_hexacopter.step`

Source generator:

- `amphibious_hybrid_hexacopter_step.py`

Snapshot:

- `snapshots/amphibious_hybrid_hexacopter_iso_20260708T055146Z.png`

## Modeling Notes

- Units are millimeters.
- Origin is the estimated loaded center of gravity at the center of the water tank footprint.
- The model is a STEP-first engineering concept assembly, not a certified manufacturing design.
- Exact vendor part numbers were not provided, so motors, generator, avionics, pumps, valves, and antennas are modeled as labeled dimensional envelopes.
- Fusion 360 should import the STEP as an editable multi-body/assembly-style CAD file.

## Included Subsystems

- Six hollow carbon-fiber boom arms with internal wiring intent.
- Six motor pods with 28 inch propeller envelopes.
- Central gas-electric generator, cooling shroud, snorkel, exhaust, firewall/Faraday cage, avionics bay, LiPo trays, low-profile baffled tank, and pressure pump.
- Dual flotation pontoons with aerodynamic top fairings, stepped hull features, pump intake, mesh screen, and check valve.
- Under-arm high-pressure plumbing, six solenoid valves, and six downward spray nozzles aligned with propeller downwash.
- Elevated mast with dual RTK/GNSS and telemetry antenna envelopes.
