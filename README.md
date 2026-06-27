# FH6 Subaruu Releases

Release-only repository for FH6 Subaruu Windows x64 portable builds.

This repository publishes portable release assets only. It does not publish
source code, development logs, or private workspace history.

## Download

Latest release:

- `subaruu-default-workcar-portable-win-x64-20260627.zip`
- SHA256: `EF5900F4AC069FECD5F1536CEA9107CFC0AA34392D8231A6F6DE7A574FBF74E4`

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
- EventLab work-car recognition targets the default blue 1998 Subaru 22B first;
  a blue rally livery image is included only as an extra helper template.
- Start with a short test run before using longer presets.

## Package

The portable package is self-contained for Windows x64. A separate .NET Desktop
Runtime install is not required.
