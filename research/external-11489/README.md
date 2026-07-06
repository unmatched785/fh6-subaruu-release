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
| `ANALYSIS.md` | 외부 11,489-slot 표본 최종 해석 문서 |
| `validation_report.md` | 검증 스크립트 실행 결과 요약 |
| `validate_external_11489.py` | CSV 합계 검증 스크립트 |
| `summary.csv` | 전체 슬롯, CR/차량 보상 총량, 평균값 요약 |
| `cr_prizes.csv` | CR 보상 금액별 분포 |
| `car_rarity_summary.csv` | 차량 보상 희귀도별 분포 |
| `derived_metrics.csv` | Legendary/FE 비율, 가치 비중 등 계산값 |
| `common_vehicles_draft.csv` | Common 차량 90행 수동 전사 초안 |
| `common_vehicles_validation.md` | Common 차량 전사 합계 검증 메모 |
| `rare_vehicles_draft.csv` | Rare 차량 143행 수동 전사 초안 |
| `rare_vehicles_validation.md` | Rare 차량 전사 합계 검증 메모 |
| `epic_vehicles_draft.csv` | Epic 차량 120행 수동 전사 초안 |
| `epic_vehicles_validation.md` | Epic 차량 전사 합계 검증 메모 |
| `legendary_vehicles_draft.csv` | Legendary 차량 70행 수동 전사 초안 |
| `forza_edition_vehicles_draft.csv` | FE 차량 8행 수동 전사 초안 |
| `legendary_fe_vehicles_validation.md` | Legendary/FE 차량 전사 합계 검증 메모 |
| `wheelspin_only_reference.csv` | 별도 기준으로 확보한 휠스핀 전용/보상 차량 45종 목록 |
| `wheelspin_only_external_match.csv` | 기준 목록 45종을 외부 11,489 슬롯 표본에 매칭한 결과 |
| `wheelspin_exclusive_summary_reference.csv` | 기준 목록 기반 WX 요약값 |
| `wheelspin_exclusive_summary_draft.csv` | 이미지의 WS 컬럼을 직접 읽은 초기 초안. reference 파일이 우선 |
| `name_aliases.csv` | 이름 정규화/별칭 메모 |
| `ws_xcl_interpretation.md` | WS / Xcl 해석 메모 |
| `vehicle_level_schema.md` | 차량별 CSV로 전사할 때 사용할 스키마와 주의점 |

## Current status

현재 구조화 완료된 값은 이미지의 상단 집계표, CR 보상표, 희귀도별 차량 요약, Common/Rare/Epic/Legendary/FE 차량 상세 목록입니다.

차량명, 수량, 즉시판매가, 즉시판매 총액은 모든 희귀도에서 합계 검증을 통과했습니다.
`WS / Xcl?` 판정은 이미지 직접 판독값보다 `wheelspin_only_reference.csv`를 우선합니다.

차량별 전사 상태:

```text
1. Common 차량 목록: 전사 완료, 합계 검증 완료
2. Rare 차량 목록: 전사 완료, 합계 검증 완료
3. Epic 차량 목록: 전사 완료, 합계 검증 완료
4. Legendary 차량 목록: 전사 완료, 합계 검증 완료
5. FE 차량 목록: 전사 완료, 합계 검증 완료
6. WX 구분: wheelspin_only_reference.csv 기준으로 별도 매칭 완료
```

전체 차량 전사 합계:

```text
Common qty = 1,099 / value = 27,771,500 CR
Rare qty = 730 / value = 37,341,500 CR
Epic qty = 547 / value = 68,214,250 CR
Legendary qty = 182 / value = 434,971,000 CR
FE qty = 182 / value = 59,125,000 CR
Total car qty = 2,740 / value = 627,423,250 CR
```

WX 기준 목록 매칭 결과:

```text
WX reference vehicles = 45 rows
Matched external sample WX qty = 336
Matched external sample WX sell value = 117,100,000 CR
WX_non_FE qty = 154
WX_non_FE sell value = 57,975,000 CR
FE qty = 182
FE sell value = 59,125,000 CR
WX share of all car prizes = 336 / 2740 = 12.26%
WX share of all slots = 336 / 11489 = 2.92%
```

## Use in research

이 표본으로 할 수 있는 것:

```text
1. 전체 슬롯 기준 Legendary Car 확률 확인
2. 전체 슬롯 기준 FE 확률 확인
3. CR 보상 / 차량 보상 비율 확인
4. 차량 보상 가치가 전체 기대값에 미치는 영향 확인
5. Legendary/FE를 팔 때와 보유할 때의 평균값 차이 확인
6. Wheelspin Exclusive 기준 목록을 이용한 전체 WX 드랍률 계산
```

이 표본으로 바로 하면 안 되는 것:

```text
1. 일반휠과 슈퍼휠의 직접 비교
2. 라부엘토작과 마즈다작의 W/S 직접 산출
3. 신규 계정에 그대로 기대값 적용
```
