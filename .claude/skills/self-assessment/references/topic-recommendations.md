# 针对具体主题的建议

当某个主题存在差距时，使用以下具体建议。路径是相对于本参考文件（`.claude/skills/self-assessment/references/`）而言的。

**Slash Commands（得分 0）**：
- Tutorial: [01-slash-commands/](../../../../01-slash-commands/)
- Focus on: 内置命令参考、创建你的第一个 SKILL.md、`$ARGUMENTS` 语法
- Key exercise: 创建一个 `/optimize` 命令并测试它
- Done when: 你能创建一个带参数和动态上下文的自定义 skill

**Slash Commands（得分 1 — 需复习）**：
- Focus on: 用反引号 `!command` 语法注入动态上下文、`@file` 引用、`disable-model-invocation` 与 `user-invocable` 的区别与控制方式
- Done when: 你能创建一个既能注入实时命令输出、又能控制自身调用行为的 skill

**Memory（得分 0）**：
- Tutorial: [02-memory/](../../../../02-memory/)
- Focus on: 创建 CLAUDE.md、`/init` 和 `/memory` 命令、用于快速更新的 `#` 前缀
- Key exercise: 创建一个包含你的编码规范的项目 CLAUDE.md
- Done when: Claude 能在多个会话中记住你的偏好

**Memory（得分 1 — 需复习）**：
- Focus on: 7 层层级与优先级顺序、带路径专属规则的 .claude/rules/ 目录、`@import` 语法（最大深度 5）、Auto Memory 的 MEMORY.md（200 行限制）
- Done when: 你为不同目录设置了模块化规则，并理解完整的层级结构

**Skills（得分 0）**：
- Tutorial: [03-skills/](../../../../03-skills/)
- Focus on: SKILL.md 格式、通过 description 字段实现自动调用、渐进式披露（3 个加载层级）
- Key exercise: 安装 code-review skill 并验证它能自动触发
- Done when: 某个 skill 能根据对话上下文自动激活

**Skills（得分 1 — 需复习）**：
- Focus on: 配合 agent 字段用于 subagent 执行的 `context: fork`、`disable-model-invocation` 与 `user-invocable` 的区别、2% 的上下文预算、捆绑资源（scripts/、references/、assets/）
- Done when: 你能创建一个在 fork 出的上下文中、于 subagent 中运行的 skill

**Hooks（得分 0）**：
- Tutorial: [06-hooks/](../../../../06-hooks/)
- Focus on: 配置结构（matcher + hooks 数组）、PreToolUse/PostToolUse 事件、退出码（0=成功，2=阻塞）、JSON 输入/输出格式
- Key exercise: 创建一个校验 Bash 命令的 PreToolUse hook
- Done when: 某个 hook 能在危险命令执行前将其阻止

**Hooks（得分 1 — 需复习）**：
- Focus on: 全部 25 种 hook 事件（包括 PostToolUseFailure、StopFailure、TaskCreated、CwdChanged、FileChanged、PostCompact、Elicitation、ElicitationResult）、4 种 hook 类型（command、http、prompt、agent）、SKILL.md frontmatter 中的组件级 hook、带 allowedEnvVars 的 HTTP hook、用于 SessionStart/CwdChanged/FileChanged 的 `CLAUDE_ENV_FILE`
- Done when: 你能创建一个基于 prompt 的 Stop hook，以及一个 skill 内的组件级 hook

**MCP（得分 0）**：
- Tutorial: [05-mcp/](../../../../05-mcp/)
- Focus on: `claude mcp add` 命令、传输类型（推荐 HTTP）、GitHub MCP 设置、环境变量展开
- Key exercise: 添加 GitHub MCP server 并查询 PR
- Done when: 你能通过 MCP 从外部服务查询实时数据

**MCP（得分 1 — 需复习）**：
- Focus on: 项目级 .mcp.json（需要团队批准）、OAuth 2.0 认证、通过 `@server:resource` 提及的 MCP resource、Tool Search（ENABLE_TOOL_SEARCH）、`claude mcp serve`、输出限制（10k/25k/50k）
- Done when: 你有一个项目级 .mcp.json，并理解 Tool Search 的 auto 模式

**Subagents（得分 0）**：
- Tutorial: [04-subagents/](../../../../04-subagents/)
- Focus on: agent 文件格式（.claude/agents/*.md）、内置 agent（general-purpose、Plan、Explore）、tools/model/permissionMode 配置
- Key exercise: 创建一个 code-reviewer subagent 并测试任务委派
- Done when: Claude 能把代码审查委派给你的自定义 agent

**Subagents（得分 1 — 需复习）**：
- Focus on: worktree 隔离（`isolation: worktree`）、持久化 agent 记忆（带 scope 的 `memory` 字段）、后台 agent（Ctrl+B/Ctrl+F）、用 `Task(agent_name)` 实现的 agent 白名单、agent 团队（`--teammate-mode`）
- Done when: 你有一个带持久化记忆、运行在 worktree 隔离中的 subagent

**Checkpoints（得分 0）**：
- Tutorial: [08-checkpoints/](../../../../08-checkpoints/)
- Focus on: Esc+Esc 和 /rewind 的使用、5 种 rewind 选项（恢复代码+对话、只恢复对话、只恢复代码、摘要、取消）、局限性（Bash 文件系统操作不被追踪）
- Key exercise: 做一些实验性改动，然后回退恢复
- Done when: 你能放心地做实验，因为知道自己可以随时回退

**Advanced Features（得分 0）**：
- Tutorial: [09-advanced-features/](../../../../09-advanced-features/)
- Focus on: 规划模式（/plan 或 Shift+Tab）、权限模式（5 种）、扩展思考（Alt+T 切换）
- Key exercise: 用规划模式设计一个功能，然后实现它
- Done when: 你能在规划模式和实现模式之间流畅切换

**Advanced Features（得分 1 — 需复习）**：
- Focus on: 远程控制（`claude remote-control`）、网页会话（`claude --remote`）、桌面交接（`/desktop`）、worktree（`claude -w`）、任务列表（Ctrl+T）、企业级托管设置
- Done when: 你能在 CLI、网页和桌面应用之间交接会话

**Plugins（得分 0）**：
- Tutorial: [07-plugins/](../../../../07-plugins/)
- Focus on: 插件结构（.claude-plugin/plugin.json）、插件能捆绑什么（命令、agent、MCP、hook、设置）、从 marketplace 安装
- Key exercise: 安装一个插件并探索它的组件
- Done when: 你理解什么时候该用插件、什么时候该用独立组件

**Plugins（得分 1 — 需复习）**：
- Focus on: 创建 plugin.json 清单、插件 hook（hooks/hooks.json）、LSP 配置（.lsp.json）、`${CLAUDE_PLUGIN_ROOT}` 变量、用于测试的 --plugin-dir、marketplace 发布
- Done when: 你能为你的团队创建并测试一个插件

**CLI（得分 0）**：
- Tutorial: [10-cli/](../../../../10-cli/)
- Focus on: 交互模式 vs print 模式、带管道的 `claude -p`、`--output-format json`、会话管理（-c/-r）
- Key exercise: 把一个文件通过管道传给 `claude -p` 并获得 JSON 输出
- Done when: 你能在脚本中非交互式地使用 Claude

**CLI（得分 1 — 需复习）**：
- Focus on: 带 JSON 配置的 --agents 参数、用于结构化输出的 --json-schema、--fallback-model、--from-pr、--strict-mcp-config、用 for 循环做批处理、`claude mcp serve`
- Done when: 你有一个使用 Claude 并输出结构化 JSON 的 CI/CD 脚本
