'''
@create_time: 2026/3/16 下午7:47
@Author: GeChao
@File: 27 CSVloader.py
'''
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="../data/stu.csv",
    csv_args={
        "delimiter": ",", # 指定分隔符
        "quotechar": '"', # 指定带有分隔符文本的引号包围是单引号还是双引号
        "fieldnames": ['a', 'b', 'c', 'd']
    },
    encoding="utf-8",
)

# 批量加载 .load() -> [Document, Document,...]
documents = loader.load()

for document in documents:
    print(document)

# 懒加载 .lazy_load() 迭代器[Document]
for document in loader.lazy_load():
    print(document)
