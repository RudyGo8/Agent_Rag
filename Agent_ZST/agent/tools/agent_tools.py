'''
@create_time: 2026/3/20 下午6:02
@Author: GeChao
@File: agent_tools.py
'''
from langchain_core.tools import tool
from rag.rag_service import RagSummarizeService
import random
from utils.config_handler import agent_conf
from utils.path_tool import get_abs_path
import os
from utils.logger_handler import logger

rag = RagSummarizeService()
user_ids = ["1234567890", "9876543210", "1111111111", "2222222222", "3333333333"]
month_arr = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
extra_data = {}


@tool(description="从向量存储中检索参考资料")
def rag_summarize(query: str) -> str:
    return rag.rag_summarize(query)


@tool(description="获取指定城市的天气，以消息字符串的形式返回")
def get_weather(city: str) -> str:
    return f"城市{city}的天气为晴天，气温26摄氏度，空气湿度50%，南风1级"


@tool(description="获取用户所在的名称，以纯字符串形式返回")
def get_user_location() -> str:
    return random.choice(["北京", "上海", "广州", "深圳", "天津", "重庆", "武汉", "成都", "杭州", "苏州"])


@tool(description="获取用户的ID，以纯字符串形式返回")
def get_user_id() -> str:
    return random.choice(user_ids)


@tool(description="获取当前月份，以纯字符形式返回")
def get_current_month() -> str:
    return random.choice(month_arr)


def generate_external_data():
    """
    {
    "user_id": "1234567890",
    "user_location": "北京",
    "current_month": "January"
    }
    :return:
    """
    if not extra_data:
        extra_data_path = get_abs_path(agent_conf["extra_data_path"])

        if not os.path.exists(extra_data_path):
            raise FileNotFoundError(f"外部文件{extra_data_path}不存在")

        with open(extra_data_path, "r", encoding="utf-8") as f:
            for line in f.readlines()[1:]:
                arr: list[str] = line.strip().split(',')

                user_id: str = arr[0].replace('"', "")
                feature: str = arr[1].replace('"', "")
                efficiency: str = arr[2].replace('"', "")
                consumables: str = arr[3].replace('"', "")
                comparison: str = arr[4].replace('"', "")
                time: str = arr[5].replace('"', "")

                if user_id not in extra_data:
                    extra_data[user_id] = {}

                extra_data[user_id][time] = {
                    "特征": feature,
                    "效率": efficiency,
                    "消耗品": consumables,
                    "比较": comparison
                }


@tool(description="从外部系统中获取指定用户在指定月份的使用记录，以纯字符串形式返回，如果未检索到返回空字符串")
def fetch_external_data(user_id: str, month: str) -> str:
    generate_external_data()

    try:
        return extra_data[user_id][month]
    except KeyError:
        logger.warning(f"{fetch_external_data}未能检索到用户：{user_id}在{month}的使用记录数据")
        return ""


@tool(description="无入参，无返回值，调用后触发中间件自动为报告生成的场景动态注入上下文信息，为后续提示词切换提供上下文信息")
def fill_context_for_report():
    return "fill_context_for_report已调用"


if __name__ == '__main__':
    print(fetch_external_data("1005", "2025-06"))
