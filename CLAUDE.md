# Autonomous Tree-Watering Drone — Project Context

Two-phase project: **v1** is the near-term build target (electric, buildable now, funded via Stardance).
**v2** is the original amphibious hybrid hexacopter concept, kept as the long-term vision once v1 proves the
autonomy loop works. Do not conflate the two — v1 intentionally cuts most of v2's complexity.

## The problem being solved

Uncle's tree farm, up to ~100 acres of trees, planted in dense nursery-style rows (a few feet apart), mixed
maturity (young saplings + some established trees). A pond sits roughly centrally and is the only water
source. Farthest planted rows are 800m+ (0.5mi+) from the pond. The goal: a drone that autonomously waters
trees — flies out, sprays, comes back to the pond to refill and recharge, and repeats — without a human
manually refilling it or flying it tree-by-tree.

Realistic scope check: a small onboard tank can deliver a light dose (0.5–2 gal equivalent spread over a
transect) — genuinely useful for young/nursery stock and drought-stress relief, not a replacement for full
irrigation of mature trees. At nursery density, per-tree GPS waypoints don't scale (thousands of trees) — the
mission model is **row-transect spraying** (fly straight passes down rows, meter water to ground speed),
the same approach real agricultural spray drones use, not stop-and-dose per tree.

Covering all ~100 acres is inherently a multi-day, many-dock-cycle operation — that's fine and is in fact the
point: the system should run continuously (transect → low tank/battery → auto RTL → refill/recharge → relaunch)
over hours and days without supervision, not finish the whole farm in one flight.

## v1 — build target (do this first)

All-electric. No combustion engine, no amphibious hull, no pond-harvesting hardware on the airframe itself —
all of that complexity is pushed onto a **fixed ground dock at the pond**, not the drone.

**Airframe:** hexacopter (6 arms, keeping the original 6-arm identity), off-the-shelf frame class — no custom
carbon boom fabrication for v1. Motors/ESCs/props sized to the actual payload (a small tank), not 28in
industrial props — that sizing was for the v2 hybrid design's 5-gallon tank + generator weight, wildly
oversized for v1.

