import requests
import os

def audit_file(file_path):
    # 替换为你实际的 Dify API Key 和 API 地址
    api_url = os.getenv("DIFY_API_URL")
    api_key = os.getenv("DIFY_API_KEY")

    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(api_url, headers=headers, files=files)
        
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "审校失败，请稍后再试。"}
