# 2026-06-28 - 이벤트랩 즐겨찾기 경로 빌드

맵 코드 입력창 대신 게임 안의 `내 즐겨찾기` 이벤트랩 경로로 들어가는 기능을 추가한 빌드입니다.

## 다운로드

- 파일: `subaruu-eventlab-favorites-portable-win-x64-20260628.zip`
- SHA256: `CF89CE2BE6651A52ED139935D7533057E04EFEF728D173422898CBF5957639AE`

## 바뀐 점

- 이벤트랩 맵 코드가 비어 있으면 `내 즐겨찾기` 경로를 사용합니다.
- 빈 맵 코드 상태에서는 공유코드 입력창을 열지 않습니다.
- 즐겨찾기 경로는 `PageDown` 7회, `Enter`, 대기, `Enter`, 대기 순서로 진행합니다.
- Xbox/Game Pass에서 Game UI 키보드가 뜨는 사용자는 이벤트랩 맵을 즐겨찾기하고 맵 코드 칸을 비우는 방식을 사용할 수 있습니다.
- 맵 코드가 입력되어 있으면 기존 공유코드 검색 경로를 유지합니다.
- 공유코드 입력은 클립보드 붙여넣기, 입력값 검증, 전경 숫자 입력 fallback 순서로 처리합니다.
- 배포 ZIP에는 `subaruu.conf`를 포함하지 않습니다.

## 검증한 내용

- Windows x64 self-contained 빌드 확인
- SUBARU 제조사 dry-run 통과
- 기본 파란 1998 SUBARU 4K 작업차 카드 dry-run 통과
- portable 폴더 기준 dry-run 통과
- ZIP 안에 `subaruu.exe`, `subaruu.default.conf`, 이벤트랩 템플릿 포함 확인
- ZIP 안에 `subaruu.conf` 미포함 확인

## 주의

이 빌드는 중간 단계 빌드입니다.
최신 사용자는 이후 menu-wait fix 빌드를 우선 받는 것이 좋습니다.
