---
name: self-assessment
version: 2.3.0
description: 全面的 Claude Code 自我评估与学习路径建议工具。运行一套覆盖 10 个功能领域的多分类测验，生成含各主题分数的详细技能画像，识别具体差距，并给出带优先级排序的个性化学习路径。适用于用户说 "assess my level"、"take the quiz"、"find my level"、"where should I start"、"what should I learn next"、"check my skills"、"skill check" 或 "level up" 时使用。
---

# Self-Assessment & Learning Path Advisor（自我评估与学习路径建议）

覆盖 10 个功能领域的全面互动评估，用于判定 Claude Code 熟练度，识别具体的技能差距，并生成个性化的学习路径帮助你进阶。

## 操作步骤

### 步骤 1：欢迎并选择评估模式

向用户呈现评估深度的选择：

使用 AskUserQuestion，选项为：
- **Quick Assessment** —— "8 道题，约 2 分钟。判定你的整体水平（入门/中级/高级）并给出学习路径。"
- **Deep Assessment** —— "5 个分类的详细问题，约 5 分钟。给出各主题的技能分数，识别具体差距，并构建有优先级的学习路径。"

如果用户选择 **Quick Assessment**，进入步骤 2A。
如果用户选择 **Deep Assessment**，进入步骤 2B。

---

### 步骤 2A：Quick Assessment（快速评估）

呈现两个多选问题（AskUserQuestion 每个最多支持 4 个选项）：

**问题 1**（header："Basics"）：
"第 1/2 部分：以下哪些 Claude Code 技能你已经具备？"
选项：
1. "Start Claude Code and chat" —— 我能运行 `claude` 并与它交互
2. "Created/edited CLAUDE.md" —— 我已经设置过项目或用户级记忆
3. "Used 3+ slash commands" —— 例如 /help、/compact、/model、/clear
4. "Created custom command/skill" —— 编写过 SKILL.md 或自定义命令文件

**问题 2**（header："Advanced"）：
"第 2/2 部分：以下哪些进阶技能你已经具备？"
选项：
1. "Configured an MCP server" —— 例如 GitHub、数据库或其他外部数据源
2. "Set up hooks" —— 在 ~/.claude/settings.json 中配置过 hook
3. "Created/used subagents" —— 使用过 .claude/agents/ 做任务委派
4. "Used print mode (claude -p)" —— 使用过 `claude -p` 进行非交互或 CI/CD 场景

**评分方式：**
- 总分 0-2 = Level 1：入门（Beginner）
- 总分 3-5 = Level 2：中级（Intermediate）
- 总分 6-8 = Level 3：高级（Advanced）

带着水平结果进入步骤 3，并列出哪些具体项未被勾选，作为差距。

---

### 步骤 2B：Deep Assessment（深入评估）

呈现 5 轮问题，每轮调用一次 AskUserQuestion。每轮覆盖 2 个相关的功能领域。所有轮次都使用多选。

**重要**：AskUserQuestion 每题最多支持 4 个选项。每轮恰好 1 道题、4 个选项，覆盖 2 个主题（每个主题 2 个选项）。

---

**Round 1 — Slash Commands & Memory**（header："Commands"）

"以下哪些你做过？全选适用项。"
选项：
1. "Created a custom slash command or skill" —— 编写过带 frontmatter 的 SKILL.md 文件，或创建过 .claude/commands/ 文件
2. "Used dynamic context in commands" —— 在 skill/command 文件中使用过 `$ARGUMENTS`、`$0`/`$1`、反引号 `!command` 语法，或 `@file` 引用
3. "Set up project + personal memory" —— 同时创建过项目 CLAUDE.md 和个人 ~/.claude/CLAUDE.md（或 CLAUDE.local.md）
4. "Used memory hierarchy features" —— 理解 7 层优先级顺序，使用过 .claude/rules/ 目录、路径专属规则，或 @import 语法

**Round 1 评分：**
- 选项 1-2 对应 **Slash Commands**（0-2 分）
- 选项 3-4 对应 **Memory**（0-2 分）

---

**Round 2 — Skills & Hooks**（header："Automation"）

"以下哪些你做过？全选适用项。"
选项：
1. "Installed and used an auto-invoked skill" —— 用过一个根据 description 自动触发、无需手动 /command 调用的 skill
2. "Controlled skill invocation behavior" —— 在 SKILL.md frontmatter 中使用过 `disable-model-invocation`、`user-invocable`，或配合 agent 字段的 `context: fork`
3. "Set up a PreToolUse or PostToolUse hook" —— 配置过在工具执行前/后运行的 hook（例如命令校验器、自动格式化工具）
4. "Used advanced hook features" —— 配置过 prompt 类型的 hook、SKILL.md 中的组件级 hook、HTTP hook，或带自定义 JSON 输出（updatedInput、systemMessage）的 hook

