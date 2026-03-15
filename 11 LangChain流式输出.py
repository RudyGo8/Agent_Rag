'''
@create_time: 2026/3/11 下午5:10
@Author: GeChao
@File: 11 LangChain流式输出.py
'''
from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-max")

res = model.stream(input="你是谁呀能做什么？")
for chunk in res:
    print(chunk, end="", flush=True)

