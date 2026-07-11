"""Parametric STEP assembly for a heavy-lift amphibious hybrid hexacopter.

Units: millimeters. Origin is the vehicle center of gravity on the XY plane,
with +Z upward through the central power stack.
"""

from math import cos, radians, sin

from build123d import *


ARM_COUNT = 6
ARM_LENGTH = 650.0
ARM_OD = 42.0
PROP_DIAMETER = 711.0  # 28 inches
MOTOR_RADIUS = 48.0
MOTOR_HEIGHT = 58.0

HUB_RADIUS = 155.0
HUB_HEIGHT = 44.0

ENGINE_Z = 325.0
FIREWALL_Z = 225.0
AVIONICS_Z = 145.0
TANK_Z = 42.0
PUMP_Z = -55.0


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
        labeled(Pos(motor_x, motor_y, 108) * Cylinder(MOTOR_RADIUS, MOTOR_HEIGHT, align=(Align.CENTER, Align.CENTER, Align.CENTER)), f"industrial_brushless_motor_{idx}"),
        labeled(Pos(motor_x, motor_y, 150) * Cylinder(30, 18, align=(Align.CENTER, Align.CENTER, Align.CENTER)), f"propeller_hub_{idx}"),
    ]
    blade_len = PROP_DIAMETER / 2.0
    blade_width_root = 54.0
    blade_width_tip = 30.0
    blade_thickness = 5.0
    for side, suffix in [(1, "a"), (-1, "b")]:
        blade = Box(blade_len, blade_width_root, blade_thickness, align=(Align.MIN, Align.CENTER, Align.CENTER))
        tip = Pos(blade_len * 0.78, 0, 0) * Box(blade_len * 0.22, blade_width_tip, blade_thickness, align=(Align.MIN, Align.CENTER, Align.CENTER))
        parts.append(
            labeled(
                Pos(motor_x, motor_y, 162) * Rot(0, 0, angle_deg + (0 if side == 1 else 180)) * (blade + tip),
                f"28in_carbon_propeller_blade_{idx}_{suffix}",
            )
        )
    return parts