**Round 2 评分：**
- 选项 1-2 对应 **Skills**（0-2 分）
- 选项 3-4 对应 **Hooks**（0-2 分）

---

**Round 3 — MCP & Subagents**（header："Integration"）

"以下哪些你做过？全选适用项。"
选项：
1. "Connected an MCP server and used its tools" —— 例如用于 PR/issue 的 GitHub MCP、用于查询的数据库 MCP，或任何外部数据源
2. "Used advanced MCP features" —— 项目级 .mcp.json、OAuth 身份验证、带 @提及的 MCP resource、Tool Search，或 `claude mcp serve`
3. "Created or configured custom subagents" —— 在 .claude/agents/ 中定义过带自定义工具、模型或权限的 agent
4. "Used advanced subagent features" —— worktree 隔离、持久化 agent 记忆、通过 Ctrl+B 的后台任务、通过 `Task(agent_name)` 的 agent 白名单，或 agent 团队

**Round 3 评分：**
- 选项 1-2 对应 **MCP**（0-2 分）
- 选项 3-4 对应 **Subagents**（0-2 分）

---

**Round 4 — Checkpoints & Advanced Features**（header："Power User"）

"以下哪些你做过？全选适用项。"
选项：
1. "Used checkpoints for safe experimentation" —— 创建过 checkpoint，使用过 Esc+Esc 或 /rewind，恢复过代码和/或对话，或使用过 Summarize 选项
2. "Used planning mode or extended thinking" —— 通过 /plan、Shift+Tab 或 --permission-mode plan 激活过规划模式；用 Alt+T/Option+T 切换过扩展思考
3. "Configured permission modes" —— 通过 CLI 参数、快捷键或设置使用过 acceptEdits、plan、dontAsk 或 bypassPermissions 模式
4. "Used remote/desktop/web features" —— 使用过 `claude remote-control`、`claude --remote`、`/teleport`、`/desktop`，或 `claude -w` 的 worktree

**Round 4 评分：**
- 选项 1 对应 **Checkpoints**（0-1 分）
- 选项 2-4 对应 **Advanced Features**（0-3 分，上限为 2）

---

**Round 5 — Plugins & CLI**（header："Mastery"）

"以下哪些你做过？全选适用项。"
选项：
1. "Installed or created a plugin" —— 从 marketplace 使用过打包插件，或创建过带 plugin.json 清单的 .claude-plugin/ 目录
2. "Used plugin advanced features" —— 插件 hook、插件 MCP server、LSP 配置、插件命名空间命令，或用 --plugin-dir 参数测试
3. "Used print mode in scripts or CI/CD" —— 用 `claude -p` 配合 --output-format json、--max-turns、管道输入，或集成进 GitHub Actions / CI 流水线
4. "Used advanced CLI features" —— 会话恢复（-c/-r）、--agents 参数、用于结构化输出的 --json-schema、--fallback-model、--from-pr，或批处理循环

**Round 5 评分：**
- 选项 1-2 对应 **Plugins**（0-2 分）
- 选项 3-4 对应 **CLI**（0-2 分）

---

### 步骤 3：计算并呈现结果

#### 3A：Quick Assessment（快速评估）结果

统计总勾选数并判定水平，然后呈现：

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

#### 3B：Deep Assessment（深入评估）结果

根据 5 轮的结果计算各主题分数。每个主题得分 0-2 分。然后呈现：

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

**Deep Assessment 的整体水平计算方式：**
- 总分 0-6 = Level 1：入门（Beginner）
- 总分 7-13 = Level 2：中级（Intermediate）
- 总分 14-20 = Level 3：高级（Advanced）

---

### 步骤 4：生成个性化学习路径

根据评估结果，生成针对用户具体差距的学习路径。不要只是重复通用的水平路径——要做适配。

#### 路径生成规则

1. **跳过已掌握的主题**：如果某主题得分 2/2，不要将其纳入路径。
2. **按依赖顺序排优先级**：Slash Commands 先于 Skills，Memory 先于 Subagents，依此类推。依赖顺序为：
   - Slash Commands（无依赖）→ Skills（依赖 Slash Commands）
   - Memory（无依赖）→ Subagents（依赖 Memory）
   - CLI Basics（无依赖）→ CLI Mastery（依赖以上全部）
   - Checkpoints（无依赖）
   - Hooks（依赖 Slash Commands）
   - MCP（无依赖）→ Plugins（依赖 MCP、Skills、Hooks）
   - Advanced Features（依赖之前全部内容）
3. **对于得分 1/2 的主题**：推荐"深入学习（deep dive）"——链接到他们缺失的具体进阶章节。
4. **估算时间**：只汇总他们需要学习/复习的主题。
5. **分组为若干阶段**：把剩余主题组织成若干个逻辑阶段，每阶段 2-3 个主题。

#### 路径输出格式

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

