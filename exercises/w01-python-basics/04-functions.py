"""
写一个技能管理器：
要求：
写一个函数 add_skill(skills: list[str], skill: str, duplicate: bool = False) -> list[str]
把 skill 添加到 skills 列表
如果 duplicate=False（默认），且 skill 已存在，就不添加（用 in 判断）
如果 duplicate=True，允许重复添加
返回添加后的列表
写一个函数 format_skills(skills: list[str], prefix: str = "技能") -> str
把列表格式化成字符串，如 "技能：python, git, ai"
prefix 默认是 "技能"，可以改成别的
测试你的函数：
my_skills = []
add_skill(my_skills, "python")
add_skill(my_skills, "python")      # duplicate=False，不会重复添加
add_skill(my_skills, "git")
add_skill(my_skills, "python", duplicate=True)  # 允许重复
print(format_skills(my_skills))
print(format_skills(my_skills, prefix="我会的"))
预期输出：

技能：python, git, python
我会的：python, git, python
提示：

add_skill 里用 if skill in skills 判断是否已存在
format_skills 里用 ", ".join() 把列表转字符串（上次学过的）
"""

def add_skill(skills:list[str], skill:str, duplicate:bool = False) -> list[str]:
    if  not duplicate and skill in skills:
        return skills
    else:
        skills.append(skill)
        return skills
    
def format_skills(skills:list[str], prefix:str="技能") -> str:
    return f"{prefix}：{", ".join(skills)}"

my_skills = []
add_skill(my_skills, "python")
add_skill(my_skills, "python")      # duplicate=False，不会重复添加
add_skill(my_skills, "git")
add_skill(my_skills, "python", duplicate=True)  # 允许重复
print(format_skills(my_skills))
print(format_skills(my_skills, prefix="我会的"))
