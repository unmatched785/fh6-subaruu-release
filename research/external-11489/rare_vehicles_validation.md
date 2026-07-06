# Rare vehicle transcription validation

작성일: 2026-07-04

이 문서는 `rare_vehicles_draft.csv`의 전사 검증 메모입니다.

## Source

- 원본 이미지: `통계3.webp`
- 대상 구간: Blue 색상 Rare 차량 목록
- 전사 방식: 사용자 제공 텍스트를 기반으로 수동 정리

## Validation result

`rare_vehicles_draft.csv`는 아래 합계와 원본 요약값이 일치합니다.

| 항목 | CSV 합계 | 원본 요약값 | 판정 |
| --- | ---: | ---: | --- |
| 차량 행 수 | 143 | 143 | OK |
| Rare 차량 수량 | 730 | 730 | OK |
| Rare 차량 즉시판매 총합 | 37,341,500 CR | 37,341,500 CR | OK |
| Rare 평균 판매가 | 51,153 CR | 51,153 CR | OK |

계산:

```text
37,341,500 / 730 = 51,152.74 CR
```

## WS / Xcl status

`qty`, `sell_for_cr`, `total_sell_value_cr`는 합계 검증이 완료되었습니다.

다만 좌측 `WS / Xcl?` 컬럼은 원본 이미지와 사용자 제공 텍스트에서 정렬이 완전하지 않습니다.
현재 CSV에서는 명확하게 `yes`로 보이는 `1965 Toyota Sports 800`만 `ws_exclusive=yes`로 두고, 나머지는 `no`로 두었습니다.
`xcl`은 전체 행에서 `unknown`으로 둡니다.

따라서 차량별 WS/Xcl 판정은 아직 완전 검증값이 아닙니다.

## Current status

```text
verified=false
```

이 값은 차량명, 수량, 판매가, 총액은 합계 검증됐지만, WS/Xcl 컬럼은 추가 확인이 필요하다는 뜻입니다.

## Next step

다음 전사 대상은 Epic 차량 목록입니다.
Epic 요약 기준은 아래와 같습니다.

```text
Epic qty = 547
Epic total sell value = 68,214,250 CR
Epic avg sell value = 124,706 CR
```
