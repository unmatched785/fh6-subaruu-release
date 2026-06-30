# 최신 권장 빌드 - 구매 위치 진입 대기 보강 2026-06-30

처음 받는 사람은 이 릴리즈만 받으세요.
이전 2026-06-30 경매 시작 안전 패치까지 포함한 최신 권장 빌드입니다.

## 다운로드

- Asset: `subaruu.zip`
- SHA256: `1227F76D8383391C5F0AD86424D7DBB1F2D56EED8055D442E36A9D40195B19B6`

## 변경

- 스바루런 후 구매 위치로 들어가기 전 고정 20초 대기를 `스바루런` 탭의 `로딩 대기` 값에 연결했습니다.
- 느린 PC에서 페스티벌 복귀가 늦어 자동차 매장/상품권 화면으로 빠지는 경우 `로딩 대기`를 30~45초로 올려 테스트할 수 있습니다.
- 이 문제는 `경매장 대기`가 아니라 `로딩 대기`로 조절한다는 안내를 README/GUIDE에 추가했습니다.
- 세션 로그에 `purchase-entry-wait` 이벤트가 남습니다.

## 유지

- `로딩 대기` 기본값은 25초입니다.
- `경매장 대기` 기본값은 8초입니다.
- 구매 후 `경매 시작` 차량 선택 목록 확인에 실패하면 슈퍼휠/삭제로 넘어가지 않고 멈춥니다.

## 테스트

- `dotnet build -c Release`
- `dotnet publish -c Release -r win-x64 --self-contained true`
- ZIP 내부 `subaruu.default.conf`에서 `EventLabLoadWait=25`, `AuctionMenuWait=8` 확인
- ZIP 내부 `eventlab-templates` 포함 및 `subaruu.conf` 제외 확인

## 문제 보고

문제가 생기면 `F2`로 즉시 멈추고, `subaruu.exe` 옆의 `log` 폴더와 `subaruu.conf`를 같이 보내주세요.

사용은 전적으로 사용자 본인 책임입니다.
매주 목요일 23:30 전후에는 제조사/차량 위치가 바뀔 수 있으니 반드시 테스트런으로 확인하세요.
