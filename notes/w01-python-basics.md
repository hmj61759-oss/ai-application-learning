# Week 1 · Python 基础笔记

> 第1次会话：2025-07-17（公司 opencode）— conda 环境、数据类型、类型标注、条件判断与循环
> 第2次会话：2025-07-21（公司 opencode）— 函数、类与面向对象、异常处理
> 第3次会话：2025-07-23（公司 opencode）— 装饰器、git、HTTP 基础、Linux/Shell

---

## 一、环境管理

### Python / Conda / Anaconda / venv / uv 的关系

| 名称 | 是什么 | 比喻 |
|------|--------|------|
| Python | 语言引擎，必须要有 | 汽车引擎 |
| Anaconda | 大礼包（Python + 几百个包 + conda 工具） | 整车 |
| conda | 包管理器 + 环境管理器（Anaconda 自带） | 4S店维修工具 |
| venv | Python 自带的轻量环境管理器 | 简易工具箱 |
| uv | Rust 写的极快包管理器（Astral 公司出品） | 赛车级工具 |

**关键理解**：
- conda 和 venv **都是虚拟环境的实现方式**，不是替代 Python
- conda 能管非 Python 依赖（如 C 库），venv 只管 Python 包
- uv 速度极快（比 pip 快 10-100 倍），但只管 Python 包
- 已经装了 Anaconda 就用 conda，不用再装官方 Python 或 uv

### conda 常用命令（面试可能问）

```bash
conda create -n 环境名 python=3.12   # 创建环境
conda activate 环境名                  # 激活环境（命令行前缀会变）
conda deactivate                       # 退出环境
conda env list                         # 查看所有环境
```

### 易错点（我的追问）

- **编辑器 Run 按钮无法运行**：编辑器和终端是独立的，终端激活了 conda 环境不等于编辑器也用了。VS Code 要按 `Ctrl+Shift+P` → `Python: Select Interpreter` → 选择对应环境
- **python 找不到文件**：`python 文件名` 在当前工作目录找文件，如果文件在子目录要用完整路径 `python exercises/w01-python-basics/xxx.py`

---

## 二、数据类型

### 核心数据类型

```python
age: int = 25                    # 整数
price: float = 9.99              # 浮点数
name: str = "hmj"                # 字符串
is_student: bool = True          # 布尔

tags: list[str] = ["ai", "python"]           # 列表（可改、有序、可重复）
point: tuple[int, int] = (10, 20)            # 元组（不可改、有序）
config: dict[str, str] = {"model": "gpt-4"}  # 字典（键值对）
unique_ids: set[int] = {1, 2, 3}             # 集合（不重复）
```

### list vs tuple vs set（面试高频）

| | list | tuple | set |
|---|---|---|---|
| 可修改 | ✅ | ❌ | ✅ |
| 有序 | ✅ | ✅ | ❌ |
| 允许重复 | ✅ | ✅ | ❌ |
| 适用场景 | 通用 | 不变数据（坐标/配置） | 去重 |

### 易错点（我的练习）

- **`age='23'` vs `age=23`**：加引号变成字符串，`'23' + 1` 会报错。要有**类型意识**
- **`append('skill')` vs `append(skill)`**：加引号存的是字符串 "skill"，不加引号存的是变量的值

---

## 三、类型标注（Type Hints）

### 为什么需要

- Python 默认不限制类型，容易出 bug
- 加了类型标注后，编辑器能帮你检查错误
- **AI 项目几乎都用**（LangChain、FastAPI、OpenAI SDK 代码里全是）

### 语法

```python
# 变量
name: str = "hmj"
age: int = 23
skills: list[str] = ["python", "git"]

# 字典值类型混合时
profile: dict[str, object] = {"name": "hmj", "age": 23}
# 或严格写法（Python 3.10+）
profile: dict[str, str | int | list[str]] = {"name": "hmj", "age": 23, "skills": ["python"]}

# 函数
def greet(name: str) -> str:
    return "hello " + name
```

### 面试题

