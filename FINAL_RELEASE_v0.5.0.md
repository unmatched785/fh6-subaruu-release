# v0.5.0 final release record

This record seals the exact `v0.5.0` artifact after clean-source packaging, package QA and publication to both GitHub repositories. Do not replace an asset under the same tag; changed bytes require a new version and a new acceptance run.

## Identity

| Field | Value |
| --- | --- |
| Product version | `0.5.0` |
| Tag | `v0.5.0` |
| Promotion branch | `codex/promote-v0.5.0-20260717` |
| RC base | `v0.5.0-rc.4` / `66cf20bb3f7f00a5aa18d952898f7db16ceefc7a` |
| Artifact source commit | `03c46f4b5740cee06700ec85d9c87d308a49a78d` |
| Canonical project | `src/FH6SubaruuWheelspin.csproj` |
| .NET SDK | `10.0.300` from `global.json` |
| Runtime | `win-x64`, self-contained, single-file |
| Release date | `2026-07-17 KST` |
| Status | `SEALED` |

## Supported baseline

- FH6 Korean UI
- FHD 1920 x 1080 recommended; QHD and 4K supported only at 16:9
- Full screen or borderless full screen recommended
- 120 FPS recommended; 60 FPS verified
- Maximum driving assists
- Skill HUD off, Next activity off, Pause on focus loss off
- First challenge starts in `1998 SUBARU IMPREZA 22B-STI VERSION`
- Challenge share code `122 697 651`

Xbox Game Pass or controller-first environments that retain a virtual keyboard or text focus after code entry are outside the current supported automatic path. This known limitation does not change the keyboard-path release baseline.

## Artifact identity

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| `subaruu.zip` | `65,889,709` | `F655C61F22E8B654B8CC7692BE1BD135CD3BBD9CCB634969DEE28974F0BC8899` |
| `subaruu.exe` inside the ZIP | `63,713,782` | `92AA81BC12B6EF346215DDBB6881074D5C7427E68E451BDFBEC725B868ABE99E` |
| `subaruu.zip.sha256` | `78` | records the ZIP hash above |

## Acceptance checklist

### Source and package

- [x] Source tree is clean at the artifact source commit.
- [x] `main` history and the RC.4 history are joined in the promotion branch.
- [x] Locked restore and Release publish succeed with SDK `10.0.300`.
- [x] `BUILD_INFO.txt` records version `0.5.0`, the exact source commit and a clean source tree.
- [x] ZIP sidecar and internal `SHA256SUMS.txt` validate.
- [x] Package contains no user configuration, logs, results, captures, PDBs or source files.
- [x] README, guide, starter guide, privacy file and licenses are present.

### Automated regression

- [x] Wheelspin run guard passes.
- [x] Wheelspin sale/slot policy passes.
- [x] Capture policy passes.
- [x] OCR native runtime and tessdata warm-up pass.
- [x] Delete year/brand FHD-to-4K template dry-run passes for Mazda, Revuelto and Subaru.
- [x] Reward report self-test passes.
- [x] Package documentation and default configuration name `0.5.0` and do not describe the current build as an RC.

### Live evidence and limitations

- [x] New challenge path has been repeatedly observed at approximately 10 SP per completion.
- [x] 111 runs preserve the 990 SP requirement even at the earlier 9 SP observation: `111 × 9 = 999`.
- [x] 60 FPS has been verified; 120 FPS remains recommended.
- [x] First-run Subaru work-car requirement and skill-HUD-off baseline are documented.
- [x] Real-screen OCR fixture regression is not claimed. A fixture is a preserved FH6 screenshot with a known expected OCR result, not merely a 16:9 resolution setting.
- [x] Destructive deletion and automatic sale remain screen-based, irreversible operations whose correctness is not guaranteed.

## Publication checklist

- [x] Create annotated tag `v0.5.0` at the exact artifact source commit.
- [x] Publish the same immutable `subaruu.zip` and `.sha256` to `unmatched785/fh6-subaruu`.
- [x] Publish the same immutable assets to `unmatched785/fh6-subaruu-release`.
- [x] Confirm both releases are non-draft, non-prerelease and selected as Latest.
- [x] Re-download both ZIP assets and confirm byte size `65,889,709` and SHA-256 `F655C61F22E8B654B8CC7692BE1BD135CD3BBD9CCB634969DEE28974F0BC8899` are identical.
- [x] Set this record to `SEALED` in this evidence-only commit without rebuilding or moving the tag.

Release pages:

- Private source repository: https://github.com/unmatched785/fh6-subaruu/releases/tag/v0.5.0
- Public distribution repository: https://github.com/unmatched785/fh6-subaruu-release/releases/tag/v0.5.0

## Rebuild command

```powershell
.\tools\Build-WheelspinPackage.ps1 -ReleaseName v0.5.0 -ArchiveName subaruu.zip
.\tools\Test-FinalPackage.ps1 `
  -ArchivePath .\src\release\v0.5.0\subaruu.zip `
  -ExpectedVersion 0.5.0 `
  -ExpectedSourceCommit (git rev-parse HEAD)
```

