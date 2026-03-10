'''
@create_time: 2026/3/10 下午8:52
@Author: GeChao
@File: 02 OpenAI库的基础使用.py
'''
from openai import OpenAI

client = OpenAI(
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",

    )

response = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role": "user", "content": "你是python专家，并且不说废话"},
        {"role": "assistant", "content": "是的，我是一个python专家"},
        {"role": "user", "content": "那么，你能不能帮我写一个python程序，计算1到100的和"},
    ]
)

print(response.choices[0].message.content)