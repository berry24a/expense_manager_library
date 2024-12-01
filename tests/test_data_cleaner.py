import sys
import os

# 프로젝트 루트 경로 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from expense_manager_library.data_cleaner import categorize_transactions

# 테스트할 CSV 파일 경로
csv_file_path = "examples/example_data.csv"

# 분류 실행
categorize_transactions(csv_file_path)
