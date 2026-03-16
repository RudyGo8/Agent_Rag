'''
@create_time: 2026/3/16 下午3:48
@Author: GeChao
@File: 26 长期会话记忆.py
'''
import os, json
from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import message_to_dict, messages_from_dict, BaseMessage
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from sqlalchemy import Sequence


class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self, session_id, storage_path):
        self.session_id = session_id
        self.storage_path = storage_path
        self.file_path = os.path.join(self.storage_path, self.session_id)
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        all_messages = list(self.messages)
        all_messages.extend(messages)

        # new_messages = []
        # for message in all_messages:
        #     d = message_to_dict(message)
        #     new_messages.append(d)

        new_messages = [message_to_dict(message) for message in all_messages]

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(new_messages, f)

    @property
    def messages(self) -> list[BaseMessage]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                messages_data = json.load(f)
                return messages_from_dict(messages_data)
        except FileNotFoundError:
            return []

    def clear(self) -> None:
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([], f)

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


base_chain = prompt | print_prompt |model | str_parser
store = {}


def get_history(session_id):
    return FileChatMessageHistory(session_id, "./chat_history")


# 创建一个新的链
conversion_chain = RunnableWithMessageHistory(
    base_chain,  # 被增强的原有chain
    get_history,  # 通过会话id获取InMemoryChatMessageHistory类对象
    input_messages_key="input",  # 表示用户输入在模板中的占位符
    history_messages_key="chat_history",
)

'''
==================== System: 你需要根据会话历史回应用户问题，对话历史：
Human: 小明有两只喵，
AI: 好的，小明有两只喵，听起来很可爱呢！你是不是想继续讲一个关于小明和他猫咪的故事呢？或者你有什么问题想要问关于这两只喵的？
Human: 小刚有1只汪，
AI: 小刚有1只汪，听起来也很可爱呢！和小明的两只喵相比，小刚的汪是不是更特别呢？你是不是想继续讲关于小刚和他狗狗的故事，或者有什么问题想问呢？😊
Human: 用户提问: 小明有两只喵， ====================
第1次执行： 小明有两只喵，听起来很可爱呢！你是不是想继续讲一个关于小明和他猫咪的故事呢？或者你有什么问题想要问关于这两只喵的？
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
