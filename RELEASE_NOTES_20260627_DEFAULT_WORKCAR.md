# Default Work-Car Portable Build 2026-06-27

## Download

- `subaruu-default-workcar-portable-win-x64-20260627.zip`
- SHA256: `EF5900F4AC069FECD5F1536CEA9107CFC0AA34392D8231A6F6DE7A574FBF74E4`

## Changed

- EventLab work-car recognition now targets the default blue `1998 SUBARU`
  Impreza 22B-STi first.
- Added a blue rally livery image only as an extra helper template.
- The macro no longer depends on a discontinued shared livery/decal to find the
  work car.
- Work-car matching now searches the actual car/body/card templates before the
  generic orange `전설` label, reducing false matches against unrelated legendary
  cars or top UI labels.
- Kept the previous Windows/Xbox Game UI foreground keyboard input fix.
- Kept the settings-safe packaging behavior: `subaruu.conf` is not included in
  the zip, and user settings are backed up before saving.

## Verified

- Built as Windows x64 self-contained portable package.
- Packaged dry-run selected the target 1998 Subaru card from the sample Subaru
  garage screen with score `0.947`.
- Confirmed the package includes `subaruu.default.conf` and does not include
  `subaruu.conf`.

## Notes

This is an unofficial personal convenience tool. Use is entirely at your own
risk. Game updates, garage state, DLC ownership, and menu position can change
behavior, so start with a short test run.
