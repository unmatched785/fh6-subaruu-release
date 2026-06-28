# 2026-06-28 - 빈 맵 코드 핫픽스

맵 코드 칸을 비워도 내부 fallback 때문에 특정 코드가 다시 입력되던 문제를 수정한 핫픽스입니다.

## 다운로드

- 파일: `subaruu-empty-mapcode-hotfix-portable-win-x64-20260628.zip`
- SHA256: `F3020983EC57831B551E29FA32C61454D769A888511E7C2C33EA1FB3D737C4AB`

## 바뀐 점

- 이벤트랩 맵 코드가 비어 있을 때 `113938786`으로 강제 fallback되던 잔여 코드를 제거했습니다.
- 기본 설정의 `EventLabCode=`와 `TestEventLabCode=`를 빈 값으로 유지했습니다.
- 빈 맵 코드는 게임 안의 `내 즐겨찾기` 경로를 사용합니다.
- 빈 맵 코드 상태에서는 공유코드 입력창을 건너뛰고 `PageDown` 7회, `Enter`, 대기, `Enter`, 대기 순서로 진행합니다.
- 맵 코드가 입력되어 있으면 기존 공유코드 입력 경로를 사용합니다.
- 배포 ZIP에는 계속 `subaruu.conf`를 포함하지 않습니다.

## 검증한 내용

- Windows x64 self-contained 빌드 확인
- 실행 코드 경로에 `113938786` fallback이 남아 있지 않은 것 확인
- ZIP 안에 `subaruu.conf` 미포함 확인
- `subaruu.default.conf`의 `EventLabCode=`와 `TestEventLabCode=`가 비어 있는 것 확인
- SUBARU 제조사 dry-run 통과
- 기본 파란 1998 SUBARU 4K 작업차 카드 dry-run 통과

## 주의

이 빌드는 빈 맵 코드 동작을 바로잡은 핫픽스입니다.
최신 사용자는 이후 menu-wait fix 빌드를 우선 받는 것이 좋습니다.
