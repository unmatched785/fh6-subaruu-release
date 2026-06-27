# FH6 Subaruu - Game UI Keyboard Fix Portable 2026-06-27

Unofficial FH6 Subaruu personal convenience automation helper. Use at your own
risk.

## Included

- Windows x64 portable package
- Self-contained runtime bundle
- Mazda work preset configuration preserved from the previous release
- EventLab share-code input changed to foreground keyboard events
- Troubleshooting note for Windows/Xbox Game UI on-screen keyboard cases

## Why

Some Game Pass / Xbox Game UI environments open a separate share-code text box
and show the on-screen keyboard. In that state, sending digit key messages to
the game window can fail because the text field is not the game window itself.

This build sends only the EventLab share-code digits and search Enter as
foreground keyboard input. Do not click another window while the macro is
entering the code.

## Still Important

- Purchase manufacturer and vehicle positions are environment-specific and must
  be checked manually.
- Start with the minimal or recommended test run before a long run.
- If this still fails on a specific machine, use an EventLab favorite/manual
  route as a fallback until a separate favorite-entry mode exists.

## Hash

```text
3A8F16CD924826128D69874E8C6CEA3AEE6DAD70A184758080CB4550417813BC  subaruu-gameui-keyboard-fix-portable-win-x64-20260627.zip
```