**Q：Python 的类型标注是强制的吗？**
A：不是强制的，只是提示，运行时不检查。但编辑器和 mypy 工具可以静态检查。

---

## 四、字符串操作

### join：列表转字符串

```python
my_skills = ["python", "git", "ai"]

", ".join(my_skills)   # "python, git, ai"     ← 用 ", " 连接
"-".join(my_skills)    # "python-git-ai"
"".join(my_skills)     # "pythongitai"
```

**为什么要用**：直接 print 列表会带方括号和引号 `['python', 'git']`，用 join 输出更干净。

### f-string：格式化字符串（推荐）

```python
name = "mengjie"
age = 23

# ✅ f-string（最推荐，90% 场景用这个）
print(f"我叫{name}，今年{age}岁")

# 其他方式（了解即可）
print("我叫", name, "今年", age, "岁")        # 逗号分隔
print("我叫" + name + "今年" + str(age) + "岁")  # 拼接，麻烦
```

f-string 的 `f` = format，`{}` 里放变量名。Python 3.6+ 支持。

### 子字符串判断

```python
"learning" in "machine learning"   # True，判断"learning"是否是"machine learning"的子字符串
"nlp" in "python"                  # False
```

**注意**：`in` 有两种用法：
- `元素 in 列表` → 判断元素是否在列表中（完全匹配）
- `子字符串 in 字符串` → 判断是否包含（部分匹配）

---

## 五、条件判断与循环

### if/elif/else

```python
score: int = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "F"
```

**注意**：Python 用**缩进（4个空格）**表示代码块，不用花括号 `{}`。

### for 循环

```python
# 遍历列表（推荐，Pythonic）
for skill in skills:
    print(skill)

# 遍历数字序列
for i in range(3):    # 0, 1, 2（不包含3！）
    print(i)
```

### 标记变量（flag）模式

```python
is_ai = False   # 先假设"不是"

for keyword in ai_keywords:
    if keyword in skill:
        is_ai = True
        break   # 找到一个就够了，跳出循环

if is_ai:
    ai_skill.append(skill)
else:
    other_skill.append(skill)
```

**生活比喻**：找书时先假设"不是 AI 的"，翻到关键词就标记"是的"并停止翻找。

### any() 简化写法

```python
# 等价于上面的 flag + for + break
if any(keyword in skill for keyword in ai_keywords):
    ai_skill.append(skill)
```

`any()`：只要括号里有一个为 True，整体就为 True。

### break vs continue

- `break`：跳出整个循环
- `continue`：跳过本次，继续下一次循环

---

## 六、面试速查卡

| 问题 | 参考回答 |
|------|----------|
| Python 版本？为什么选？ | 3.12，稳定且兼容性好 |
| 怎么管理环境？ | conda，因为 AI 项目有 numpy/torch 等 C 依赖，conda 处理比 pip+venv 省心 |
| 知道 uv 吗？ | Rust 写的极快包管理器，Astral 出品，适合纯 Python 项目 |
| 类型标注强制吗？ | 不强制，运行时不检查，编辑器和 mypy 可静态检查 |
| list vs tuple？ | list 可改，tuple 不可改，tuple 更省内存适合存不变数据 |
| 格式化字符串几种方式？ | %格式化、str.format()、f-string（3.6+推荐） |
| range(3) 生成什么？ | 0,1,2，不包含 3 |

---

## 七、我的易错点总结（第1次会话）

1. **age 加引号** → 要有类型意识，数字不加引号
2. **append('skill') 加引号** → 存变量值不加引号
3. **`skill in ai_keywords` 完全匹配** → 要用 `keyword in skill` 做子字符串匹配
4. **python 找不到文件** → 注意当前工作目录，用完整路径
5. **编辑器 Run 无法运行** → 编辑器要单独选 Python 解释器

---

# 第2次会话：函数、类与面向对象、异常处理

> 日期：2025-07-21
> 环境：公司（opencode）

---

## 八、Python 函数

### 基本语法

