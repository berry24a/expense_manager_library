import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
import platform

# 한글 폰트 설정
if platform.system() == "Windows":
    rc('font', family='Malgun Gothic')
elif platform.system() == "Darwin": 
    rc('font', family='AppleGothic')
else:
    rc('font', family='NanumGothic')

# 데이터 불러오기 함수
def load_data(file_path):
    data = pd.read_csv(file_path)
    required_columns = ["카테고리", "금액", "날짜"]
    if not all(col in data.columns for col in required_columns):
        raise ValueError(f"데이터 파일에 다음 요소가 필요합니다: {', '.join(required_columns)}")
    return data

# 파이 차트 그리기 함수 
def draw_pie_chart(data, ax=None):
    grouped_data = data.groupby("카테고리")["금액"].sum()

    if ax is None:
        ax = plt.gca()

    ax.pie(grouped_data, labels=grouped_data.index, autopct="%.1f%%", startangle=90, colors=plt.cm.Set3.colors)
    ax.set_title("카테고리별 소비 금액 비율", fontsize=12)

# 라인 차트 그리기 함수 
def draw_line_chart(data, ax=None):
    data['날짜'] = pd.to_datetime(data['날짜'], format='%Y%m%d') 
    grouped_data = data.groupby("날짜")["금액"].sum()

    if ax is None:
        ax = plt.gca()

    ax.plot(grouped_data.index, grouped_data.values, marker='o', color='blue')
    ax.set_title("날짜별 소비 추이", fontsize=12)
    ax.set_xlabel("날짜")
    ax.set_ylabel("소비 금액")
    ax.grid()
    ax.tick_params(axis='x', rotation=45)

# 바 차트 그리기 함수 
def draw_bar_chart(data, ax=None):
    data['날짜'] = pd.to_datetime(data['날짜'], format='%Y%m%d')
    data['월'] = data['날짜'].dt.to_period("M")  
    grouped_data = data.groupby(["월", "카테고리"])["금액"].sum().unstack()

    if ax is None:
        ax = plt.gca()

    grouped_data.plot(kind="bar", ax=ax, color=plt.cm.Set3.colors)
    ax.set_title("카테고리별 월별 소비 금액", fontsize=12)
    ax.set_xlabel("월")
    ax.set_ylabel("소비 금액")
    ax.legend(title="카테고리", fontsize=8)
