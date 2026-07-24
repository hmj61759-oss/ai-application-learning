# 当前任务卡

> 每次学习开始前，AI 读取此文件确定今天做什么。
> 每次学习结束时，AI 更新此文件为"下次任务"。

---

## 当前任务：Week 2 · Pi 框架源码深入（第3次会话）

**所属周次**：Week 2
**预计时长**：1.5-2 小时

### 今日目标

1. **复习（10分钟）**：Week 2 第2次会话内容
   - TypeScript 基础语法
   - Pi 框架三层架构
   - Provider 概念
2. **Pi 框架 pi-agent-core 模块**：
   - 阅读 `pi-agent-core` README
   - 理解 Agent 循环：prompt → LLM → 工具调用 → 结果 → 下一轮
   - 理解 AgentState、AgentTool、AgentEvent 类型
3. **关联学习**：
   - 将 Agent 循环与 FastAPI 异步处理对比
   - 理解 AgentTool 和 Pydantic BaseModel 的关系

### 今日产出

- [ ] 在 `notes/w02-typescript-pi.md` 追加 agent-core 笔记
- [ ] 理解 Agent 循环的完整流程
- [ ] 能画出 Agent 循环的事件序列图

### 下次任务预告

Week 3：LLM 基础原理 + Ascet 项目初探 + Pi 框架 agent-core 深入

---

## 任务历史

> 每次会话结束后，将当前任务归档到此，并写上新任务。

### 2025-07-24 · Week 2 第2次会话
- 学习内容：TypeScript 速成、Pi 框架 pi-ai 模块
- 产出：练习 1 完成；笔记已写入 w02-typescript-pi.md
- 掌握情况：TS 基础和 Pi 架构 OK；JS 语法细节需要巩固

### 2025-07-24 · Week 2 第1次会话
- 学习内容：Python 异步编程、FastAPI 基础、API 部署
- 产出：创建了 /ask API 接口；笔记已写入 w02-fastapi-basics.md
- 掌握情况：异步和 FastAPI OK；模块路径、语法细节需要巩固

### 2025-07-23 · Week 1 第3次会话（Week 1 完结）
- 学习内容：装饰器、git、HTTP 基础、Linux/Shell
- 产出：练习 7-10 完成；笔记追加至 w01-python-basics.md
- 掌握情况：装饰器和 git OK；命令行格式、装饰器执行时机需要巩固

### 2025-07-21 · Week 1 第2次会话
- 学习内容：函数、类与面向对象、异常处理
- 产出：3 道练习完成（04-functions.py / 05-class.py / 06-exception.py）；笔记已追加
- 掌握情况：基本语法 OK；f-string引号嵌套、异常处理逻辑顺序需要巩固

### 2025-07-17 · Week 1 第1次会话
- 学习内容：conda 环境、数据类型、类型标注、字符串操作、条件判断与循环
- 产出：3 遗道练习完成；笔记已写入 notes/w01-python-basics.md
- 掌握情况：基础语法 OK；in 的两种用法、flag 模式需要巩固
