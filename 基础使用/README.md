# LangChain 基础使用教程

从入门到实践的 LangChain 学习示例，涵盖 API 调用、提示词工程、向量检索等内容。

## 目录分类

### API基础 (01-09)

| 文件 | 内容 |
|------|------|
| `01 测试APIKEY使用.py` | API密钥配置测试 |
| `02 OpenAI库的基础使用.py` | OpenAI SDK基础 |
| `03 OpenAI库流式调用.py` | 流式输出实现 |
| `04 OpenAI附带历史消息.py` | 多轮对话上下文 |
| `05 提示词优化案例-金融文本分类.py` | 分类提示词设计 |
| `06 Json基础使用.py` | JSON处理基础 |
| `07 提示词优化-金融信息抽取.py` | 信息抽取提示词 |
| `08 提示词优化-金融文本匹配判断.py` | 文本匹配提示词 |
| `09 余弦相似度.py` | 向量相似度计算 |

### LangChain基础 (10-24)

| 文件 | 内容 |
|------|------|
| `10 LangChain阿里云通义千问.py` | 通义千问集成 |
| `11 LangChain流式输出.py` | 流式响应 |
| `12 调用聊天模型.py` | ChatModel使用 |
| `13 消息的简写.py` | 消息语法糖 |
| `14 调用文本嵌入模型.py` | Embeddings使用 |
| `15 通用提示词模版.py` | PromptTemplate |
| `16 FewShot提示词模板.py` | Few-shot学习 |
| `17 模板类的format和invoke方法.py` | 模板调用方式 |
| `18 ChatPromptTemplate使用.py` | 对话提示词模板 |
| `19 Chain基础使用.py` | LCEL链式调用 |
| `20 运算符的重写.py` | Pipe运算符 |
| `21 Runable示例.py` | Runnable接口 |
| `22 StrOutputParser解析器.py` | 输出解析 |
| `23 JsonOutputParser解析器.py` | JSON解析 |
| `24 RunableLambda的基础使用.py` | 自定义Runnable |

### 对话记忆 (25-26)

| 文件 | 内容 |
|------|------|
| `25 临时会话记忆.py` | ConversationBufferMemory |
| `26 长期会话记忆.py` | 长期记忆管理 |

### 文档加载与向量检索 (27-33)

| 文件 | 内容 |
|------|------|
| `27 CSVloader.py` | CSV文档加载 |
| `28 JSONLoader.py` | JSON文档加载 |
| `29 PyPdf使用.py` | PDF文档处理 |
| `30 内存向量存储.py` | InMemoryVectorStore |
| `31 外部向量持久化存储.py` | Chroma向量库 |
| `32 向量检索构建提示词.py` | RAG提示词构建 |
| `33 RunnablePassthrough的使用.py` | 数据传递 |

## 依赖

```bash
pip install langchain langchain-community dashscope openai streamlit chromadb pypdf
```

## 学习路径

```
1. API基础 (01-09)
   ↓
2. LangChain基础 (10-24)
   ↓
3. 对话记忆 (25-26)
   ↓
4. 向量检索 (27-33)
```

## 快速开始

```bash
# 设置API密钥
export DASHSCOPE_API_KEY="your-api-key"

# 运行示例
python "10 LangChain阿里云通义千问.py"
```
