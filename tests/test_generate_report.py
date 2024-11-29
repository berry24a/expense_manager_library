import unittest
import pandas as pd
import sys
import os

# 프로젝트 루트를 모듈 경로에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from expense_manager_library.report_generator import generate_report

class TestGenerateReport(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            "카테고리": ["교통", "쇼핑", "식비", "쇼핑"],
            "금액": [6000, 30000, 20000, 15000],
        })

    def test_generate_report_include_both(self):
        report = generate_report(self.data, include_total=True, include_categories=True)
        self.assertIn("총 소비 금액: 71,000원", report)
        self.assertIn("쇼핑: 45,000원", report)
        self.assertIn("식비: 20,000원", report)
        self.assertIn("교통: 6,000원", report)

    def test_generate_report_only_total(self):
        report = generate_report(self.data, include_total=True, include_categories=False)
        self.assertIn("총 소비 금액: 71,000원", report)
        self.assertNotIn("식비: 20,000원", report)

    def test_generate_report_only_categories(self):
        report = generate_report(self.data, include_total=False, include_categories=True)
        self.assertNotIn("총 소비 금액", report)
        self.assertIn("쇼핑: 45,000원", report)
        self.assertIn("식비: 20,000원", report)
        self.assertIn("교통: 6,000원", report)

    def test_generate_report_empty_data(self):
        empty_data = pd.DataFrame(columns=["카테고리", "금액"])
        report = generate_report(empty_data, include_total=True, include_categories=True)
        self.assertIn("총 소비 금액: 0원", report)
    def test_generate_report_include_both(self):
        report = generate_report(self.data, include_total=True, include_categories=True)
        # 결과를 파일로 저장
        with open("test_report.txt", "w", encoding="utf-8") as file:
            file.write(report)
        self.assertIn("총 소비 금액: 71,000원", report)
        self.assertIn("쇼핑: 45,000원", report)
        self.assertIn("식비: 20,000원", report)
        self.assertIn("교통: 6,000원", report)

if __name__ == "__main__":
    unittest.main()
