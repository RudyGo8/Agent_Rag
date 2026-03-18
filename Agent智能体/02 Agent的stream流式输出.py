'''
@create_time: 2026/3/18 下午8:23
@Author: GeChao
@File: 02 Agent的stream流式输出.py
'''
from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool


@tool(description="获取股价， 传入股票名称， 返回字符串信息")
def get_price(name: str) -> str:
    return f"股票{name}的价格是20元"


@tool(description="获取股票信息， 传入股票名称， 返回字符串信息")
def get_info(name: str) -> str:
    return f"股票{name}, 是一家A股上市公司，专注于AI开发！"


agent = create_agent(
    model=ChatTongyi(model="qwen3-max"),
    tools=[get_price, get_info],
    system_prompt="你是一个智能助手，可以回答股票相关问题，记住请告知我思考过程，让我知道你为什么调用某个工具"
)

for chunk in agent.stream(
        {"messages": [{"role": "user", "content": "股票AI的股价是多少,并介绍一下？"}]},
        stream_mode="values"
):
    latest_message = chunk['messages'][-1]
    if latest_message.content:
        print(type(latest_message).__name__, latest_message.content)

    try:
        if latest_message.tool_calls:
            print(f"工具调用：{[tc['name'] for tc in latest_message.tool_calls]}")
    except AttributeError as e:
        pass
'''
HumanMessage 股票AI的股价是多少,并介绍一下？
工具调用：['get_price', 'get_info']
ToolMessage 股票AI, 是一家A股上市公司，专注于AI开发！
AIMessage 股票AI的当前股价是20元。这是一家A股上市公司，专注于AI（人工智能）领域的开发。如果您对该公司或其业务有更多具体问题，欢迎继续提问！
'''