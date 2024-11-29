import unittest
import pandas as pd
from expense_manager_library.report_generator import generate_report

class TestGenerateReport(unittest.TestCase):

    # 테스트용 데이터 
    def setUp(self):
        self.data = pd.DataFrame({
            "카테고리": ["교통", "쇼핑", "식비", "쇼핑"],
            "금액": [6000, 30000, 20000, 15000],
        })

    # 총 금액 및 카테고리 포함 테스트
    def test_generate_report_include_both(self):
        report = generate_report(self.data, include_total=True, include_categories=True)
        self.assertIn("총 소비 금액: 50,000원", report)
        self.assertIn("식비: 30,000원", report)
        self.assertIn("교통: 5,000원", report)

    # 총 금액만 포함 테스트
    def test_generate_report_only_total(self):
        report = generate_report(self.data, include_total=True, include_categories=False)
        self.assertIn("총 소비 금액: 50,000원", report)
        self.assertNotIn("식비: 30,000원", report)

    # 카테고리만 포함 테스트
    def test_generate_report_only_categories(self):
        report = generate_report(self.data, include_total=False, include_categories=True)
        self.assertNotIn("총 소비 금액", report)
        self.assertIn("식비: 30,000원", report)

    # 빈 데이터 테스트
    def test_generate_report_empty_data(self):
        empty_data = pd.DataFrame(columns=["카테고리", "금액"])
        report = generate_report(empty_data, include_total=True, include_categories=True)
        self.assertIn("총 소비 금액: 0원", report)

if __name__ == "__main__":
    unittest.main()
