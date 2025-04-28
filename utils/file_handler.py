# from utils.dify_api import audit_text

# def handle_uploaded_file(uploaded_file):
#     # 获取文件路径
#     file_path = f"uploaded_files/{uploaded_file.name}"

#     # 保存文件到本地
#     with open(file_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())

#     # 读取文件内容
#     file_text = ""
#     if uploaded_file.type == "application/pdf":
#         # 这里用一些PDF阅读库来提取PDF内容，例如 PyPDF2 或 pdfplumber
#         import pdfplumber
#         with pdfplumber.open(file_path) as pdf:
#             file_text = "\n".join([page.extract_text() for page in pdf.pages])
#     elif uploaded_file.type == "application/msword" or uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
#         # 处理Word文件
#         import docx
#         doc = docx.Document(file_path)
#         file_text = "\n".join([para.text for para in doc.paragraphs])
#     elif uploaded_file.type == "application/vnd.ms-excel" or uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
#         # 处理Excel文件
#         import pandas as pd
#         df = pd.read_excel(file_path)
#         file_text = df.to_string()
#     elif uploaded_file.type == "text/markdown":
#         # 处理Markdown文件
#         file_text = uploaded_file.getvalue().decode("utf-8")

#     # 调用审校API
#     audit_result = audit_text(file_text)

#     return file_path, audit_result

# from utils.dify_api import audit_text
# import pdfplumber
# import docx
# import pandas as pd

# def handle_uploaded_file(uploaded_file):
#     # 获取文件路径
#     file_path = f"uploaded_files/{uploaded_file.name}"

#     # 保存文件到本地
#     with open(file_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())

#     # 读取文件内容
#     file_text = ""
#     if uploaded_file.type == "application/pdf":
#         # 这里用一些PDF阅读库来提取PDF内容，例如 PyPDF2 或 pdfplumber
#         with pdfplumber.open(file_path) as pdf:
#             file_text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text() is not None])
#     elif uploaded_file.type == "application/msword" or uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
#         # 处理Word文件
#         doc = docx.Document(file_path)
#         file_text = "\n".join([para.text for para in doc.paragraphs])
#     elif uploaded_file.type == "application/vnd.ms-excel" or uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
#         # 处理Excel文件
#         df = pd.read_excel(file_path)
#         file_text = df.to_string()
#     elif uploaded_file.type == "text/markdown":
#         # 处理Markdown文件
#         file_text = uploaded_file.getvalue().decode("utf-8")

#     # 调用审校API
#     audit_result = audit_text(file_text)

#     return file_path, audit_result  # 返回文件路径和审校结果


import os

def handle_uploaded_file(uploaded_file):
    # 获取文件保存路径
    file_path = f"uploaded_files/{uploaded_file.name}"

    # 检查目录是否存在，如果不存在则创建
    if not os.path.exists("uploaded_files"):
        os.makedirs("uploaded_files")

    # 保存文件到本地
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # 读取文件内容
    file_text = ""
    if uploaded_file.type == "application/pdf":
        # 这里用一些PDF阅读库来提取PDF内容，例如 PyPDF2 或 pdfplumber
        import pdfplumber
        with pdfplumber.open(file_path) as pdf:
            file_text = "\n".join([page.extract_text() for page in pdf.pages])
    elif uploaded_file.type == "application/msword" or uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        # 处理Word文件
        import docx
        doc = docx.Document(file_path)
        file_text = "\n".join([para.text for para in doc.paragraphs])
    elif uploaded_file.type == "application/vnd.ms-excel" or uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        # 处理Excel文件
        import pandas as pd
        df = pd.read_excel(file_path)
        file_text = df.to_string()
    elif uploaded_file.type == "text/markdown":
        # 处理Markdown文件
        file_text = uploaded_file.getvalue().decode("utf-8")

    # 调用审校API
    audit_result = audit_text(file_text)

    return file_path, audit_result
