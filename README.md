# AI 应用开发工程师 · 秋招学习仓库

> 目标：2025年9月秋招，岗位 AI 应用开发工程师
> 周期：2025-07-17 起，约 8 周
> 学习者背景：Python 基础薄弱，AI 零基础，实习中接触 Ascet Agent 项目

## 这个仓库是什么

这是一个**以 Git 为中枢、由 AI Agent 辅助**的个人学习仓库。它解决一个核心问题：

> 公司用 opencode，家里用 codex，两个 AI 互相不知道对方说了什么。怎么让学习连续？

答案：**把学习状态全部沉淀到仓库文件里**。每次开始学习前，AI 先读仓库；每次结束前，AI 把进度写回仓库。Git 就是两个环境之间的"共享记忆"。

## 仓库结构

```
.
├── README.md              # 你正在看的文件：项目说明 + 使用方法
├── AGENTS.md              # AI Agent 协作规则（opencode 和 codex 都读这个）
├── ROADMAP.md             # 8 周学习路线图（总纲，不轻易改动）
├── PROGRESS.md            # 进度追踪表（每周更新）
├── CURRENT_TASK.md        # 当前任务卡（每次学习开始前更新）
├── SESSION_HANDOFF.md     # 会话交接日志（每次学习结束时写）
├── opencode.json          # opencode 配置（公司端）
├── notes/                 # 学习笔记（按主题组织）
├── exercises/             # 练习代码（按主题组织）
├── projects/              # 实战项目
│   └── ascet-agent/       # Ascet Agent 项目分析与简历提炼
└── reviews/               # 周复盘记录
```

## 怎么用（日常流程）

### 每次开始学习时（3 步）

```bash
# 1. 拉取最新进度
git pull

# 2. 打开 AI Agent（opencode 或 codex），说：
#    "继续学习，先读 CURRENT_TASK.md 和 SESSION_HANDOFF.md"

# 3. AI 会告诉你上次学到哪、今天该做什么
```

### 每次结束学习时（3 步）

```bash
# 1. 让 AI 更新 SESSION_HANDOFF.md 和 CURRENT_TASK.md
#    说："今天学习结束，更新交接文件"

# 2. 提交进度
git add -A && git commit -m "学习进度: <主题> <日期>"
git push

# 3. 下次在另一台电脑 git pull 即可无缝继续
```

## 学习方法论

1. **输入 → 动手 → 输出**：每个知识点都要写笔记 + 写代码 + 能口述
2. **简历导向**：所有学习最终服务于简历和面试，不做无用功
3. **项目驱动**：Ascet Agent 项目是核心，基础知识围绕它补
4. **间隔重复**：笔记定期回顾，PROGRESS.md 里有回顾标记位

## 当前进度

查看 [PROGRESS.md](./PROGRESS.md) 了解详细进度，[CURRENT_TASK.md](./CURRENT_TASK.md) 了解今天该做什么。
