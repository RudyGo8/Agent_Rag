'''
@create_time: 2026/3/10 下午9:12
@Author: GeChao
@File: 04 OpenAI附带历史消息.py
'''
from openai import OpenAI

client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",

)

response = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role": "system", "content": "你是AI助理，回答很简洁"},
        {"role": "user", "content": "小明有两条宠物"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "小红有三条宠物"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "总共有几只宠物"},
    ],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content,
          end=" ",
          flush=True)