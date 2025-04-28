import requests
import os

def audit_file(file_path):
    api_base = os.getenv("DIFY_API_URL")
    api_key = os.getenv("DIFY_API_KEY")

    if not api_base or not api_key:
        raise ValueError("DIFY_API_URL or DIFY_API_KEY not configured!")

    url = f"{api_base}/v1/workflows/execute-files"  # 这里假设用的是Dify的文件审校接口
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    # 发送文件
    with open(file_path, "rb") as f:
        files = {
            "file": (os.path.basename(file_path), f)
        }
        response = requests.post(url, headers=headers, files=files)

    if response.status_code != 200:
        raise Exception(f"Dify API Error: {response.status_code} {response.text}")

    result = response.json()

    # 假设返回格式是 { "audit_report": "xxx" }
    return result.get("audit_report", "未检测到审校结果")

