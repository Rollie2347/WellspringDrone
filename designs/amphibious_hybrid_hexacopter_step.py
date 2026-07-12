"""Parametric STEP assembly for a heavy-lift amphibious hybrid hexacopter.

Units: millimeters. Origin is the vehicle center of gravity on the XY plane,
with +Z upward through the central power stack.
"""

from math import cos, radians, sin

from build123d import *


# ---- Airframe ----
ARM_COUNT = 6
ARM_LENGTH = 760.0  # must exceed PROP_DIAMETER (hexagon: adjacent motor spacing == ARM_LENGTH)
ARM_OD = 42.0
ARM_Z = 108.0  # shared Z height for arm booms, motors, motor mounts, and the spray line's arm segment
PROP_DIAMETER = 711.0  # 28 inches
MOTOR_RADIUS = 48.0
MOTOR_HEIGHT = 58.0

HUB_RADIUS = 155.0
HUB_HEIGHT = 44.0
HUB_Z = 92.0

# ---- Central power stack (Z heights) ----
ENGINE_Z = 325.0
FIREWALL_Z = 225.0
AVIONICS_Z = 145.0
TANK_Z = 42.0
PUMP_Z = -55.0

# ---- Propeller geometry ----
PROP_HUB_RADIUS = 30.0
PROP_HUB_HEIGHT = 18.0
PROP_HUB_Z = 150.0
BLADE_Z = 162.0
BLADE_WIDTH_ROOT = 54.0
BLADE_WIDTH_TIP = 30.0
BLADE_THICKNESS = 5.0
BLADE_TIP_START_FRACTION = 0.78
BLADE_TIP_LENGTH_FRACTION = 0.22

# ---- Arm hardware ----
ARM_ROOT_CLAMP_X = 260.0
ARM_ROOT_CLAMP_SIZE = (120.0, 66.0, 26.0)
MOTOR_MOUNT_X_INSET = 60.0  # motor mount plate sits at ARM_LENGTH - this
MOTOR_MOUNT_SIZE = (128.0, 82.0, 22.0)

# ---- Pontoons ----
PONTOON_Y = 310.0
PONTOON_Z = -160.0
PONTOON_HULL_SIZE = (1040.0, 145.0, 70.0)
FAIRING_X = -75.0
FAIRING_Z = -112.0
FAIRING_SIZE = (900.0, 118.0, 34.0)
HULL_STEP_X = 18.0
HULL_STEP_Z = -205.0
HULL_STEP_SIZE = (300.0, 145.0, 28.0)
PLANING_PAD_X = 370.0
PLANING_PAD_SIZE = (160.0, 105.0, 46.0)
CROSS_TUBE_FRONT_X = -380.0
CROSS_TUBE_REAR_X = 380.0
CROSS_TUBE_Z = -117.0
CROSS_TUBE_RADIUS = 18.0
CROSS_TUBE_LENGTH = 210.0
SPREADER_FRONT_X = 0.0
SPREADER_REAR_X = 360.0
SPREADER_Z = -118.0
SPREADER_RADIUS = 18.0
SPREADER_LENGTH = 760.0
FILTER_SCREEN_POS = (-420.0, -310.0, -225.0)
FILTER_SCREEN_SIZE = (88.0, 100.0, 42.0)
CHECK_VALVE_POS = (-310.0, -310.0, -206.0)
CHECK_VALVE_RADIUS = 18.0
CHECK_VALVE_LENGTH = 170.0

