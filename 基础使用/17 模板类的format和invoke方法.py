'''
@create_time: 2026/3/11 下午6:45
@Author: GeChao
@File: 17 模板类的format和invoke方法.py
'''
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
from langchain_core.prompts import ChatPromptTemplate

template = PromptTemplate.from_template("我的邻居是:{lastname}, 最喜欢： {hobby}")

res = template.format(lastname="Rudy", hobby=" running")
print(res, type(res))


res2 = template.invoke({"lastname": "Rudy", "hobby": " running"})
print(res2, type(res2))