import unittest
import pandas as pd
import os
import sys
import os

# 프로젝트 루트를 모듈 경로에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from expense_manager_library.report_generator import save_report_to_pdf, generate_report

class TestSaveReportToPDF(unittest.TestCase):

    # 테스트용 데이터
    def setUp(self):
        self.data = pd.DataFrame({
            "날짜": ["20240101", "20240102", "20240103", "20240104"],
            "카테고리": ["교통", "쇼핑", "식비", "쇼핑"],
            "금액": [6000, 30000, 20000, 15000],
        })
        self.report_text = generate_report(self.data, include_total=True, include_categories=True)
        self.pdf_path = "results/test_report.pdf"


    # 테스트 후 파일 제거
    def remove(self):
        if os.path.exists(self.pdf_path):
            os.remove(self.pdf_path)

    # PDF 파일 생성 테스트
    def test_save_report_to_pdf_file_creation(self):
        save_report_to_pdf(self.data, self.report_text, ["pie"], show_report=True, pdf_path=self.pdf_path)
        self.assertTrue(os.path.exists(self.pdf_path))

    # PDF 파일이 비어있지 않은지 확인
    def test_save_report_to_pdf_file_not_empty(self):
        save_report_to_pdf(self.data, self.report_text, ["pie", "line"], show_report=True, pdf_path=self.pdf_path)
        self.assertTrue(os.path.exists(self.pdf_path))
        self.assertTrue(os.path.getsize(self.pdf_path) > 0)


    # 그래프 없이 보고서만 생성 테스트
    def test_save_report_to_pdf_no_graphs(self):
        save_report_to_pdf(self.data, self.report_text, [], show_report=True, pdf_path=self.pdf_path)
        self.assertTrue(os.path.exists(self.pdf_path))
        self.assertTrue(os.path.getsize(self.pdf_path) > 0)

if __name__ == "__main__":
    unittest.main()
