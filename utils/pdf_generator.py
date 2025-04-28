from fpdf import FPDF

def generate_pdf(audit_result):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", size=12)
    
    # 添加标题
    pdf.cell(200, 10, txt="审校报告", ln=True, align='C')
    
    # 添加审校结果
    for key, value in audit_result.items():
        if isinstance(value, str):
            pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)
        elif isinstance(value, list):
            pdf.cell(200, 10, txt=f"{key}: ", ln=True)
            for item in value:
                pdf.cell(200, 10, txt=f"- {item}", ln=True)

    pdf_output_path = "audit_report.pdf"
    pdf.output(pdf_output_path)
    return pdf_output_path