def make_pontoons():
    parts = []
    for side, y in [("left", -310.0), ("right", 310.0)]:
        parts.extend(
            [
                labeled(Pos(0, y, -160) * Box(1040, 145, 70, align=(Align.CENTER, Align.CENTER, Align.CENTER)), f"{side}_carbon_fiber_flotation_pontoon_main_hull"),
                labeled(Pos(-75, y, -112) * Box(900, 118, 34, align=(Align.CENTER, Align.CENTER, Align.CENTER)), f"{side}_aerodynamic_curved_top_fairing_envelope"),
                labeled(Pos(18, y, -205) * Box(300, 145, 28, align=(Align.CENTER, Align.CENTER, Align.CENTER)), f"{side}_stepped_hull_break_step_behind_cog"),
                labeled(Pos(370, y, -205) * Box(160, 105, 46, align=(Align.CENTER, Align.CENTER, Align.CENTER)), f"{side}_rear_hydrodynamic_planing_pad"),
                labeled(Pos(-380, y, -117) * Rot(0, 90, 0) * Cylinder(18, 210, align=(Align.CENTER, Align.CENTER, Align.CENTER)), f"{side}_front_cross_tube_mount"),
                labeled(Pos(380, y, -117) * Rot(0, 90, 0) * Cylinder(18, 210, align=(Align.CENTER, Align.CENTER, Align.CENTER)), f"{side}_rear_cross_tube_mount"),
            ]
        )
    parts.extend(
        [
            labeled(Pos(0, 0, -118) * Rot(90, 0, 0) * Cylinder(18, 760, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "front_pontoon_spreader_tube"),
            labeled(Pos(360, 0, -118) * Rot(90, 0, 0) * Cylinder(18, 760, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "rear_pontoon_spreader_tube"),
            labeled(Pos(-420, -310, -225) * Box(88, 100, 42, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "dual_stage_marine_filter_pump_mesh_screen"),
            labeled(Pos(-310, -310, -206) * Rot(0, 90, 0) * Cylinder(18, 170, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "inline_one_way_check_valve_to_tank"),
        ]
    )
    return parts


def make_central_stack():
    parts = [
        cyl_z(HUB_RADIUS, HUB_HEIGHT, 92, "cnc_aluminum_hexagonal_center_hub_envelope"),
        cyl_z(118, 86, ENGINE_Z, "5kw_6kw_gas_electric_generator_engine"),
        labeled(Pos(0, 0, ENGINE_Z + 28) * Cylinder(142, 38, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "forced_air_cooling_shroud_and_fin_duct"),
        labeled(Pos(-72, 0, ENGINE_Z + 86) * Rot(0, -28, 0) * Cylinder(22, 140, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "upward_snorkel_air_intake_with_splash_guard"),
        labeled(Pos(110, -55, ENGINE_Z + 45) * Rot(0, 62, -28) * Cylinder(13, 190, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "upward_outward_exhaust_pipe"),
        cyl_z(168, 18, FIREWALL_Z, "solid_cnc_aluminum_firewall_faraday_cage"),
        labeled(Pos(0, 0, AVIONICS_Z) * Box(260, 210, 80, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "sealed_waterproof_avionics_bay"),
        labeled(Pos(-82, 0, AVIONICS_Z) * Box(78, 190, 34, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "isolated_dry_drawer_lipo_tray_left"),
        labeled(Pos(82, 0, AVIONICS_Z) * Box(78, 190, 34, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "isolated_dry_drawer_lipo_tray_right"),
        labeled(Pos(0, 0, TANK_Z) * Box(520, 380, 92, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "low_profile_5_gallon_composite_water_tank_at_cog"),
        labeled(Pos(0, 0, PUMP_Z) * Box(190, 105, 58, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "agricultural_diaphragm_pressure_pump_below_tank"),
    ]
    for x in [-170, -85, 0, 85, 170]:
        parts.append(labeled(Pos(x, 0, TANK_Z + 52) * Box(8, 350, 42, align=(Align.CENTER, Align.CENTER, Align.CENTER)), f"tank_longitudinal_baffle_x_{int(x)}"))
    for y in [-120, -40, 40, 120]:
        parts.append(labeled(Pos(0, y, TANK_Z + 53) * Box(480, 8, 40, align=(Align.CENTER, Align.CENTER, Align.CENTER)), f"tank_lateral_baffle_y_{int(y)}"))
    return parts


def make_spray_system(angle_deg, idx):
    parts = [
        arm_cylinder(angle_deg, 8.0, ARM_LENGTH - 90, -14.0, f"under_arm_high_pressure_fluid_line_{idx}"),
        radial_box(angle_deg, ARM_LENGTH * 0.72, 0, -55, 42, 24, 20, f"electronic_solenoid_valve_{idx}"),
        labeled(
            Pos(cos(radians(angle_deg)) * (ARM_LENGTH * 0.82), sin(radians(angle_deg)) * (ARM_LENGTH * 0.82), -82)
            * Rot(0, 0, angle_deg)
            * Cylinder(16, 28, align=(Align.CENTER, Align.CENTER, Align.CENTER)),
            f"downwash_aligned_atomizing_spray_nozzle_{idx}",
        ),
    ]
    return parts


def make_mast():
    return [
        labeled(Pos(0, 0, 500) * Cylinder(16, 380, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "15in_carbon_fiber_antenna_mast"),
        labeled(Pos(-55, 0, 715) * Cylinder(42, 16, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "rtk_gnss_antenna_left_high_above_emi"),
        labeled(Pos(55, 0, 715) * Cylinder(42, 16, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "gps_telemetry_antenna_right_high_above_emi"),
        labeled(Pos(0, 0, 690) * Box(150, 18, 16, align=(Align.CENTER, Align.CENTER, Align.CENTER)), "antenna_crossbar_far_from_ignition_coil"),
    ]


def gen_step():
    parts = []
    parts.extend(make_central_stack())
    parts.extend(make_pontoons())
    parts.extend(make_mast())

    for i in range(ARM_COUNT):
        angle = i * 60.0
        parts.append(arm_cylinder(angle, ARM_OD / 2.0, ARM_LENGTH, 108, f"hollow_carbon_fiber_boom_arm_internal_wiring_{i + 1}"))
        parts.append(radial_box(angle, 260, 0, 108, 120, 66, 26, f"arm_root_clamp_cnc_aluminum_{i + 1}"))
        parts.append(radial_box(angle, ARM_LENGTH - 60, 0, 108, 128, 82, 22, f"motor_mount_plate_{i + 1}"))
        parts.extend(make_propeller(angle, i + 1))
        parts.extend(make_spray_system(angle, i + 1))

    return Compound(children=parts, label="amphibious_gas_electric_agricultural_hexacopter")


if __name__ == "__main__":
    from build123d import export_step

    export_step(gen_step(), "amphibious_hybrid_hexacopter.step")
