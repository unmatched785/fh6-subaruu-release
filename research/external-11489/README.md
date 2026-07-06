# External 11,489-slot wheelspin sample

이 디렉터리는 이미지로 확보한 외부 휠스핀 대형 표본을 구조화해 보관합니다.
기존 개인 실측 문서인 `WHEELSPIN_RESEARCH.md`와는 분리된 자료입니다.

## Source conditions

원본 이미지의 메모 기준 조건입니다.

```text
Total sample = 11,489 spins
Super Wheelspin = 3 spins로 계산
All Clothes / Horns / Emotes 획득 후 기록
획득 가능한 차량을 최소 1대씩 보유한 뒤 기록
연속 개봉 표본
게임 크래시로 일부 기록 누락 가능성 있음
```

이 표본은 `일반휠`과 `슈퍼휠`을 분리하지 않은 혼합 슬롯 표본입니다.
따라서 `W/S`, 즉 일반 슬롯과 슈퍼 슬롯의 상대 확률을 직접 계산하는 데 쓰면 안 됩니다.

## Files

| 파일 | 내용 |
| --- | --- |
| `summary.csv` | 전체 슬롯, CR/차량 보상 총량, 평균값 요약 |
| `cr_prizes.csv` | CR 보상 금액별 분포 |
| `car_rarity_summary.csv` | 차량 보상 희귀도별 분포 |
| `derived_metrics.csv` | Legendary/FE 비율, 가치 비중 등 계산값 |
| `common_vehicles_draft.csv` | Common 차량 90행 수동 전사 초안 |
| `common_vehicles_validation.md` | Common 차량 전사 합계 검증 메모 |
| `vehicle_level_schema.md` | 차량별 CSV로 전사할 때 사용할 스키마와 주의점 |

## Current status

현재 구조화 완료된 값은 이미지의 상단 집계표, CR 보상표, 희귀도별 차량 요약, Common 차량 상세 목록입니다.

Common 차량 상세 전사는 수량/판매가/총액 합계 검증을 통과했습니다.
다만 `WS / Xcl?` 컬럼은 원본 이미지와 제공 텍스트의 정렬이 완전하지 않으므로 아직 완전 검증값이 아닙니다.

차량별 전사는 아래 순서로 진행합니다.

```text
1. Common 차량 목록: 전사 완료, 합계 검증 완료, WS/Xcl 미검증
2. Rare 차량 목록
3. Epic 차량 목록
4. Legendary + FE 차량 목록
```

## Use in research

이 표본으로 할 수 있는 것:

```text
1. 전체 슬롯 기준 Legendary Car 확률 확인
2. 전체 슬롯 기준 FE 확률 확인
3. CR 보상 / 차량 보상 비율 확인
4. 차량 보상 가치가 전체 기대값에 미치는 영향 확인
5. Legendary/FE를 팔 때와 보유할 때의 평균값 차이 확인
6. 차량별 표가 완성되면 Wheelspin Exclusive 전체 드랍률 계산
```

이 표본으로 바로 하면 안 되는 것:

```text
1. 일반휠과 슈퍼휠의 직접 비교
2. 라부엘토작과 마즈다작의 W/S 직접 산출
3. 신규 계정에 그대로 기대값 적용
```
