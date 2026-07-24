# Week 2 · FastAPI 基础笔记

> 第1次会话：2025-07-24（公司 opencode）— Python 异步编程、FastAPI 基础、API 文档机制

---

## 一、Python 异步编程

### 为什么需要异步？

异步编程是**同时处理多个任务**的技术。在 AI 应用中特别重要，因为调用 LLM API 通常需要等待（网络延迟），如果用同步方式，程序会卡住。

```python
# 同步方式（会卡住）
def sync_call_llm():
    result1 = call_llm_api("prompt1")  # 等待 1 秒
    result2 = call_llm_api("prompt2")  # 等待 1 秒
    result3 = call_llm_api("prompt3")  # 等待 1 秒
    # 总共等待 3 秒

# 异步方式（并发执行）
async def async_call_llm():
    task1 = call_llm_api_async("prompt1")  # 启动，不等待
    task2 = call_llm_api_async("prompt2")  # 启动，不等待  
    task3 = call_llm_api_async("prompt3")  # 启动，不等待
    result1, result2, result3 = await task1, await task2, await task3
    # 总共等待约 1 秒（3 个请求同时进行）
```

### 基本语法

```python
import asyncio

# 定义异步函数
async def async_hello(name: str) -> str:
    await asyncio.sleep(1)  # 模拟异步等待（不会卡住其他任务）
    return f"你好，{name}！"

# 调用异步函数
async def main():
    result = await async_hello("mengjie")
    print(result)

# 运行异步程序
asyncio.run(main())
```

### 关键概念

| 概念 | 说明 | 例子 |
|------|------|------|
| `async def` | 定义异步函数 | `async def func():` |
| `await` | 等待异步操作完成 | `Result = await async_func()` |
| `asyncio.run()` | 运行异步程序 | `asyncio.run(main())` |
| `asyncio.sleep()` | 异步等待（不卡住其他任务） | `await asyncio.sleep(1)` |
| `asyncio.gather()` | 并发执行多个任务 | `await asyncio.gather(task1, task2, task3)` |

### 面试高频

**Q：为什么 AI 应用要用异步？**
A：因为调用 LLM API 有网络延迟，用异步可以并发处理多个请求，提高效率。比如同时处理 3 个用户的请求，异步方式只需要 1 秒，同步方式需要 3 秒。

---

## 二、FastAPI 基础

### FastAPI 是什么？

FastAPI 是**现代 Python Web 框架**，特别适合 AI 应用开发，因为：

1. **性能优秀**：基于 Starlette + Uvicorn，比 Flask 快很多
2. **类型安全**：内置 Pydantic，自动校验数据
3. **自动生成 API 文档**：开箱即用的 Swagger UI
4. **异步友好**：天然支持 async/await

### Web 框架对比

```python
# Flask（老一代框架）
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    prompt = data['prompt']
    # 处理逻辑
    return jsonify({"answer": f"AI 回答：{prompt}"})
```

```python
# FastAPI（新一代框架）
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    prompt: str

@app.post('/ask')
async def ask(question: Question):
    # 处理逻辑
    return {"answer": f"AI 回答：{question.prompt}"}
```

**FastAPI 的优势**：
- **自动校验**：Flask 需要手动检查 `data['prompt']`，FastAPI 自动校验
- **类型安全**：Pydantic 自动解析和校验数据类型
- **异步支持**：`async def` 天然支持，Flask 需要额外配置
- **自动生成文档**：访问 `/docs` 就能看到 API 文档

### 技术栈拆解

```
FastAPI（应用框架）
├── Starlette（异步基础框架，处理 WebSocket、后台任务等）
├── Pydantic（数据校验和解析）
└── Uvicorn（ASGI 服务器，运行 FastAPI 应用）
```

**类比**：
- **FastAPI** = 乐高积木的说明书（告诉你怎么搭）
- **Starlette** = 乐高的基础零件（提供底层功能）
- **Pydantic** = 检查员（检查输入是否符合要求）
- **Uvicorn** = 电动马达（让整个装置运转起来）

### 基本用法

```python
from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

# 定义请求体的数据结构
class Question(BaseModel):
    prompt: str
    max_tokens: int = 100  # 默认值

# 创建 FastAPI 应用
app = FastAPI()

# 定义 API 路由
@app.post("/ask")
async def ask(question: Question):
    # 模拟调用 LLM API（异步等待）
    await asyncio.sleep(0.5)
    
    # 返回响应
    return {
        "answer": f"AI 回答：{question.prompt}",
        "tokens_used": len(question.prompt),
        "max_tokens": question.max_tokens
    }
```

### FastAPI + 异步 + LLM API 调用

```python
from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.post("/chat")
async def chat(prompt: str):
    # 模拟调用 LLM API
    await asyncio.sleep(1)  # 模拟网络延迟
    return {"response": f"AI 回答：{prompt}"}
```

### 面试高频

**Q：FastAPI 和 Flask 区别？**
A：FastAPI 支持异步、内置数据校验、自动生成文档、性能更好。Flask 是同步的，需要手动校验数据。AI 应用调用 LLM 有延迟，异步特性很重要。

**Q：为什么 AI 应用用 FastAPI？**
A：FastAPI 性能好、支持异步、内置数据校验、自动生成文档。调用 LLM API 有网络延迟，异步特性很重要。Pydantic 自动校验用户输入，安全性好。

---

## 三、FastAPI 工作机制与部署

### 服务启动过程

```bash
uvicorn main:app --reload
```

