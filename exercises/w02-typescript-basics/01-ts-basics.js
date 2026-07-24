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
