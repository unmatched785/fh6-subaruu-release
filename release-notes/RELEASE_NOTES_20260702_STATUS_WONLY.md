# 최신 권장 빌드 - 스바루런 입력 단순화와 실행 상태 기록 2026-07-02

처음 받는 사람은 이 릴리즈만 받으세요.
이전 2026-07-01 구매 메뉴 간격 조정까지 포함한 최신 권장 빌드입니다.

## 다운로드

- Asset: `subaruu.zip`
- SHA256: `3C5E59588A4DBF835FC9D90E5334C9ABAC3B36F00E5667A09D13E16F1E9DF1E6`

## 변경

- 스바루런 주행 입력을 `W` 단독 유지로 단순화했습니다.
- 기존 `W + ↑ 방향키` 동시 입력은 환경에 따라 다르게 처리될 수 있어 기본 입력에서 제외했습니다.
- 실행 중 현재 탭, 회차, 진행 단계, 마지막 정상 지점, 정지 사유를 `log/last-run-status.txt`에 저장합니다.
- 문제 보고 시 세션 로그와 함께 마지막 실행 상태를 더 빠르게 확인할 수 있습니다.
- README/GUIDE에 `last-run-status.txt` 안내와 `다음에 할 일` 설정 확인 안내를 보강했습니다.

## 확인

- `dotnet build -c Release`
- `dotnet publish -c Release -r win-x64 --self-contained true`
- ZIP 안쪽 루트 폴더가 `subaruu/` 하나인 것 확인
- ZIP 안에 `subaruu.conf`, `subaruu.conf.bak`, `log` 폴더가 포함되지 않는 것 확인
- ZIP 내부 README/GUIDE에서 `W` 단독 입력, `다음에 할 일`, `last-run-status.txt` 안내 확인
- 패키지 SHA256 계산 완료

## 문제 보고

문제가 생기면 `F2`로 즉시 멈추고, `subaruu.exe` 옆의 `log` 폴더와 `subaruu.conf`를 같이 보내주세요.
`last-run-status.txt`도 `log` 폴더 안에 함께 저장됩니다.

사용은 전적으로 사용자 본인 책임입니다.
매주 목요일 23:30 전후에는 제조사/차량 위치가 바뀔 수 있으니 반드시 테스트런으로 확인하세요.
