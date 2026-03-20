'''
@create_time: 2026/3/16 下午2:54
@Author: GeChao
@File: 25 临时会话记忆.py
'''
from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

model = ChatTongyi(models="qwen3-max")
str_parser = StrOutputParser()

# prompt = PromptTemplate.from_template(
#     "你需要根据会话历史回应用户问题，对话历史： {chat_history}, 用户提问: {input}, 请回答"
# )

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你需要根据会话历史回应用户问题，对话历史："),
        MessagesPlaceholder("chat_history"),
        ("human", "用户提问: {input}"),

    ]
)


def print_prompt(full_prompt):
    print("=" * 20, full_prompt.to_string(), "=" * 20)
    return full_prompt


base_chain = prompt | model | str_parser
store = {}


def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


# 创建一个新的链
conversion_chain = RunnableWithMessageHistory(
    base_chain,  # 被增强的原有chain
    get_history,  # 通过会话id获取InMemoryChatMessageHistory类对象
    input_messages_key="input",  # 表示用户输入在模板中的占位符
    history_messages_key="chat_history",
)

'''
第1次执行： 好的，小明有两只喵，听起来很可爱呢！你是不是想继续讲一个关于小明和他猫咪的故事呢？或者你有什么问题想要问关于这两只喵的？
第2次执行： 小刚有1只汪，听起来也很可爱！你是不是想讲一个关于小刚和他狗狗的故事呢？或者你想知道更多关于这只汪的信息？
第3次执行： 小明有两只喵，小刚有1只汪，所以总共有 2 + 1 = 3 只宠物。
'''

if __name__ == '__main__':
    session_config = {
        "configurable": {
            "session_id": "user_01"
        }
    }
    res = conversion_chain.invoke({"input": "小明有两只喵，"}, session_config)
    print("第1次执行：", res)
    res = conversion_chain.invoke({"input": "小刚有1只汪，"}, session_config)
    print("第2次执行：", res)
    res = conversion_chain.invoke({"input": "总共有几只宠物，"}, session_config)
    print("第3次执行：", res)
