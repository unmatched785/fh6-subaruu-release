# FH6 Subaruu Releases

Release-only repository for FH6 Subaruu Windows x64 portable builds.

This repository publishes portable release assets only. It does not publish
source code, development logs, or private workspace history.

## Download

Latest release:

- `subaruu-eventlab-load-wait-portable-win-x64-20260628.zip`
- SHA256: `3E435A8CADFE1EDB0468C00319E96795BACA6F47BA1CECFBCF4360D32B5F410A`

## Notes

- This is an unofficial personal convenience tool.
- Use is entirely at your own risk.
- Game updates, resolution, garage state, DLC ownership, and menu position can
  change behavior.
- Purchase manufacturer and vehicle positions must be checked manually in your
  own environment.
- If the Windows/Xbox Game UI on-screen keyboard opens at the share-code input,
  this build sends the share code as foreground keyboard input.
- Release packages no longer include `subaruu.conf`; user settings are generated
  locally and backed up as `subaruu.conf.bak` before changes are saved.
- For EventLab image mode, the safest setup is keeping only the target 1998
  Subaru work car in favorites.
- Sparse manufacturer lists where SUBARU is already selected are accepted
  without unnecessary grid movement.
- If EventLab loading is slow and Enter is sent too early, raise the All-in-one
  tab `로딩` value from the default 20 seconds to 30-45 seconds.
- EventLab work-car recognition targets exact default-blue 1998 Subaru card
  images first. Body-only matching is stricter and used only as a backup because
  similar blue Subaru favorites can reduce visual discrimination.
- Start with a short test run before using longer presets.

## Package

The portable package is self-contained for Windows x64. A separate .NET Desktop
Runtime install is not required.
