# v1 Buy List — live vendor links (Recommended/Budget-trim checked 2026-07-12, Bare-bones checked 2026-07-15)

Real, currently-live listings for the locked BOM in `CLAUDE.md`, plus a third **Bare-bones tier** (added
2026-07-15, see below) built outside that BOM to hit a hard $1,800 ceiling for the drone alone. Prices and stock
change — re-verify before ordering if this file is more than a few weeks old. Every weight already cited in
`v1/power_budget.py` was re-confirmed against the live vendor page in this pass (no discrepancies found).

**Headline finding: current real prices run well above the original BOM estimate ranges in `CLAUDE.md`.**
Core flight hardware (frame + motors + ESCs + props + FC + GPS + telemetry + battery + charger, no water
system/dock/misc yet) prices out at:

- **Recommended tier: ~$3,859** vs. the ~$1,858-2,529 the BOM table implied for this same set of categories.
- **Budget-trim tier: ~$2,715-3,195** vs. the "$1,400-1,900 whole-project" figure `CLAUDE.md` currently states.

Biggest drivers: the named ESC (Hobbywing XRotor Pro H60A, $85 each x6 = $510 vs. an implied ~$25-35/ESC in
the old estimate) and the named battery (Tattu Plus 22000mAh, $487 each x2 = $974 vs. $300-440 total in the old
estimate) are both far pricier than the original category ranges assumed. GPS and telemetry came in *under* the
old estimate. **This means the Stardance funding ask in `pitch/Stardance_Pitch_Draft.md` ($1,400-1,900 /
$2,200-3,100) is now stale again** — see "What needs a decision" at the bottom.

## Recommended tier

| Item | Vendor | Price | Weight | Link |
|---|---|---|---|---|
| Tarot X6 1000mm hex frame (TL6X001) | ReadyMadeRC | $419.99 | 2,000g (2,700g shipping) | https://www.readymaderc.com/products/details/85932-tarot-x6-6-axis-hexacopter-tl6x001 |
| T-Motor MN4014 KV400 ×6 | T-Motor Store | $96.90 ea ($581.40) | 171g ea, confirmed | https://store.tmotor.com/goods-348-MN4014+KV400.html |
| Hobbywing XRotor Pro H60A ESC ×6 | HobbywingDirect | $84.99 ea ($509.94, on sale from $140) | 53g ea, confirmed | https://www.hobbywingdirect.com/products/xrotor-pro-h60a-esc |
| T-Motor P16x5.4 CF prop, 5 pairs (10 props = 6 flying + 4 spares) | T-Motor Store | $62.90/pair ($314.50) | 25g/blade, confirmed | https://store.tmotor.com/product/polish-carbon-fiber-16x5_4-prop.html |
| CubePilot Cube Orange+ Standard Set | irlock.com | $451.00 | not captured this pass (73g cited previously, unchallenged) | https://irlock.com/products/cube-orange-plus-standard-set — **verify SKU**, see note below |
| CUAV NEO 3 Pro GPS | UnmannedRC | $169.00 | 33g, confirmed | https://unmannedrc.com/products/cuav-neo-3-pro-gps-module-gnss-u-blox-m9n-can-bus |
| RFD900x-US Modem Bundle (pair) | ReadyMadeRC | $287.01 | 14.5g/modem, confirmed | https://www.readymaderc.com/products/details/rfdesign-rfd900x-us-telemetry-modem-bundle-fcc |
| Tattu Plus 22000mAh 6S1P 25C ×2 | Genstattu | $486.99 ea ($973.98) | 2,650g ea, confirmed | https://genstattu.com/tattu-plus-25c-22000mah-6s1p-xt90-smart-lipo-battery.html |
| HOTA D6 Pro charger (325W, 1-6S) | Pyrodrone | $151.99 | not listed | https://pyrodrone.com/products/hota-d6-pro-charger-ac200w-dc650w-15a |
| **Core hardware subtotal** | | **$3,858.81** | | |

