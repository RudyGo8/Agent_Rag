# RAG项目案例

完整的 RAG（检索增强生成）项目模板，基于 LangChain + Chroma + 通义千问。

## 项目结构

```
RAG项目案例/
├── app_qa.py               # 问答Web界面
├── app_file_uploader.py    # 文件上传Web界面
├── rag.py                  # RAG核心逻辑
├── vector_stores.py        # 向量存储管理
├── knowledge_base.py       # 知识库管理
├── file_history_store.py   # 文件历史记录
├── config_data.py         # 配置管理
├── chroma_db/             # Chroma向量数据库
├── chat_history/         # 聊天历史记录
└── data/                  # 知识库数据
```

## 核心模块

| 模块 | 功能 |
|------|------|
| `rag.py` | RAG检索、上下文构建、答案生成 |
| `vector_stores.py` | Chroma向量库创建和管理 |
| `knowledge_base.py` | 知识库文档加载和分块 |
| `app_qa.py` | Streamlit问答界面 |
| `app_file_uploader.py` | 文档上传和管理界面 |

## 流程图

```
用户问题
    ↓
向量检索（Chroma）
    ↓
获取相关文档
    ↓
构建Prompt（问题+上下文）
    ↓
LLM生成答案
    ↓
返回结果
```

## 依赖

```bash
pip install streamlit langchain langchain-community langchain-chroma dashscope pypdf pyyaml
```

## 快速开始

1. **配置API密钥**
```bash
export DASHSCOPE_API_KEY="your-api-key"
```

2. **启动问答应用**
```bash
streamlit run app_qa.py
```

3. **启动文件上传**
```bash
streamlit run app_file_uploader.py
```

## 功能特性

- [x] PDF/TXT文档加载
- [x] 文本分块处理
- [x] Chroma向量存储
- [x] 相似度检索
- [x] Streamlit Web界面
- [x] 聊天历史记录
- [x] MD5去重机制
