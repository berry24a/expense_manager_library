import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from expense_manager_library.data_cleaner import categorize_transactions
from expense_manager_library.visualizer import load_data
from expense_manager_library.report_generator import generate_report, save_report_to_pdf

file_path = "examples/example_data.csv" # csv 파일 경로
data = file_path

categorize_transactions(data)

categorize_data = load_data("results/classified_data.csv")

# 보고서 생성
report_text = generate_report(
    categorize_data,
    include_total=True,
    include_categories=True,
    include_monthly=True 
)

print(report_text)

# pdf로 저장
save_report_to_pdf(
    categorize_data,
    report_text,
    selected_graphs=["pie", "line", "bar"],  
    show_report=True, 
    font_color="black",
    pdf_path="results/example_report.pdf" 
)

print("PDF 파일이 저장되었습니다: results/example_report.pdf")
