# Week 1 · Python 基础笔记（第1次会话）

> 日期：2025-07-17
> 环境：公司（opencode）
> 学习内容：conda 环境、数据类型、类型标注、条件判断与循环

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

## 七、我的易错点总结

1. **age 加引号** → 要有类型意识，数字不加引号
2. **append('skill') 加引号** → 存变量值不加引号
3. **`skill in ai_keywords` 完全匹配** → 要用 `keyword in skill` 做子字符串匹配
4. **python 找不到文件** → 注意当前工作目录，用完整路径
5. **编辑器 Run 无法运行** → 编辑器要单独选 Python 解释器
