
import os
import time

def handle_uploaded_file(uploaded_file):
    # 定义统一上传文件夹
    upload_dir = "uploaded_files"
    os.makedirs(upload_dir, exist_ok=True)  # 自动创建目录（如果没有）

    # 防止重名，加上时间戳
    filename = f"{int(time.time())}_{uploaded_file.name}"
    file_path = os.path.join(upload_dir, filename)

    # 保存上传的文件
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path
