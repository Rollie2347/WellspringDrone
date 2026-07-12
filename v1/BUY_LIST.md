# v1 Buy List — live vendor links (checked 2026-07-12)

Real, currently-live listings for the locked BOM in `CLAUDE.md`. Prices and stock change — re-verify before
ordering if this file is more than a few weeks old. Every weight already cited in `v1/power_budget.py` was
re-confirmed against the live vendor page in this pass (no discrepancies found).

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