**Flight controller:** Pixhawk/Cube-class running ArduCopter. Standard GPS module (1-3m accuracy is fine —
row-transect spraying doesn't need RTK precision). ArduPilot's built-in survey/grid mission mode is the right
tool for row-transect flights.

**Telemetry:** long-range radio (RFD900x-class, multi-km rated) — required because of the 800m+ max range to
the farthest rows. A stock short-range hobby telemetry module (~100-300m) is not sufficient here. Missions run
off pre-loaded waypoints regardless of live link, but a reliable monitoring/failsafe link at this range needs
the right radio.

**Water system:** small tank (sized once real per-tree/per-transect dosing is worked out — start around
0.5-2 gal), 12V diaphragm pump, 1-2 solenoid-valve nozzles aligned with prop downwash, flow metered to
ground speed during transects.

**Ground dock (at the pond):** fixed structure with an alignment guide for autonomous landing, a pond-water
intake pump + coarse filter feeding a holding reservoir, and a float/flow sensor that tops off the drone's
tank automatically once docked. Charging contacts for autonomous recharge are a stretch goal — manual battery
swap between sorties is acceptable for v1.

**v1 demo scope:** prove the full closed loop — transect spray, low-tank/battery detection, auto return-to-dock,
pond refill, relaunch — on **one representative test row or small block near the pond**, not the whole farm.
Scaling to the full ~100 acres afterward is running the proven loop longer/more often, not new engineering.

## v2 — vision (later, not the current build)

The original CAD package in `designs/` describes the full aspirational version:

- 5-6kW gas-electric hybrid generator (cooling shroud, snorkel intake, angled exhaust)
- Aluminum firewall / Faraday cage isolating engine EMI from avionics
- Waterproofed avionics bay, isolated buffer LiPo trays
- Low-profile baffled 5-gallon composite water tank at CG
- Dual amphibious carbon fiber pontoons with stepped hydrodynamic hulls
- Submersible dual-stage marine filtration pump + check valve (on-drone water harvesting from the pond)
- Agricultural diaphragm pump + 6 downwash-aligned solenoid nozzles
- Dual RTK-GNSS antennas on a 15in carbon fiber mast

This is real engineering worth pursuing once v1 has flight hours and a working demo behind it — it's a much
stronger pitch for grants like Lemelson-MIT InvenTeams with a working v1 as proof of feasibility. Keep the CAD
package and its parametric source (`amphibious_hybrid_hexacopter_step.py`, build123d) as the reference design
for this phase; nothing in it is being built yet.

## Canonical directory (v2 CAD package)

```
designs/
├── amphibious_hybrid_hexacopter.step             # main Fusion 360 import file
├── amphibious_hybrid_hexacopter_step.py          # parametric source generator (build123d)
├── amphibious_hybrid_hexacopter_README.md        # design notes
├── amphibious_hexacopter_blueprint.svg           # secondary export/review asset
├── amphibious_hexacopter_plan_for_fusion.dxf     # secondary export/review asset
├── amphibious_hexacopter_fusion.obj/.mtl         # secondary export/review assets
├── *.zip                                          # export/review packs
└── snapshots/*.png                                # visual snapshots
```

Regenerate via `cd designs && .venv-cad\Scripts\activate && python amphibious_hybrid_hexacopter_step.py`
(Windows; use `source .venv-cad/bin/activate` on Mac/Linux). Units mm, origin at loaded CG. Edit the `.py`
source first, never hand-edit the STEP — `designs/.claude/settings.json` has a PreToolUse hook that hard-blocks
Edit/Write/Bash on any `.step` file for exactly this reason, so attempting to hand-edit it will just fail.

There's no lint/test step beyond running the generator — a clean run is the only automated correctness signal;
visually check the result (`cad:cad-viewer` skill, or compare against `designs/snapshots/`) before treating a
regen as done, since the script won't error on geometrically-wrong output.

**Code architecture of `amphibious_hybrid_hexacopter_step.py`:** built with `build123d`, output is one flat
`Compound` of labeled primitive solids — no assembly/mates hierarchy. Constants at the top (`ARM_LENGTH`,
`ENGINE_Z`, `TANK_Z`, etc.) are the single source of truth for dimensions/heights; change geometry by editing
these, not by hand-adjusting positions inside part functions. Placement helpers (`cyl_z`, `arm_cylinder`,
`radial_box`) place everything via polar coordinates (angle/radius/Z) around the hexacopter's 6-fold symmetry —
use these for anything repeating per-arm rather than computing `cos`/`sin` inline. Part-group functions
(`make_propeller`, `make_pontoons`, `make_central_stack`, `make_spray_system`, `make_mast`) each return a list of
labeled shapes for one subsystem; `gen_step()` loops the 6 arms at 60° spacing calling the per-arm functions,
then appends the once-only subsystems. Every shape must go through `labeled(shape, name)` — that's what keeps
individual solids identifiable (e.g. `dual_stage_marine_filter_pump_mesh_screen`) once merged into one Compound;
unlabeled geometry is unidentifiable downstream in Fusion 360. Remember these are dimensional envelopes sized to
plausible numbers, not real vendor parts/datasheets — don't treat any dimension as sourced or validated.

The secondary export files (`amphibious_hexacopter_blueprint.svg`, `amphibious_hexacopter_plan_for_fusion.dxf`,
`amphibious_hexacopter_fusion.obj`/`.mtl`) are derived from the STEP via Fusion 360, not generated by the Python
script — they don't update automatically when the STEP is regenerated and need a manual re-export to stay in sync.

## v1 — locked bill of materials

Philosophy: overshoot rather than cut it close — margin on lift, battery capacity, and telemetry range costs
comparatively little and buys a lot of slack for a first build (payload creep, wind, longer transects than
planned). Two tiers below: **Recommended** uses proven, well-documented components even where that costs more;
**Budget-trim** swaps the priciest items for cheaper equivalents if funding doesn't stretch far enough.

### Recommended (overshoot) tier — ~$2,200-$3,100 total

| Part | Component | Est. price |
|---|---|---|
| Frame | Tarot X6 1000mm foldable carbon fiber hex frame (TL6X001) | $180-250 |
| Motors (x6) | Heavy-lift hex motors, ~400-500KV, sized for 15-17in props on 6S (generous margin over minimum lift calc) | $270-390 |
| ESCs (x6) | 40-60A BLHeli32/opto ESCs | $150-210 |
| Props (x6 + spares) | 15-17in carbon fiber props | $90-150 |
| Flight controller | CubePilot Cube Orange+ Standard Set (carrier board included) | $275-400 |
| GPS | CUAV NEO 3 Pro (u-blox M9N + compass, GPS/GLONASS/Galileo/BeiDou) | $198-229 |
| Telemetry | RFD900x-US Modem Bundle (pair, multi-km rated — big margin over the 800m need) | $335-360 |
| Battery (x2, hot-swap) | 6S 16,000-22,000mAh LiPo/Li-ion smart batteries | $300-440 |
| Charger | 6S-capable balance charger | $60-100 |
| Water system | 5L tank + 24V diaphragm pump (~8L/min, e.g. XTL-3210 class) + 2x solenoid valve nozzles + tubing | $120-180 |
| Ground dock | Submersible 12V pond intake pump, mesh prefilter, float switch, holding reservoir, mounting/alignment structure hardware | $150-250 |
| Misc | Wiring, connectors, fasteners, landing gear reinforcement, antenna mounts (Mission Planner/QGroundControl is free) | $80-150 |

This is noticeably above the earlier back-of-envelope $650-1,050 guess — that number assumed generic
budget parts; this list swaps in name-brand, well-supported components (Cube Orange+, RFD900x, CUAV GPS)
because reliability on a first autonomous build matters more than shaving $200. Current committed budget
($600+ savings, plus realistic Stardance A/S-tier funding of $120-350) covers roughly a third to half of this
— expect to need additional funding or a trimmed tier below to close the gap.

### Budget-trim alternative (swap these if funding is short)

- Flight controller: a Pixhawk-clone (e.g. Holybro Pixhawk 6C or similar) instead of Cube Orange+ — saves
  ~$150-250.
- Telemetry: a standard SiK-based 433/915MHz radio pair (~1-2km rated, still well past the 800m need) instead
  of RFD900x — saves ~$280-320.
- Motors/ESCs: generic hobby-grade hex power combo instead of name-brand — saves ~$150-250, less documented
  support if something goes wrong.

Trimming all three brings the total down to roughly $1,400-1,900 — still overshooting the original rough
estimate, but closer to what $600 + Stardance funding can realistically cover.

## Known gaps / next steps

1. v1: BOM locked above (recommended + trim tiers) — still need to actually order parts and confirm current
   prices/availability before committing.
2. v1: battery voltage architecture (6S here) should be double-checked against final motor choice before
   ordering — don't mix motor KV/prop size without redoing the thrust/current math.
3. v1: dock design (alignment guide, intake pump, reservoir, float sensor) not yet started — this is the
   novel/hard engineering piece and deserves real design attention, not an afterthought.
4. v1: exact tree maturity mix and per-tree/per-transect water dosing still unconfirmed — refine tank sizing
   once known.
5. v2: no vendor parts or structural analysis yet (unchanged from original design doc) — dimensional envelopes
   only.
6. Consolidate any secondary export packs sitting outside `designs/` into the one canonical folder. (Done as
   of this project setup — everything now lives under `designs/`.)

## Onboarding order for a fresh session

1. Read this file first for the v1/v2 split and current build target.
2. If working on v1: no CAD onboarding needed yet beyond the dock structure — this is mostly an electronics/
   firmware/mission-planning build using off-the-shelf frame parts.
3. If working on v2 (CAD): read `designs/amphibious_hybrid_hexacopter_README.md`, then
   `amphibious_hybrid_hexacopter_step.py`, then open the STEP in Fusion 360 alongside a `designs/snapshots/`
   image before making changes.

## Related files in this project

- `pitch/Stardance_Pitch_Draft.md` — the funding pitch draft for #outpost-idea-pool (project name: Wellspring).
- `pitch/wellspring_concept_sketch.svg` — concept sketch referenced by the pitch draft.