#### 针对具体主题的建议

当某个主题存在差距时，使用以下具体建议：

**Slash Commands（得分 0）**：
- Tutorial: [01-slash-commands/](../../../01-slash-commands/)
- Focus on: 内置命令参考、创建你的第一个 SKILL.md、`$ARGUMENTS` 语法
- Key exercise: 创建一个 `/optimize` 命令并测试它
- Done when: 你能创建一个带参数和动态上下文的自定义 skill

**Slash Commands（得分 1 — 需复习）**：
- Focus on: 用反引号 `!command` 语法注入动态上下文、`@file` 引用、`disable-model-invocation` 与 `user-invocable` 的区别与控制方式
- Done when: 你能创建一个既能注入实时命令输出、又能控制自身调用行为的 skill

**Memory（得分 0）**：
- Tutorial: [02-memory/](../../../02-memory/)
- Focus on: 创建 CLAUDE.md、`/init` 和 `/memory` 命令、用于快速更新的 `#` 前缀
- Key exercise: 创建一个包含你的编码规范的项目 CLAUDE.md
- Done when: Claude 能在多个会话中记住你的偏好

**Memory（得分 1 — 需复习）**：
- Focus on: 7 层层级与优先级顺序、带路径专属规则的 .claude/rules/ 目录、`@import` 语法（最大深度 5）、Auto Memory 的 MEMORY.md（200 行限制）
- Done when: 你为不同目录设置了模块化规则，并理解完整的层级结构

**Skills（得分 0）**：
- Tutorial: [03-skills/](../../../03-skills/)
- Focus on: SKILL.md 格式、通过 description 字段实现自动调用、渐进式披露（3 个加载层级）
- Key exercise: 安装 code-review skill 并验证它能自动触发
- Done when: 某个 skill 能根据对话上下文自动激活

**Skills（得分 1 — 需复习）**：
- Focus on: 配合 agent 字段用于 subagent 执行的 `context: fork`、`disable-model-invocation` 与 `user-invocable` 的区别、2% 的上下文预算、捆绑资源（scripts/、references/、assets/）
- Done when: 你能创建一个在 fork 出的上下文中、于 subagent 中运行的 skill

**Hooks（得分 0）**：
- Tutorial: [06-hooks/](../../../06-hooks/)
- Focus on: 配置结构（matcher + hooks 数组）、PreToolUse/PostToolUse 事件、退出码（0=成功，2=阻塞）、JSON 输入/输出格式
- Key exercise: 创建一个校验 Bash 命令的 PreToolUse hook
- Done when: 某个 hook 能在危险命令执行前将其阻止

**Hooks（得分 1 — 需复习）**：
- Focus on: 全部 25 种 hook 事件（包括 PostToolUseFailure、StopFailure、TaskCreated、CwdChanged、FileChanged、PostCompact、Elicitation、ElicitationResult）、4 种 hook 类型（command、http、prompt、agent）、SKILL.md frontmatter 中的组件级 hook、带 allowedEnvVars 的 HTTP hook、用于 SessionStart/CwdChanged/FileChanged 的 `CLAUDE_ENV_FILE`
- Done when: 你能创建一个基于 prompt 的 Stop hook，以及一个 skill 内的组件级 hook

**MCP（得分 0）**：
- Tutorial: [05-mcp/](../../../05-mcp/)
- Focus on: `claude mcp add` 命令、传输类型（推荐 HTTP）、GitHub MCP 设置、环境变量展开
- Key exercise: 添加 GitHub MCP server 并查询 PR
- Done when: 你能通过 MCP 从外部服务查询实时数据

**MCP（得分 1 — 需复习）**：
- Focus on: 项目级 .mcp.json（需要团队批准）、OAuth 2.0 认证、通过 `@server:resource` 提及的 MCP resource、Tool Search（ENABLE_TOOL_SEARCH）、`claude mcp serve`、输出限制（10k/25k/50k）
- Done when: 你有一个项目级 .mcp.json，并理解 Tool Search 的 auto 模式

