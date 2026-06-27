# subaruu-settings-safe-portable-win-x64-20260627

Settings-protection release for the FH6 Subaruu portable build.

## Download

- Asset: `subaruu-settings-safe-portable-win-x64-20260627.zip`
- SHA256: `BFE1EFDF308CF371D41F6FAA95F09425EAB0A42D27B13504356804931838912F`

## Changed

- The release ZIP no longer ships `subaruu.conf`, so extracting a new build over
  an existing folder should not overwrite a user's saved settings.
- First-run defaults now live in `subaruu.default.conf`.
- The app still saves personal settings to `subaruu.conf`.
- Before changing an existing `subaruu.conf`, the app writes
  `subaruu.conf.bak`.
- Portable package notes were updated to explain the new settings behavior.

## Kept

- Windows/Xbox Game UI foreground share-code input fix.
- Mazda work preset and current EventLab vision templates.

## Reminder

Use is at your own risk. Menu positions can change with game updates, DLC
ownership, garage state, and favorite lists. Check purchase and work-car
positions in your own environment before long runs.
