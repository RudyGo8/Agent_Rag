'''
@create_time: 2026/3/16 下午9:12
@Author: GeChao
@File: 29 PyPdf使用.py
'''
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path="./data/pdf1.pdf",
    mode="single", # 默认是page模式，每个页面形成一个Document文档对象
    password="xxx"
)

for doc in loader.lazy_load():
    print(doc)