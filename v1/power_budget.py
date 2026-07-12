"""v1 thrust/power budget calculator for the Recommended-tier BOM in CLAUDE.md.

Every SOURCED constant below is cited to a real vendor/datasheet page (checked July 2026).
Every UNSOURCED constant is left as None on purpose -- no BOM line was locked to a specific
product for these, so there's no real weight to cite yet. The calculator reports AUW as a
floor estimate (known components only) and prints which line items are still missing so it's
obvious the true AUW will be higher. Fill in the None values with real numbers once those
parts are picked, then re-run.

Motor + prop thrust/current data source: T-Motor MN4014 KV400 official test data,
https://store.tmotor.com/product/mn4014-kv400-motor-navigator-type.html (T-Motor 16x5.4 CF
propeller, 6S / 22.2V). This is the specific in-range candidate (400KV, 16-17in, 6S) picked to
match the Recommended-tier BOM description in CLAUDE.md ("~400-500KV, sized for 15-17in props").
"""

MOTOR_COUNT = 6

# --- Sourced component masses (grams) ---
FRAME_G = 2000.0           # Tarot X6 1000mm-class hex frame TL6X001; store.foxtech.com / readymaderc.com
FC_SET_G = 73.0            # Cube Orange+ Standard Set (module + carrier board + Power Brick Mini + cables); bzbuas.com
GPS_G = 33.0               # CUAV NEO 3 Pro (NEO-M9N + RM3100 compass); doc.cuav.net
TELEMETRY_AIR_G = 14.5     # RFD900x-US, single airborne unit (ground unit doesn't fly); readymaderc.com / worldronemarket.com
ESC_EACH_G = 53.0          # Hobbywing XRotor Pro H60A, 40A continuous / 60A rated, 4-6S; hobbywingdirect.com
MOTOR_EACH_G = 171.0       # T-Motor MN4014 KV400 with cables; store.tmotor.com
PROP_EACH_G = 25.0         # T-Motor P16x5.4 CF, one complete propeller; store.tmotor.com
BATTERY_FLYING_G = 2650.0  # Tattu Plus 22000mAh 6S1P 25C -- ONE battery airborne (BOM's x2 is a hot-swap spare, not both flying); genstattu.com
BATTERY_CAPACITY_MAH = 22000.0

# --- Unsourced component masses (grams) -- no specific product picked yet, do not guess ---
TANK_SHELL_G = None        # empty 5L tank shell -- not sourced to a specific product
PUMP_G = None              # e.g. "XTL-3210 class" 12/24V diaphragm pump named in the BOM --
                            # reseller listings for this part disagree wildly (72g to 1060g+
                            # depending on seller/packaging); get the real number from whichever
                            # listing is actually ordered
SOLENOID_VALVES_G = None   # x2 solenoid nozzle valves -- not sourced
TUBING_FITTINGS_G = None   # -- not sourced
MISC_HARDWARE_G = None     # wiring, connectors, fasteners, landing gear reinforcement, antenna mounts -- not sourced

WATER_PAYLOAD_G_MIN = 1893.0   # 0.5 gal
WATER_PAYLOAD_G_MAX = 7571.0   # 2.0 gal
TANK_CAPACITY_FULL_G = 5000.0  # 5L tank BOM line, full-tank worst case

# (throttle_pct, current_A, thrust_g) per motor, T-Motor MN4014 KV400 + 16x5.4 CF prop, 6S
THRUST_TABLE = [
    (50, 6.4, 1410),
    (65, 11.0, 1920),
    (75, 14.6, 2380),
    (85, 19.1, 2790),
    (100, 22.5, 3020),
]


def known_dry_mass_g():
    return (
        FRAME_G + FC_SET_G + GPS_G + TELEMETRY_AIR_G
        + ESC_EACH_G * MOTOR_COUNT + MOTOR_EACH_G * MOTOR_COUNT
        + PROP_EACH_G * MOTOR_COUNT + BATTERY_FLYING_G
    )


def unsourced_items():
    items = {
        "tank_shell_g": TANK_SHELL_G,
        "pump_g": PUMP_G,
        "solenoid_valves_g": SOLENOID_VALVES_G,
        "tubing_fittings_g": TUBING_FITTINGS_G,
        "misc_hardware_g": MISC_HARDWARE_G,
    }
    return {k: v for k, v in items.items() if v is None}


def interp_thrust_table(per_motor_thrust_needed_g):
    """Linearly interpolate (throttle%, current_A) for a target per-motor thrust.
    Returns (throttle_pct, current_A, out_of_range) -- out_of_range True means the AUW
    cannot hover within the tested envelope (at/above 100% throttle)."""
    table = THRUST_TABLE
    if per_motor_thrust_needed_g <= table[0][2]:
        return table[0][0], table[0][1], False
    if per_motor_thrust_needed_g >= table[-1][2]:
        return table[-1][0], table[-1][1], True
    for (t0, c0, g0), (t1, c1, g1) in zip(table, table[1:]):
        if g0 <= per_motor_thrust_needed_g <= g1:
            frac = (per_motor_thrust_needed_g - g0) / (g1 - g0)
            return t0 + frac * (t1 - t0), c0 + frac * (c1 - c0), False
    raise AssertionError("unreachable")


def run(water_payload_g, label):
    dry = known_dry_mass_g()
    auw = dry + water_payload_g
    per_motor = auw / MOTOR_COUNT
    max_thrust_total = MOTOR_COUNT * THRUST_TABLE[-1][2]
    margin_pct = (max_thrust_total / auw - 1.0) * 100.0
    throttle, current_per_motor, out_of_range = interp_thrust_table(per_motor)
    total_current = current_per_motor * MOTOR_COUNT
    usable_mah = BATTERY_CAPACITY_MAH * 0.8  # 80% usable -- standard LiPo/Li-ion safety margin, not full discharge

    print(f"--- {label} ---")
    print(f"known dry mass (excludes TBD hardware listed above): {dry:.0f} g")
    print(f"water payload: {water_payload_g:.0f} g")
    print(f"AUW (floor estimate): {auw:.0f} g ({auw / 1000:.2f} kg)")
    print(f"max thrust @ 100% throttle, 6 motors: {max_thrust_total:.0f} g")
    print(f"thrust margin: {margin_pct:.0f}%")
    if out_of_range:
        print("WARNING: required hover throttle is at/above the top of the tested thrust table -- this AUW cannot hover on this motor/prop combo")
    else:
        print(f"est. hover throttle: {throttle:.0f}%  |  est. current per motor: {current_per_motor:.1f} A  |  est. total current: {total_current:.1f} A")
        hover_minutes = (usable_mah / 1000.0) / total_current * 60.0
        print(f"est. hover-only flight time (80% usable battery): {hover_minutes:.1f} min")
    print()


if __name__ == "__main__":
    missing = unsourced_items()
    if missing:
        print("UNSOURCED COMPONENTS -- excluded from AUW below, so the real AUW will be higher than shown:")
        for k in missing:
            print(f"  - {k}")
        print()

    run(0.0, "Dry (no water payload)")
    run(WATER_PAYLOAD_G_MIN, "Min mission payload (0.5 gal)")
    run(WATER_PAYLOAD_G_MAX, "Max mission payload (2.0 gal)")
    run(TANK_CAPACITY_FULL_G, "Full 5L tank (worst case)")
