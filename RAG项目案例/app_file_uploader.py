'''
@create_time: 2026/3/17 下午8:59
@Author: GeChao
@File: app_file_uploader.py
'''
import time

# 基于Streamlit完成WEB网页上传服务

import streamlit as st
from knowledge_base import KnowledgeBaseService

st.title("知识库")

# file_uploader
uploader_file = st.file_uploader(
    "请上传TXT文件",
    type=['txt'],
    accept_multiple_files=False,  # False表示仅支持一个文件的上传
)

service = KnowledgeBaseService()

# session_state就是一个字典
if "service" not in st.session_state:
    st.session_state["service"] = KnowledgeBaseService()

if uploader_file is not None:
    file_name = uploader_file.name
    file_type = uploader_file.type
    file_size = uploader_file.size / 1024

    st.subheader(f"文件名：{file_name}")
    st.write(f"格式: {file_type} | 大小: {file_size:.2f} KB")

    text = uploader_file.getvalue().decode('utf-8')
    with st.spinner("载入知识库中。。。"):
        time.sleep(1)
        result = st.session_state["service"].upload_by_str(text, file_name)
        st.write(result)
