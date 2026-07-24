//要求：用 TypeScript 思维写一个技能管理器：
// 义一个接口 Skill，包含：name: string, level: number, category: string
// 定义一个类型别名 SkillCategory = "technical" | "soft" | "domain"
// 写一个泛型函数 addItem<T>，能添加任意类型的项目到列表
// 创建一个技能列表，用接口约束

// 定义接口（类似 Python 的 Pydantic BaseModel）
interface Skill {
    name: string;
    level: number;
    category: SkillCategory;
}

// 类型别名（限定取值范围）
type SkillCategory = "technical" | "soft" | "domain";

// 泛型函数（T 表示任意类型）
function addItem<T>(item: T, list: T[]): T[] {
    return [...list, item];
}

// 使用
const mySkills: Skill[] = [];

const pythonSkill: Skill = {
    name: "python",
    level: 5,
    category: "technical"
};

const updatedSkills = addItem(pythonSkill, mySkills);
console.log(updatedSkills);