**Subagents（得分 0）**：
- Tutorial: [04-subagents/](../../../04-subagents/)
- Focus on: agent 文件格式（.claude/agents/*.md）、内置 agent（general-purpose、Plan、Explore）、tools/model/permissionMode 配置
- Key exercise: 创建一个 code-reviewer subagent 并测试任务委派
- Done when: Claude 能把代码审查委派给你的自定义 agent

**Subagents（得分 1 — 需复习）**：
- Focus on: worktree 隔离（`isolation: worktree`）、持久化 agent 记忆（带 scope 的 `memory` 字段）、后台 agent（Ctrl+B/Ctrl+F）、用 `Task(agent_name)` 实现的 agent 白名单、agent 团队（`--teammate-mode`）
- Done when: 你有一个带持久化记忆、运行在 worktree 隔离中的 subagent

**Checkpoints（得分 0）**：
- Tutorial: [08-checkpoints/](../../../08-checkpoints/)
- Focus on: Esc+Esc 和 /rewind 的使用、5 种 rewind 选项（恢复代码+对话、只恢复对话、只恢复代码、摘要、取消）、局限性（Bash 文件系统操作不被追踪）
- Key exercise: 做一些实验性改动，然后回退恢复
- Done when: 你能放心地做实验，因为知道自己可以随时回退

**Advanced Features（得分 0）**：
- Tutorial: [09-advanced-features/](../../../09-advanced-features/)
- Focus on: 规划模式（/plan 或 Shift+Tab）、权限模式（5 种）、扩展思考（Alt+T 切换）
- Key exercise: 用规划模式设计一个功能，然后实现它
- Done when: 你能在规划模式和实现模式之间流畅切换

**Advanced Features（得分 1 — 需复习）**：
- Focus on: 远程控制（`claude remote-control`）、网页会话（`claude --remote`）、桌面交接（`/desktop`）、worktree（`claude -w`）、任务列表（Ctrl+T）、企业级托管设置
- Done when: 你能在 CLI、网页和桌面应用之间交接会话

**Plugins（得分 0）**：
- Tutorial: [07-plugins/](../../../07-plugins/)
- Focus on: 插件结构（.claude-plugin/plugin.json）、插件能捆绑什么（命令、agent、MCP、hook、设置）、从 marketplace 安装
- Key exercise: 安装一个插件并探索它的组件
- Done when: 你理解什么时候该用插件、什么时候该用独立组件

**Plugins（得分 1 — 需复习）**：
- Focus on: 创建 plugin.json 清单、插件 hook（hooks/hooks.json）、LSP 配置（.lsp.json）、`${CLAUDE_PLUGIN_ROOT}` 变量、用于测试的 --plugin-dir、marketplace 发布
- Done when: 你能为你的团队创建并测试一个插件

**CLI（得分 0）**：
- Tutorial: [10-cli/](../../../10-cli/)
- Focus on: 交互模式 vs print 模式、带管道的 `claude -p`、`--output-format json`、会话管理（-c/-r）
- Key exercise: 把一个文件通过管道传给 `claude -p` 并获得 JSON 输出
- Done when: 你能在脚本中非交互式地使用 Claude

**CLI（得分 1 — 需复习）**：
- Focus on: 带 JSON 配置的 --agents 参数、用于结构化输出的 --json-schema、--fallback-model、--from-pr、--strict-mcp-config、用 for 循环做批处理、`claude mcp serve`
- Done when: 你有一个使用 Claude 并输出结构化 JSON 的 CI/CD 脚本

---

### 步骤 5：提供后续操作

呈现结果后，询问用户接下来想做什么：

使用 AskUserQuestion，选项为：
- **Start learning** —— "帮我现在就开始学习路径中的第一个主题"
- **Deep dive on a gap** —— "详细讲解我的某个差距领域，让我在这里学会它"
- **Practice project** —— "搭建一个覆盖我差距领域的练习项目"
- **Retake assessment** —— "我想重新测验（也许换一种模式）"

如果选择 **Start learning**：阅读第一个差距教程的 README.md，带用户完成第一个练习。
如果选择 **Deep dive on a gap**：询问是哪个差距主题，然后阅读对应教程的 README.md 并结合示例讲解关键概念。
如果选择 **Practice project**：设计一个结合他们 2-3 个差距主题、带具体步骤的小项目。
如果选择 **Retake assessment**：回到步骤 1。

## 错误处理

### 某一轮用户没有选择任何项
该轮对应主题按 0 分处理。继续进入下一轮。

### 所有轮次用户都没有选择任何项
判定为 Level 1：入门（Beginner）。鼓励从头开始学习。输出完整的 Level 1 路径。

### 用户想要重新测验
从步骤 1 重新开始一次全新的评估。

### 用户不认同自己的判定水平
认可用户的看法。询问他们认为自己属于哪个水平。呈现该水平对应的路径，并针对他们可能遗漏的主题做一次前置知识核查。

### 用户询问某个具体主题
如果用户在测验过程中说了类似 "tell me about hooks" 或 "I want to learn MCP" 的话，记下来。呈现结果后，无论该主题得分如何，都在学习路径中重点标出它。

## 验证

### 触发测试集

**应当触发：**
- "assess my level"
- "take the quiz"
- "find my level"
- "where should I start"
- "what level am I"
- "learning path quiz"
- "self-assessment"
- "what should I learn next"
- "check my skills"
- "skill check"
- "level up"
- "how good am I at Claude Code"
- "evaluate my Claude Code knowledge"

**不应触发：**
- "review my code"
- "create a skill"
- "help me with MCP"
- "explain slash commands"
- "what is a checkpoint"
