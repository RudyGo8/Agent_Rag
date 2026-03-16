'''
@create_time: 2026/3/16 上午11:12
@Author: GeChao
@File: 22 StrOutputParser解析器.py
'''
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import AIMessage


parser = StrOutputParser()
model = ChatTongyi(models="qwen3-max")
prompt = PromptTemplate.from_template(
    "我邻居姓：{lastname}, 刚生了{gender}, 请起名，仅告知我名字无需其他内容。"
)

chain = prompt | model | parser | model | parser

res: str = chain.invoke({'lastname': "葛", "gender": "女儿"})

print(res)
print(type(res))