```python
def greet(name: str) -> str:
    """跟某人打招呼"""           # 文档字符串，推荐写
    return f"你好，{name}！"
```

- `def` 定义函数
- `name: str` 参数 + 类型标注
- `-> str` 返回值类型标注
- `return` 返回结果；没有 return 则返回 `None`

### 参数的 5 种形式（面试高频）

```python
# 1. 位置参数（按顺序传）
def add(a: int, b: int) -> int:
    return a + b

# 2. 默认参数（有默认值，可不传）
def greet(name: str, greeting: str = "你好") -> str:
    return f"{greeting}，{name}！"

# 3. 关键字参数（按名字传，不按顺序）
greet(greeting="Hello", name="mengjie")

# 4. *args（任意个位置参数，打包成 tuple）
def sum_all(*numbers: int) -> int:
    return sum(numbers)

# 5. **kwargs（任意个关键字参数，打包成 dict）
def show_info(**info: str) -> None:
    for key, value in info.items():
        print(f"{key}: {value}")
```

**默认参数的坑**：必须放在非默认参数后面
```python
# ❌ 错误
def greet(name: str = "hmj", greeting: str) -> str:
# ✅ 正确
def greet(greeting: str, name: str = "hmj") -> str:
```

### Pythonic 写法（面试加分）

```python
# ❌ 不 Pythonic
if duplicate == False:
if len(skills) > 0:

# ✅ Pythonic
if not duplicate:
if skills:
```

**Pythonic** = 用 Python 社区推荐的优雅方式写代码，来自 PEP 8 规范。

---

## 九、Python 类与面向对象

### 为什么需要类？

把**数据和操作数据的函数**打包在一起，不用到处传参数。

```python
# 函数方式：每次传 skills 列表
my_skills = []
add_skill(my_skills, "python")

# 类方式：数据和操作绑定
manager = SkillManager()
manager.add("python")
```

### 基本语法

```python
class SkillManager:
    """技能管理器类"""
    
    def __init__(self):              # 初始化方法，创建对象时自动调用
        self.skills: list[str] = []  # 实例属性
    
    def add(self, skill: str) -> None:      # 实例方法
        if skill not in self.skills:
            self.skills.append(skill)
    
    def format(self, prefix: str = "技能") -> str:
        return f"{prefix}：{', '.join(self.skills)}"
```

### 关键概念

| 概念 | 说明 |
|------|------|
| `class` | 定义类的关键字 |
| `__init__` | 初始化方法，创建对象时自动调用 |
| `self` | 指向对象自己，访问属性和方法 |
| 实例属性 | 每个对象自己的数据，`self.skills` |
| 实例方法 | 对象可以调用的函数 |

**`self` 的理解**：
- `self` 就是对象自己，类似 "myself"
- `self.skills` = "这个对象自己的 skills 列表"
- 调用时不用传 self，Python 自动传：`manager.add("python")` 实际是 `SkillManager.add(manager, "python")`

### 继承（了解概念）

```python
class Animal:
    def __init__(self, name: str):
        self.name = name
    def speak(self) -> str:
        return "..."

class Dog(Animal):           # Dog 继承 Animal
    def speak(self) -> str:  # 重写父类方法
        return "汪汪！"

dog = Dog("旺财")
print(dog.name)      # 旺财（继承自 Animal）
print(dog.speak())   # 汪汪！（自己的实现）
```

---

## 十、异常处理

### 为什么需要？

让程序出错时不崩溃，优雅地处理错误。

```python
# 没有异常处理：程序崩溃
skills.remove("java")   # ❌ ValueError，程序停止

# 有异常处理：程序继续
try:
    skills.remove("java")
except ValueError:
    print("技能不存在")
print("继续执行")   # 会执行
```

### 基本语法

```python
try:
    # 可能出错的代码
    result = 10 / 0
except ZeroDivisionError as e:      # 捕获特定异常
    print(f"出错了：{e}")
except (ValueError, TypeError) as e: # 捕获多种异常
    print(f"其他错误：{e}")
except Exception as e:               # 捕获所有异常（兜底，不推荐滥用）
    print(f"未知错误：{e}")
else:
    # try 没出错时执行（可选）
    print(f"结果是 {result}")
finally:
    # 无论是否出错都执行（可选，常用于清理资源）
    print("清理工作")
```

