# Legendary and FE vehicle transcription validation

작성일: 2026-07-04

이 문서는 Legendary 및 Forza Edition 차량 목록 전사 검증 메모입니다.

## Source

- 원본 이미지: `통계5.webp`
- 대상 구간: Orange 색상 Legendary 차량 목록 + Purple FE 차량 목록
- 전사 방식: 사용자 제공 텍스트와 원본 이미지를 대조하여 수동 정리

## Validation result

| 항목 | CSV 합계 | 원본 요약값 | 판정 |
| --- | ---: | ---: | --- |
| Legendary 차량 행 수 | 70 | 70 | OK |
| Legendary 차량 수량 | 182 | 182 | OK |
| Legendary 즉시판매 총합 | 434,971,000 CR | 434,971,000 CR | OK |
| Legendary 평균 판매가 | 2,389,951 CR | 2,389,951 CR | OK |
| FE 차량 행 수 | 8 | 8 | OK |
| FE 차량 수량 | 182 | 182 | OK |
| FE 즉시판매 총합 | 59,125,000 CR | 59,125,000 CR | OK |
| FE 평균 판매가 | 324,863 CR | 324,863 CR | OK |

계산:

```text
Legendary avg = 434,971,000 / 182 = 2,389,950.55 CR
FE avg        = 59,125,000 / 182 = 324,862.64 CR
```

## WS summary

현재 전사 기준으로 명확히 확인한 WS 값은 아래와 같습니다.

| 구분 | WS 행 수 | WS 획득 수량 | WS 즉시판매 총합 |
| --- | ---: | ---: | ---: |
| Legendary | 11 | 31 | 37,182,500 CR |
| FE | 8 | 182 | 59,125,000 CR |
| Legendary + FE | 19 | 213 | 96,307,500 CR |

계산:

```text
Legendary WS qty share = 31 / 182 = 17.03%
Legendary WS value share = 37,182,500 / 434,971,000 = 8.55%
FE WS qty share = 182 / 182 = 100.00%
```

## Current status

```text
verified=false
```

차량명, 수량, 판매가, 총액은 합계 검증됐지만, `Xcl?` 및 Car Mastery 관련 열은 아직 완전 구조화하지 않았습니다.
