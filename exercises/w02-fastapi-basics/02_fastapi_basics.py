from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

# 定义请求体的数据结构
class Question(BaseModel):
    prompt: str
    max_tokens: int = 100

# 创建FastAPI应用
app = FastAPI()

# 定义API路由
@app.post("/ask")
async def ask(question:Question):
    # 模拟调用LLM API（异步等待）
    await asyncio.sleep(0.5)

    # 返回响应
    return {
        "answer": f"AI 回答：{question.prompt}",
        "tokens_used": len(question.prompt),
        "max_tokens": question.max_tokens
    }

# 运行服务的代码
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)