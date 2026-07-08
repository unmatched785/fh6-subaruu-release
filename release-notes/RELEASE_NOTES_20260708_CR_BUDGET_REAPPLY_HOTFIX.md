# 긴급 패치 - 보유 CR 재적용 고정 문제 수정 2026-07-08

보유 CR을 낮게 입력해 `적용`한 뒤, 더 큰 보유 CR로 다시 `적용`해도 구매/강화/삭제 대수가 이전 저예산 값에 고정될 수 있던 문제를 수정했습니다.

## 다운로드

- Asset: `subaruu.zip`
- SHA256: `B61BCADBDEDDCBE8C752C98F71E6D3D58EABFA4D7EF42B54ADE2116F0B03C889`

## 변경

- `보유CR` 적용 시 화면에 줄어든 값이 아니라 내부 목표 프리셋 값을 기준으로 다시 계산합니다.
- 스바루작, 라부엘토작, 마즈다작의 1회차 구매/강화/삭제 구성을 먼저 유지하고, 보유 CR이 부족할 때 회차를 먼저 줄입니다.
- 예를 들어 스바루작 4회차가 1 CR 부족하고 3회차는 가능하면, 구매 33대, 강화 33대, 삭제 32대 구성으로 3회차까지만 제한합니다.
- 보유 CR이 충분해져도 회차를 자동으로 최대치까지 늘리지는 않습니다. 사용자가 정한 목표 회차 안에서만 복구하거나 줄입니다.
- 1회차 전체도 살 수 없을 때만 구매/강화/삭제 대수를 가능한 범위로 줄입니다.
- `F1` 시작 시에도 적용 버튼과 같은 목표 프리셋 기준으로 다시 예산 검사를 수행하고, 화면 값도 실제 실행값과 맞게 복구합니다.
- 하단 상태창의 예산 계산 로그에서 프리셋명을 빼고 `346,750 CR x 25대 x 1회 = 8,668,750 CR`처럼 수식 중심으로 줄였습니다.
- 예산 적용의 목표값을 설정 파일에 저장해, 앱을 닫았다가 다시 열어도 이전 저예산 결과에 갇히지 않도록 했습니다.
- README와 STARTER_GUIDE의 보유 CR 설명을 현재 보유금 입력 방식과 긴급 패치 기준으로 정리했습니다.

## 확인

- `dotnet build SubaruuDirectRun.csproj -c Release -v minimal`
- `dotnet publish SubaruuDirectRun.csproj -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true`
- ZIP 안쪽 루트 폴더가 `subaruu/` 하나인 것 확인
- ZIP 안에 `subaruu.conf`, `subaruu.conf.bak`, `log` 폴더가 포함되지 않는 것 확인
- ZIP SHA256 계산 완료

## 문제 보고

문제가 생기면 `F2`로 즉시 멈추고, `subaruu.exe` 옆의 `log` 폴더와 `subaruu.conf`를 같이 보내주세요.
`last-run-status.txt`도 `log` 폴더 안에 함께 저장됩니다.

사용은 전적으로 사용자 본인 책임입니다.
