# Agent智能体

LangChain Agent 开发学习示例，基于通义千问 API。

## 文件说明

| 文件 | 内容 |
|------|------|
| `01 Agent智能体初体验.py` | Agent基础概念和创建 |
| `02 Agent的stream流式输出.py` | Agent流式输出实现 |
| `03 ReAct.py` | ReAct（Reasoning + Acting）模式 |
| `04 middleware中间件.py` | Agent中间件开发 |

## 核心概念

### Agent 组成

```
Agent = Model + Tools + Prompt
```

- **Model** - 大语言模型（qwen3-max）
- **Tools** - Agent可调用的工具函数
- **Prompt** - 指导Agent行为的提示词

### ReAct 模式

ReAct = Reasoning + Acting

让Agent在执行过程中交替进行：
1. **Thought** - 思考下一步应该做什么
2. **Action** - 执行具体操作
3. **Observation** - 观察执行结果

## 依赖

```bash
pip install langchain langchain-community dashscope streamlit
```

## 快速开始

```bash
# 设置API密钥
export DASHSCOPE_API_KEY="your-api-key"

# 运行示例
python "01 Agent智能体初体验.py"
```