# ---- Central stack detail ----
ENGINE_RADIUS = 118.0
ENGINE_HEIGHT = 86.0
COOLING_SHROUD_Z_OFFSET = 28.0  # relative to ENGINE_Z
COOLING_SHROUD_RADIUS = 142.0
COOLING_SHROUD_HEIGHT = 38.0
SNORKEL_POS_OFFSET = (-72.0, 0.0, 86.0)  # x, y, z-relative-to-ENGINE_Z
SNORKEL_ROT = (0.0, -28.0, 0.0)
SNORKEL_RADIUS = 22.0
SNORKEL_LENGTH = 140.0
EXHAUST_POS_OFFSET = (110.0, -55.0, 45.0)  # x, y, z-relative-to-ENGINE_Z
EXHAUST_ROT = (0.0, 62.0, -28.0)
EXHAUST_RADIUS = 13.0
EXHAUST_LENGTH = 190.0
FIREWALL_RADIUS = 168.0
FIREWALL_HEIGHT = 18.0
AVIONICS_BAY_SIZE = (260.0, 210.0, 80.0)
LIPO_TRAY_X = 82.0
LIPO_TRAY_SIZE = (78.0, 190.0, 34.0)
TANK_SIZE = (520.0, 380.0, 92.0)
PUMP_SIZE = (190.0, 105.0, 58.0)
TANK_BAFFLE_X_POSITIONS = [-170.0, -85.0, 0.0, 85.0, 170.0]
TANK_BAFFLE_LONG_Z_OFFSET = 52.0  # relative to TANK_Z
TANK_BAFFLE_LONG_SIZE = (8.0, 350.0, 42.0)
TANK_BAFFLE_Y_POSITIONS = [-120.0, -40.0, 40.0, 120.0]
TANK_BAFFLE_LAT_Z_OFFSET = 53.0  # relative to TANK_Z
TANK_BAFFLE_LAT_SIZE = (480.0, 8.0, 40.0)

# ---- Spray system ----
SPRAY_LINE_RADIUS = 8.0
SPRAY_LINE_LENGTH_INSET = 90.0  # arm_cylinder length = ARM_LENGTH - this
SPRAY_LINE_Z = -14.0
VALVE_X_FRACTION = 0.72  # fraction of ARM_LENGTH
VALVE_Z = -55.0
VALVE_SIZE = (42.0, 24.0, 20.0)
NOZZLE_X_FRACTION = 0.82  # fraction of ARM_LENGTH
NOZZLE_Z = -82.0
NOZZLE_RADIUS = 16.0
NOZZLE_HEIGHT = 28.0

# ---- Mast ----
MAST_Z = 500.0
MAST_RADIUS = 16.0
MAST_HEIGHT = 380.0
ANTENNA_X = 55.0
ANTENNA_Z = 715.0
ANTENNA_RADIUS = 42.0
ANTENNA_HEIGHT = 16.0
CROSSBAR_Z = 690.0
CROSSBAR_SIZE = (150.0, 18.0, 16.0)


def labeled(shape, name):
    shape.label = name
    return shape


def cyl_z(radius, height, z, name):
    return labeled(Pos(0, 0, z) * Cylinder(radius, height, align=(Align.CENTER, Align.CENTER, Align.CENTER)), name)


def arm_cylinder(angle_deg, radius, length, z, name):
    mid = length / 2.0
    x = cos(radians(angle_deg)) * mid
    y = sin(radians(angle_deg)) * mid
    return labeled(Pos(x, y, z) * Rot(0, 90, angle_deg) * Cylinder(radius, length, align=(Align.CENTER, Align.CENTER, Align.CENTER)), name)


def radial_box(angle_deg, x_from_center, y_offset, z, sx, sy, sz, name):
    x = cos(radians(angle_deg)) * x_from_center - sin(radians(angle_deg)) * y_offset
    y = sin(radians(angle_deg)) * x_from_center + cos(radians(angle_deg)) * y_offset
    return labeled(Pos(x, y, z) * Rot(0, 0, angle_deg) * Box(sx, sy, sz, align=(Align.CENTER, Align.CENTER, Align.CENTER)), name)


