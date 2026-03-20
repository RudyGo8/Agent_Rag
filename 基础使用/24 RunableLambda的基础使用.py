'''
@create_time: 2026/3/16 下午1:21
@Author: GeChao
@File: 24 RunableLambda的基础使用.py
'''
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

str_parser = StrOutputParser()

model = ChatTongyi(models="qwen3-max")

first_prompt = PromptTemplate.from_template(
    "我邻居姓:{lastname}, 刚生了{gender}, 请起名，仅生成一个名字，并告知我名字，不要额外信息,"
    "要求key是name，value是起的名字"
)

second_prompt = PromptTemplate.from_template(
    "姓名{name}, 请帮我解析含义"
)

# my_func = RunnableLambda(lambda ai_msg: {"name": ai_msg.content})
# chain = first_prompt | model | my_func | second_prompt | model | str_parser

chain = first_prompt | model | RunnableLambda(lambda ai_msg: {"name": ai_msg.content}) | second_prompt | model | str_parser

for chunk in chain.stream({"lastname": "葛", "gender": "女孩"}):
    print(chunk, end= "", flush=True)