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

    result = response.json()
    return result.get("answer", "未检测到审校结果")
