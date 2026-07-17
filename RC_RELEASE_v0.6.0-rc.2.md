# v0.6.0-rc.2 release record

This record identifies the exact RC artifact for the background W focus-recovery experiment. Do not replace assets under the same tag; changed bytes require a new RC tag.

## Identity

| Field | Value |
| --- | --- |
| Product version | `0.6.0-rc.2` |
| Tag | `v0.6.0-rc.2` |
| Branch | `codex/background-w-reassert-v0.6.0-rc.2` |
| Stable base | `v0.5.0` |
| RC base | `v0.6.0-rc.1` |
| Artifact source commit | `03367c1ab3fca8aefdb887035438d828a47eb23b` |
| Release date | `2026-07-17 KST` |
| Status | `PUBLISHED - AWAITING GAME TEST` |

## RC acceptance

- [x] Foreground-window transitions trigger immediate W reassertion while W is held.
- [x] A 750ms target-window keepalive covers activation-processing races.
- [x] Reassertion targets only the FH6 window and does not use global keyboard injection.
- [x] W-up disables keepalive before cleanup.
- [x] Background restrictions from RC.1 remain unchanged.
- [ ] Real FH6 Alt+Tab round trip while driving.
- [ ] Browser keyboard and mouse remain unaffected during the round trip.

## Artifact

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| `subaruu.zip` | `65,896,571` | `0C60176E9201C6D036A4A76E693E6E442991F07ABB7CDA617D07C9540A2EC0CE` |
| `subaruu.exe` | `63,718,517` | `B74C39729C7D7BF81E01CF8013966D55B3B0EFBF2F0EAAED79A3E94B48DBE1FC` |

Package QA passed with 41 files, 40 manifest entries, 7 licenses, 3 versioned documents and all 7 packaged self-test suites. The package identifies the source tree as clean. Immutable real-screen wheelspin OCR fixtures are intentionally outside this package and were not run; the background path disables all OCR.

## Publication

- [x] [Private source repository prerelease](https://github.com/unmatched785/fh6-subaruu/releases/tag/v0.6.0-rc.2)
- [x] [Public distribution repository prerelease](https://github.com/unmatched785/fh6-subaruu-release/releases/tag/v0.6.0-rc.2)
- [x] Both ZIP assets re-downloaded and SHA-256 verified

Both releases are non-draft prereleases with `subaruu.zip` and `subaruu.zip.sha256`. Re-downloaded ZIPs were `65,896,571` bytes and matched the recorded SHA-256. The stable `v0.5.0` release remains Latest in both repositories.

