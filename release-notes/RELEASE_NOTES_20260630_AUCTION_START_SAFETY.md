# 최신 권장 빌드 - 경매 시작 안전 패치 2026-06-30

처음 받는 사람은 이 릴리즈만 받으세요.
이전 2026-06-29 릴리즈들의 수정 사항을 포함한 최신 권장 빌드입니다.

## 다운로드

- Asset: `subaruu.zip`
- SHA256: `95FA4523CB9E1AA7215792D4A82EF3A58C50100BB6955C2BD9D74F5724DBEA8A`

## 변경

- `스바루런` 탭의 `로딩 대기` 기본값을 25초로 조정했습니다.
- `슈퍼휠` 탭에 `경매장 대기` 값을 추가하고 기본값을 8초로 설정했습니다.
- 구매 후 `경매 시작` 차량 선택 목록이 보이는지 확인합니다.
- 차량 선택 목록 확인에 실패하면 슈퍼휠/삭제로 넘어가지 않고 멈춥니다.
- `스바루작`, `라부엘토작`, `마즈다작` 프리셋이 제조사/구매차 이동횟수까지 채웁니다.
- 배포 ZIP에 `eventlab-templates` 폴더가 안정적으로 포함되도록 빌드 설정을 보강했습니다.

## 테스트

- `dotnet publish -c Release -r win-x64 --self-contained true`
- ZIP 내부 `subaruu.default.conf`에서 `EventLabLoadWait=25`, `AuctionMenuWait=8` 확인
- ZIP 내부 `eventlab-templates` 포함 및 `subaruu.conf` 제외 확인
- 테스트런에서 구매 2대, 슈퍼휠 2대, 삭제 1대 완료 확인
- 세션 로그에서 `auctionWait=8s`, `auction-start-verify OK`, `natural-finish` 확인

## 문제 보고

문제가 생기면 `F2`로 즉시 멈추고, `subaruu.exe` 옆의 `log` 폴더와 `subaruu.conf`를 같이 보내주세요.

사용은 전적으로 사용자 본인 책임입니다.
매주 목요일 23:30 전후에는 제조사/차량 위치가 바뀔 수 있으니 반드시 테스트런으로 확인하세요.
