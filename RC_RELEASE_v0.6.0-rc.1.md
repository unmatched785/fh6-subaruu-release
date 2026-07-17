# v0.6.0-rc.1 release record

This record identifies the exact RC artifact for the background-input experiment. Do not replace assets under the same tag; changed bytes require a new RC tag.

## Identity

| Field | Value |
| --- | --- |
| Product version | `0.6.0-rc.1` |
| Tag | `v0.6.0-rc.1` |
| Branch | `codex/background-mode-v0.6.0-rc.1` |
| Stable base | `v0.5.0` |
| Artifact source commit | `30466a7d89ba8ff20d13f06362af107400cc16f8` |
| Release date | `2026-07-17 KST` |
| Status | `ARTIFACT VALIDATED - AWAITING PUBLICATION AND GAME TEST` |

## RC acceptance

- [x] Background policy allows only Subaru run and challenge-only test.
- [x] Result OCR is forced off.
- [x] Test cycles are forced to one and purchase/mastery/delete are forced to zero.
- [x] Purchase, mastery, delete, wheelspin and all-in-one tabs are locked.
- [x] Background code digits and submit use target-window messages.
- [x] Foreground activation, screen capture and mouse click paths fail closed during a background run.
- [x] Minimized FH6 and failed target-window messages stop the run.
- [x] W and other held keys are released during cleanup.
- [ ] Real FH6 test with the game fully covered by a browser.
- [ ] Background W movement verified.
- [ ] Background challenge code entry verified.

## Artifact

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| `subaruu.zip` | `65,895,243` | `B486B2CDE2F79AE17764154A0B887667525C7E197433E9CAB02B0623701683D4` |
| `subaruu.exe` | `63,717,882` | `BEBED95875274981AA88B0E9858F7EF15667DF1E06D574FE35296E3865D89AEA` |

Package QA passed with 41 files, 40 manifest entries, 7 licenses, 3 versioned documents and all 7 packaged self-tests. The package identifies the source tree as clean. Immutable real-screen wheelspin OCR fixtures are intentionally outside this package and were not run; the background path disables all OCR.

## Publication

- [ ] Private source repository prerelease
- [ ] Public distribution repository prerelease
- [ ] Both ZIP assets re-downloaded and SHA-256 verified