**Cube Orange+ note:** the $451 price above is confirmed live but is the ADS-B carrier variant. GetFPV and
RobotShop (likely carrying the plain Standard Set) blocked automated fetch (403) — get an exact quote from one
of those before ordering, since CubePilot reseller naming is inconsistent.

## Budget-trim tier (swap these three, keep everything else from Recommended)

| Item | Vendor | Price | Weight | Link |
|---|---|---|---|---|
| Holybro Pixhawk 6C (plastic case) | Holybro | $165.99 | 34.6g | https://holybro.com/products/pixhawk-6c |
| Holybro SiK Telemetry Radio V3, 100mW 915MHz, pair | Holybro | $58.99 ea ($117.98) | 23.5g w/ antenna | https://holybro.com/products/sik-telemetry-radio-v3 |
| SunnySky X4110S 400KV motor ×6 | SunnySky USA | $46.99 ea ($281.94) | 165g ea | https://sunnyskyusa.com/products/sunnysky-x4110s-motors |
| Hobbywing XRotor 40A 2-6S Opto ESC ×6 (cheap option) | ReadyMadeRC | $19.99 ea ($119.94) | 32g ea | https://www.readymaderc.com/products/details/85497-hobbywing-xrotor-40a-2-6s-opto-esc-for-multirotor |
| *Alternative:* T-Motor FLAME 60A 12S ESC ×6 (more headroom) | T-Motor Store | $99.99 ea ($599.94) | 73.5g ea (third-party source, not T-Motor's own page) | https://store.tmotor.com/product/flame-60a-12s-V2-esc.html |
| **Core hardware subtotal (cheap ESC)** | | **$2,715.31** | | |
| **Core hardware subtotal (T-Motor FLAME ESC)** | | **$3,195.31** | | |

**ESC caution:** 40A continuous is thin margin for an MN4014-class motor spinning a 16x5.4 prop under
hover/climb load. The $19.99 Hobbywing 40A is real and live but has less headroom than the Recommended tier's
H60A. The T-Motor FLAME 60A is a safer budget-adjacent alternative if the extra ~$480 fits.

## Bare-bones tier (drone only, no dock — target ≤$1,800, everything in-stock & shippable within 2 weeks, checked 2026-07-15)

Self-contained list, unlike the two tiers above: it includes its own water system and misc hardware rather than
sharing the sections below, because the whole point is one number that has to land under $1,800 for the flying
airframe alone. Every category from the locked BOM is still represented — this is a cheaper version of the same
essential systems (fly autonomously, spray water, come home on telemetry), not a cut-down subset. Improve later
by swapping any row for its Recommended/Budget-trim equivalent above once more funding lands.

Vendor bias is deliberately toward US-warehouse / Amazon-fulfilled listings over China-direct ones (even at the
same nominal price) specifically to hit the 2-week arrival requirement — see per-row notes.

| Item | Vendor | Price | Weight | Link | Notes |
|---|---|---|---|---|---|
| QWinOut Q650 650mm 3K carbon folding-arm hex frame | Amazon (ASIN B08HZ4377Q, Amazon-fulfilled) | $95.86 | not captured | https://www.amazon.com/QWinOut-Aircraft-Folding-Quadcopter-Helicopter/dp/B08HZ4377Q | Buy the Amazon listing, not qwinout.com direct — same product, but direct ships from China and risks the 2-week window. Verify price on the actual Amazon page before ordering. |
| SunnySky V3508 700KV motor ×6 | BuddyRC | $42.99 ea ($257.94) | 97-107g ea (sources disagree slightly) | https://www.buddyrc.com/products/sunnysky-v3508-motor | Sized for 12-13in props, standard pairing for a 650mm-class hex — not a novel/oversized combo like v2's prop-overlap bug, so frame/prop clearance isn't a concern here. **Thrust margin at 6S is NOT verified against a real datasheet — see caution below.** |
| Hobbywing XRotor 40A ESC ×6 (BLHeli_S, not Pro/32) | HobbywingDirect | $17.99 ea ($107.94) | not captured | https://www.hobbywingdirect.com/products/xrotor-40a-esc | Rated for 550-650mm multirotors, 2-6S. Plain BLHeli_S is fine for ArduCopter (no DShot/per-ESC telemetry, unlike the Pro tier's H60A). |
| HQProp 12x4.5 CW/CCW, ~4 total 2-packs (6 flying + 2 spare) | ReadyMadeRC | ~$23 (CW/CCW per-pack prices found were inconsistent — verify both packs cost the same before ordering) | not captured | https://www.readymaderc.com/products/details/85965-hq-prop-12x4-5-cw | Matches motor row above. |
| Holybro Pixhawk 6C Mini | Holybro (official store) | $130.99 | not captured | https://holybro.com/products/pixhawk-6c-mini | Deliberately not a "Pixhawk 2.4.8" clone — those run FMUv2/1MB flash, which current ArduCopter (4.3+) has dropped support for. 6C Mini has real, maintained ArduCopter support. |
| Holybro M9N Micro GPS w/ IST8310 compass | RaceDayQuads | $46.99 | not captured | https://www.racedayquads.com/products/holybro-m9n-micro-gps-w-ist8310-compass-10th-gen | u-blox M9N, standard ArduCopter GPS+compass. |
| Holybro SiK Telemetry Radio V3, 100mW/915MHz, pair | Holybro (official store) | $58.99/pair | 23.5g/unit | https://holybro.com/products/sik-telemetry-radio-v3 | ~300m+ stock range — fine for a dock-adjacent bare-bones demo, well short of the 800m+ full-farm range the Recommended tier's RFD900x covers. Upgrade this row first once funding allows. |
| Tattu G-Tech 6S 10000mAh 30C, EC5 plug (single, no hot-swap spare) | Genstattu (official Tattu US store) | $216.99 | not captured | https://genstattu.com/ta-30c-10000-6s1p-ec5.html | EC5 connector — needs an EC5-to-XT60/XT90 adapter (folded into misc row below) to match typical ESC/PDB wiring. Single battery only; no swap-and-relaunch until a second is bought later. |
| HOBBYMATE Imax B6-clone AC/DC 1-6S balance charger | Amazon | ~$25-30 (price not confirmed — Amazon blocked automated fetch) | — | https://www.amazon.com/HOBBYMATE-Battery-Balance-Charger-Adapter/dp/B01NB9A36R | Verify live price/stock before ordering. |
| Chapin 2 Gal. poly tank sprayer (water tank) | Home Depot | ~$20.92 (search-sourced, not directly fetched) | — | https://www.homedepot.com/p/Chapin-2-Gal-Lawn-Garden-and-Multi-Purpose-Poly-Tank-Sprayer-with-Foaming-and-Adjustable-Nozzles-20542/322891897 | 2 gal exceeds the mission's 0.5-2 gal target range at the top end — fine, just don't fill it past ~2 gal payload. Cheapest verified ready-made tank with an integrated cap/outlet found. |
| 12V mini diaphragm pump (~5L/min class) | Amazon | ~$15-25 (price not confirmed — Amazon blocked automated fetch) | — | https://www.amazon.com/wrtgerht-Agricultural-Electric-Pressure-Diaphragm/dp/B0B84DCY2M | Verify live price before ordering — a same-family SKU showed a $137 price that's almost certainly a different variant; don't assume that number applies to this listing. |
| U.S. Solid 1/2" NPT brass 12V DC solenoid valve, normally closed | U.S. Solid (official store) | $34.95 | — | https://ussolid.com/products/u-s-solid-1-2-brass-electric-solenoid-valve-12v-dc-normally-closed-viton-air-water-oil-fuel-html | Single valve/nozzle (both other tiers spec two) — bare-bones cuts spray coverage width, not reliability. |
| Tubing/fittings (generic 1/2" ID vinyl/silicone + barbed fittings) | Amazon/hardware store | ~$10-15 estimate | — | — | No itemized kit found, same gap as the other tiers — buy à la carte. |
| Misc: XT60/XT90 connectors, EC5 adapter, 14AWG silicone wire, basic PDB, M3 screw assortment | Amazon | ~$35-40 estimate | — | — | Bucket estimate, not itemized — individually cheap, Amazon blocked automated price fetch across the board. |
| **Total (verified rows + estimated rows)** | | **≈ $1,095-1,185** | | | **≈ $615-705 under the $1,800 ceiling.** |

**Caution — thrust margin is the one real open question on this tier, unlike the Recommended/Budget-trim tiers
above which trace to `v1/power_budget.py`'s sourced T-Motor MN4014 thrust table.** No 6S thrust datasheet for the
SunnySky V3508 700KV + HQProp 12x4.5 combo was found (SunnySky's own published test data only covers 4S/14.8-16V,
not 6S/22.2V). A rough hand estimate (motor+ESC+FC+battery+full 2gal tank AUW vs. typical 3508-class 700KV max
thrust on a 12-13in prop) suggests margin could be as thin as ~20-25% with a full tank — well below the ~60%+
margin this project's own methodology targets for the other tiers (see `CLAUDE.md` known gap #2). **Do not order
the motors/props/frame rows until someone extends `v1/power_budget.py` with a real sourced thrust curve for this
combo** (either from a V3508 6S datasheet if one turns up, or from bench-testing after ordering just the motor/ESC/
prop/battery). The ~$600-700 of headroom under $1,800 is exactly enough room to move up to the frame/motor/prop
combo that already has verified thrust data (Tarot X6 class frame + T-Motor MN4014 + 16x5.4in props) if the V3508
margin turns out to be inadequate — that swap alone would cost roughly an extra $700-750 versus the rows above.

### Bare-bones tier — build instructions

Two things below are **not in the table above and not priced anywhere in this document** — both are needed to
actually fly this, budget ~$20-40 each and add them to whichever tier you order:

- **RC transmitter/receiver pair.** Nothing in the locked BOM (any tier) includes one, because autonomous
  missions run off pre-loaded waypoints. But you still want manual stick control for ESC calibration, motor
  direction tests, and the first several stabilize/loiter hovers before trusting autonomous mode — don't skip
  straight to a waypoint mission on an airframe that's never flown. If you already own an RC transmitter from
  another hobby build, you just need a compatible receiver (e.g. FrSky/Crossfire/ELRS depending on what TX you
  have).
- **12V relay or MOSFET switch module** (e.g. a simple opto-isolated relay board), wired to one of the FC's AUX/
  servo outputs. The pump and solenoid valve both need to be switched on/off by the flight controller during a
  spray transect — nothing in the BOM currently bridges "FC output pin" to "12V pump/valve power," and neither
  draws little enough current to drive directly off an FC pin.

**Assembly order:**

1. **Frame.** Assemble the QWinOut Q650 arms/center plates/landing gear per its included instructions. Don't
   mount motors yet — easier to route ESC wiring through the arms first if the frame design allows it.
2. **Motors + ESCs.** Bolt one SunnySky V3508 to the base of each arm. Solder (or bullet-connect) each Hobbywing
   XRotor 40A ESC's three motor leads to its motor — exact phase order doesn't matter yet, direction gets fixed
   in software via Mission Planner's motor test, not by wire order. Route each ESC's power leads back toward the
   center for the power distribution step below. Zip-tie/heat-shrink each ESC to its arm, away from prop wash
   turbulence but with airflow for cooling.
3. **Power distribution.** Mount a basic PDB (or use bare wiring) at the frame center. Solder all 6 ESC power
   leads plus the battery lead (through the EC5-to-XT60/XT90 adapter, since the Tattu battery is EC5 and most
   PDBs/ESCs expect XT60/XT90) to the PDB's power rails. Keep this wiring short and don't power anything on yet.
4. **Flight controller.** Mount the Pixhawk 6C Mini at the frame's center of gravity on vibration-dampening
   foam/grommets, arrow pointing toward the front of the frame (whichever arm you're designating as front — the
   Q650 isn't symmetric-labeled out of the box, so pick one and stay consistent). Connect ESC signal wires to
   the FC's MAIN OUT rail — **don't guess the 1-6 motor-to-output mapping by wire position; Mission Planner's
   initial setup wizard has a "Hexa X" motor-order diagram, follow that exactly** to avoid a reversed-motor crash
   on first spin-up.
5. **GPS/compass.** Mount the M9N on a short mast or the frame's rear arm, as far from the ESC/power wiring and
   battery as the frame allows — compass interference from nearby high-current wiring is the most common cause
   of erratic ArduCopter GPS/heading behavior on a first build.
6. **Telemetry radio.** Mount the air-side SiK radio away from the GPS antenna (RF interference) with its
   antenna vertical and clear of carbon fiber (which attenuates RF) — zip-tie to a landing gear leg or boom tip
   rather than burying it in the center stack.
7. **Water system.** Strap-mount the Chapin tank at/near the frame's CG (a full tank will shift balance —
   compensate by keeping other heavy components, like the battery, centered too). Mount the diaphragm pump and
   solenoid valve below the tank outlet, tubing routed to one nozzle aligned with a prop's downwash. Wire the
   pump and valve through the relay/MOSFET module (see gap above) to a spare battery tap and an FC AUX output —
   do not wire them directly to FC power/signal pins.
8. **RC receiver.** Mount and bind per its manual; connect to the FC's RC input.
9. **Software setup (Mission Planner or QGroundControl).** Flash ArduCopter firmware, select frame class "Hexa"
   / frame type "X", run the accelerometer, compass, and radio calibration wizards, then the ESC calibration
   procedure (props still off). Configure failsafes now, not after first flight — battery voltage cutoffs
   matched to the Tattu 10000mAh's real discharge curve, RC-loss and telemetry-loss RTL behavior, and a geofence
   — see `CLAUDE.md` known gap #5, none of this is done automatically.
10. **Ground test, props off.** Power up, run Mission Planner's motor test to confirm all 6 spin the correct
    direction per the Hexa-X diagram and respond to the right throttle/attitude commands before anything is
    load-bearing.
11. **Props on, restrained test.** With the airframe physically restrained (not just "on a table" — hexacopters
    can flip/skitter at partial throttle), verify throttle response and stability behavior in Stabilize mode at
    low throttle before ever letting it free-hover.
12. **First free flights.** Stabilize, then Loiter, hand-catch-safe altitude, no payload, no wind, until you
    trust the airframe — only then load the water system and attempt a transect. Confirm VLOS/Part 107 posture
    per `CLAUDE.md` known gap #7 before flying outdoors at all.

## Water system (both tiers — candidates found, pricing/dimensions not fully resolved)

| Item | Vendor | Price | Dimensions | Weight | Link |
|---|---|---|---|---|---|
| Tank: EFT "5L Medicine Box" (MX405 5L frame) | RCDrone | $154.73 | not published on this listing | not published | https://rcdrone.top/products/5l-water-tank-medicine-box |
| Pump: XTL-3210 12V 100W 8L/min | offthegridsun.com | $44.00 | disputed — see below | disputed — see below | https://offthegridsun.com/index.php?main_page=product_info&products_id=2077 |
| Solenoid valve, 1/2" brass 12V NC (×2 needed) | Amazon | price blocked on fetch | 65×60×35mm | 218g | https://www.amazon.com/Normally-Electrical-Solenoid-Magnetic-Purification/dp/B07Y5YKWH4 |
| Tubing/fittings | rcdrone.top, sprayersupplies.com | no itemized kit found — sold à la carte | — | — | — |

**Pump data conflict — unresolved, do not use either number without independent verification:** every indexed
listing for the XTL-3210 cites 47×34×22mm / 72g, but that's implausibly small/light for an 8A-draw, 100W brush
diaphragm pump. A separate cluster of listings (Daraz, Al Annabi, Alibaba) puts the same nominal part at
180×95×65mm / 800g-1kg, which is physically more plausible but has no listing with a real spec-sheet PDF either.
Two independent research passes couldn't resolve this from search data — it needs either a seller with an actual
datasheet, or a physical measurement after ordering. **Do not lock CAD mounting geometry to either number yet.**

**Tank dimensions:** aggregator data for 5L drone tanks is unreliable — one listing's "750×750×480mm" is
almost certainly a copy-paste from a full airframe spec, not the tank. No verified tank dimension exists yet.

## Ground dock (fixed structure at the pond — not flown, so weight doesn't matter, dimensions do)

| Item | Vendor | Price | Dimensions | Weight | Link |
|---|---|---|---|---|---|
| Submersible intake pump: TIGEROAR 12V 1500GPH | Amazon | not retrieved (fetch blocked) | 180×180×291mm | 3.35kg | https://www.amazon.com/TIGEROAR-Thermoplastic-Submersible-Transferring-Camouflage/dp/B0953Z8CVC |
| Prefilter: American Pond "Pump Pal" | Amazon | not retrieved | 254mm dia × 152mm tall | not given | https://www.amazon.com/American-Pond-Large-PreFilter-Submersible/dp/B00THFLFTY |
| Float switch: uxcell ZP2508 vertical, 2-pack | Amazon | not retrieved | body 19mm dia × 36mm; cable 36cm | 30g (pair) | https://www.amazon.com/uxcell-Liquid-Sensor-Vertical-Switch/dp/B00TGQ1D5K |
| Reservoir: TORVA 30gal RV tank | Amazon | not retrieved | 34×13×16.5in | 8.5kg net | https://www.amazon.com/TORVA-Drinking-Holding-Portable-Storage/dp/B0DNMQJQG6 |

## Misc hardware (both tiers)

| Item | Vendor | Price | Weight | Link |
|---|---|---|---|---|
| XT60 connector pairs w/ 14AWG wire, 5-pair | Amazon | not retrieved | ~17.5g/pair | https://www.amazon.com/JFtech-Connectors-Silicone-Airplane-Quadcopter/dp/B07HQBDW7V |
| 12AWG silicone wire, 13ft | Amazon | not retrieved | — | https://www.amazon.com/iFlight-Silicone-Temperature-Resistant-Flexible/dp/B071L7YC2F |
| M3/M4/M5 screw+nut assortment, 500pc | Amazon | not retrieved | — | https://www.amazon.com/Hosim-Assortment-Prototyping-Accessories-Quadcopter/dp/B0778NDDS6 |
| Landing gear reinforcement | — | no purchasable product exists | — | consistently DIY/3D-printed in every real hex build found — fold this into the v1 dock/bracket CAD design instead of buying it |
| Antenna mount: QwinOut plastic GPS folding mount | Amazon | ~$11 (AU listing, US price unconfirmed) | 8g | https://www.amazon.com/QWinOut-Plastic-Foldable-Quadcopter-Multirotor/dp/B01HEZZKIK |

Amazon blocked most direct automated fetches (403/500/503) — the products above are real, live-search-confirmed
listings, but re-check price/stock on the actual page before ordering.

## What needs a decision

1. **Budget ask is stale again.** Real current prices push both tiers well above what `pitch/Stardance_Pitch_Draft.md`
   currently states. Say the word and I'll update it again with these numbers — holding off since you may want
   to make cost-cutting calls first (e.g. cheaper battery, fewer spare props, cheaper charger).
2. **Water system tank/pump dimensions are unresolved**, not just imprecise — the two pump-spec clusters differ
   by ~14x in weight. This blocks precise CAD mounting geometry (see below).
