import streamlit as st
import os
from utils.file_handler import handle_uploaded_file
from utils.dify_api import audit_file
from utils.pdf_generator import generate_pdf
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 配置
st.set_page_config(page_title="YFZ12 审校助手", layout="wide")

# 登录认证
def authenticate_user():
    password = st.text_input("请输入密码", type="password")
    if password == os.getenv("ADMIN_PASSWORD"):
        return True
    return False

# 文件上传部分
def upload_file():
    uploaded_file = st.file_uploader("上传您的文件（PDF, Word, Excel, Markdown）", type=["pdf", "docx", "xlsx", "md"])
    if uploaded_file is not None:
        return uploaded_file
    return None

# 主页面
def main():
    if authenticate_user():
        st.title("YFZ12 审校助手")
        st.markdown("上传文件进行审校，支持 PDF、Word、Excel、Markdown 格式。")

        uploaded_file = upload_file()

        if uploaded_file:
            st.write("文件已上传，正在处理...")
            file_path = handle_uploaded_file(uploaded_file)

            # 审校
            audit_result = audit_file(file_path)

            # 显示审校结果
            st.subheader("审校报告")
            st.write(audit_result)

            # 生成并提供下载PDF报告
            pdf_path = generate_pdf(audit_result)
            st.download_button("下载审校报告（PDF）", data=pdf_path, file_name="audit_report.pdf", mime="application/pdf")
        
            # 聊天提问部分
            question = st.text_input("提问（例如：哪里错得最严重？）")
            if question:
                response = audit_result.get("response_to_question", "问题未能回答，请稍后再试。")
                st.write(response)
        else:
            st.info("请上传文件进行审校。")
    else:
        st.error("密码错误，请重新输入。")

if __name__ == "__main__":
    main()
