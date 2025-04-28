import requests
import os

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

    data = {
        "query": "请帮我审校以下内容并指出所有错误。",
        "inputs": {
            "text": file_text
        },
        "response_mode": "blocking",
        "user": "audit_user"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        import streamlit as st
        st.error(f"Dify API返回错误：{response.status_code} - {response.text}")
        return "调用Dify失败，请检查API KEY、Agent配置或文件格式。"

    result = response.json()
    return result.get("answer", "未检测到审校结果")
