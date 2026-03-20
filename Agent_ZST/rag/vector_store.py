'''
@create_time: 2026/3/19 下午1:13
@Author: GeChao
@File: vector_store.py
'''
from langchain_chroma import Chroma


class VectorStoreService:
    def __init__(self):
        self.vector_store = Chroma(
            collection_name=None,
            embedding_function=None,
            persist_directory=None
        )
        self.spliter = None
