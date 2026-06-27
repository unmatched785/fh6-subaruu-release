# Manufacturer Selected Fix Portable Build 2026-06-27

## Download

- `subaruu-manufacturer-selected-fix-portable-win-x64-20260627.zip`
- SHA256: `E5A49CE73FC20D52DA045929D3DB3F9DA95359994837DE86EC8488370A6580BB`

## Changed

- Fixed a freeze-like EventLab image-mode case on sparse manufacturer lists where
  SUBARU is already selected and is the only visible manufacturer item.
- Already-selected SUBARU now passes at score `0.920` instead of `0.930`.
- If the selected cell passes, the macro skips the surrounding manufacturer grid
  scan and uses movement `0,0`.
- Kept the generic manufacturer grid threshold at `0.800`.
- Kept the WULING safety margin: observed selected WULING samples around `0.887`
  remain below the new selected-SUBARU threshold.
- Kept the fast exact-card work-car recognition from the previous build.
- Kept the settings-safe packaging behavior: `subaruu.conf` is not included in
  the zip, and user settings are backed up before saving.

## Verified

- Built as Windows x64 self-contained portable package.
- Sparse selected-SUBARU screenshot: selected score `0.923`, accepted with
  movement `0,0`.
- WULING-selected screenshots: selected scores `0.880` and `0.887`, not accepted
  as selected SUBARU.
- Default blue 4K work-car card still matches as exact card with score `1.000`.
- Confirmed the package includes `subaruu.default.conf` and does not include
  `subaruu.conf`.

## Notes

This is an unofficial personal convenience tool. Use is entirely at your own
risk. Game updates, resolution, garage state, DLC ownership, and menu position
can change behavior, so start with a short test run.
