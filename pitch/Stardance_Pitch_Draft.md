# Stardance #outpost-idea-pool pitch draft

(Post this in #outpost-idea-pool, then tag @alexren per the X-tier process. If X-tier doesn't land, this same
pitch/description works for a standard project submission at A or S tier.)

## Project name (placeholder — swap for whatever you like)

Wellspring — an autonomous, self-refilling agricultural watering drone

## What it does

My uncle runs a ~100-acre tree farm with a pond as the only water source. Trees are planted in dense
nursery-style rows, and the farthest rows are over half a mile from the pond. Right now watering is manual.

Wellspring is a hexacopter drone that waters the trees completely on its own, with no human refilling it or
flying it by hand:

1. It flies scripted row-transect passes over the trees (like a real agricultural spray drone), releasing a
   metered spray as it goes.
2. When its onboard tank or battery gets low, it automatically returns to a fixed dock built at the pond.
3. The dock pulls water from the pond, filters it, and refills the drone's tank automatically — no person
   involved.
4. The drone relaunches and picks up the next section, repeating for hours/days until the whole property has
   been covered, then starting the cycle again.

The interesting engineering isn't really the drone itself — it's the closed loop: autonomous mission planning,
low-resource detection and failsafe return, and a self-refilling ground station that has to align and dock
reliably every single time without a person there to help it. That's the part I want to actually build and get
working end-to-end, even on a small test section, before scaling it to the full farm.

This is a real problem for a real farm, not a demo — my uncle would genuinely use this.

## Why it's a bigger build than a normal project

This isn't "attach a spray nozzle to a drone." It's a fully closed autonomous loop: flight controller running
scripted missions (ArduPilot), long-range telemetry (the farm is big enough that stock hobby radios won't reach
the far corners), a metered water-delivery system tied to ground speed, and a custom-built ground station that
has to handle water intake, filtration, and precision autonomous docking on its own. Long-term, this is a
stepping stone to a much bigger version (gas-electric hybrid power, amphibious hull, on-drone water harvesting)
that I'm treating as a v2 once this proves out.

## Sketch (see `wellspring_concept_sketch.svg`)

Shows: the hexacopter (6 arms, motors, tank + downward nozzles, GPS/telemetry antenna) flying a back-and-forth
transect pattern over a labeled row of trees, a dock structure at the pond edge with an intake pump/filter and
alignment guide, and the autonomy loop labeled 1-4 (spray transect → low tank/battery → auto return-to-dock →
refill + relaunch) with the ~100-acre property boundary and the 800m+ farthest-row distance marked.

## Rough budget ask

Parts for a working v1 (frame, motors/ESCs/props, flight controller, GPS, long-range telemetry radio, water
pump/tank/valves, dock pump + filter + reservoir): roughly $650-$1,050. Have $600+ already committed; Stardance
funding would close the gap and let the dock (the genuinely novel part) be built properly instead of cut for
cost.

> Note: the locked BOM in the project `CLAUDE.md` (recommended + budget-trim tiers) supersedes the rough
> $650-1,050 estimate above with more realistic, name-brand pricing — update this pitch's budget ask before
> posting if you want the numbers to match.
