from fpdf import FPDF
import os
import tempfile

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font('DejaVu', '', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', uni=True)
        self.set_font('DejaVu', '', 12)

def generate_pdf(content):
    pdf = PDF()
    pdf.add_page()

    lines = content.split('\n')
    for line in lines:
        pdf.multi_cell(0, 10, line)

    output_path = os.path.join(tempfile.gettempdir(), "audit_report.pdf")
    pdf.output(output_path)
    return output_path
