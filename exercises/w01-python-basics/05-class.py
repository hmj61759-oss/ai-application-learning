"""
把刚才的函数版技能管理器改写成类：

要求：

定义 SkillManager 类
__init__ 里初始化 self.skills 为空列表
add 方法：添加技能，支持 duplicate 参数
format 方法：格式化输出，支持 prefix 参数
count 方法：返回技能数量
额外加一个方法 remove(skill: str) -> bool：删除技能，删除成功返回 True，技能不存在返回 False
测试代码：

manager = SkillManager()
manager.add("python")
manager.add("git")
manager.add("python")           # 不会重复
manager.add("ai")
print(manager.format())         # 技能：python, git, ai
print(manager.count())          # 3

print(manager.remove("git"))    # True
print(manager.remove("java"))   # False（不存在）
print(manager.format())         # 技能：python, ai
提示：

remove 方法里用 list.remove() 删除元素，但要先判断是否存在（否则会报错）
或者用 try/except（下个知识点要学）
"""
class SkillManager:
    """技能管理器类"""
    def __init__(self):
        self.skills: list[str] = []

    def add_skill(self, skill:str, duplicate:bool=False) -> list[str]:
        """添加技能"""
        if not duplicate and skill in self.skills:
            return
        self.skills.append(skill)
        return self.skills
    
    def format(self, prefix: str='技能') -> str:
        """格式化输出"""
        return f"{prefix}：{','.join(self.skills)}"
    
    def count(self) -> int:
        """返回技能数量"""
        return len(self.skills)
    
    def remove(self, skill:str) -> bool:
        if skill in self.skills:
            self.skills.remove(skill)
            return True
        return False
    
manager = SkillManager()
manager.add_skill("python")
manager.add_skill("git")
manager.add_skill("python")
manager.add_skill("ai")
print(manager.format())
print(manager.count())
print(manager.remove("git"))
print(manager.remove("java"))
print(manager.format())



