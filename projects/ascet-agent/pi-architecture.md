# Pi 框架架构分析

> 本文档记录对 Pi 框架的学习和理解，用于简历准备和面试。
> Pi 是 Ascet Agent 项目的底层框架，TypeScript 编写。

## Pi 是什么

Pi 是一个开源的 AI Agent 框架（by @earendil-works），核心目标是构建"可自我扩展的编码 Agent"。

- 官网：https://pi.dev
- GitHub：pi-mono 仓库
- 语言：TypeScript（ESM，Node ≥ 22.19）
- 架构：monorepo（npm workspaces）

## 四层架构

```
┌─────────────────────────────────────────────────────┐
│  ascet-extension（你的实习项目）                      │
│  13个ASCET工具 + Bosch LLM Provider + 调度器          │
├─────────────────────────────────────────────────────┤
│  pi-coding-agent（CLI + 扩展系统）                    │
│  AgentSession + 扩展加载器 + 内置工具(bash/read/edit) │
├─────────────────────────────────────────────────────┤
│  pi-agent-core（Agent 运行时）                        │
│  Agent循环 + 状态管理 + 工具执行 + 事件流              │
├─────────────────────────────────────────────────────┤
│  pi-ai（统一 LLM API）                                │
│  多Provider(OpenAI/Anthropic/Google) + 工具定义 + 流式 │
└─────────────────────────────────────────────────────┘
```

## 各层职责

### 1. pi-ai（统一 LLM API）
- 统一封装多个 LLM Provider（OpenAI/Anthropic/Google 等 30+）
- 定义 Message/Tool/Event 类型
- 流式响应处理
- 认证管理（API Key / OAuth / 环境变量）

### 2. pi-agent-core（Agent 运行时）
- **Agent 循环**：prompt → LLM → 工具调用 → 结果 → 下一轮
- **状态管理**：AgentState（systemPrompt/model/tools/messages）
- **工具执行**：parallel/sequential 模式
- **事件流**：agent_start → turn_start → message → tool_execution → turn_end → agent_end
- **Session 持久化**：JSONL 格式
- **上下文压缩**：超长时自动 compaction

### 3. pi-coding-agent（CLI + 扩展系统）
- 三种运行模式：interactive（TUI）/ print（一次性）/ rpc（供外部调用）
- AgentSession：封装 Agent 状态 + 事件订阅 + 持久化
- **扩展系统**：用 jiti 动态加载 .ts 扩展，支持注册工具/命令/Provider
- 内置工具：bash/read/edit/write/grep/find/ls

### 4. ascet-extension（实习项目）
- 注册 13 个 ASCET 工具（4个运维 + 9个领域）
- 注册 Bosch LLM Farm Provider（公司内网 LLM 网关）
- 调度器：ASCET ToolAPI 调用串行化（并发不安全）
- 9 个子代理 profile（用于 full-check 工作流）

## Agent 循环详解（面试重点）

```
用户输入 "读取config.json"
│
├─ agent_start
├─ turn_start
├─ 发送 userMessage 给 LLM
├─ LLM 流式响应（assistantMessage）
│   └─ LLM 决定调用 read 工具
├─ tool_execution_start { toolName: "read", args: {path: "config.json"} }
├─ tool_execution_end { result: "文件内容..." }
├─ 把工具结果发回给 LLM
├─ LLM 看到结果后继续响应（可能再调工具，或给出最终回答）
├─ turn_end
├─ agent_end
```

**关键设计**：
- 两层循环：内层处理工具调用+steering，外层处理follow-up
- steering：用户中途打断注入新指令
- follow-up：Agent 本要停止时，队列里还有任务

## ASCET 扩展如何工作（简历核心）

```typescript
// packages/ascet-extension/src/index.ts（简化）
export default function ascetExtension(pi: AscetExtensionAPI) {
  registerBoschLlmFarmProvider(pi);          // 1. 注册自定义 LLM Provider
  for (const tool of canonicalAscetTools) {  // 2. 注册 13 个工具
    pi.registerTool(tool);
  }
  pi.registerCommand("ascet-status", ...);   // 3. 注册斜杠命令
}
```

**三个扩展能力**：
1. `registerProvider` — 注册 Bosch 内网 LLM 网关
2. `registerTool` — 注册 ASCET 领域工具（LLM 可调用）
3. `registerCommand` — 注册用户可用的斜杠命令

## 学习进度

- [ ] W2：读 pi-ai README + types.ts
- [ ] W3：读 pi-agent-core README + ASCET 扩展入口
- [ ] W5：读 agent-loop.ts + 工具注册 + 调度器（重点周）

## 面试问题预案

### Q：你的 Ascet Agent 项目用了什么框架？
A：基于 Pi（一个开源 AI Agent 框架）开发。Pi 提供了 Agent 运行时和扩展系统，我们通过开发 ascet-extension 包把 ASCET 的领域能力（工具调用、LLM Provider）注入进去。

### Q：Agent 是怎么工作的？
A：（用 Agent 循环图回答，见上）

### Q：你们怎么扩展 Pi 的？
A：通过 Pi 的扩展系统，用 registerTool 注册了 13 个 ASCET 工具，用 registerProvider 注册了 Bosch 内网 LLM 网关。扩展用 jiti 动态加载，不需要重新编译主程序。

### Q：为什么 ASCET 工具需要调度器？
A：ASCET 的 ToolAPI 不支持并发调用，所以所有工具调用必须通过调度器资源 `ascet.toolapi.global` 串行化，避免并发冲突。