def make_propeller(angle_deg, idx):
    motor_x = cos(radians(angle_deg)) * ARM_LENGTH
    motor_y = sin(radians(angle_deg)) * ARM_LENGTH
    parts = [
        labeled(Pos(motor_x, motor_y, ARM_Z) * Cylinder(MOTOR_RADIUS, MOTOR_HEIGHT, align=(Align.CENTER, Align.CENTER, Align.CENTER)), f"industrial_brushless_motor_{idx}"),
        labeled(Pos(motor_x, motor_y, PROP_HUB_Z) * Cylinder(PROP_HUB_RADIUS, PROP_HUB_HEIGHT, align=(Align.CENTER, Align.CENTER, Align.CENTER)), f"propeller_hub_{idx}"),
    ]
    blade_len = PROP_DIAMETER / 2.0
    for side, suffix in [(1, "a"), (-1, "b")]:
        blade = Box(blade_len, BLADE_WIDTH_ROOT, BLADE_THICKNESS, align=(Align.MIN, Align.CENTER, Align.CENTER))
        tip = Pos(blade_len * BLADE_TIP_START_FRACTION, 0, 0) * Box(blade_len * BLADE_TIP_LENGTH_FRACTION, BLADE_WIDTH_TIP, BLADE_THICKNESS, align=(Align.MIN, Align.CENTER, Align.CENTER))
        parts.append(
            labeled(
                Pos(motor_x, motor_y, BLADE_Z) * Rot(0, 0, angle_deg + (0 if side == 1 else 180)) * (blade + tip),
                f"28in_carbon_propeller_blade_{idx}_{suffix}",
            )
        )
    return parts


