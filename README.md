# expense_manager_library

expense_manager_library는 개인의 소비 데이터를 분석하고 보고서를 생성하는 파이썬 라이브러리입니다. 이 라이브러리를 사용하여 카테고리별 소비 금액, 월별 소비 내역, 그래프를 포함한 PDF 보고서를 생성할 수 있습니다.

## 주요 기능
- **소비 데이터 분석**: CSV 파일로부터 소비 데이터를 불러와 자동으로 카테고리를 분류합니다.
- **그래프 생성**: 원형 차트, 선형 차트, 막대 차트 등 다양한 시각화를 제공합니다.
- **카테고리별 소비 금액 합계 및 비율 계산**: 데이터에서 주요 소비 패턴을 추출합니다.
- **월별 소비 금액 분석**: 월별 소비 금액과 카테고리 비율을 분석합니다.
- **PDF 보고서 생성**: 그래프와 데이터를 포함한 지출 보고서를 PDF로 저장합니다.

## CSV 데이터 구성
- **열 정보**:
  - `날짜`: 거래 날짜 (형식: `YYYYMMDD`)
  - `거래처`: 거래가 발생한 가게이나 서비스 이름
  - `금액`: 해당 거래의 금액 (단위: 원)
### 예시 데이터
| 날짜       | 거래처      | 금액   |
|------------|-------------|--------|
| 20241026   | 스타벅스    | 4500   |
| 20241027   | CU          | 3000   |
  
## 설치 방법
```bash
pip install expense_manager_library
```

## CSV 파일 입력 방법
```bash
from expense_manager_library.data_cleaner import categorize_transactions

csv_file_path = "자신의 파일 경로 입력.csv"

categorize_transactions(csv_file_path)
```

## 개발자 소개
- **한여진** : 팀장, `report_generator` 모듈 개발 및 라이브러리 관리
- **연소윤** : `data_cleaner` 모듈 개발
- **박지은** : `visualizer` 모듈 개발
- **임아진** : 코드 검토 및 피드백 제공, Sample Usage Repository 구현
