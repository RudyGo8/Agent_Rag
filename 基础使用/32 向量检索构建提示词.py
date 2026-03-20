'''
@create_time: 2026/3/17 下午3:38
@Author: GeChao
@File: 32 向量检索构建提示词.py
'''
from langchain_community.chat_models import ChatTongyi
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

input_text = "怎么学习呢"

# 检索向量库
result = vector_store.similarity_search(input_text, k=2)
reference_text = "["
for doc in result:
    reference_text += doc.page_content
reference_text += "]"


def print_prompt(prompt):
    print(prompt.to_string())
    print("=" * 20)
    return prompt


chain = prompt | print_prompt | model | StrOutputParser()

res = chain.invoke({"input": input_text, "context": reference_text})
print(res)
