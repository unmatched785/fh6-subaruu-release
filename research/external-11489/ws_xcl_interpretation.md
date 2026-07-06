# WS / Xcl interpretation

작성일: 2026-07-04

## 결론

원본 표의 좌측 `WS Xcl?` 영역은 두 정보를 한 칸에 겹쳐 보여주는 방식으로 해석합니다.

```text
텍스트 yes/no = Wheelspin Exclusive 여부
주황색 배경 = Wheelspin Exclusive 표시
분홍색 배경 = Car Mastery bonus car 관련 표시
```

따라서 `yes`가 주황색으로 보이는 차량은 휠스핀 전용/보상 풀 차량으로 봅니다.
반대로 `no`가 분홍색으로 보이는 차량은 휠스핀 전용차가 아니라, Car Mastery bonus car 관련 표시가 있는 차량으로 봅니다.

예시:

```text
orange yes 1965 Toyota Sports 800 = Wheelspin Exclusive
pink no 2023 Honda Civic Type R = not Wheelspin Exclusive, but has bonus-car marker
pink no 2020 Chevrolet Corvette Stingray Coupe = not Wheelspin Exclusive, but has bonus-car marker
pink no 1995 Ferrari F50 = not Wheelspin Exclusive, but has bonus-car marker
```

## Important nuance

사용자가 제공한 기준 목록의 source는 아래처럼 되어 있습니다.

```text
Wheelspin, Seasonal
```

따라서 여기서 말하는 `Wheelspin Exclusive`는 문자 그대로 `휠스핀에서만 나온다`는 뜻이라기보다는, 오토쇼 기본판매 차량이 아닌 `Wheelspin / Seasonal 보상 풀 차량`으로 보는 것이 안전합니다.

실무적으로는 이 연구에서 `WX`로 세는 대상입니다.

## Application rule

차량별 CSV의 `ws_exclusive` 값은 아래 우선순위로 보정합니다.

```text
1. 원본 이미지에서 주황색 yes로 명확히 보이는 차량
2. 사용자가 제공한 wheelspin-only 기준 목록
3. 이름 정규화표(name_aliases.csv)
```

최종 기준 파일은 아래입니다.

```text
research/external-11489/wheelspin_only_reference.csv
```

원본 이미지에서 읽은 `WS Xcl?` 값과 별도 기준 목록이 충돌하면, 추가 스크린샷 검증값을 우선합니다.

## Corrected cases

추가 스크린샷 검증으로 아래를 보정했습니다.

```text
1965 Toyota Sports 800 = yes, 추가
1973 Nissan Skyline H/T 2000GT-R = no
1993 Nissan 240SX = yes
```

## Difference from Xcl?

원본 메모에는 좌측 컬럼에 대해 아래와 같은 설명이 있었습니다.

```text
The left-most column indicates if the car is a Wheelspin Exclusive (Orange)
or if it contains a Car Mastery bonus car (Pink).
```

따라서 원본 표의 좌측 영역에는 두 종류의 표시가 섞여 있습니다.

```text
Orange yes = Wheelspin Exclusive
Pink no = not Wheelspin Exclusive, but contains / relates to a Car Mastery bonus car
```

이 때문에 `WS Xcl?`를 단일한 완전 검증 컬럼으로 보지 않고, `ws_exclusive`와 `xcl_or_bonus_car_marker`를 분리해서 해석하는 것이 안전합니다.
