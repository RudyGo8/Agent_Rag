'''
@create_time: 2026/3/18 下午1:03
@Author: GeChao
@File: vector_stores.py
'''
from langchain_chroma import Chroma
import config_data as config


class VectorStoreService(object):
    def __init__(self, embedding):
        """
        :param embedding: 嵌入模型的传入
        """

        self.embedding = embedding

        self.vector_store = Chroma(
            collection_name=config.collection_name,  # 数据库的表名
            embedding_function=self.embedding,
            persist_directory=config.persist_directory,  # 数据库本地存储文件夹
        )  # 向量存储的实例 Chroma向量库对象

    def get_retriever(self):
        """返回向量检索器，方便加入Chain"""
        return self.vector_store.as_retriever(search_kwargs={"k": config.similarity_threshold})

"""
[Document(id='cf897da0-4f68-44d4-a207-962d06696017', metadata={'source': '尺码推荐.txt', 'created_at': xxx]
"""
if __name__ == '__main__':
    from langchain_community.embeddings import DashScopeEmbeddings
    retriever = VectorStoreService(DashScopeEmbeddings(model="text-embedding-v4")).get_retriever()
    res = retriever.invoke('我的体重130斤，尺码推荐')
    print(res)