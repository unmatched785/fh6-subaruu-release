# Common vehicle transcription validation

작성일: 2026-07-04

이 문서는 `common_vehicles_draft.csv`의 전사 검증 메모입니다.

## Source

- 원본 이미지: `통계2.webp`
- 대상 구간: Green 색상 Common 차량 목록
- 전사 방식: 사용자 제공 텍스트를 기반으로 수동 정리

## Validation result

`common_vehicles_draft.csv`는 아래 합계와 원본 요약값이 일치합니다.

| 항목 | CSV 합계 | 원본 요약값 | 판정 |
| --- | ---: | ---: | --- |
| 차량 행 수 | 90 | 90 | OK |
| Common 차량 수량 | 1,099 | 1,099 | OK |
| Common 차량 즉시판매 총합 | 27,771,500 CR | 27,771,500 CR | OK |
| Common 평균 판매가 | 25,270 CR | 25,270 CR | OK |

계산:

```text
27,771,500 / 1,099 = 25,270.7 CR
```

## Important caveat

`qty`, `sell_for_cr`, `total_sell_value_cr`는 합계 검증이 완료되었습니다.

다만 좌측 `WS / Xcl?` 컬럼은 원본 이미지와 사용자 제공 텍스트에서 정렬이 완전하지 않습니다.
현재 CSV에서는 Common 차량의 `ws_exclusive`를 일단 `no`로 두고, `xcl`은 `unknown`으로 둡니다.
따라서 차량별 WS/Xcl 판정은 아직 완전 검증값이 아닙니다.

## Current status

```text
verified=false
```

이 값은 차량명, 수량, 판매가, 총액은 합계 검증됐지만, WS/Xcl 컬럼은 아직 추가 확인이 필요하다는 뜻입니다.

## Next step

다음 전사 대상은 Rare 차량 목록입니다.
Rare 요약 기준은 아래와 같습니다.

```text
Rare qty = 730
Rare total sell value = 37,341,500 CR
Rare avg sell value = 51,153 CR
```