启动过程：
1. **Uvicorn 启动 HTTP 服务器**
2. **监听 127.0.0.1:8000 端口**
3. **加载 main.py 中的 app (FastAPI 实例)**
4. **FastAPI 扫描所有路由装饰器 (@app.post 等)**
5. **建立路由映射表**

### URL 路径映射

```
http://127.0.0.1:8000/          → 没有定义根路由 → 404 Not Found
http://127.0.0.1:8000/ask        → @app.post("/ask") → 你的问答接口
http://127.0.0.1:8000/docs       → FastAPI 自动生成 → API 文档页面
http://127.0.0.1:8000/redoc      → FastAPI 自动生成 → ReDoc 文档
```

### FastAPI 自动功能

```python
@app.post("/ask")  # 你定义的路由
async def ask(question: Question):
    # 你的业务逻辑
```

FastAPI 自动：
- **创建 /ask POST 接口**（你写的）
- **生成 /docs 页面**（Swagger UI 文档）
- **生成 /redoc 页面**（ReDoc 文档）
- **数据校验**（Pydantic 自动校验 Question）
- **JSON 序列化**（自动转为 JSON 响应）

### API 文档页面

**Swagger UI**（`/docs`）和 **ReDoc**（`/redoc`）的 HTML/CSS/JS 都是 FastAPI 预先打包好的，你不需要写前端代码。

### 模块导入路径问题

**问题**：文件名包含连字符 `-` 会导致 Python 模块导入失败
```bash
# ❌ 错误：文件名包含连字符
exercises/w02-fastapi-basics/02-fastapi-basics.py

# ✅ 正确：使用下划线
exercises/w02_fastapi_basics/02_fastapi_basics.py
```

**解决方案**：创建入口文件 `main.py` 导入模块
```python
from exercises.w02_fastapi_basics import 02_fastapi_basics
app = 02_fastapi_basics.app
```

---

## 四、代码逐行解释

### 异步函数代码解释

```python
from fastapi import FastAPI          # 导入 FastAPI 类，用来创建 Web 应用
from pydantic import BaseModel      # 导入 BaseModel，用来定义数据结构（校验输入）
import asyncio                      # 导入 asyncio，用来做异步操作（模拟 API 调用延迟）

class Question(BaseModel):          # 定义数据模型：规定请求必须包含 prompt(str)，max_tokens(int，默认100)
    prompt: str                      # Pydantic 会自动校验：如果用户传 {"prompt": 123}，会报错因为 prompt 应该是 str
    max_tokens: int = 100           # max_tokens 是整数，默认值 100

app = FastAPI()                     # 创建 FastAPI 应用实例，就像创建一个"网站服务器"

@app.post("/ask")                   # 装饰器：告诉 FastAPI 这个函数处理 POST /ask 请求
async def ask(question: Question):  # 定义处理函数，参数 question 自动解析为 Question 类型
    await asyncio.sleep(0.5)        # 模拟调用 LLM API 的延迟（0.5秒），但不会卡住其他请求
    return {                        # 返回响应
        "answer": f"AI 回答：{question.prompt}",      # question.prompt 是用户输入的 prompt
        "tokens_used": len(question.prompt),          # 计算 prompt 长度
        "max_tokens": question.max_tokens             # 返回用户设置的最大 token 数
    }
```

### 常见错误及解决

1. **`return{` 缺少空格** → Python 解析错误，导致路由无法注册
2. **文件名包含连字符** → Python 模块导入失败
3. **没有定义根路由** → 访问 `/` 返回 404

---

## 五、面试速查卡（Week 2 新增）

| 问题 | 参考回答 |
|------|----------|
| 为什么用异步？ | 调用 LLM API 有网络延迟，异步可以并发处理多个请求，提高效率 |
| `async def` 和 `await` 作用？ | `async def` 定义异步函数，`await` 等待异步操作完成 |
| FastAPI vs Flask？ | FastAPI 支持异步、内置数据校验、自动生成文档、性能更好 |
| Pydantic 作用？ | 自动校验和解析请求数据，确保类型安全 |
| FastAPI 自动生成什么？ | API 文档（/docs）、数据校验、JSON 序列化 |
| 如何定义 API 路由？ | `@app.post("/path")` 或 `@app.get("/path")` |
| 如何处理请求体？ | 用 Pydantic BaseModel 定义数据结构，函数参数自动解析 |

---

## 六、我的易错点总结（第1次会话）

1. **`return{` 缺少空格** → Python 解析错误，导致路由无法注册，访问 404
2. **文件名包含连字符** → Python 模块名不能包含 `-`，要用 `_` 代替
3. **混淆根路由和 API 路由** → `/` 是根路由（未定义返回 404），`/ask` 是 API 路由
4. **不理解 FastAPI 自动功能** → 不需要手动写前端，/docs 页面自动生成
5. **模块导入路径错误** → 需要正确的包结构和入口文件

---

## 七、实践成果

### 完成的 API 接口

```python
# 创建了 /ask POST 接口，支持：
# 1. 异步处理（提高并发性能）
# 2. 数据校验（Pydantic 自动校验）
# 3. 自动文档（/docs 页面）
# 4. JSON 序列化（自动响应格式）
```

### 测试结果

- ✅ API 文档页面正常显示（http://127.0.0.1:8000/docs）
- ✅ /ask 接口正常工作
- ✅ 数据校验功能正常
- ✅ 异步处理功能正常

---

## 八、下节课预告

**Week 2 第2次会话**：TypeScript 速成 + Pi 框架源码阅读（`pi-ai` README）
- 学习 TypeScript 基础（为读 Pi 源码准备）
- 阅读 `pi-ai` 模块的 README（理解统一 LLM API 设计）
- 将 FastAPI 知识与 Pi 框架关联