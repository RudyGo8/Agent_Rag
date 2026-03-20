'''
@create_time: 2026/3/11 下午5:35
@Author: GeChao
@File: 14 调用文本嵌入模型.py
'''
from langchain_community.embeddings import DashScopeEmbeddings

# 创建模型对象，不传model默认使用的是text-embeddings-v1
model = DashScopeEmbeddings()

print(model.embed_query("我喜欢你"))
print(model.embed_documents(["我喜欢你", "你真聪明"]))
