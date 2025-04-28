#!/bin/bash
# 启动streamlit并用ngrok暴露外网
streamlit run app.py &
ngrok http 8501
