#!/usr/bin/env python3
"""Validate the external 11,489-slot wheelspin transcription files.

Run from repository root:

    python research/external-11489/validate_external_11489.py

The script intentionally validates only numeric fields that should be stable:
row counts, quantities, total sell values, and WX reference-match totals.
It does not validate Xcl/Car Mastery columns because those are not fully structured yet.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, Iterable, Tuple

ROOT = Path(__file__).resolve().parent

VEHICLE_EXPECTED: Dict[str, Tuple[str, int, int, int]] = {
    "common_vehicles_draft.csv": ("Common", 90, 1099, 27_771_500),
    "rare_vehicles_draft.csv": ("Rare", 143, 730, 37_341_500),
    "epic_vehicles_draft.csv": ("Epic", 120, 547, 68_214_250),
    "legendary_vehicles_draft.csv": ("Legendary", 70, 182, 434_971_000),
    "forza_edition_vehicles_draft.csv": ("Forza Edition", 8, 182, 59_125_000),
}

TOTAL_EXPECTED = {
    "car_qty": 2_740,
    "car_value": 627_423_250,
}

WX_EXPECTED = {
    "rows": 46,
    "qty": 339,
    "value": 117_475_000,
    "non_fe_qty": 157,
    "non_fe_value": 58_350_000,
    "fe_qty": 182,
    "fe_value": 59_125_000,
}

SUMMARY_EXPECTED = {
    "total_slots": 11_489,
    "cr_prize_slots": 8_749,
    "car_prize_slots": 2_740,
    "total_cr_prize_value": 457_147_000,
    "total_car_prize_value": 627_423_250,
    "total_value_all_sold": 1_084_570_250,
    "avg_per_spin_all_sold": 94_401,
    "avg_per_spin_keep_legendary_fe": 51_395,
    "avg_per_spin_cr_only": 39_790,
}


def read_csv(path: Path) -> Iterable[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        yield from csv.DictReader(f)


def parse_int(value: str) -> int:
    return int(value.replace(",", "").strip())


def assert_equal(label: str, actual: int, expected: int) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: actual={actual:,} expected={expected:,}")


def validate_vehicle_files() -> tuple[int, int]:
    total_qty = 0
    total_value = 0

    for filename, (rarity, expected_rows, expected_qty, expected_value) in VEHICLE_EXPECTED.items():
        rows = list(read_csv(ROOT / filename))
        qty = sum(parse_int(r["qty"]) for r in rows)
        value = sum(parse_int(r["total_sell_value_cr"]) for r in rows)

        assert_equal(f"{rarity} rows", len(rows), expected_rows)
        assert_equal(f"{rarity} qty", qty, expected_qty)
        assert_equal(f"{rarity} value", value, expected_value)

        total_qty += qty
        total_value += value

    assert_equal("total car qty", total_qty, TOTAL_EXPECTED["car_qty"])
    assert_equal("total car value", total_value, TOTAL_EXPECTED["car_value"])
    return total_qty, total_value


def validate_wx_reference() -> tuple[int, int, int, int]:
    rows = list(read_csv(ROOT / "wheelspin_only_external_match.csv"))
    qty = sum(parse_int(r["external_qty"]) for r in rows)
    value = sum(parse_int(r["external_total_sell_value_cr"]) for r in rows)
    fe_rows = [r for r in rows if r["external_rarity"] == "Forza Edition"]
    non_fe_rows = [r for r in rows if r["external_rarity"] != "Forza Edition"]
    fe_qty = sum(parse_int(r["external_qty"]) for r in fe_rows)
    fe_value = sum(parse_int(r["external_total_sell_value_cr"]) for r in fe_rows)
    non_fe_qty = sum(parse_int(r["external_qty"]) for r in non_fe_rows)
    non_fe_value = sum(parse_int(r["external_total_sell_value_cr"]) for r in non_fe_rows)

    assert_equal("WX rows", len(rows), WX_EXPECTED["rows"])
    assert_equal("WX qty", qty, WX_EXPECTED["qty"])
    assert_equal("WX value", value, WX_EXPECTED["value"])
    assert_equal("WX non-FE qty", non_fe_qty, WX_EXPECTED["non_fe_qty"])
    assert_equal("WX non-FE value", non_fe_value, WX_EXPECTED["non_fe_value"])
    assert_equal("FE qty in WX reference", fe_qty, WX_EXPECTED["fe_qty"])
    assert_equal("FE value in WX reference", fe_value, WX_EXPECTED["fe_value"])
    return qty, value, non_fe_qty, non_fe_value


def validate_summary() -> None:
    rows = {r["metric"]: r for r in read_csv(ROOT / "summary.csv")}
    for metric, expected in SUMMARY_EXPECTED.items():
        assert_equal(f"summary {metric}", parse_int(rows[metric]["value"]), expected)


def main() -> int:
    validate_summary()
    total_qty, total_value = validate_vehicle_files()
    wx_qty, wx_value, non_fe_qty, non_fe_value = validate_wx_reference()

    print("PASS external 11,489 validation")
    print(f"car_qty={total_qty:,}")
    print(f"car_value={total_value:,}")
    print(f"wx_qty={wx_qty:,}")
    print(f"wx_value={wx_value:,}")
    print(f"wx_non_fe_qty={non_fe_qty:,}")
    print(f"wx_non_fe_value={non_fe_value:,}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
