"""v1 pump + valve mount bracket -- build123d source for the locked v1 BOM in CLAUDE.md.

Mounts the diaphragm pump and 2 solenoid valves onto a single Tarot X6 1000mm hex frame (TL6X001) arm
tube. Kept separate from v1/cad/tank_mount_bracket_step.py (which carries the heavier tank load on its
own two-tube clamp) so each printed part stays small and simple -- this one is light enough for a single
clamp point.

Frame interface and envelope-not-exact-fit rationale: see the docstring in tank_mount_bracket_step.py,
same reasoning applies here (search-derived arm tube OD, unresolved pump/valve vendor dimensions per
v1/BUY_LIST.md). The pump pad uses elongated slots (not fixed holes) and the valve clips are open rings
secured with a zip-tie through the gap, both sized to a generous plausible envelope.

Coordinate system: origin at the plate's center, top face at Z=0. Plate extends down (-Z) into the arm
clamp and up (+Z) into the pump pad and valve clips. Arm clamp axis runs along X (matching the frame
tube direction); valve clip axis runs along Y (matching the valve body's long axis).
"""

from build123d import *

import math

# --- Frame interface (Tarot X6 1000mm hex, TL6X001) -- see tank_mount_bracket_step.py for sourcing ---
ARM_TUBE_OD_MM = 25.0
ARM_TUBE_CLEARANCE_MM = 1.5
ARM_CLAMP_WALL_MM = 3.0
ARM_CLAMP_LENGTH_MM = 30.0
ARM_CLAMP_GAP_DEG = 100.0
ARM_CLAMP_OVERLAP_MM = 1.5  # push the clamp up into the deck so the two solids share real volume

# --- Pump pad (adjustable slotted mount, not exact-fit) ---
PUMP_PAD_LENGTH_MM = 90.0
PUMP_PAD_WIDTH_MM = 60.0
PUMP_PAD_HEIGHT_MM = 6.0
PUMP_SLOT_OVERALL_LENGTH_MM = 20.0  # elongated slot (not a fixed hole) for +-mounting adjustment
PUMP_SLOT_WIDTH_MM = 4.5            # M4 clearance
PUMP_SLOT_INSET_MM = 15.0           # slot center offset from pad center, both axes
PUMP_PAD_CENTER_X_MM = -55.0

# --- Valve clips (open rings, zip-tie secured -- generous mid-range envelope) ---
VALVE_CLIP_INNER_DIA_MM = 40.0
VALVE_CLIP_WIDTH_MM = 15.0
VALVE_CLIP_WALL_THICKNESS_MM = 3.0
VALVE_CLIP_GAP_DEG = 90.0
VALVE_CLIP_CENTER_X_MM = 60.0
VALVE_CLIP_SPACING_Y_MM = 70.0

# --- Base deck ---
PLATE_LENGTH_MM = 200.0
PLATE_WIDTH_MM = 110.0
PLATE_THICKNESS_MM = 4.0


def make_base_plate():
    with BuildPart() as bp:
        with BuildSketch() as sk:
            Rectangle(PLATE_LENGTH_MM, PLATE_WIDTH_MM)
        extrude(amount=PLATE_THICKNESS_MM)
    return bp.part


def make_arm_clamp():
    outer_r = ARM_TUBE_OD_MM / 2 + ARM_TUBE_CLEARANCE_MM + ARM_CLAMP_WALL_MM
    inner_r = ARM_TUBE_OD_MM / 2 + ARM_TUBE_CLEARANCE_MM
    with BuildPart() as cp:
        with BuildSketch(Plane.YZ) as sk:
            Circle(outer_r)
        extrude(amount=ARM_CLAMP_LENGTH_MM)
        with BuildSketch(Plane.YZ) as sk2:
            Circle(inner_r)
        extrude(amount=ARM_CLAMP_LENGTH_MM + 2.0, mode=Mode.SUBTRACT)
        # pie-slice wedge cut for the open gap -- see tank_mount_bracket_step.py for why this must be a
        # wedge from the ring's center, not a rectangle
        gap_half_rad = math.radians(ARM_CLAMP_GAP_DEG / 2)
        far = outer_r + 5.0
        p_left = (-far * math.sin(gap_half_rad), -far * math.cos(gap_half_rad))
        p_right = (far * math.sin(gap_half_rad), -far * math.cos(gap_half_rad))
        with BuildSketch(Plane.YZ) as sk3:
            with BuildLine():
                Polyline((0, 0), p_left, p_right, (0, 0))
            make_face()
        extrude(amount=ARM_CLAMP_LENGTH_MM + 2.0, mode=Mode.SUBTRACT)
    part = cp.part
    part.locate(Location((0, 0, -inner_r - ARM_CLAMP_WALL_MM + ARM_CLAMP_OVERLAP_MM)))
    part.label = "arm_clamp_saddle"
    return part


