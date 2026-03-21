# Agent_ZST - 扫地机器人智能客服系统

基于 RAG + ReAct Agent 的智能客服系统，专注于扫地机器人领域的问答服务，支持生成个性化使用报告。

## 项目架构

```
Agent_ZST/
├── app.py                      # Streamlit Web应用入口
├── agent/                      # Agent智能体核心模块
│   ├── react_agent.py          # ReAct Agent实现
│   └── tools/                  # Agent工具集
│       ├── agent_tools.py      # 7个可调用工具
│       └── middleware.py       # 中间件（日志、提示词切换）
├── rag/                        # RAG检索增强模块
│   ├── rag_service.py         # RAG总结服务
│   └── vector_store.py        # 向量存储服务
├── model/                      # 模型工厂
│   └── factory.py             # Chat和Embedding模型管理
├── utils/                      # 工具函数
│   ├── config_handler.py       # YAML配置加载
│   ├── file_handler.py        # 文件处理、MD5计算
│   ├── logger_handler.py      # 日志管理
│   ├── path_tool.py          # 路径工具
│   └── prompt_loader.py       # 提示词加载
├── config/                     # 配置文件
│   ├── rag.yml                # RAG配置（模型名称）
│   ├── chroma.yml            # Chroma配置（分块、路径）
│   ├── agent.yml             # Agent配置
│   └── prompts.yml           # 提示词路径配置
├── prompts/                    # 提示词模板
│   ├── main_prompt.txt       # Agent主提示词
│   ├── rag_summarize.txt     # RAG总结提示词
│   └── report_prompt.txt     # 报告生成提示词
└── data/                       # 知识库数据
    ├── *.txt                  # 扫地机器人知识文档
    └── *.pdf                  # PDF格式文档
```

## 核心模块

### 1. Agent层 (`agent/`)

| 模块 | 功能 |
|------|------|
| `react_agent.py` | 基于ReAct模式的智能体，支持流式输出、动态提示词切换 |
| `agent_tools.py` | 7个工具：RAG检索、天气查询、用户信息获取、报告生成等 |
| `middleware.py` | 中间件：工具调用监控、模型执行日志、提示词动态切换 |

### 2. RAG层 (`rag/`)

| 模块 | 功能 |
|------|------|
| `rag_service.py` | 文档检索、上下文构建、LLM总结生成 |
| `vector_store.py` | Chroma向量库管理、文本分块、MD5去重 |

### 3. 模型层 (`model/`)

| 模型 | 类型 | 说明 |
|------|------|------|
| `chat_model` | qwen3-max | 通义千问对话模型 |
| `embed_model` | text-embedding-v4 | 通义千问Embedding模型 |

## 技术栈

- **Streamlit** - Web界面
- **LangChain/LangGraph** - Agent开发框架
- **Chroma** - 向量数据库
- **DashScope** - 阿里云通义千问API
- **PyPDFLoader** - PDF文档加载

## 业务流程

```
用户提问 → Streamlit接收 → Agent推理(ReAct)
                                    ↓
                          是否需要调用工具？
                                    ↓
              ┌─────────────────────┼─────────────────────┐
              ↓                     ↓                     ↓
         RAG检索              天气/用户信息         外部数据获取
              ↓                     ↓                     ↓
              └─────────────────────┼─────────────────────┘
                                    ↓
                            LLM生成回答
                                    ↓
                          流式输出展示
```

## 快速开始

1. **安装依赖**
```bash
pip install streamlit langchain langchain-community langchain-chroma dashscope pypdf pyyaml
```

2. **配置API密钥**
```bash
export DASHSCOPE_API_KEY="your-api-key"
```

3. **启动应用**
```bash
cd Agent_ZST
streamlit run app.py
```

4. **初始化知识库**（首次运行）
```bash
python -m rag.vector_store
```

## 配置文件说明

| 文件 | 配置项 |
|------|--------|
| `rag.yml` | `chat_model_name`, `embedding_model_name` |
| `chroma.yml` | `collection_name`, `persist_directory`, `chunk_size`, `chunk_overlap`, `data_path` |
| `agent.yml` | 外部数据路径等Agent相关配置 |
| `prompts.yml` | 提示词模板文件路径 |

## 特色功能

- **动态提示词切换** - 报告生成场景自动切换提示词
- **MD5去重机制** - 避免重复加载文档到向量库
- **流式响应** - 实时展示AI思考和回答过程
- **多工具协同** - RAG检索 + 天气 + 用户信息 + 外部数据

## 目录说明

| 目录 | 说明 |
|------|------|
| `data/` | 知识库文档（txt/pdf） |
| `logs/` | 运行日志，按日期自动生成 |
| `chroma_db/` | Chroma向量数据库文件 |
| `prompts/` | 提示词模板 |
