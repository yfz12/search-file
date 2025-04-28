from fpdf import FPDF
import os
import tempfile

def generate_pdf(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    lines = content.split('\n')
    for line in lines:
        pdf.multi_cell(0, 10, line)

    output_path = os.path.join(tempfile.gettempdir(), "audit_report.pdf")
    pdf.output(output_path)
    return output_path
