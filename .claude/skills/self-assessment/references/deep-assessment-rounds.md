# Deep Assessment — 各轮问题

Deep Assessment 的 5 轮问题。每轮调用一次 AskUserQuestion（多选，最多 4 个选项）。每轮覆盖 2 个功能领域，各 2 个选项。为了不重新读取本文件也能计算结果，各轮评分映射在 SKILL.md 的步骤 2B 中重复了一份。

---

**Round 1 — Slash Commands & Memory**（header："Commands"）

"以下哪些你做过？全选适用项。"
选项：
1. "Created a custom slash command or skill" —— 编写过带 frontmatter 的 SKILL.md 文件，或创建过 .claude/commands/ 文件
2. "Used dynamic context in commands" —— 在 skill/command 文件中使用过 `$ARGUMENTS`、`$0`/`$1`、反引号 `!command` 语法，或 `@file` 引用
3. "Set up project + personal memory" —— 同时创建过项目 CLAUDE.md 和个人 ~/.claude/CLAUDE.md（或 CLAUDE.local.md）
4. "Used memory hierarchy features" —— 理解 7 层优先级顺序，使用过 .claude/rules/ 目录、路径专属规则，或 @import 语法

**评分：** 选项 1-2 → **Slash Commands**（0-2）；选项 3-4 → **Memory**（0-2）

---

**Round 2 — Skills & Hooks**（header："Automation"）

"以下哪些你做过？全选适用项。"
选项：
1. "Installed and used an auto-invoked skill" —— 用过一个根据 description 自动触发、无需手动 /command 调用的 skill
2. "Controlled skill invocation behavior" —— 在 SKILL.md frontmatter 中使用过 `disable-model-invocation`、`user-invocable`，或配合 agent 字段的 `context: fork`
3. "Set up a PreToolUse or PostToolUse hook" —— 配置过在工具执行前/后运行的 hook（例如命令校验器、自动格式化工具）
4. "Used advanced hook features" —— 配置过 prompt 类型的 hook、SKILL.md 中的组件级 hook、HTTP hook，或带自定义 JSON 输出（updatedInput、systemMessage）的 hook

**评分：** 选项 1-2 → **Skills**（0-2）；选项 3-4 → **Hooks**（0-2）

---

**Round 3 — MCP & Subagents**（header："Integration"）

"以下哪些你做过？全选适用项。"
选项：
1. "Connected an MCP server and used its tools" —— 例如用于 PR/issue 的 GitHub MCP、用于查询的数据库 MCP，或任何外部数据源
2. "Used advanced MCP features" —— 项目级 .mcp.json、OAuth 身份验证、带 @提及的 MCP resource、Tool Search，或 `claude mcp serve`
3. "Created or configured custom subagents" —— 在 .claude/agents/ 中定义过带自定义工具、模型或权限的 agent
4. "Used advanced subagent features" —— worktree 隔离、持久化 agent 记忆、通过 Ctrl+B 的后台任务、通过 `Task(agent_name)` 的 agent 白名单，或 agent 团队

**评分：** 选项 1-2 → **MCP**（0-2）；选项 3-4 → **Subagents**（0-2）

---

**Round 4 — Checkpoints & Advanced Features**（header："Power User"）

"以下哪些你做过？全选适用项。"
选项：
1. "Used checkpoints for safe experimentation" —— 创建过 checkpoint，使用过 Esc+Esc 或 /rewind，恢复过代码和/或对话，或使用过 Summarize 选项
2. "Used planning mode or extended thinking" —— 通过 /plan、Shift+Tab 或 --permission-mode plan 激活过规划模式；用 Alt+T/Option+T 切换过扩展思考
3. "Configured permission modes" —— 通过 CLI 参数、快捷键或设置使用过 acceptEdits、plan、dontAsk 或 bypassPermissions 模式
4. "Used remote/desktop/web features" —— 使用过 `claude remote-control`、`claude --remote`、`/teleport`、`/desktop`，或 `claude -w` 的 worktree

**评分：** 选项 1 → **Checkpoints**（0-1）；选项 2-4 → **Advanced Features**（0-3，上限为 2）

---

**Round 5 — Plugins & CLI**（header："Mastery"）

"以下哪些你做过？全选适用项。"
选项：
1. "Installed or created a plugin" —— 从 marketplace 使用过打包插件，或创建过带 plugin.json 清单的 .claude-plugin/ 目录
2. "Used plugin advanced features" —— 插件 hook、插件 MCP server、LSP 配置、插件命名空间命令，或用 --plugin-dir 参数测试
3. "Used print mode in scripts or CI/CD" —— 用 `claude -p` 配合 --output-format json、--max-turns、管道输入，或集成进 GitHub Actions / CI 流水线
4. "Used advanced CLI features" —— 会话恢复（-c/-r）、--agents 参数、用于结构化输出的 --json-schema、--fallback-model、--from-pr，或批处理循环

**评分：** 选项 1-2 → **Plugins**（0-2）；选项 3-4 → **CLI**（0-2）
