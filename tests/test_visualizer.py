import os
from visualizer import load_data, draw_pie_chart, draw_line_chart, draw_bar_chart

# 테스트 데이터 파일 경로
DATA_FILE = "examples/example_data.csv"

# 테스트 함수
def test_visualizer():
    if not os.path.exists(DATA_FILE):
        print(f"Error: {DATA_FILE} 파일이 존재하지 않습니다. 데이터를 준비해주세요.")
        return

    print("데이터를 로드 중입니다...")
    data = load_data(DATA_FILE)
    print("데이터 로드 완료!")
    
    print("파이 차트를 그리는 중입니다...")
    draw_pie_chart(data)
    
    print("라인 차트를 그리는 중입니다...")
    draw_line_chart(data)
    
    print("바 차트를 그리는 중입니다...")
    draw_bar_chart(data)

if __name__ == "__main__":
    test_visualizer()
