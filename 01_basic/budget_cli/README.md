# 💰 Budget CLI

Python 기초 학습 — 가계부 커맨드라인 앱

## 기능

- 수입/지출 거래 추가
- 전체 거래 목록 조회
- 수입/지출/잔액 요약
- JSON 파일로 자동 저장/불러오기

## 사용법

```bash
python budget.py
```

## 함수 설명

| 함수                | 설명                              |
| ------------------- | --------------------------------- |
| `add_transaction()` | 날짜/타입/메모/금액 입력받아 추가 |
| `show_all()`        | 전체 거래 목록 출력               |
| `get_summary()`     | 수입/지출/잔액 계산 및 출력       |
| `save_to_file()`    | budget.json에 저장                |
| `load_from_file()`  | 시작 시 budget.json 불러오기      |

## 사용 기술

- Python 내장 모듈: `json`, `os`, `datetime`
