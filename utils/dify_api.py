import requests
import os

def audit_file(file_path):
    api_base = os.getenv("DIFY_API_URL")
    api_key = os.getenv("DIFY_API_KEY")

    if not api_base or not api_key:
        raise ValueError("DIFY_API_URL or DIFY_API_KEY not configured!")

    url = f"{api_base}/v1/chat-messages"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # 读取文件内容
    with open(file_path, "r", encoding="utf-8") as f:
        file_content = f.read()

    # 构建聊天消息体
    data = {
        "inputs": {
            "text": file_content
        },
        "response_mode": "blocking"  # 阻塞式，一次返回完整结果
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        import streamlit as st
        st.error(f"Dify API返回错误：{response.status_code} - {response.text}")
        return "调用Dify失败，请检查API KEY、Agent配置或文件格式。"

    result = response.json()

    # 拿到回答
    return result.get("answer", "未检测到审校结果")
