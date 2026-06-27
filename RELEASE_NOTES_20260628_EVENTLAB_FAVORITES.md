# EventLab Favorites Build 2026-06-28

Portable Windows x64 build:

- `subaruu-eventlab-favorites-portable-win-x64-20260628.zip`
- SHA256: `CF89CE2BE6651A52ED139935D7533057E04EFEF728D173422898CBF5957639AE`

## Changes

- Empty EventLab map code now uses the in-game `My Favorites` route.
- With empty map code, the macro skips the share-code input box and sends `PageDown` 7 times, then `Enter`, wait, `Enter`, wait.
- Xbox/Game Pass users whose share-code input opens the Game UI keyboard should favorite the EventLab map and leave the map-code field empty.
- Non-empty map code still uses the share-code route.
- Share-code input now tries clipboard paste, verifies the pasted code by copying it back, then falls back to direct foreground digit input if verification fails.
- The package still does not include `subaruu.conf`, so existing user settings are not overwritten by the ZIP.

## Verification

- Published self-contained Windows x64 build succeeded.
- Manufacturer dry-run on the sparse selected-SUBARU report screen passed with selected SUBARU score `0.923`.
- Work-car dry-run on the default-blue 1998 SUBARU 4K card passed with exact card score `1.000`.
- Package dry-runs passed from the portable folder.
- ZIP contents were checked for `subaruu.exe`, `subaruu.default.conf`, EventLab templates, and no `subaruu.conf`.

## Reminder

This is an unofficial personal convenience tool. Use is entirely at your own risk.
