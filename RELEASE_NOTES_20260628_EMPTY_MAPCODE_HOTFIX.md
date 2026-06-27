# Empty Map-Code Hotfix Build 2026-06-28

Portable Windows x64 build:

- `subaruu-empty-mapcode-hotfix-portable-win-x64-20260628.zip`
- SHA256: `F3020983EC57831B551E29FA32C61454D769A888511E7C2C33EA1FB3D737C4AB`

## Changes

- Fixed a leftover fallback that forced `113938786` when the EventLab map-code field was blank.
- The default config now leaves `EventLabCode=` and `TestEventLabCode=` blank.
- Empty EventLab map code uses the in-game `My Favorites` route.
- With empty map code, the macro skips the share-code input box and sends `PageDown` 7 times, then `Enter`, wait, `Enter`, wait.
- Non-empty map code still uses the share-code route with clipboard paste, verification, and foreground digit fallback.
- The package still does not include `subaruu.conf`, so existing user settings are not overwritten by the ZIP.

## Verification

- Published self-contained Windows x64 build succeeded.
- No `113938786` fallback remains in the executable code path.
- ZIP contents were checked: no `subaruu.conf`, and `subaruu.default.conf` contains blank `EventLabCode=` and `TestEventLabCode=`.
- Manufacturer dry-run on the sparse selected-SUBARU report screen passed with selected SUBARU score `0.923`.
- Work-car dry-run on the default-blue 1998 SUBARU 4K card passed with exact card score `1.000`.

## Reminder

This is an unofficial personal convenience tool. Use is entirely at your own risk.
