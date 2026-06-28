# 2026-06-28 - 이벤트랩 로딩 대기값 분리 빌드

느린 PC에서 이벤트랩 맵 로딩 전에 Enter가 너무 빨리 들어가던 문제를 조절할 수 있게 만든 빌드입니다.

## 다운로드

- 파일: `subaruu-eventlab-code-wait-portable-win-x64-20260628.zip`
- SHA256: `66F5BE0F5B0429095345A6D940892187857D00D085EDEC0402A24679481381B5`

## 바뀐 점

- 이벤트랩 로딩 대기 입력값을 스바루런 탭의 `로딩 대기`로 옮겼습니다.
- 기본 로딩 대기는 20초입니다.
- 느린 PC에서는 `로딩 대기`를 30~45초로 올려 이벤트맵 로딩을 더 기다릴 수 있습니다.
- 당시 빌드에서는 코드 검색 결과 대기와 맵 선택 Enter 간격도 같은 값의 영향을 받도록 넓혔습니다.
- 배포 ZIP에는 계속 `subaruu.conf`를 포함하지 않습니다.

## 검증한 내용

- Windows x64 self-contained 빌드 확인
- SUBARU 제조사 dry-run 통과
- 기본 파란 1998 SUBARU 4K 작업차 카드 dry-run 통과
- ZIP 안에 `subaruu.exe`, `subaruu.default.conf`, 이벤트랩 템플릿 포함 확인
- ZIP 안에 `subaruu.conf` 미포함 확인
- 이전 `eventlab-load-wait-20260628` 릴리즈는 이 수정 릴리즈로 대체했습니다.

## 주의

이 빌드는 이후 menu-wait fix 빌드에서 다시 정리되었습니다.
최신 사용자는 최신 릴리즈를 우선 받는 것이 좋습니다.
