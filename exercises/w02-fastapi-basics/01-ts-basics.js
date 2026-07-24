///要求：用 TypeScript 思维写一个技能管理器：
// 定义一个接口 Skill，包含：name: string, level: number, category: string
// 定义一个类型别名 SkillCategory = "technical" | "soft" | "domain"
// 写一个泛型函数 addItem<T>，能添加任意类型的项目到列表
// 创建一个技能列表，用接口约束

// 对应 TypeScript: interface Skill { name: string; level: number; category: string }
const skill1 = {
    name: "python",
    level: 5,
    category: "technical"
};

const skill2 = {
    name: "communication",
    level: 7,
    category: "soft"
};

// 对应 TypeScript: function addItem<T>(item: T, list: T[]): T[]
function addItem(item, list) {
    return [...list, item];
}

// 对应 TypeScript: const mySkills: Skill[] = []
let mySkills = [];

// 添加技能
mySkills = addItem(skill1, mySkills);
mySkills = addItem(skill2, mySkills);

// 打印结果
console.log(mySkills);
console.log(`技能数量: ${mySkills.length}`);

