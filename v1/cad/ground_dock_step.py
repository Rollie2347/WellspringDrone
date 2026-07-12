"""v1 ground dock small parts -- build123d source for the locked v1 BOM in CLAUDE.md.

Scope decision (2026-07-12): the dock's big components (submersible intake pump ~180x180x291mm/3.35kg,
~30gal holding reservoir ~34x13x16.5in per v1/BUY_LIST.md) are too large/heavy to sensibly custom-print --
generic hardware-store pipe clamps and ratchet straps are the right fastener for those, not FDM brackets.
This file scopes to the two genuinely novel small parts worth printing: a float-switch mount (clips the
switch to the reservoir wall) and a landing alignment guide post (funnels the drone's landing gear toward
a centered position on approach, one per corner of the landing pad).

Envelope, not exact-fit: the float switch body (uxcell ZP2508, ~19mm dia x 36mm) is the one dimension here
with a reasonably confirmed listing -- see v1/BUY_LIST.md. The alignment guide's corner spacing is a
placement guess (Tarot X6's landing gear leg spread wasn't in the confirmed Foxtech spec, only leg height
395mm) -- adjust GUIDE_CORNER_SPACING_MM once the real frame is available.

Coordinate system: each part is modeled at its own local origin (not positioned relative to each other --
these are independent parts meant for different install locations at the dock). Base/mounting face at
Z=0, part extends +Z.
"""

from build123d import *

import math

# --- Float switch mount (uxcell ZP2508-class vertical float switch) ---
FLOAT_SWITCH_BODY_DIA_MM = 19.0   # confirmed listing dimension, v1/BUY_LIST.md
FLOAT_SWITCH_CLEARANCE_MM = 1.5
FLOAT_CLIP_WALL_MM = 3.0
FLOAT_CLIP_HEIGHT_MM = 20.0       # short clip band, not a full-length sleeve -- switch body is 36mm long,
                                   # only needs one grip point plus the mounting plate's own thickness
FLOAT_CLIP_GAP_DEG = 70.0
FLOAT_PLATE_LENGTH_MM = 60.0
FLOAT_PLATE_WIDTH_MM = 40.0
FLOAT_PLATE_THICKNESS_MM = 4.0
FLOAT_PLATE_HOLE_DIA_MM = 4.5     # M4 clearance
FLOAT_PLATE_HOLE_INSET_MM = 8.0

# --- Landing alignment guide post (funnel cone, one per landing-pad corner) ---
GUIDE_BASE_DIA_MM = 150.0
GUIDE_TOP_DIA_MM = 60.0
GUIDE_HEIGHT_MM = 80.0
GUIDE_WALL_MM = 4.0
GUIDE_FLANGE_DIA_MM = 180.0
GUIDE_FLANGE_THICKNESS_MM = 5.0
GUIDE_FLANGE_HOLE_DIA_MM = 5.5    # M5 clearance
GUIDE_FLANGE_HOLE_COUNT = 4
GUIDE_FLANGE_HOLE_RADIUS_MM = 80.0
GUIDE_CORNER_SPACING_MM = 700.0   # placement guess for landing-pad corner layout, NOT the Tarot X6's
                                   # confirmed spec (only wheelbase 960mm and leg height 395mm are
                                   # confirmed, not leg spread) -- adjust once the real frame/dock
                                   # platform is measured


def make_float_switch_bracket():
    clip_inner_r = FLOAT_SWITCH_BODY_DIA_MM / 2 + FLOAT_SWITCH_CLEARANCE_MM
    clip_outer_r = clip_inner_r + FLOAT_CLIP_WALL_MM
    with BuildPart() as fb:
        with BuildSketch() as sk:
            Rectangle(FLOAT_PLATE_LENGTH_MM, FLOAT_PLATE_WIDTH_MM)
        extrude(amount=FLOAT_PLATE_THICKNESS_MM)
        for x_sign in (-1, 1):
            x_pos = x_sign * (FLOAT_PLATE_LENGTH_MM / 2 - FLOAT_PLATE_HOLE_INSET_MM)
            with BuildSketch(Plane.XY.offset(FLOAT_PLATE_THICKNESS_MM)) as hole_sk:
                with Locations((x_pos, 0)):
                    Circle(FLOAT_PLATE_HOLE_DIA_MM / 2)
            extrude(amount=FLOAT_PLATE_THICKNESS_MM + 2.0, both=True, mode=Mode.SUBTRACT)
        # clip ring standing up from the plate, axis vertical (Z), gap facing +Y for side insertion
        with BuildSketch(Plane.XY.offset(FLOAT_PLATE_THICKNESS_MM)) as clip_sk:
            Circle(clip_outer_r)
        extrude(amount=FLOAT_CLIP_HEIGHT_MM)
        with BuildSketch(Plane.XY.offset(FLOAT_PLATE_THICKNESS_MM)) as clip_sk2:
            Circle(clip_inner_r)
        extrude(amount=FLOAT_CLIP_HEIGHT_MM + 2.0, mode=Mode.SUBTRACT)
        gap_half_rad = math.radians(FLOAT_CLIP_GAP_DEG / 2)
        far = clip_outer_r + 5.0
        p_left = (-far * math.sin(gap_half_rad), far * math.cos(gap_half_rad))
        p_right = (far * math.sin(gap_half_rad), far * math.cos(gap_half_rad))
        with BuildSketch(Plane.XY.offset(FLOAT_PLATE_THICKNESS_MM)) as gap_sk:
            with BuildLine():
                Polyline((0, 0), p_left, p_right, (0, 0))
            make_face()
        extrude(amount=FLOAT_CLIP_HEIGHT_MM + 2.0, mode=Mode.SUBTRACT)
    part = fb.part
    part.label = "float_switch_bracket"
    return part


