'''
@create_time: 2026/3/11 下午9:23
@Author: GeChao
@File: 19 Chain基础使用.py
'''
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个 helpful assistant"),
        MessagesPlaceholder("history"),
        ('human', "请再来一首唐诗"),
    ]
)

history_data = [
    ("human", "你来写一首唐诗"),
    ("ai", "床前明月光，疑是地上霜。"),
    ("human", "再来一句"),
    ("ai", "白日依山，黄河入海。"),
]

model = ChatTongyi(model="qwen3-max")

chain = chat_prompt_template | model
# 通过链式调用invoke或stream
# res= chain.invoke({"history": history_data})
# print(res.content)

for chunk in chain.stream({"history": history_data}):
    print(chunk.content, end="", flush=True)
