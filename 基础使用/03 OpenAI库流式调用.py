'''
@create_time: 2026/3/10 下午9:10
@Author: GeChao
@File: 03 OpenAI库流式调用.py
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
    ],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content,
          end=" ",
          flush=True)

