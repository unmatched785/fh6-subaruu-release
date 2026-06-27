# EventLab Code Wait Build 2026-06-28

Portable Windows x64 build:

- `subaruu-eventlab-code-wait-portable-win-x64-20260628.zip`
- SHA256: `66F5BE0F5B0429095345A6D940892187857D00D085EDEC0402A24679481381B5`

## Changes

- Moved the EventLab loading wait input to the Subaru Run tab as `로딩 대기`.
- Default EventLab loading wait remains 20 seconds.
- Slow PCs can raise `로딩 대기` to 30-45 seconds if Enter is sent before EventLab/map screens finish loading.
- The same value now widens the code-search result wait and map-selection Enter intervals, not only the final vehicle-entry wait.
- The package still does not include `subaruu.conf`, so existing user settings are not overwritten by the ZIP.

## Verification

- Published self-contained Windows x64 build succeeded.
- Manufacturer dry-run on the sparse selected-SUBARU report screen passed with selected SUBARU score `0.923`.
- Work-car dry-run on the default-blue 1998 SUBARU 4K card passed with exact card score `1.000`.
- ZIP contents were checked for `subaruu.exe`, `subaruu.default.conf`, EventLab templates, and no `subaruu.conf`.
- The previous `eventlab-load-wait-20260628` release was deleted before this corrected release was published.

## Reminder

This is an unofficial personal convenience tool. Use is entirely at your own risk.
