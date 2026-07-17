'''
场景：你有一个技能清单，要筛选出哪些是 AI 相关技能。
# 给定数据
all_skills: list[str] = ["python", "git", "machine learning", "english", "deep learning", "sql", "nlp"]
ai_keywords: list[str] = ["learning", "nlp", "ai", "ml"]

要求：
遍历 all_skills，判断每个技能是否和 AI 相关（包含 ai_keywords 里的任意关键词）
把 AI 相关的技能存到一个新列表 ai_skills 里
把非 AI 技能存到 other_skills 里

最后打印两个列表，格式：
AI相关技能：machine learning, deep learning, nlp
其他技能：python, git, english, sql
'''
all_skills: list[str] = ["python", "git", "machine learning", "english", "deep learning", "sql", "nlp"]
ai_keywords: list[str] = ["learning", "nlp", "ai", "ml"]

ai_skill: list[str] = []
other_skill: list[str] = []

for skill in all_skills:
    # 遍历每个关键词，看是否有任何一个关键词包含在 skill 里
    is_ai = False
    for keyword in ai_keywords:
        if keyword in skill:
            is_ai = True
            break

    if is_ai:
        ai_skill.append(skill)
    else:
        other_skill.append(skill)
    

ai_skill_str = ",".join(ai_skill)
other_skill_str = ",".join(other_skill)
print(f"AI相关技能：{ai_skill_str}\n其他技能：{other_skill_str}")