# WS / Xcl interpretation

작성일: 2026-07-04

## 결론

원본 표의 `WS Xcl?`는 사실상 `Wheelspin Exclusive?`로 해석하는 것이 맞습니다.
즉 해당 차량이 일반 오토쇼/기본 구매 차량이 아니라, 휠스핀 계열 보상 풀에 포함된 전용/준전용 차량인지를 표시하는 열입니다.

다만 이 표의 `yes`만 기계적으로 신뢰하는 것보다, 별도 공식/정리 목록인 `wheelspin_only_reference.csv`를 기준으로 구분하는 편이 안전합니다.
이미지 OCR과 행 정렬 문제 때문에 일부 행은 `yes/no`가 밀려 보일 수 있습니다.

## Important nuance

사용자가 제공한 기준 목록의 source는 아래처럼 되어 있습니다.

```text
Wheelspin, Seasonal
```

따라서 여기서 말하는 `Wheelspin Exclusive`는 문자 그대로 `휠스핀에서만 나온다`는 뜻이라기보다는, 오토쇼 기본판매 차량이 아닌 `Wheelspin / Seasonal 보상 풀 차량`으로 보는 것이 안전합니다.

실무적으로는 이 연구에서 `WX`로 세는 대상입니다.

## Application rule

차량별 CSV의 `ws_exclusive` 값은 최종적으로 아래 파일을 기준으로 보정합니다.

```text
research/external-11489/wheelspin_only_reference.csv
```

원본 이미지에서 읽은 `WS Xcl?` 값은 보조 자료로만 사용합니다.

## Difference from Xcl?

원본 메모에는 좌측 컬럼에 대해 아래와 같은 설명이 있었습니다.

```text
The left-most column indicates if the car is a Wheelspin Exclusive (Orange)
or if it contains a Car Mastery bonus car (Pink).
```

따라서 원본 표의 좌측 영역에는 두 종류의 표시가 섞여 있을 수 있습니다.

```text
Orange yes = Wheelspin Exclusive 쪽으로 해석
Pink 표시 = Car Mastery bonus car 관련 표시로 해석
```

이 때문에 `WS Xcl?`를 단일한 완전 검증 컬럼으로 보지 않고, 별도 기준 목록과 대조하는 방식으로 처리합니다.
