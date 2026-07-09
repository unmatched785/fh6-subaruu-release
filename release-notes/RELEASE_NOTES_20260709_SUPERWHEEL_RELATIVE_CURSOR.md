# 슈퍼휠 강화 상대 좌표 선택 2026-07-09

슈퍼휠/강화 차량 선택 흐름을 더 짧게 조정한 릴리즈입니다.

## 다운로드

- Asset: `subaruu.zip`
- SHA256: `7F858246DB88917A0DA582BD441351F314C6F14CCC8C39116E1690516492C701`

## 변경

- 슈퍼휠/강화 단계에서 반복적으로 제조사/필터 전체 재적용을 하던 흐름을 상대 좌표 이동 방식으로 변경했습니다.
- 최근 추가 정렬은 차량마다 계속 적용합니다.
- 테스트런 권장값 9대 기준 2회차 자연 종료를 확인했습니다.

## 확인

- `dotnet publish SubaruuDirectRun.csproj -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true`
- ZIP 안쪽 루트 폴더가 `subaruu/` 하나인 것 확인
- ZIP 안에 `subaruu.conf`, `subaruu.conf.bak`, `log` 폴더가 포함되지 않는 것 확인
- ZIP SHA256 계산 완료
- 테스트런 9대 x 2회차 `natural-finish` 확인

## 문제 보고

강화 단계에서 엉뚱한 차량을 고르거나, 포인트가 부족하거나, 이벤트랩 시간이 비정상적으로 느리면 `F2`로 즉시 멈추고 `subaruu.exe` 옆의 `log` 폴더와 `subaruu.conf`를 같이 보내주세요.
`last-run-status.txt`도 `log` 폴더 안에 함께 저장됩니다.

사용은 전적으로 사용자 본인 책임입니다.