def make_pontoons():
    parts = []
    for side, y in [("left", -PONTOON_Y), ("right", PONTOON_Y)]:
        parts.extend(
            [
                labeled(Pos(0, y, PONTOON_Z) * Box(*PONTOON_HULL_SIZE, align=(Align.CENTER, Align.CENTER, Align.CENTER)), f"{side}_carbon_fiber_flotation_pontoon_main_hull"),
                labeled(Pos(FAIRING_X, y, FAIRING_Z) * Box(*FAIRING_SIZE, align=(Align.CENTER, Align.CENTER, Align.CENTER)), f"{side}_aerodynamic_curved_top_fairing_envelope"),
                labeled(Pos(HULL_STEP_X, y, HULL_STEP_Z) * Box(*HULL_STEP_SIZE, align=(Align.CENTER, Align.CENTER, Align.CENTER)), f"{side}_stepped_hull_break_step_behind_cog"),
                labeled(Pos(PLANING_PAD_X, y, HULL_STEP_Z) * Box(*PLANING_PAD_SIZE, align=(Align.CENTER, Align.CENTER, Align.CENTER)), f"{side}_rear_hydrodynamic_planing_pad"),
                labeled(Pos(CROSS_TUBE_FRONT_X, y, CROSS_TUBE_Z) * Rot(0, 90, 0) * Cylinder(CROSS_TUBE_RADIUS, CROSS_TUBE_LENGTH, align=(Align.CENTER, Align.CENTER, Align.CENTER)), f"{side}_front_cross_tube_mount"),
                labeled(Pos(CROSS_TUBE_REAR_X, y, CROSS_TUBE_Z) * Rot(0, 90, 0) * Cylinder(CROSS_TUBE_RADIUS, CROSS_TUBE_LENGTH, align=(Align.CENTER, Align.CENTER, Align.CENTER)), f"{side}_rear_cross_tube_mount"),
            ]
        )
    parts.extend(
        [
            labeled(Pos(SPREADER_FRONT_X, 0, SPREADER_Z) * Rot(90, 0, 0) * Cylinder(SPREADER_RADIUS, SPREADER_LENGTH, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "front_pontoon_spreader_tube"),
            labeled(Pos(SPREADER_REAR_X, 0, SPREADER_Z) * Rot(90, 0, 0) * Cylinder(SPREADER_RADIUS, SPREADER_LENGTH, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "rear_pontoon_spreader_tube"),
            labeled(Pos(*FILTER_SCREEN_POS) * Box(*FILTER_SCREEN_SIZE, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "dual_stage_marine_filter_pump_mesh_screen"),
            labeled(Pos(*CHECK_VALVE_POS) * Rot(0, 90, 0) * Cylinder(CHECK_VALVE_RADIUS, CHECK_VALVE_LENGTH, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "inline_one_way_check_valve_to_tank"),
        ]
    )
    return parts


def make_central_stack():
    parts = [
        cyl_z(HUB_RADIUS, HUB_HEIGHT, HUB_Z, "cnc_aluminum_hexagonal_center_hub_envelope"),
        cyl_z(ENGINE_RADIUS, ENGINE_HEIGHT, ENGINE_Z, "5kw_6kw_gas_electric_generator_engine"),
        labeled(Pos(0, 0, ENGINE_Z + COOLING_SHROUD_Z_OFFSET) * Cylinder(COOLING_SHROUD_RADIUS, COOLING_SHROUD_HEIGHT, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "forced_air_cooling_shroud_and_fin_duct"),
        labeled(
            Pos(SNORKEL_POS_OFFSET[0], SNORKEL_POS_OFFSET[1], ENGINE_Z + SNORKEL_POS_OFFSET[2]) * Rot(*SNORKEL_ROT) * Cylinder(SNORKEL_RADIUS, SNORKEL_LENGTH, align=(Align.CENTER, Align.CENTER, Align.CENTER)),
            "upward_snorkel_air_intake_with_splash_guard",
        ),
        labeled(
            Pos(EXHAUST_POS_OFFSET[0], EXHAUST_POS_OFFSET[1], ENGINE_Z + EXHAUST_POS_OFFSET[2]) * Rot(*EXHAUST_ROT) * Cylinder(EXHAUST_RADIUS, EXHAUST_LENGTH, align=(Align.CENTER, Align.CENTER, Align.CENTER)),
            "upward_outward_exhaust_pipe",
        ),
        cyl_z(FIREWALL_RADIUS, FIREWALL_HEIGHT, FIREWALL_Z, "solid_cnc_aluminum_firewall_faraday_cage"),
        labeled(Pos(0, 0, AVIONICS_Z) * Box(*AVIONICS_BAY_SIZE, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "sealed_waterproof_avionics_bay"),
        labeled(Pos(-LIPO_TRAY_X, 0, AVIONICS_Z) * Box(*LIPO_TRAY_SIZE, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "isolated_dry_drawer_lipo_tray_left"),
        labeled(Pos(LIPO_TRAY_X, 0, AVIONICS_Z) * Box(*LIPO_TRAY_SIZE, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "isolated_dry_drawer_lipo_tray_right"),
        labeled(Pos(0, 0, TANK_Z) * Box(*TANK_SIZE, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "low_profile_5_gallon_composite_water_tank_at_cog"),
        labeled(Pos(0, 0, PUMP_Z) * Box(*PUMP_SIZE, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "agricultural_diaphragm_pressure_pump_below_tank"),
    ]
    for x in TANK_BAFFLE_X_POSITIONS:
        parts.append(labeled(Pos(x, 0, TANK_Z + TANK_BAFFLE_LONG_Z_OFFSET) * Box(*TANK_BAFFLE_LONG_SIZE, align=(Align.CENTER, Align.CENTER, Align.CENTER)), f"tank_longitudinal_baffle_x_{int(x)}"))
    for y in TANK_BAFFLE_Y_POSITIONS:
        parts.append(labeled(Pos(0, y, TANK_Z + TANK_BAFFLE_LAT_Z_OFFSET) * Box(*TANK_BAFFLE_LAT_SIZE, align=(Align.CENTER, Align.CENTER, Align.CENTER)), f"tank_lateral_baffle_y_{int(y)}"))
    return parts


def make_spray_system(angle_deg, idx):
    parts = [
        arm_cylinder(angle_deg, SPRAY_LINE_RADIUS, ARM_LENGTH - SPRAY_LINE_LENGTH_INSET, SPRAY_LINE_Z, f"under_arm_high_pressure_fluid_line_{idx}"),
        radial_box(angle_deg, ARM_LENGTH * VALVE_X_FRACTION, 0, VALVE_Z, *VALVE_SIZE, f"electronic_solenoid_valve_{idx}"),
        labeled(
            Pos(cos(radians(angle_deg)) * (ARM_LENGTH * NOZZLE_X_FRACTION), sin(radians(angle_deg)) * (ARM_LENGTH * NOZZLE_X_FRACTION), NOZZLE_Z)
            * Rot(0, 0, angle_deg)
            * Cylinder(NOZZLE_RADIUS, NOZZLE_HEIGHT, align=(Align.CENTER, Align.CENTER, Align.CENTER)),
            f"downwash_aligned_atomizing_spray_nozzle_{idx}",
        ),
    ]
    return parts


def make_mast():
    return [
        labeled(Pos(0, 0, MAST_Z) * Cylinder(MAST_RADIUS, MAST_HEIGHT, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "15in_carbon_fiber_antenna_mast"),
        labeled(Pos(-ANTENNA_X, 0, ANTENNA_Z) * Cylinder(ANTENNA_RADIUS, ANTENNA_HEIGHT, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "rtk_gnss_antenna_left_high_above_emi"),
        labeled(Pos(ANTENNA_X, 0, ANTENNA_Z) * Cylinder(ANTENNA_RADIUS, ANTENNA_HEIGHT, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "gps_telemetry_antenna_right_high_above_emi"),
        labeled(Pos(0, 0, CROSSBAR_Z) * Box(*CROSSBAR_SIZE, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "antenna_crossbar_far_from_ignition_coil"),
    ]


def gen_step():
    parts = []
    parts.extend(make_central_stack())
    parts.extend(make_pontoons())
    parts.extend(make_mast())

    for i in range(ARM_COUNT):
        angle = i * (360.0 / ARM_COUNT)
        parts.append(arm_cylinder(angle, ARM_OD / 2.0, ARM_LENGTH, ARM_Z, f"hollow_carbon_fiber_boom_arm_internal_wiring_{i + 1}"))
        parts.append(radial_box(angle, ARM_ROOT_CLAMP_X, 0, ARM_Z, *ARM_ROOT_CLAMP_SIZE, f"arm_root_clamp_cnc_aluminum_{i + 1}"))
        parts.append(radial_box(angle, ARM_LENGTH - MOTOR_MOUNT_X_INSET, 0, ARM_Z, *MOTOR_MOUNT_SIZE, f"motor_mount_plate_{i + 1}"))
        parts.extend(make_propeller(angle, i + 1))
        parts.extend(make_spray_system(angle, i + 1))

    return Compound(children=parts, label="amphibious_gas_electric_agricultural_hexacopter")


def sanity_check(assembly):
    """Cheap geometry regression guards. Returns a list of warning strings (empty if clean)."""
    warnings = []

    bbox = assembly.bounding_box()
    span_x = bbox.max.X - bbox.min.X
    span_y = bbox.max.Y - bbox.min.Y
    span_z = bbox.max.Z - bbox.min.Z

    max_radial_reach = ARM_LENGTH + PROP_DIAMETER / 2.0
    max_plan_span = 2.0 * max_radial_reach * 1.05  # 5% margin

    if span_x > max_plan_span or span_y > max_plan_span:
        warnings.append(
            f"assembly footprint {span_x:.0f}x{span_y:.0f}mm exceeds the expected rotor-disk "
            f"envelope of {max_plan_span:.0f}mm - check for a mis-placed part"
        )
    if span_x < max_radial_reach or span_y < max_radial_reach:
        warnings.append(
            f"assembly footprint {span_x:.0f}x{span_y:.0f}mm is far smaller than the rotor "
            f"layout implies - parts may have collapsed onto the origin"
        )
    # Empirically ~969mm tall (pontoon bottom to mast top) as of this design; generous margin
    # so future mast/antenna tuning doesn't require re-deriving this bound by hand.
    if span_z > 1400.0:
        warnings.append(f"assembly height {span_z:.0f}mm exceeds the plausible envelope")

    adjacent_motor_spacing = 2.0 * ARM_LENGTH * sin(radians(180.0 / ARM_COUNT))
    if adjacent_motor_spacing < PROP_DIAMETER:
        warnings.append(
            f"adjacent rotor disks overlap by {PROP_DIAMETER - adjacent_motor_spacing:.0f}mm: "
            f"motor spacing {adjacent_motor_spacing:.0f}mm < prop diameter {PROP_DIAMETER:.0f}mm "
            f"(ARM_LENGTH vs PROP_DIAMETER mismatch)"
        )

    return warnings


if __name__ == "__main__":
    from build123d import export_step

    assembly = gen_step()
    for warning in sanity_check(assembly):
        print(f"WARNING: {warning}")
    export_step(assembly, "amphibious_hybrid_hexacopter.step")
