"""v1 tank mount bracket -- build123d source for the locked v1 BOM in CLAUDE.md.

Mounts the water tank onto the Tarot X6 1000mm hex frame (TL6X001)'s carbon arm tubes. One monolithic
FDM-printable bracket: two arm-clamp saddles underneath a flat deck, with a strapped tank cradle on top.
Kept as its own small part (not combined with the pump/valve mount in v1/cad/pump_valve_mount_step.py)
so each piece stays well within a normal desktop FDM bed -- an earlier combined draft's footprint grew
past 350mm once the tank cradle, pump pad, and valve clips were laid out without overlapping.

Frame interface -- wheelbase 960mm, single arm length 392mm, center plate diameter 328mm, net weight
2000g, all confirmed 2026-07-12 from store.foxtech.com's TL6X001 product page. ARM_TUBE_OD_MM below is
NOT from that page (Foxtech doesn't list tube OD) -- it's a search-derived figure repeated across several
reseller listings, not an official datasheet number. Verify it with calipers once the frame is in hand.

Envelope, not exact-fit (2026-07-12): the 5L tank has unresolved vendor dimensions -- see v1/BUY_LIST.md
(search-result tank dimensions look corrupted, e.g. one listing's figure is an order of magnitude too
large to be a 5L tank). The tank cradle below is a generous strap-adjustable box sized to a plausible 5L
envelope (210x160x150mm proportions), not a snug pocket -- swap the TANK_ENVELOPE_*_MM constants for
real numbers once the tank is ordered and measured, then re-run sanity_check().

Coordinate system: origin at the plate's center, top face at Z=0. Plate extends down (-Z) into the arm
clamps and up (+Z) into the tank cradle walls. Arm clamp axis runs along X, matching the local direction
the frame's carbon tubes run past the mount point.
"""

from build123d import *

import math

# --- Frame interface (Tarot X6 1000mm hex, TL6X001) ---
ARM_TUBE_OD_MM = 25.0            # search-derived, NOT an official Tarot datasheet figure -- verify before
                                   # printing the final version
ARM_TUBE_CLEARANCE_MM = 1.5       # per side, so the tube slides in without binding
ARM_CLAMP_WALL_MM = 3.0
ARM_CLAMP_LENGTH_MM = 30.0
ARM_CLAMP_GAP_DEG = 100.0         # open arc for the tube to snap through / for zip-tie access
ARM_CLAMP_SPACING_MM = 180.0      # estimated local spacing between two adjacent arms near the center
                                   # plate; this is a placement guess, not measured -- adjust once the
                                   # real frame is available

# --- Tank envelope (adjustable strap mount, not exact-fit -- see module docstring) ---
TANK_ENVELOPE_LENGTH_MM = 210.0
TANK_ENVELOPE_WIDTH_MM = 160.0
TANK_CRADLE_WALL_HEIGHT_MM = 35.0
TANK_CRADLE_WALL_THICKNESS_MM = 3.0
TANK_STRAP_SLOT_WIDTH_MM = 10.0
TANK_STRAP_SLOT_HEIGHT_MM = 4.0
TANK_STRAP_SLOT_INSET_MM = 12.0   # slot center height above the plate's top face

# --- Base deck: sized to the cradle footprint plus a small lip, not the earlier combined layout ---
PLATE_MARGIN_MM = 10.0
PLATE_LENGTH_MM = TANK_ENVELOPE_LENGTH_MM + 2 * TANK_CRADLE_WALL_THICKNESS_MM + 2 * PLATE_MARGIN_MM
PLATE_WIDTH_MM = TANK_ENVELOPE_WIDTH_MM + 2 * TANK_CRADLE_WALL_THICKNESS_MM + 2 * PLATE_MARGIN_MM
PLATE_THICKNESS_MM = 4.0


def make_base_plate():
    with BuildPart() as bp:
        with BuildSketch() as sk:
            Rectangle(PLATE_LENGTH_MM, PLATE_WIDTH_MM)
        extrude(amount=PLATE_THICKNESS_MM)
    return bp.part


