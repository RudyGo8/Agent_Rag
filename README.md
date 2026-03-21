# Agent_Rag - AI智能应用学习项目

基于 LangChain + 通义千问 的 AI 应用学习项目集，包含 RAG、Agent、LangChain 基础等内容。

## 项目列表

| 项目 | 说明 |
|------|------|
| [Agent_ZST](./Agent_ZST/) | 扫地机器人智能客服系统（RAG + ReAct Agent） |
| [Agent智能体](./Agent智能体/) | LangChain Agent 开发学习示例 |
| [RAG项目案例](./RAG项目案例/) | 完整的 RAG 项目模板 |
| [基础使用](./基础使用/) | LangChain 基础教程（33个示例） |

## 项目简介

### Agent_ZST
扫地机器人领域的智能客服系统，基于 RAG 检索增强 + ReAct Agent 模式，支持：
- 知识库问答
- 天气查询
- 用户信息获取
- 个性化报告生成

### Agent智能体
LangChain Agent 开发入门，包含：
- Agent 基础创建
- 流式输出
- ReAct 模式
- 中间件开发

### RAG项目案例
完整的 RAG 项目模板，包含：
- 文档加载（PDF/TXT/CSV）
- Chroma 向量存储
- 相似度检索
- Streamlit Web界面

### 基础使用
LangChain 基础教程，按功能分为：
- API 基础（01-09）
- LangChain 基础（10-24）
- 对话记忆（25-26）
- 向量检索（27-33）

## 技术栈

- **LangChain** - Agent/RAG 开发框架
- **LangGraph** - Agent 状态管理
- **Chroma** - 向量数据库
- **DashScope** - 通义千问 API
- **Streamlit** - Web 界面

## 快速开始

### 1. 安装依赖
```bash
pip install langchain langchain-community langchain-chroma dashscope streamlit pypdf pyyaml
```

### 2. 配置 API 密钥
```bash
export DASHSCOPE_API_KEY="your-api-key"
```

### 3. 运行示例
```bash
# Agent_ZST 智能客服
cd Agent_ZST
streamlit run app.py

# RAG 项目案例
cd RAG项目案例
streamlit run app_qa.py

# 基础教程
cd 基础使用
python "10 LangChain阿里云通义千问.py"
```

## 目录结构

```
Agent_Rag/
├── Agent_ZST/              # 智能客服系统
├── Agent智能体/            # Agent开发示例
├── RAG项目案例/            # RAG项目模板
├── 基础使用/              # LangChain教程
├── data/                  # 共享数据
├── chroma_db/            # 共享向量库
├── chat_history/         # 聊天历史
├── venv/                 # Python虚拟环境
└── requirements.txt      # 依赖清单
```

## 学习路径

```
1. 基础使用（LangChain API / 提示词 / 向量检索）
       ↓
2. Agent智能体（Agent创建 / ReAct / 中间件）
       ↓
3. RAG项目案例（完整项目结构）
       ↓
4. Agent_ZST（生产级应用）
```
