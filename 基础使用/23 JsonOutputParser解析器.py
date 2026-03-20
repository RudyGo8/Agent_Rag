'''
@create_time: 2026/3/16 下午12:36
@Author: GeChao
@File: 23 JsonOutputParser解析器.py
'''
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate

str_parser = StrOutputParser()
json_parser = JsonOutputParser()

model = ChatTongyi(models="qwen3-max")

first_prompt = PromptTemplate.from_template(
    "我邻居姓:{lastname}, 刚生了{gender}, 请起名，并封装到JSON格式返回给我,"
    "要求key是name，value是起的名字"
)

second_prompt = PromptTemplate.from_template(
    "姓名{name}, 请帮我解析含义"
)

chain = first_prompt | model | json_parser | second_prompt | model | str_parser

for chunk in chain.stream({"lastname": "葛", "gender": "女儿"}):
    print(chunk, end="", flush=True)
