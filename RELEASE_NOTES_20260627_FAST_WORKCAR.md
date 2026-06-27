# Fast Work-Car Portable Build 2026-06-27

## Download

- `subaruu-fast-workcar-portable-win-x64-20260627.zip`
- SHA256: `F24269F52D8AB84468D053054F5611070C2DD0ABEB4826023EB9E369B3669F45`

## Changed

- Added a 4K default blue `1998 SUBARU` work-car card helper template.
- Work-car recognition now checks exact default blue 22B card images first.
- If an exact card match reaches a strong score, the macro accepts it
  immediately and skips slower `1998 SUBARU` text and `전설` fallback scans.
- Body-only matching is stricter and used only as a backup, because similar blue
  Subaru favorites can reduce visual discrimination.
- Kept the optional blue rally livery helper, but the macro does not depend on
  any shared livery/decal being available.
- Kept the previous Windows/Xbox Game UI foreground keyboard input fix.
- Kept the settings-safe packaging behavior: `subaruu.conf` is not included in
  the zip, and user settings are backed up before saving.

## Verified

- Built as Windows x64 self-contained portable package.
- Packaged dry-run selected the provided default blue 4K card with exact-card
  score `1.000` in about `140ms`.
- Packaged dry-run selected the target 1998 Subaru card from the sample Subaru
  garage screen through the stricter body backup with score `0.947` in about
  `109ms`.
- Confirmed the package includes `subaruu.default.conf` and does not include
  `subaruu.conf`.

## Notes

This is an unofficial personal convenience tool. Use is entirely at your own
risk. Game updates, garage state, DLC ownership, and menu position can change
behavior, so start with a short test run. For EventLab image mode, the safest
setup is keeping only the target 1998 Subaru work car in favorites.
