import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from expense_manager_library.report_generator import generate_report, save_report_to_pdf

# 샘플
data = pd.DataFrame({
    "카테고리": ["교통", "쇼핑", "식비", "쇼핑"],
    "금액": [6000, 30000, 20000, 15000],
    "날짜": ["20241031", "20241031", "20241102", "20241105"]
})

# 보고서 생성
report_text = generate_report(
    data,
    include_total=True,
    include_categories=True,
    include_monthly=True 
)

print("지출 보고서:")
print(report_text)

# pdf로 저장
save_report_to_pdf(
    data=data,
    report_text=report_text,
    selected_graphs=["pie", "line", "bar"],  
    show_report=True, 
    pdf_path="results/example_report.pdf" 
)

print("PDF 파일이 저장되었습니다: results/example_report.pdf")
