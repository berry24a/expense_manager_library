import pandas as pd
import numpy as np

# 데이터(사용자의 지출내역) 읽어오기
file_path = "examples/example_data.csv" 
data = pd.read_csv(file_path)

# 키워드와 카테고리 정의
categories_keywords = {
    "식비": ["육앤샤", "배달", "푸드", "식당", "마라탕", "서브웨이", "파스타", "솥밥", "우동", "일백집", "고기", "밥", "회", "술", "맥주", "소주", "일식", "중식", "한식", "짜장면", "짬뽕", "치킨", "떡볶이", "족발", "보쌈"],
    "카페/간식": ["스타벅스", "커피", "카페", "빵집", "뚜레쥬르", "베이커리", "투썸", "메가", "쥬시", "쥬씨", "스벅"],
    "교통": ["버스", "바이크", "KTX", "지하철", "택시", "기차", "자전거", "킥보드"],
    "편의점, 마트": ["CU", "세븐일레븐", "GS25", "마트", "편의점", "이마트24", "씨유", "지에스"],
    "쇼핑": ["에이블리", "쿠팡", "쇼핑", "서적", "무신사", "카카오선물하기", "지그재그", "옷", "백화점", "쇼핑", "아울렛"],
    "여가": ["CGV", "영화", "노래방", "PC방", "피씨방", "피시방", "여가", "시네마", "메가박스", "뮤지컬", "콘서트", "야구", "축구", "베구", "농구"]
}

# 데이터 정리
data["거래처"] = data["거래처"].str.lower() 
all_keywords = {keyword.lower(): category for category, keywords in categories_keywords.items() for keyword in keywords}

# 카테고리 분류 함수
def categorize(usages, keyword_map):
    result = []
    for usage in usages:
        categorized = "기타"  # 기본값
        for keyword, category in keyword_map.items():
            if keyword in usage:  # 키워드가 사용처에 포함되어 있는지 확인
                categorized = category
                break 
        result.append(categorized)
    return result

# 카테고리 분류 실행
data["카테고리"] = categorize(data["거래처"], all_keywords)

# 분류 결과 저장
output_path = "results/classified_data.csv"
data.to_csv(output_path, index=False, encoding="utf-8-sig")

print(f"분류된 파일이 저장되었습니다: {output_path}")
