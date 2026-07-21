'''
场景：给 SkillManager 加一个 get_skill(index: int) -> str 方法，按索引获取技能。

要求：
在 SkillManager 类里加 get_skill 方法
如果索引越界，捕获 IndexError，返回字符串 "索引越界"（而不是让程序崩溃）
如果 skills 列表为空，主动抛出 ValueError（用 raise），提示"技能列表为空"
测试代码：

manager = SkillManager()
manager.add_skill("python")
manager.add_skill("git")

print(manager.get_skill(0))    # python
print(manager.get_skill(1))    # git
print(manager.get_skill(5))    # 索引越界

empty_manager = SkillManager()
try:
    empty_manager.get_skill(0)
except ValueError as e:
    print(f"错误：{e}")        # 错误：技能列表为空
提示：

get_skill 里先用 if not self.skills: 判断列表是否为空，空就 raise ValueError("技能列表为空")
然后用 try/except IndexError 包住 return self.skills[index]
'''

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
    
    def get_skill(self, index: int) -> str:
        # 先判断列表是否为空 因为空列表访问任何索引都会抛 IndexError
        if not self.skills:
            raise ValueError("技能列表为空")

        # 再访问索引
        try:
            return self.skills[index]
        except IndexError:
            return "索引越界"

      
    
manager = SkillManager()
manager.add_skill("python")
manager.add_skill("git")
print(manager.get_skill(0))
print(manager.get_skill(1))
print(manager.get_skill(5))

empty_manager = SkillManager()
try:
    empty_manager.get_skill(0)
except ValueError as e:
    print(f"错误：{e}")



