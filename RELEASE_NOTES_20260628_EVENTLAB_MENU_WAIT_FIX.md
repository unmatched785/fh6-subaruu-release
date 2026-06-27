# EventLab Menu-Wait Fix Build 2026-06-28

Portable Windows x64 build:

- `subaruu-eventlab-menu-wait-fix-portable-win-x64-20260628.zip`
- SHA256: `412FA3708A89B36C453C408C81050658D0A689543001D5869E7882C9274D3AD7`

## Changes

- Empty map-code mode is enabled for public distribution again.
- Empty map code uses the in-game `My Favorites` EventLab route.
- My Favorites route uses `PageDown` 7 times, then `Enter` 1/2, 3-second wait, `Enter` 2/2, 3-second wait.
- EventLab internal menu selections use fixed 3-second waits.
- The Subaru Run tab `로딩 대기` value is now reserved for the actual EventLab map loading wait after selecting the work car.
- Work-car image mode now selects by keyboard first: detect the target card, move with Up/Down, verify the selected card, then press Enter.
- Mouse click remains only as a backup if keyboard selection verification fails.
- Non-empty map code still uses the share-code route with clipboard paste, verification, and foreground digit fallback.
- The package still does not include `subaruu.conf`, so existing user settings are not overwritten by the ZIP.

## Verification

- Published self-contained Windows x64 build succeeded.
- User local run confirmed the empty map-code favorites route works.
- ZIP contents were checked: no `subaruu.conf`, and `subaruu.default.conf` contains blank `EventLabCode=` and `TestEventLabCode=`.
- Manufacturer dry-run on the sparse selected-SUBARU report screen passed with selected SUBARU score `0.923`.
- Work-car dry-run on the default-blue 1998 SUBARU 4K card passed with exact card score `1.000` and `runtimeSelection=keyboard-first`.

## Reminder

This is an unofficial personal convenience tool. Use is entirely at your own risk.
