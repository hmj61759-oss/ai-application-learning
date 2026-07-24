# Week 2 · TypeScript 速成 + Pi 框架笔记

> 第2次会话：2025-07-24（公司 opencode）— TypeScript 基础、Pi 框架 pi-ai 模块

---

## 一、TypeScript 速成

### TypeScript 是什么？

TypeScript 是**带类型的 JavaScript**，Pi 框架用它写的。

### Python vs JavaScript vs TypeScript 对比

| 概念 | Python | JavaScript | TypeScript |
|------|--------|------------|------------|
| 变量声明 | `name = "hmj"` | `let name = "hmj"` | `let name: string = "hmj"` |
| 常量 | `NAME = "hmj"` (约定) | `const name = "hmj"` | `const name: string = "hmj"` |
| 函数 | `def add(a, b):` | `function add(a, b) {` | `function add(a: number, b: number): number {` |
| 输出 | `print(x)` | `console.log(x)` | `console.log(x)` |
| 字符串模板 | `f"你好{name}"` | `` `你好${name}` `` | `` `你好${name}` `` |
| 对象 | `{"name": "hmj"}` | `{name: "hmj"}` | `{name: "hmj"}` |
| 展开列表 | `[*old, item]` | `[...old, item]` | `[...old, item]` |
| 类型标注 | `name: str = "hmj"` | 无 | `let name: string = "hmj"` |

### 基本类型

```typescript
let name: string = "mengjie";
let age: number = 23;
let isActive: boolean = true;
let skills: string[] = ["python", "ai"];
```

### Interface（接口）

描述对象的"形状"（类似 Python 的 Pydantic BaseModel）：

```typescript
interface Skill {
    name: string;
    level: number;
    category: string;
    isActive?: boolean;  // ? 表示可选字段
}

const mySkill: Skill = {
    name: "python",
    level: 5,
    category: "technical"
};
```

### Type（类型别名）

```typescript
type SkillCategory = "technical" | "soft" | "domain";  // 联合类型
type ID = string | number;
```

### 泛型（Generic）

```typescript
function addItem<T>(item: T, list: T[]): T[] {
    return [...list, item];
}

// 调用时 T 被替换为具体类型
addItem<Skill>(pythonSkill, mySkills);   // T = Skill
addItem<number>(5, [1, 2, 3]);            // T = number
```

**类比 Python 泛型**：
```python
from typing import TypeVar, List
T = TypeVar('T')
def add_item(item: T, list_: List[T]) -> List[T]:
    return [*list_, item]
```

### ES Module

```typescript
// 导出
export interface User { name: string; }
export function greet(name: string): string { return `Hello, ${name}`; }
export default class UserManager { }

// 导入
import UserManager, { User, greet } from './userManager';
```

### 面试高频

**Q：TypeScript 和 JavaScript 区别？**
A：TypeScript 有类型系统，编译时检查错误，IDE 提示更好，适合大型项目。JavaScript 运行时才发现类型错误。

---

## 二、Pi 框架 pi-ai 模块

### 核心设计理念

`pi-ai` 是一个**统一 LLM API**：不管用 OpenAI、Anthropic 还是 Google，用同一套代码调用。

### 三层架构

```
┌─────────────────────────────────────────┐
│  Models 集合（用户面向的统一入口）        │
│  - getModel / stream / complete         │
│  - 路由请求到对应的 Provider             │
├─────────────────────────────────────────┤
│  Provider（运行时单元，每个 LLM 一个）    │
│  - 拥有模型列表、认证方式、流式行为       │
├─────────────────────────────────────────┤
│  API Implementation（底层协议）          │
│  - anthropic-messages / openai-responses │
│  - 不同厂商共享同一套协议实现             │
└─────────────────────────────────────────┘
```

### Provider 概念

Provider = 运行时单元，拥有：
- 模型列表（getModels）
- 认证方式（API Key / OAuth）
- 流式行为（stream）

**对比 opencode.json**：opencode.json 里的 provider 配置和 Pi 的 Provider 概念一样——都是封装"怎么连接某个 LLM"。

### Quick Start 流程

```typescript
// 1. 创建 Models 集合
const models = builtinModels();

// 2. 查找模型
const model = models.getModel('openai', 'gpt-4o-mini');

// 3. 定义工具（TypeBox Schema）
const tools: Tool[] = [{
  name: 'get_time',
  description: 'Get the current time',
  parameters: Type.Object({
    timezone: Type.Optional(Type.String())
  })
}];

// 4. 构建上下文
const context: Context = {
  systemPrompt: 'You are a helpful assistant.',
  messages: [{ role: 'user', content: 'What time is it?' }],
  tools
};

// 5. 流式调用
const s = models.stream(model, context);
for await (const event of s) {
  // 处理事件
}

// 6. 获取结果
const finalMessage = await s.result();
```

### Tool 定义对比

| 概念 | Pi (TypeScript) | Python |
|------|----------------|--------|
| 数据校验 | TypeBox Schema | Pydantic BaseModel |
| 工具定义 | `Tool[]` 数组 | 函数 + 装饰器 |
| 参数描述 | `Type.Object({...})` | `class Params(BaseModel)` |

### 流式事件类型

```
start → text_start → text_delta* → text_end
                   → thinking_start → thinking_delta* → thinking_end
                   → toolcall_start → toolcall_delta* → toolcall_end
      → done | error
```

### 对比 FastAPI

| 概念 | FastAPI | Pi 框架 |
|------|---------|---------|
| 数据校验 | Pydantic | TypeBox |
| 类型系统 | type hints | TypeScript |
| 异步 | async/await | async/await |
| HTTP 调用 | requests/httpx | Provider 内部封装 |
| 配置 | opencode.json | Provider 注册 |
| API 文档 | /docs 自动生成 | 无（面向开发者） |

---

## 三、面试速查卡

| 问题 | 参考回答 |
|------|----------|
| TypeScript 和 JS 区别？ | TS 有类型系统，编译时检查错误，适合大型项目 |
| interface 和 type 区别？ | interface 描述对象结构，type 给类型起别名（可表示联合类型） |
| 泛型作用？ | 让函数/接口处理多种类型，调用时确定具体类型 |
| Pi 的 pi-ai 做了什么？ | 统一 LLM API，封装 30+ Provider，三层架构：Models → Provider → API |
| 为什么用统一 API？ | 不同厂商 API 格式不同，统一层屏蔽差异，切换模型只改一行代码 |
| Pi 的 Tool 和 Python 区别？ | Pi 用 TypeBox Schema，Python 用 Pydantic，核心思路一样 |
| Provider 是什么？ | 运行时单元，拥有模型列表、认证方式、流式行为 |

---

## 四、我的易错点总结

1. **JS 变量声明** → 需要 `let` 或 `const`，Python 不用
2. **JS 对象 key 不加引号** → `{name: "hmj"}` 不是 `{"name": "hmj"}`
3. **JS 字符串模板** → 用反引号 `` ` `` 和 `${}`，不是 `f""` 和 `{}`
4. **TypeScript 类型标注** → `let name: string`，不是 `name: str`
5. **文件名规则** → Python 和 JS 模块名都不能包含连字符 `-`

---

## 五、下节课预告

**Week 2 第3次会话**：深入 Pi 框架源码（`pi-agent-core` + Agent 循环）
- 阅读 `pi-agent-core` README
- 理解 Agent 循环：prompt → LLM → 工具调用 → 结果 → 下一轮
- 对比 FastAPI 的异步处理