def make_pump_pad():
    with BuildPart() as pp:
        with BuildSketch() as sk:
            Rectangle(PUMP_PAD_LENGTH_MM, PUMP_PAD_WIDTH_MM)
        extrude(amount=PUMP_PAD_HEIGHT_MM)
        for x_sign in (-1, 1):
            for y_sign in (-1, 1):
                x_pos = x_sign * (PUMP_PAD_LENGTH_MM / 2 - PUMP_SLOT_INSET_MM)
                y_pos = y_sign * (PUMP_PAD_WIDTH_MM / 2 - PUMP_SLOT_INSET_MM)
                with BuildSketch(Plane.XY.offset(PUMP_PAD_HEIGHT_MM)) as slot_sk:
                    with Locations((x_pos, y_pos)):
                        SlotOverall(PUMP_SLOT_OVERALL_LENGTH_MM, PUMP_SLOT_WIDTH_MM)
                # both=True: a plain positive amount extrudes along +Z, away from the pad, and cuts
                # nothing -- must go both directions (or explicitly -Z) to pass through the material
                extrude(amount=PUMP_PAD_HEIGHT_MM + 2.0, both=True, mode=Mode.SUBTRACT)
    part = pp.part
    part.locate(Location((PUMP_PAD_CENTER_X_MM, 0, PLATE_THICKNESS_MM)))
    part.label = "pump_mount_pad"
    return part


def make_valve_clip(y_center):
    outer_r = VALVE_CLIP_INNER_DIA_MM / 2 + VALVE_CLIP_WALL_THICKNESS_MM
    inner_r = VALVE_CLIP_INNER_DIA_MM / 2
    with BuildPart() as vc:
        with BuildSketch(Plane.XZ) as sk:
            Circle(outer_r)
        extrude(amount=VALVE_CLIP_WIDTH_MM)
        with BuildSketch(Plane.XZ) as sk2:
            Circle(inner_r)
        extrude(amount=VALVE_CLIP_WIDTH_MM + 2.0, mode=Mode.SUBTRACT)
        # pie-slice wedge cut for the open gap, centered on the top (+Z) so the valve drops in from above
        gap_half_rad = math.radians(VALVE_CLIP_GAP_DEG / 2)
        far = outer_r + 5.0
        p_left = (-far * math.sin(gap_half_rad), far * math.cos(gap_half_rad))
        p_right = (far * math.sin(gap_half_rad), far * math.cos(gap_half_rad))
        with BuildSketch(Plane.XZ) as sk3:
            with BuildLine():
                Polyline((0, 0), p_left, p_right, (0, 0))
            make_face()
        extrude(amount=VALVE_CLIP_WIDTH_MM + 2.0, mode=Mode.SUBTRACT)
    part = vc.part
    overlap = 1.5
    part.locate(Location((VALVE_CLIP_CENTER_X_MM, y_center, PLATE_THICKNESS_MM + outer_r - overlap)))
    part.label = f"valve_clip_y{int(y_center)}"
    return part


def labeled(shape, name):
    shape.label = name
    return shape


def gen_step():
    parts = [
        labeled(make_base_plate(), "pump_valve_mount_deck"),
        make_arm_clamp(),
        make_pump_pad(),
        make_valve_clip(VALVE_CLIP_SPACING_Y_MM / 2),
        make_valve_clip(-VALVE_CLIP_SPACING_Y_MM / 2),
    ]
    assembly = Compound(children=parts)
    assembly.label = "v1_pump_valve_mount_bracket"
    sanity_check(assembly)
    return assembly


def sanity_check(assembly):
    bbox = assembly.bounding_box()
    size = bbox.size
    if size.X > 260 or size.Y > 260 or size.Z > 120:
        print(f"WARNING: bounding box {size} exceeds a plausible desktop-FDM-bed-friendly envelope "
              f"(expected roughly <=260x260x120mm) -- check for a placement error")
    if size.X < 80 or size.Y < 80:
        print(f"WARNING: bounding box {size} looks too small to carry a pump + 2 valves -- check for a "
              f"scale error")


if __name__ == "__main__":
    gen_step()
