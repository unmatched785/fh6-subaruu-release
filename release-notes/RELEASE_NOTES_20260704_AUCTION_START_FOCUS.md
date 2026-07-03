# 최신 권장 빌드 - 경매 시작 포커스 보정 2026-07-04

처음 받는 사람은 이 릴리즈만 받으세요.
이전 2026-07-03 이벤트랩 코드 입력과 작업차 인식 개선 빌드까지 포함한 최신 권장 빌드입니다.

## 다운로드

- Asset: `subaruu.zip`
- SHA256: `891EFACA81D2A1F53F47C2E43A22BD17035BF0D721F3DF84C59A38FE788E5D35`

## 변경

- 테스트런/올인원에서 구매 후 경매장으로 이동할 때 `경매 시작` 포커스를 보정합니다.
- 경매장 메뉴 포커스가 다른 항목에 남아 있어도 `경매 시작 > 차량 선택 목록`으로 들어가도록 보강했습니다.
- 이 구간에 `auction-start-focus` 로그를 남겨 새 빌드 적용 여부를 확인할 수 있습니다.

## 확인

- `dotnet build -c Release`
- `dotnet publish -c Release -r win-x64 --self-contained true`
- 테스트런 최소런 정상 완료
- ZIP 안쪽 루트 폴더가 `subaruu/` 하나인 것 확인
- ZIP 안에 `subaruu.conf`, `subaruu.conf.bak`, `log` 폴더가 포함되지 않는 것 확인
- 패키지 SHA256 계산 완료

## 문제 보고

문제가 생기면 `F2`로 즉시 멈추고, `subaruu.exe` 옆의 `log` 폴더와 `subaruu.conf`를 같이 보내주세요.
`last-run-status.txt`도 `log` 폴더 안에 함께 저장됩니다.

사용은 전적으로 사용자 본인 책임입니다.
매주 목요일 23:30 전후에는 제조사/차량 위치가 바뀔 수 있으니 반드시 테스트런으로 확인하세요.