### 常见异常类型（面试可能问）

| 异常 | 什么时候发生 |
|------|------------|
| `ValueError` | 值不对，如 `int("abc")` |
| `TypeError` | 类型不对，如 `"a" + 1` |
| `KeyError` | 字典 key 不存在 |
| `IndexError` | 列表索引越界 |
| `FileNotFoundError` | 文件不存在 |
| `ZeroDivisionError` | 除以 0 |

### `raise` 主动抛出异常

```python
def get_skill(self, index: int) -> str:
    if not self.skills:
        raise ValueError("技能列表为空")   # 主动报错
    return self.skills[index]
```

- `try/except`：**被动**捕获错误
- `raise`：**主动**制造错误（发现条件不对，主动报错）

### `isinstance()` 类型检查

```python
isinstance("hello", str)   # True
isinstance(123, str)       # False

def add_skill(skill: str):
    if not isinstance(skill, str):
        raise TypeError("skill 必须是字符串")
```

### 什么时候用异常处理？

**✅ 该用**：文件读写、网络请求、用户输入、调用外部 API（LLM API 可能报错）

**❌ 不该用**：
- 用异常控制流程（用 try 代替 if）
- 捕获所有异常然后 pass（隐藏 bug）

```python
# ❌ 不好
try:
    skills.remove("java")
except:
    pass

# ✅ 好
if "java" in skills:
    skills.remove("java")
```

### 判断条件 vs 异常处理

- **能预见的条件**用 `if`（如列表是否为空）
- **无法预料的错误**用 `try/except`（如索引越界）

```python
def get_skill(self, index: int) -> str:
    if not self.skills:                    # 能预见：列表是否为空
        raise ValueError("技能列表为空")
    try:
        return self.skills[index]          # 无法预料：索引是否越界
    except IndexError:
        return "索引越界"
```

---

## 十一、面试速查卡（第2次会话新增）

| 问题 | 参考回答 |
|------|----------|
| `*args` 和 `**kwargs` 区别？ | `*args` 收集位置参数成 tuple，`**kwargs` 收集关键字参数成 dict |
| 默认参数的坑？ | 必须放在非默认参数后面 |
| `== False` 和 `not` 区别？ | 功能一样，但 `not` 更 Pythonic（PEP 8 推荐） |
| Pythonic 是什么？ | 用 Python 社区推荐的优雅方式写代码，来自 PEP 8 |
| `self` 是什么？ | 指向对象自己，访问实例属性和方法，调用时自动传入 |
| `raise` 和 `try/except` 区别？ | raise 主动抛出，try/except 被动捕获 |
| `isinstance()` 干什么？ | 判断对象是否是某类型，用于运行时类型检查 |
| 什么时候用异常处理？ | 文件/网络/用户输入等不可控场景；不用来控制流程 |

---

# 第3次会话：装饰器、git、HTTP 基础、Linux/Shell

> 日期：2025-07-23
> 环境：公司（opencode）

---

## 十三、装饰器

### 什么是装饰器？

**装饰器**是在不修改原函数的情况下，给函数增加额外功能的函数。用 `@` 语法使用。

```python
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"开始调用 {func.__name__}")
        result = func(*args, **kwargs)
        print(f"结束调用 {func.__name__}")
        return result
    return wrapper

@log_call
def greet(name: str) -> str:
    return f"你好，{name}"

greet("mengjie")
# 输出：
# 开始调用 greet
# 结束调用 greet
```

### 装饰器本质

- `@装饰器名` 等价于 `函数 = 装饰器(函数)`
- 装饰器接收一个函数，返回一个新函数
- `*args, **kwargs`：接收任意参数，原样传给原函数
- `return func(*args, **kwargs)`：调用原函数并返回结果

