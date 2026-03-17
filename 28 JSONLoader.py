'''
@create_time: 2026/3/16 下午8:14
@Author: GeChao
@File: 28 JSONLoader.py
'''
from langchain_community.document_loaders import JSONLoader

loader = JSONLoader(
    file_path= "./data/stu.json",
    jq_schema=".",
    text_content= False
)

document = loader.load()
print(document)