def make_alignment_guide_post():
    base_r = GUIDE_BASE_DIA_MM / 2
    top_r = GUIDE_TOP_DIA_MM / 2
    flange_r = GUIDE_FLANGE_DIA_MM / 2
    with BuildPart() as gp:
        with BuildSketch() as flange_sk:
            Circle(flange_r)
        extrude(amount=GUIDE_FLANGE_THICKNESS_MM)
        for i in range(GUIDE_FLANGE_HOLE_COUNT):
            angle = math.radians(360.0 / GUIDE_FLANGE_HOLE_COUNT * i)
            x_pos = GUIDE_FLANGE_HOLE_RADIUS_MM * math.cos(angle)
            y_pos = GUIDE_FLANGE_HOLE_RADIUS_MM * math.sin(angle)
            with BuildSketch(Plane.XY.offset(GUIDE_FLANGE_THICKNESS_MM)) as hole_sk:
                with Locations((x_pos, y_pos)):
                    Circle(GUIDE_FLANGE_HOLE_DIA_MM / 2)
            extrude(amount=GUIDE_FLANGE_THICKNESS_MM + 2.0, both=True, mode=Mode.SUBTRACT)
        # tapered funnel shell (loft between base and top circles), hollow with GUIDE_WALL_MM thickness
        with BuildSketch(Plane.XY.offset(GUIDE_FLANGE_THICKNESS_MM)) as base_sk:
            Circle(base_r)
        with BuildSketch(Plane.XY.offset(GUIDE_FLANGE_THICKNESS_MM + GUIDE_HEIGHT_MM)) as top_sk:
            Circle(top_r)
        loft([base_sk.sketch, top_sk.sketch])
        with BuildSketch(Plane.XY.offset(GUIDE_FLANGE_THICKNESS_MM + GUIDE_WALL_MM)) as base_sk2:
            Circle(base_r - GUIDE_WALL_MM)
        with BuildSketch(Plane.XY.offset(GUIDE_FLANGE_THICKNESS_MM + GUIDE_HEIGHT_MM)) as top_sk2:
            Circle(max(top_r - GUIDE_WALL_MM, 1.0))
        loft([base_sk2.sketch, top_sk2.sketch], mode=Mode.SUBTRACT)
    part = gp.part
    part.label = "alignment_guide_post"
    return part


def labeled(shape, name):
    shape.label = name
    return shape


def gen_step():
    float_bracket = labeled(make_float_switch_bracket(), "float_switch_bracket")
    guide_post = labeled(make_alignment_guide_post(), "alignment_guide_post")
    guide_post.locate(Location((GUIDE_CORNER_SPACING_MM + 200.0, 0, 0)))
    assembly = Compound(children=[float_bracket, guide_post])
    assembly.label = "v1_ground_dock_parts"
    sanity_check(float_bracket, guide_post)
    return assembly


def sanity_check(float_bracket, guide_post):
    fb_bbox = float_bracket.bounding_box()
    gp_bbox = guide_post.bounding_box()
    if fb_bbox.size.X > 150 or fb_bbox.size.Y > 150 or fb_bbox.size.Z > 60:
        print(f"WARNING: float_switch_bracket bounding box {fb_bbox.size} looks too big for a small clip "
              f"bracket -- check for a scale error")
    if gp_bbox.size.X > 250 or gp_bbox.size.Y > 250 or gp_bbox.size.Z > 150:
        print(f"WARNING: alignment_guide_post bounding box {gp_bbox.size} exceeds a plausible desktop-"
              f"FDM-bed envelope (expected roughly <=250x250x150mm) -- check for a placement/scale error")


if __name__ == "__main__":
    gen_step()
