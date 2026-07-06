# External 11,489 validation report

작성일: 2026-07-04

검증 스크립트:

```text
research/external-11489/validate_external_11489.py
```

실행 명령:

```bash
python research/external-11489/validate_external_11489.py
```

## Result

```text
PASS external 11,489 validation
car_qty=2,740
car_value=627,423,250
wx_qty=336
wx_value=117,100,000
wx_non_fe_qty=154
wx_non_fe_value=57,975,000
```

## Checked values

### Vehicle transcription totals

| Rarity | Row count | Qty | Total sell value |
| --- | ---: | ---: | ---: |
| Common | 90 | 1,099 | 27,771,500 CR |
| Rare | 143 | 730 | 37,341,500 CR |
| Epic | 120 | 547 | 68,214,250 CR |
| Legendary | 70 | 182 | 434,971,000 CR |
| Forza Edition | 8 | 182 | 59,125,000 CR |
| Total | 431 | 2,740 | 627,423,250 CR |

### WX reference-match totals

| Metric | Value |
| --- | ---: |
| WX reference rows | 45 |
| WX + FE matched qty | 336 |
| WX + FE matched sell value | 117,100,000 CR |
| non-FE WX qty | 154 |
| non-FE WX sell value | 57,975,000 CR |
| FE qty | 182 |
| FE sell value | 59,125,000 CR |

## Notes

- `WX + FE`는 `Wheelspin / Seasonal` 기준 목록 45종 전체입니다.
- `non-FE WX`는 위 목록에서 Forza Edition 차량 8종을 제외한 값입니다.
- `FE`는 별도 통계로 유지합니다.
- `Xcl?` 및 Car Mastery 관련 열은 아직 검증 대상에 넣지 않았습니다.