def make_arm_clamp(x_center):
    outer_r = ARM_TUBE_OD_MM / 2 + ARM_TUBE_CLEARANCE_MM + ARM_CLAMP_WALL_MM
    inner_r = ARM_TUBE_OD_MM / 2 + ARM_TUBE_CLEARANCE_MM
    with BuildPart() as cp:
        with BuildSketch(Plane.YZ) as sk:
            Circle(outer_r)
        extrude(amount=ARM_CLAMP_LENGTH_MM)
        with BuildSketch(Plane.YZ) as sk2:
            Circle(inner_r)
        extrude(amount=ARM_CLAMP_LENGTH_MM + 2.0, mode=Mode.SUBTRACT)
        # cut the open gap: a pie-slice wedge from the ring's center, spanning the gap angle, centered
        # on the bottom (-Z) direction -- NOT a rectangle, which would slice clean through both walls
        # instead of leaving a small angular notch
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
    overlap = 1.5  # push the clamp up into the deck slightly so the two solids share real volume,
                    # not just a coincident face -- guarantees a fused, printable connection
    part.locate(Location((x_center, 0, -inner_r - ARM_CLAMP_WALL_MM + overlap)))
    part.label = f"arm_clamp_saddle_x{int(x_center)}"
    return part


def make_tank_cradle():
    outer_l = TANK_ENVELOPE_LENGTH_MM + 2 * TANK_CRADLE_WALL_THICKNESS_MM
    outer_w = TANK_ENVELOPE_WIDTH_MM + 2 * TANK_CRADLE_WALL_THICKNESS_MM
    with BuildPart() as tc:
        with BuildSketch() as sk:
            Rectangle(outer_l, outer_w)
        extrude(amount=TANK_CRADLE_WALL_HEIGHT_MM)
        with BuildSketch(Plane.XY) as sk2:
            Rectangle(TANK_ENVELOPE_LENGTH_MM, TANK_ENVELOPE_WIDTH_MM)
        extrude(amount=TANK_CRADLE_WALL_HEIGHT_MM, mode=Mode.SUBTRACT)
        # strap slots through the front/back walls (Plane.XZ, normal along Y), two per wall, at
        # TANK_STRAP_SLOT_INSET_MM height above the deck
        for y_wall in (outer_w / 2, -outer_w / 2):
            for x_pos in (-outer_l / 4, outer_l / 4):
                with BuildSketch(Plane.XZ.offset(y_wall)) as slot_sk:
                    with Locations((x_pos, TANK_STRAP_SLOT_INSET_MM)):
                        SlotOverall(TANK_STRAP_SLOT_WIDTH_MM, TANK_STRAP_SLOT_HEIGHT_MM)
                extrude(amount=TANK_CRADLE_WALL_THICKNESS_MM + 2.0, both=True, mode=Mode.SUBTRACT)
    part = tc.part
    part.locate(Location((0, 0, PLATE_THICKNESS_MM)))
    part.label = "tank_strap_cradle"
    return part


def labeled(shape, name):
    shape.label = name
    return shape


def gen_step():
    parts = [
        labeled(make_base_plate(), "tank_mount_deck"),
        make_arm_clamp(-ARM_CLAMP_SPACING_MM / 2),
        make_arm_clamp(ARM_CLAMP_SPACING_MM / 2),
        make_tank_cradle(),
    ]
    assembly = Compound(children=parts)
    assembly.label = "v1_tank_mount_bracket"
    sanity_check(assembly)
    return assembly


def sanity_check(assembly):
    bbox = assembly.bounding_box()
    size = bbox.size
    if size.X > 260 or size.Y > 260 or size.Z > 120:
        print(f"WARNING: bounding box {size} exceeds a plausible desktop-FDM-bed-friendly envelope "
              f"(expected roughly <=260x260x120mm) -- check for a placement error")
    if size.X < 100 or size.Y < 100:
        print(f"WARNING: bounding box {size} looks too small for a bracket meant to carry a 5L tank -- "
              f"check for a scale error")


if __name__ == "__main__":
    gen_step()
