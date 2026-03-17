'''
@create_time: 2026/3/17 下午4:47
@Author: GeChao
@File: 33 RunnablePassthrough的使用.py
'''
from langchain_community.chat_models import ChatTongyi
from langchain_core.documents import Document
from langchain_core.runnables import RunnablePassthrough
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatTongyi(model="qwen3-max")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "以我提供的已知参考资料为主，简洁和专业的回答用户问题，参考资料：{context}."),
        ('user', "用户提问:{input}")
    ]
)

vector_store = InMemoryVectorStore(embedding=DashScopeEmbeddings(model="text-embedding-v4"))

# 准备一下资料（向量库的数据)
# add_texts 传入一个list[str]
vector_store.add_texts(["AI应用开发，是最喜欢的技术", "学AI, 掌握人生先锋", "AI，让生活更美好"])

input_text = "为什么学AI?"
# langchain中向量存储对象，有一个方法：as_retriever, 可以返回一个Runable接口的子类
retriever = vector_store.as_retriever(search_kwargs={"k": 2})


def format_func(docs: list[Document]):
    if not docs:
        return "无相关资料"

    formatted_str = "["
    for doc in docs:
        formatted_str += doc.page_content
    formatted_str += "]"
    return formatted_str


def print_prompt(prompt):
    print(prompt.to_string())
    print("=" * 20)
    return prompt


chain = (
        {"input": RunnablePassthrough(), "context": retriever | format_func} | prompt | print_prompt | model | StrOutputParser()
)

res = chain.invoke(input_text)
'''
System: 以我提供的已知参考资料为主，简洁和专业的回答用户问题，参考资料：[学AI, 掌握人生先锋AI，让生活更美好].
Human: 用户提问:为什么学AI?
====================
学AI是因为它能帮助我们掌握人生先锋技术，让生活更美好。通过学习AI，不仅可以提升个人竞争力，还能更好地理解和应用智能科技，解决实际问题，创造更多价值。
'''
print(res)
