# Epic vehicle transcription validation

작성일: 2026-07-04

이 문서는 `epic_vehicles_draft.csv`의 전사 검증 메모입니다.

## Source

- 원본 이미지: `통계4.webp`
- 대상 구간: Pink 색상 Epic 차량 목록
- 전사 방식: 사용자 제공 텍스트와 원본 이미지를 대조하여 수동 정리

## Validation result

`epic_vehicles_draft.csv`는 아래 합계와 원본 요약값이 일치합니다.

| 항목 | CSV 합계 | 원본 요약값 | 판정 |
| --- | ---: | ---: | --- |
| 차량 행 수 | 120 | 120 | OK |
| Epic 차량 수량 | 547 | 547 | OK |
| Epic 차량 즉시판매 총합 | 68,214,250 CR | 68,214,250 CR | OK |
| Epic 평균 판매가 | 124,706 CR | 124,706 CR | OK |

계산:

```text
68,214,250 / 547 = 124,706.12 CR
```

## WS / Xcl status

`qty`, `sell_for_cr`, `total_sell_value_cr`는 합계 검증이 완료되었습니다.

Epic 구간은 원본 이미지에서 주황색 `yes`가 비교적 잘 보이므로, 명확하게 보이는 WS 차량은 `ws_exclusive=yes`로 반영했습니다.
다만 `Xcl?` 또는 Car Mastery bonus car 관련 표시는 아직 구조화하지 않았으므로 `xcl=unknown`으로 둡니다.

현재 전사 기준 Epic WS 차량은 아래와 같습니다.

| 항목 | 값 |
| --- | ---: |
| WS 차량 행 수 | 26 |
| WS 차량 획득 수량 | 120 |
| WS 차량 즉시판매 총합 | 20,666,500 CR |
| Epic 전체 수량 중 WS 비중 | 21.94% |
| Epic 전체 가치 중 WS 비중 | 30.30% |

계산:

```text
WS qty share = 120 / 547 = 21.94%
WS value share = 20,666,500 / 68,214,250 = 30.30%
```

## Current status

```text
verified=false
```

이 값은 차량명, 수량, 판매가, 총액은 합계 검증됐지만, `Xcl?` 및 Car Mastery 관련 열은 아직 추가 구조화가 필요하다는 뜻입니다.

## Next step

다음 전사 대상은 Legendary + FE 차량 목록입니다.
Legendary / FE 요약 기준은 아래와 같습니다.

```text
Legendary qty = 182
Legendary total sell value = 434,971,000 CR
Legendary avg sell value = 2,389,951 CR

FE qty = 182
FE total sell value = 59,125,000 CR
FE avg sell value = 324,863 CR
```
