# FH6 Subaruu Releases

Release-only repository for FH6 Subaruu Windows x64 portable builds.

This repository publishes portable release assets only. It does not publish
source code, development logs, or private workspace history.

## Download

Latest release:

- `subaruu-eventlab-menu-wait-fix-portable-win-x64-20260628.zip`
- SHA256: `412FA3708A89B36C453C408C81050658D0A689543001D5869E7882C9274D3AD7`

## Notes

- This is an unofficial personal convenience tool.
- Use is entirely at your own risk.
- Game updates, resolution, garage state, DLC ownership, and menu position can
  change behavior.
- Purchase manufacturer and vehicle positions must be checked manually in your
  own environment.
- If the Windows/Xbox Game UI on-screen keyboard blocks share-code input,
  favorite the EventLab map and leave the map-code field empty. Empty map code
  uses the in-game `My Favorites` route instead of the share-code input box.
- Empty map-code EventLab menu selections use fixed 3-second waits. The Subaru
  Run tab `로딩 대기` value is used after selecting the work car, while the
  actual EventLab map loads.
- If a map code is entered, this build still tries clipboard paste first,
  verifies it, then falls back to direct foreground digit input.
- Release packages no longer include `subaruu.conf`; user settings are generated
  locally and backed up as `subaruu.conf.bak` before changes are saved.
- For EventLab image mode, the safest setup is keeping only the target 1998
  Subaru work car in favorites.
- Work-car image mode selects by keyboard first, verifies the selected card,
  and uses mouse click only as a backup.
- Sparse manufacturer lists where SUBARU is already selected are accepted
  without unnecessary grid movement.
- If EventLab loading is slow and Enter is sent too early, raise the Subaru Run
  tab `로딩 대기` value from the default 20 seconds to 30-45 seconds.
- EventLab work-car recognition targets exact default-blue 1998 Subaru card
  images first. Body-only matching is stricter and used only as a backup because
  similar blue Subaru favorites can reduce visual discrimination.
- Start with a short test run before using longer presets.

## Package

The portable package is self-contained for Windows x64. A separate .NET Desktop
Runtime install is not required.
