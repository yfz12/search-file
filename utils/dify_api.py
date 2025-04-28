import requests
import os
import streamlit as st  # 既然你在用streamlit，可以提前导入

def audit_text(file_text):
    api_base = os.getenv("DIFY_API_URL")
    api_key = os.getenv("DIFY_API_KEY")

    if not api_base or not api_key:
        raise ValueError("DIFY_API_URL or DIFY_API_KEY not configured!")

    url = f"{api_base}/v1/chat-messages"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # 核心改动在这里
    query_content = f"请帮我审校以下内容并指出所有错误：\n\n{file_text}"
    
    # query_content = f"""
    # 请你作为一名专业的文本审校员，对以下内容进行全面细致的审校。要求：

    # - 找出所有错别字、语法错误、标点使用错误、用词不当、逻辑错误或排版错误。
    # - 按照表格形式返回，每条错误包含以下字段：
    #     1. 错误片段（引用原文或部分原文）
    #     2. 错误类型（错别字 / 语法错误 / 用词不当 / 逻辑错误 / 标点错误 / 排版错误等）
    #     3. 修改建议（具体改法）

    # 如果没有发现错误，请在表格中说明："未发现明显错误"。
    # 表格使用清晰简洁的文字，便于用户理解。
    # 请勿添加多余解释。

    # 以下是需要审校的内容：
    # {file_text}
    # """


    data = {
        "query": query_content,
        "inputs": {},  # 不传inputs了
        "response_mode": "blocking",
        "user": "audit_user"
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        st.error(f"调用Dify API失败：{str(e)}")
        return "调用Dify失败，请检查API KEY、Agent配置或文件格式。"