### 实用例子：计时装饰器

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 执行耗时：{end - start:.2f}秒")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "完成"
```

### 面试高频

**Q：装饰器是什么？**
A：装饰器是一个接收函数返回函数的函数，用 @ 语法使用，作用是在不修改原函数的情况下增加功能，常用于日志、计时、权限校验等。

---

## 十四、git 基本操作

### 核心概念

```
工作区（你的电脑文件）
    ↓ git add
暂存区（准备提交的文件）
    ↓ git commit
本地仓库（提交历史）
    ↓ git push
远程仓库（GitHub）
```

### 常用命令

```bash
# 基本流程
git add -A              # 把所有改动加入暂存区
git commit -m "说明"     # 提交到本地仓库
git push                # 推送到 GitHub
git pull                # 从 GitHub 拉取最新

# 查看状态
git status              # 看哪些文件改了
git log --oneline -5    # 看最近5次提交

# 分支操作
git branch              # 查看分支
git branch feature      # 创建分支
git checkout feature    # 切换到分支
git checkout main       # 切回主分支
git merge feature       # 把 feature 合并到 main
```

### 分支的作用

- **隔离开发**：新功能在 feature 分支开发，不影响 main 的稳定性
- **多人协作**：每个人在自己的分支开发，互不干扰
- **修复 bug**：紧急 bug 从 main 拉分支修复，不影响其他开发

### 面试回答模板

**Q：你怎么用 git 协作？**
A：在 main 分支保持稳定，每个功能开一个 feature 分支开发，开发完合并回 main。用 git pull 同步远程，git push 推送本地改动。

**Q：git init 和 git clone 的区别？**
A：`git init` 是从零创建一个新仓库，`git clone` 是从远程复制一个已有仓库。

**Q：什么时候用分支？**
A：开发新功能、修 bug、多人协作时用分支。主分支保持稳定，每个功能开一个 feature 分支，开发完合并回主分支。

---

## 十五、HTTP 基础

### HTTP 请求结构

```
POST https://api.openai.com/v1/chat/completions
Authorization: Bearer sk-xxx
Content-Type: application/json

{
  "model": "gpt-4",
  "messages": [{"role": "user", "content": "你好"}]
}
```

| 部分 | 说明 | 例子 |
|------|------|------|
| **方法** | 要做什么操作 | `POST`（发送数据） |
| **URL** | 请求哪个地址 | `https://api.openai.com/v1/chat/completions` |
| **请求头** | 附加信息 | `Authorization: Bearer sk-xxx` |
| **请求体** | 发送的数据 | `{"model": "gpt-4", ...}` |

### 请求方法（面试高频）

| 方法 | 作用 | AI 场景 |
|------|------|---------|
| `GET` | 获取数据 | 获取模型列表 |
| `POST` | 发送数据 | **调用 LLM API（最常用）** |
| `PUT` | 更新数据 | 更新配置 |
| `DELETE` | 删除数据 | 删除会话 |

**记忆口诀**：GET 取、POST 发、PUT 改、DELETE 删

### 状态码（面试高频）

| 状态码 | 含义 | 说明 |
|--------|------|------|
| `200` | 成功 | 请求正常处理 |
| `400` | 客户端错误 | 参数不对、JSON 格式错 |
| `401` | 未授权 | API Key 错误或过期 |
| `404` | 找不到 | URL 不存在 |
| `429` | 请求太多 | **调用 LLM 超过频率限制** |
| `500` | 服务器错误 | LLM 服务挂了 |

**4xx vs 5xx**：4xx 是客户端的问题（你发错了），5xx 是服务器的问题（服务挂了）。

### 调用 LLM API 流程

```
你的代码                          LLM 服务器
   │                                 │
   │  POST /v1/chat/completions      │
   │  Header: Authorization: Bearer  │
   │  Body: {"model":"gpt-4", ...}   │
   │ ──────────────────────────────→ │
   │                                 │
   │  200 OK                         │
   │  {"choices":[{"message":...}]}  │
   │ ←────────────────────────────── │
   │                                 │
```

