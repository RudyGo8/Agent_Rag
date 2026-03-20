'''
@create_time: 2026/3/17 上午11:00
@Author: GeChao
@File: 30 内存向量存储.py
'''
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

vector_store = InMemoryVectorStore(embedding=DashScopeEmbeddings())

loader = CSVLoader(
    file_path="../data/info.csv",
    encoding="utf-8",
    source_column="source",

)
documents = loader.load()

# 向量存储的 新增、删除、检索
vector_store.add_documents(
    documents=documents,  # 被添加的文档
    ids=["id" + str(i) for i in range(1, len(documents) + 1)]  # 给添加的文档提供id（字符串） list[str]

)

# 删除 传入[id, id ...]
vector_store.delete(["id1", "id2"])

# 检索
result = vector_store.similarity_search(
    query="AI应用开发",
    k=2
)
'''
[Document(id='id3', metadata={'source': 'AI应用开发，是最喜欢的技术', 'row': 2}, page_content='source: AI应用开发，是最喜欢的技术\ninfo: None')]
'''
print(result)
