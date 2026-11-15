# Voltage Drop Calculator (Ontario / CEC)

Calculates voltage drop for a feeder or branch circuit from load current, one-way run length, conductor size and material, and reports it against the Canadian Electrical Code Rule 8-102 guidelines of 3% per branch circuit and 5% total.

**Live web tool:** https://dust2engineering.github.io/ontario-voltage-drop-calculator/web/

## How it works

- VD = 2 x K x I x L / A (single-phase) or 1.732 x K x I x L / A (three-phase), L in feet, A in circular mils.
- K = 12.9 ohm-cmil/ft for copper and 21.2 for aluminum at 75 C.

## Data in this repository

- voltage-drop-data.json — conductor circular-mil areas and constants, machine-readable.

## Command line

```bash
python3 voltage_drop.py --amps 60 --length-m 45 --size '6 AWG' --voltage 208 --phase 3
```

## Worked examples

- [rooftop-feeder-60a.md](examples/rooftop-feeder-60a.md)
- [parking-lighting-16a.md](examples/parking-lighting-16a.md)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Electrical. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
