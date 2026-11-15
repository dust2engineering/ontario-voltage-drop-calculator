#!/usr/bin/env python3
"""Voltage drop calculator (CEC Rule 8-102 guideline: 3% branch / 5% total)."""
import argparse, json, os
D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "voltage-drop-data.json")))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--amps", type=float, required=True)
    p.add_argument("--length-m", type=float, required=True, help="one-way run length, m")
    p.add_argument("--size", required=True, choices=list(D["conductor_area_cmil"]))
    p.add_argument("--voltage", type=float, default=208)
    p.add_argument("--phase", default="3", choices=["1", "3"])
    p.add_argument("--material", default="copper_75C", choices=list(D["K_ohm_cmil_per_ft"]))
    a = p.parse_args()
    L_ft = a.length_m * 3.28084
    K = D["K_ohm_cmil_per_ft"][a.material]
    A = D["conductor_area_cmil"][a.size]
    vd = (2 if a.phase == "1" else 1.732) * K * a.amps * L_ft / A
    pct = vd / a.voltage * 100
    print(f"{a.size} {a.material}, {a.amps:g} A, one-way {a.length_m:g} m ({L_ft:.0f} ft), {a.voltage:g} V {'single' if a.phase == '1' else 'three'}-phase")
    print(f"Voltage drop: {vd:.2f} V = {pct:.2f}% -> {'within the 3% branch-circuit guideline' if pct <= 3 else 'ABOVE the 3% branch guideline - upsize the conductor or shorten the run' if pct <= 5 else 'ABOVE the 5% total guideline - upsize the conductor'}")

if __name__ == "__main__":
    main()
