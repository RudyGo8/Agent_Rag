'''
@create_time: 2026/3/18 下午9:24
@Author: GeChao
@File: 04 middleware中间件.py
'''
from langchain.agents import create_agent
from langchain.agents.middleware import before_agent, after_agent, before_model, after_model, wrap_tool_call, wrap_model_call
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool
from langchain.agents import AgentState
from langgraph.runtime import Runtime


@tool(description="查询天气，传入城市名称字符串，返回字符串天气信息")
def get_weather(city: str) -> str:
    return f"{city}天气：晴天"


"""
1.agent执行前
2.agent执行后
3.model执行前
4.model执行后
5.工具执行中
6.模型执行中
"""


@before_agent
def log_before_agent(state: AgentState, runtime: Runtime) -> None:
    # agent执行前会调用这个函数并传入state和runtime两个对象
    print(f"[before agent] agent启动， 并附带{len(state['messages'])}消息")


@after_agent
def log_after_agent(state: AgentState, runtime: Runtime) -> None:
    print(f"[after agent] agent执行完毕，共生成{len(state['messages'])}消息")


@after_model
def log_befor_model(state: AgentState, runtime: Runtime) -> None:
    print(f"[after_model]模型即将调用，并附带{len(state['messages'])}消息")


@before_model
def log_after_model(state: AgentState, runtime: Runtime) -> None:
    print(f"[after_model]模型调用结束，并附带{len(state['messages'])}消息")


@wrap_model_call
def model_call_hook(request, handler):
    print("模型调用中")
    return handler(request)


@wrap_tool_call
def moniter_tool(request, handler):
    print(f"工具执行：{request.tool_call['name']}")
    print(f"工具执行传入参数：{request.tool_call['args']}")

    return handler(request)


agent = create_agent(
    model=ChatTongyi(model="qwen3-max"),
    tools=[get_weather],
    middleware=[log_before_agent, log_after_agent, log_befor_model, log_after_model, moniter_tool, model_call_hook]
)

res = agent.invoke({"messages": [{"role": "user", "content": "上海这里的天气如何，如何穿衣养生？"}]})
print("*" * 20, res)
