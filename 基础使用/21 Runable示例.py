'''
@create_time: 2026/3/15 下午4:45
@Author: GeChao
@File: 21 Runable示例.py
'''
from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

prompt = PromptTemplate.from_template("你是一个AI助手！")
model = Tongyi(models="qwen3-max")


chain = prompt | model | prompt | model
# chain.invoke()
# chain.stream()
'''
first=PromptTemplate(input_variables=[], input_types={}, partial_variables={}, template='你是一个AI助手！') middle=[Tongyi(client=<class 'dashscope.aigc.generation.Generation'>, model_kwargs={}), PromptTemplate(input_variables=[], input_types={}, partial_variables={}, template='你是一个AI助手！')] last=Tongyi(client=<class 'dashscope.aigc.generation.Generation'>, model_kwargs={})
<class 'langchain_core.runnables.base.RunnableSequence'>
'''
print(chain)
print(type(chain))
