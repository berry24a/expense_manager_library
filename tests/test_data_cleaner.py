import unittest
import os
import pandas as pd
from expense_manager_library.data_cleaner import classify_expenses

class TestDataCleaner(unittest.TestCase):
    def setUp(self):
        # 테스트용 CSV 파일 생성
        self.test_csv = "test_data.csv"
        self.test_output_csv = "test_classified_data.csv"

        # 테스트 데이터 생성
        data = pd.DataFrame({
            "거래처": ["밥", "택시", "백화점", "뮤지컬", "한양"]
        })
        data.to_csv(self.test_csv, index=False, encoding="utf-8-sig")

    def tearDown(self):
        # 테스트 종료 후 파일 삭제
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)
        if os.path.exists(self.test_output_csv):
            os.remove(self.test_output_csv)

    def test_classify_expenses(self):
        # classify_expenses 함수 실행
        classify_expenses(self.test_csv, self.test_output_csv)

        # 결과 파일 로드 및 검증
        result = pd.read_csv(self.test_output_csv)
        expected_categories = ["식비", "교통", "쇼핑", "여가", "기타"]
        self.assertListEqual(result["카테고리"].tolist(), expected_categories)

if __name__ == "__main__":
    unittest.main()
