# EventLab Load Wait Build 2026-06-28

Portable Windows x64 build:

- `subaruu-eventlab-load-wait-portable-win-x64-20260628.zip`
- SHA256: `3E435A8CADFE1EDB0468C00319E96795BACA6F47BA1CECFBCF4360D32B5F410A`

## Changes

- Added the All-in-one tab `로딩` value.
- Default EventLab loading wait is 20 seconds.
- Slow PCs can raise `로딩` to 30-45 seconds if Enter is sent before the EventLab vehicle/manufacturer screen finishes loading.
- The value is used after EventLab map selection and after work-car selection before the final Enter.
- The package still does not include `subaruu.conf`, so existing user settings are not overwritten by the ZIP.

## Verification

- Published self-contained Windows x64 build succeeded.
- Manufacturer dry-run on the sparse selected-SUBARU report screen passed with selected SUBARU score `0.923`.
- Work-car dry-run on the default-blue 1998 SUBARU 4K card passed with exact card score `1.000`.
- ZIP contents were checked for `subaruu.exe`, `subaruu.default.conf`, EventLab templates, and no `subaruu.conf`.

## Reminder

This is an unofficial personal convenience tool. Use is entirely at your own risk.
