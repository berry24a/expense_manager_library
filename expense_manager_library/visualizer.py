import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
import platform

# 한글 폰트 설정
if platform.system() == "Windows":
    rc('font', family='Malgun Gothic')
elif platform.system() == "Darwin":  # macOS
    rc('font', family='AppleGothic')
else:  # Linux
    rc('font', family='NanumGothic')

# 데이터 불러오기 함수
def load_data(file_path):
    data = pd.read_csv(file_path)
    required_columns = ["카테고리", "금액", "날짜"]
    if not all(col in data.columns for col in required_columns):
        raise ValueError(f"데이터 파일에 다음 요소가 필요합니다: {', '.join(required_columns)}")
    return data

# 파이 차트 그리기 함수
def draw_pie_chart(data):
    grouped_data = data.groupby("카테고리")["금액"].sum()

    plt.figure(figsize=(8, 8))
    plt.pie(grouped_data, labels=grouped_data.index, autopct="%.1f%%", startangle=90, colors=plt.cm.Set3.colors)
    plt.title("카테고리별 소비 금액 비율", fontsize=16)
    plt.tight_layout()
    plt.show()

# 라인 차트 그리기 함수
def draw_line_chart(data):
    data['날짜'] = pd.to_datetime(data['날짜'], format='%Y%m%d') 
    grouped_data = data.groupby("날짜")["금액"].sum()

    plt.figure(figsize=(12, 6))
    plt.plot(grouped_data.index, grouped_data.values, marker='o', color='black')
    plt.title("날짜별 소비 추이")
    plt.xlabel("날짜")
    plt.ylabel("소비 금액")
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 바 차트 그리기 함수
def draw_bar_chart(data):
    data['날짜'] = pd.to_datetime(data['날짜'], format='%Y%m%d')
    data['월'] = data['날짜'].dt.to_period("M")  
    grouped_data = data.groupby(["월", "카테고리"])["금액"].sum().unstack()

    grouped_data.plot(kind="bar", figsize=(12, 6), color=plt.cm.Set3.colors)
    plt.title("카테고리별 월별 소비 금액")
    plt.xlabel("월")
    plt.ylabel("소비 금액")
    plt.xticks(rotation=45)
    plt.legend(title="카테고리")
    plt.tight_layout()
    plt.show()

# 실행 테스트
if __name__ == "__main__":
    try:
        file_path = "classified_data.csv"  # 데이터 파일 경로
        data = load_data(file_path)
      
        draw_pie_chart(data)

        draw_line_chart(data)

        draw_bar_chart(data)

    except Exception as e:
        print(f"오류 발생: {e}")
