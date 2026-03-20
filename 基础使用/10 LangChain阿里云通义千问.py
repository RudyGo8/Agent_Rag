'''
@create_time: 2026/3/11 下午4:45
@Author: GeChao
@File: 10 LangChain阿里云通义千问.py
'''
from langchain_community.llms.tongyi import Tongyi

# 不用qwen3-max， 因为qwen3-max是聊天模型， qwen-max是大语言模型
model = Tongyi(model="qwen-max")

# 调用invoke向模型提问
res = model.invoke(input="你是谁啊能做什么？")
print(res)


# from langchain_ollama import OllamaLLM
'''本地测试'''
# model = OllamaLLM(model="qwen2.5:14b")
# res = model.invoke(input="你是谁啊能做什么？")
# print(res)
