'''
@create_time: 2026/3/18 下午7:10
@Author: GeChao
@File: 01 Agent智能体初体验.py
'''
from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool


@tool(description="获取天气情况")
def get_weather() -> str:
    return "晴天"


agent = create_agent(
    model=ChatTongyi(model="qwen3-max"),
    tools=[get_weather],
    system_prompt="您是一个聊天助手，可以回答用户问题"
)

res = agent.invoke(
    {
        "messages": [
            {"role": "user", "content": "明天上海的天气怎么样？"}
        ]
    }
)

'''
HumanMessage 明天上海的天气怎么样？
AIMessage 
ToolMessage 晴天
AIMessage 明天上海的天气是晴天，适合外出活动！记得做好防晒措施哦。
'''
for msg in res["messages"]:
    print(type(msg).__name__, msg.content)
