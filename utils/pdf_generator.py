from fpdf import FPDF
import os

def generate_pdf(audit_text):
    output_dir = "generated_reports"
    os.makedirs(output_dir, exist_ok=True)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # 按行分段写入
    for line in audit_text.split("\n"):
        pdf.multi_cell(0, 10, line)

    output_path = os.path.join(output_dir, "audit_report.pdf")
    pdf.output(output_path)

    # 读取生成的PDF文件，返回给Streamlit下载用
    with open(output_path, "rb") as f:
        pdf_bytes = f.read()

    return pdf_bytes
