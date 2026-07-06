# Vehicle-level transcription schema

외부 이미지에는 차량별 상세 행이 포함되어 있지만, 현재 단계에서는 전체 차량 행을 CSV로 전사하지 않았습니다.
이 문서는 나중에 차량별 표를 전사할 때 사용할 스키마입니다.

## Current status

- 상단 집계표와 희귀도별 요약값은 CSV로 전사했습니다.
- 차량별 전체 행은 이미지의 글자 크기와 행 수 때문에 자동 전사 오류 가능성이 높습니다.
- 차량별 행은 별도 수동 검증 또는 고해상도 원본 확보 후 전사하는 것이 좋습니다.

## Suggested CSV columns

```csv
source_image,rarity,car_name,wheelspin_exclusive,car_mastery_bonus_car,car_mastery_wheelspin,car_mastery_super_wheelspin,car_mastery_cr,qty,sell_for_cr,total_sell_value_cr,auction_practical_cr,notes
```

## Column definitions

| column | meaning |
| --- | --- |
| `source_image` | 원본 이미지 식별자 |
| `rarity` | Common / Rare / Epic / Legendary / FE |
| `car_name` | 차량명 |
| `wheelspin_exclusive` | 원본 좌측 WS 컬럼의 yes/no |
| `car_mastery_bonus_car` | 원본 Xcl? 또는 보너스 차량 여부로 보이는 컬럼 |
| `car_mastery_wheelspin` | Car Mastery에 Wheelspin 보상이 있는지 |
| `car_mastery_super_wheelspin` | Car Mastery에 Super Wheelspin 보상이 있는지 |
| `car_mastery_cr` | Car Mastery에 CR 보상이 있는지 |
| `qty` | 해당 표본에서 나온 수량 |
| `sell_for_cr` | 즉시판매 CR |
| `total_sell_value_cr` | `sell_for_cr * qty` |
| `auction_practical_cr` | 원본의 Practical Auction 값. 있는 경우만 |
| `notes` | 판독 불확실성, 색상표기, 예외 등 |

## Recommended handling

차량별 행은 아래 순서로 전사하는 편이 안전합니다.

```text
1. Legendary / FE 차량부터 전사
2. Epic 차량 전사
3. Rare / Common 차량 전사
4. 합계가 원본 요약값과 맞는지 검증
```

검증 기준:

```text
Common qty = 1099
Rare qty = 730
Epic qty = 547
Legendary qty = 182
FE qty = 182
Total car qty = 2740
Total car value = 627,423,250 CR
```

합계가 맞지 않으면 차량명 또는 수량 판독 오류가 있는 것으로 봅니다.
