# 输出模板

评估结果与学习路径的空白 Markdown 模板。SKILL.md 引用本文件以保持主体精简；完整的示例和验证规则仍保留在 SKILL.md 中。

## Quick Assessment 结果（步骤 3A）

```markdown
## Claude Code Skill Assessment Results

### Your Level: [Level 1: Beginner / Level 2: Intermediate / Level 3: Advanced]

You checked **N/8** items.

[根据水平给出的一句话激励总结]

### Your Skill Profile

| Area | Status |
|------|--------|
| Basic CLI & Conversations | [Checked/Gap] |
| CLAUDE.md & Memory | [Checked/Gap] |
| Slash Commands (built-in) | [Checked/Gap] |
| Custom Commands & Skills | [Checked/Gap] |
| MCP Servers | [Checked/Gap] |
| Hooks | [Checked/Gap] |
| Subagents | [Checked/Gap] |
| Print Mode & CI/CD | [Checked/Gap] |

### Identified Gaps

[针对每个未勾选的项目，给出一行描述说明要学什么，并附上教程链接]

### Your Personalized Learning Path

[输出该水平对应的学习路径——见步骤 4]
```

## Deep Assessment 结果（步骤 3B）

```markdown
## Claude Code Skill Assessment Results

### Overall Level: [Level 1 / Level 2 / Level 3]

**Total Score: N/20 points**

[一句话激励总结]

### Your Skill Profile

| Feature Area | Score | Mastery | Status |
|-------------|-------|---------|--------|
| Slash Commands | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| Memory | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| Skills | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| Hooks | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| MCP | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| Subagents | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| Checkpoints | N/1 | [None/Proficient] | [Learn/Mastered] |
| Advanced Features | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| Plugins | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| CLI | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |

**Mastery key:** 0 = None（无）, 1 = Basic（基础）, 2 = Proficient（熟练）

### Strength Areas
[列出得分 2/2 的主题——这些已经掌握]

### Priority Gaps (Learn Next)
[列出得分 0 的主题——这些需要优先关注，按依赖顺序排列]

### Review Areas
[列出得分 1/2 的主题——基础已掌握，但进阶功能尚未使用]

### Your Personalized Learning Path

[输出针对差距的学习路径——见步骤 4]
```

## Learning Path（学习路径，步骤 4）

```markdown
### Your Personalized Learning Path

**Estimated time**: ~N hours (adjusted for your current skills)

#### Phase 1: [阶段名称] (~N hours)
[仅当他们在这些领域有差距时才展示]

**[主题名称]** — [从零学习 / 深入进阶功能]
- Tutorial: [教程目录链接]
- Focus on: [他们需要的具体章节/概念]
- Key exercise: [一个具体的练习]
- You'll know it's done when: [具体的达标标准]

**[主题名称]** — ...

---

#### Phase 2: [阶段名称] (~N hours)
...

---

### Recommended Practice Projects

Based on your gaps, try these real-world exercises to solidify your learning:

1. **[项目名称]**：[结合 2-3 个差距主题的一行描述]
2. **[项目名称]**：[一行描述]
3. **[项目名称]**：[一行描述]
```
