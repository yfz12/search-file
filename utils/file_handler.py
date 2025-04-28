import os
import tempfile
import fitz  # PyMuPDF
import docx
import pandas as pd

def handle_uploaded_file(uploaded_file):
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def extract_text_from_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    elif ext == ".xlsx":
        return extract_text_from_excel(file_path)
    elif ext == ".md":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        raise ValueError("不支持的文件格式！")

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def extract_text_from_excel(file_path):
    df = pd.read_excel(file_path, sheet_name=None)
    text = ""
    for sheet_name, sheet_df in df.items():
        text += f"\n--- Sheet: {sheet_name} ---\n"
        text += sheet_df.to_string(index=False)
    return text