### 面试回答模板

**Q：你怎么调用 LLM API？**
A：用 HTTP POST 请求，在请求头带 API Key 做鉴权，请求体用 JSON 格式传 model 和 messages，服务器返回 JSON 格式的响应。

---

## 十六、Linux/Shell 常用命令

> 了解即可，面试可能问

### 常用命令速查

| 命令 | 作用 | Windows 对应 |
|------|------|-------------|
| `cd` | 切换目录 | `cd`（一样） |
| `ls` | 列出文件 | `dir` 或 `ls`（PowerShell 支持） |
| `cat` | 查看文件内容 | `cat`（PowerShell 支持） |
| `grep` | 搜索文件内容 | `Select-String` |
| `mkdir` | 创建目录 | `mkdir`（一样） |
| `rm` | 删除文件 | `Remove-Item` |
| `cp` | 复制 | `Copy-Item` |
| `mv` | 移动/重命名 | `Move-Item` |

### 管道符 `|`

把前一个命令的输出，作为后一个命令的输入：
```bash
ls | grep "py"        # 列出文件并筛选包含 "py" 的
cat log.txt | grep "error"  # 查看日志，筛选错误信息
```

### 面试回答

**Q：你熟悉 Linux 命令吗？**
A：常用 cd/ls/cat/grep/mkdir，会用管道符组合命令。部署时用过 ps 查进程。

---

## 十七、面试速查卡（第3次会话新增）

| 问题 | 参考回答 |
|------|----------|
| 装饰器是什么？ | 装饰器是接收函数返回函数的函数，用 @ 语法，作用是不修改原函数增加功能，常用于日志/计时/权限校验 |
| `*args, **kwargs` 作用？ | 接收任意参数，让装饰器能用在任何函数上 |
| git 工作流程？ | git add → git commit → git push；git pull 同步远程 |
| 什么时候用分支？ | 开发新功能/修 bug/多人协作时，主分支保持稳定 |
| HTTP 方法区别？ | GET 取数据，POST 发数据（LLM API 用这个），PUT 改数据，DELETE 删数据 |
| 常见状态码？ | 200 成功，401 未授权，404 找不到，429 请求太多，500 服务器错误 |
| 4xx vs 5xx 区别？ | 4xx 客户端错误（你发错了），5xx 服务器错误（服务挂了） |
| 怎么调用 LLM API？ | HTTP POST 请求，Header 带 API Key，Body 传 JSON 数据 |

---

## 十八、我的易错点总结（第3次会话）

1. **git 命令在错误目录** → 要在含 .git 文件夹的目录下执行
2. **命令行参数格式** → `git add -A`（有横杠），`git checkout main`（空格分隔）
3. **装饰器位置** → `print` 要在 wrapper 函数里（调用时执行），不是在装饰器函数里（定义时执行）
4. **装饰器返回值** → 要 `return wrapper`，不是 `return 字符串`
5. **HTTP 方法混淆** → 调用 LLM API 用 POST（发送数据），不是 GET（获取数据）

---

## Week 1 总结

### 学习内容回顾

| 模块 | 核心知识点 |
|------|-----------|
| **环境管理** | conda 环境、虚拟环境、包管理 |
| **Python 基础** | 数据类型、类型标注、字符串操作、控制流 |
| **Python 进阶** | 函数、类与面向对象、异常处理、装饰器 |
| **计算机基础** | git 版本控制、HTTP 协议、Linux 命令 |

### 面试准备要点

1. **Python 语法**：类型标注、函数参数、类定义、异常处理
2. **git 操作**：分支管理、协作流程
3. **HTTP 基础**：请求方法、状态码、LLM API 调用流程
4. **装饰器原理**：实现方式、应用场景

### 下周预告（Week 2）

- **Python 异步编程**：async/await（LLM API 调用常用）
- **FastAPI 基础**：AI 应用后端首选框架
- **TypeScript 速成**：为读 Pi 框架源码准备
- **Pi 框架学习**：开始读 `pi-ai` 模块源码
