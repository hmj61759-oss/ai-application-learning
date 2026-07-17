my_name: str = 'mengjie'
my_skills: list[str] = ["python", "git", "ai"]
profile: dict[str, object] = {"name":'mengjie',"age":23,'skills':my_skills}
print(my_skills[1])
my_skills.append('english')
print(my_skills)
skills_str = ", ".join(my_skills)
print(f"我叫{my_name}，今年{profile['age']}岁,掌握的技能有：{skills_str}")
