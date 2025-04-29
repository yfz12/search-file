# import streamlit as st
# import os
# from utils.file_handler import handle_uploaded_file, extract_text_from_file
# from utils.dify_api import audit_text
# from utils.pdf_generator import generate_pdf
# from dotenv import load_dotenv

# # 加载环境变量
# load_dotenv()

# # 页面设置
# st.set_page_config(page_title="YFZ12 审校助手", layout="wide")

# # 登录
# def authenticate_user():
#     password = st.text_input("请输入密码", type="password")
#     if password == os.getenv("ADMIN_PASSWORD"):
#         return True
#     return False

# # 上传文件
# def upload_file():
#     uploaded_file = st.file_uploader("上传您的文件（PDF, Word, Excel, Markdown）", type=["pdf", "docx", "xlsx", "md"])
#     return uploaded_file

# # 主流程
# def main():
#     if authenticate_user():
#         st.title("YFZ12 审校助手")
#         st.markdown("上传文件进行审校，支持 PDF、Word、Excel、Markdown 格式。")

#         uploaded_file = upload_file()

#         if uploaded_file:
#             st.write("文件已上传，正在处理...")
#             file_path = handle_uploaded_file(uploaded_file)
#             file_text = extract_text_from_file(file_path)

#             # 审校
#             audit_result = audit_text(file_text)

#             # 展示结果
#             st.subheader("审校报告")
#             st.write(audit_result)

#             # 生成 PDF
#             pdf_path = generate_pdf(audit_result)
#             st.download_button("下载审校报告（PDF）", data=open(pdf_path, "rb"), file_name="audit_report.pdf", mime="application/pdf")
            
#             # 可提问
#             question = st.text_input("提问（例如：哪里错得最严重？）")
#             if question:
#                 st.write("暂不支持细分提问")  # 暂留
#         else:
#             st.info("请上传文件进行审校。")
#     else:
#         st.error("密码错误，请重新输入。")

# if __name__ == "__main__":
#     main()


import streamlit as st
import os
from utils.file_handler import handle_uploaded_file
from utils.dify_api import audit_text
from utils.pdf_generator import generate_pdf
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 页面设置
st.set_page_config(page_title="YFZ12 审校助手", layout="wide")

# 登录
def authenticate_user():
    password = st.text_input("请输入密码", type="password")
    if password == os.getenv("ADMIN_PASSWORD"):
        return True
    return False

# 上传文件
def upload_file():
    uploaded_file = st.file_uploader("上传您的文件（PDF, Word, Excel, Markdown）", type=["pdf", "docx", "xlsx", "md"])
    return uploaded_file

# 主流程
def main():
    if authenticate_user():
        st.title("YFZ12 审校助手")
        st.markdown("上传文件进行审校，支持 PDF、Word、Excel、Markdown 格式。")

        uploaded_file = upload_file()

        if uploaded_file:
            st.write("文件已上传，正在处理...")
            file_path, audit_result = handle_uploaded_file(uploaded_file)  # 获取文件路径和审校结果

            # 展示审校结果
            st.subheader("审校报告")
            st.write(audit_result)

            # # 生成 PDF
            # pdf_path = generate_pdf(audit_result)
            # st.download_button("下载审校报告（PDF）", data=open(pdf_path, "rb"), file_name="audit_report.pdf", mime="application/pdf")
            
            # 可提问
            question = st.text_input("提问（例如：哪里错得最严重？）")
            if question:
                st.write("暂不支持细分提问")  # 暂留
        else:
            st.info("请上传文件进行审校。")
    else:
        st.write("请输入密码")

if __name__ == "__main__":
    main()
