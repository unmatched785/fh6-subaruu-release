# 2026-06-27 - 설정 보호 빌드

새 배포 ZIP을 기존 폴더에 덮어 풀었을 때 사용자 설정이 기본값으로 덮어써지는 문제를 막은 빌드입니다.

## 다운로드

- 파일: `subaruu-settings-safe-portable-win-x64-20260627.zip`
- SHA256: `BFE1EFDF308CF371D41F6FAA95F09425EAB0A42D27B13504356804931838912F`

## 바뀐 점

- 배포 ZIP에서 `subaruu.conf`를 제거했습니다.
- 첫 실행 기본값은 `subaruu.default.conf`에서 읽습니다.
- 사용자 설정은 계속 `subaruu.conf`에 저장합니다.
- 기존 `subaruu.conf`를 변경하기 전 `subaruu.conf.bak` 백업을 남깁니다.
- portable 패키지 안내 문구를 설정 보호 방식에 맞춰 수정했습니다.

## 유지된 내용

- Windows/Xbox Game UI 공유코드 전경 입력 대응
- 마즈다작 프리셋
- 당시 이벤트랩 이미지 인식 템플릿

## 주의

게임 업데이트, DLC 보유 상태, 차고 상태, 즐겨찾기 목록에 따라 메뉴 위치가 달라질 수 있습니다.
긴 작업 전에는 구매 위치와 작업차 위치를 본인 환경에서 확인하세요.
