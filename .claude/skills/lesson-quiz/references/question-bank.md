# Lesson Quiz — 题库

每节课 10 道题。每道题包含：类别、题目文本、选项（3-4 个）、正确答案、解释、复习章节。

---

## Lesson 01：Slash Commands

### Q1
- **Category**: conceptual
- **Question**: Claude Code 中的 slash command 分为哪四种类型？
- **Options**: A) Built-in、skills、plugin commands、MCP prompts | B) Built-in、custom、hook commands、API prompts | C) System、user、plugin、terminal commands | D) Core、extension、macro、script commands
- **Correct**: A
- **Explanation**: Claude Code 有内置命令（如 /help、/compact）、skills（SKILL.md 文件）、插件命令（带命名空间的 plugin-name:command），以及 MCP prompts（/mcp__server__prompt）。
- **Review**: Types of Slash Commands 章节

### Q2
- **Category**: practical
- **Question**: 如何把用户提供的全部参数传给一个 skill？
- **Options**: A) 使用 `${args}` | B) 使用 `$ARGUMENTS` | C) 使用 `$@` | D) 使用 `$INPUT`
- **Correct**: B
- **Explanation**: `$ARGUMENTS` 会捕获命令名之后的全部文本。如需按位置获取参数，可使用 `$0`、`$1` 等。
- **Review**: Argument handling 章节

### Q3
- **Category**: conceptual
- **Question**: 当一个 skill（.claude/skills/name/SKILL.md）和一个同名的旧版命令（.claude/commands/name.md）同时存在时，哪个优先？
- **Options**: A) 旧版命令优先 | B) skill 优先 | C) 谁先创建谁优先 | D) Claude 会让用户选择
- **Correct**: B
- **Explanation**: 同名情况下 skill 的优先级高于旧版命令。skill 系统取代了更早的命令系统。
- **Review**: Skill precedence 章节

### Q4
- **Category**: practical
- **Question**: 如何把实时的 shell 输出注入到 skill 的 prompt 中？
- **Options**: A) 使用 `$(command)` 语法 | B) 使用 `!`command`` （感叹号加反引号）语法 | C) 使用 `@shell:command` 语法 | D) 使用 `{command}` 语法
- **Correct**: B
- **Explanation**: `!`command`` 语法会运行一个 shell 命令，并在 Claude 看到 prompt 之前把其输出注入其中。
- **Review**: Dynamic context injection 章节

### Q5
- **Category**: conceptual
- **Question**: skill frontmatter 中的 `disable-model-invocation: true` 做了什么？
- **Options**: A) 完全阻止该 skill 运行 | B) 只允许用户手动调用它（Claude 不能自动调用） | C) 把它从 /help 菜单中隐藏 | D) 关闭该 skill 的 AI 处理能力
- **Correct**: B
- **Explanation**: `disable-model-invocation: true` 表示只有用户可以通过 `/command-name` 手动触发该命令，Claude 永远不会自动调用它，这对有副作用的操作（例如部署）很有用。
- **Review**: Controlling invocation 章节

### Q6
- **Category**: practical
- **Question**: 你想创建一个只能由 Claude 自动调用（在用户的 / 菜单中隐藏）的 skill，应该设置哪个 frontmatter 字段？
- **Options**: A) `disable-model-invocation: true` | B) `user-invocable: false` | C) `hidden: true` | D) `auto-only: true`
- **Correct**: B
- **Explanation**: `user-invocable: false` 会把该 skill 从用户的 slash 菜单中隐藏，但允许 Claude 根据上下文自动调用它。
- **Review**: Invocation control matrix 章节

### Q7
- **Category**: practical
- **Question**: 新建一个名为 "deploy" 的自定义 skill，正确的目录结构是什么？
- **Options**: A) `.claude/commands/deploy.md` | B) `.claude/skills/deploy/SKILL.md` | C) `.claude/skills/deploy.md` | D) `.claude/deploy/SKILL.md`
- **Correct**: B
- **Explanation**: skill 存放在 `.claude/skills/` 下的一个目录中，目录里有一个 `SKILL.md` 文件。目录名要与命令名一致。
- **Review**: Skill types and locations 章节

### Q8
- **Category**: conceptual
- **Question**: 插件命令是如何避免与用户命令产生命名冲突的？
- **Options**: A) 使用 `plugin-name:command-name` 命名空间 | B) 使用特殊的 .plugin 扩展名 | C) 加上 `p/` 前缀 | D) 自动覆盖用户命令
- **Correct**: A
- **Explanation**: 插件命令使用类似 `pr-review:check-security` 的命名空间，以避免与独立的用户命令冲突。
- **Review**: Plugin commands 章节

### Q9
- **Category**: practical
- **Question**: 你想限制某个 skill 能使用哪些工具，应该添加哪个 frontmatter 字段？
- **Options**: A) `tools: [Read, Grep]` | B) `allowed-tools: [Read, Grep]` | C) `permissions: [Read, Grep]` | D) `restrict-tools: [Read, Grep]`
- **Correct**: B
- **Explanation**: SKILL.md frontmatter 中的 `allowed-tools` 字段用于限定该命令可以调用哪些工具。
- **Review**: Frontmatter fields reference 章节

### Q10
- **Category**: conceptual
- **Question**: skill 中的 `@file` 语法是用来做什么的？
- **Options**: A) 引入另一个 skill | B) 引用一个文件，把它的内容纳入 prompt | C) 创建一个符号链接 | D) 设置文件权限
- **Correct**: B
- **Explanation**: skill 中的 `@path/to/file` 语法会把被引用文件的内容纳入 prompt，让 skill 可以引入模板或上下文文件。
- **Review**: File references 章节

---

## Lesson 02：Memory

### Q1
- **Category**: conceptual
- **Question**: Claude Code 的记忆层级（memory hierarchy）有几层？优先级最高的是哪一层？
- **Options**: A) 5 层，User Memory 最高 | B) 7 层，Managed Policy 最高 | C) 3 层，Project Memory 最高 | D) 7 层，Auto Memory 最高
- **Correct**: B
- **Explanation**: 记忆层级共有 7 层：Managed Policy > Project Memory > Project Rules > User Memory > User Rules > Local Project Memory > Auto Memory。由管理员设置的 Managed Policy 优先级最高。
- **Review**: Memory hierarchy 章节

### Q2
- **Category**: practical
- **Question**: 在对话过程中，如何快速给记忆添加一条新规则？
- **Options**: A) 使用 `/memory` 命令，或直接用对话的方式说出来 | B) 在消息前加 `#` 前缀（例如 `# always use TypeScript`） | C) 输入 `/rule "rule text"` | D) 使用 `@add-memory "rule text"`
- **Correct**: A
- **Explanation**: 推荐的添加记忆方式是使用 `/memory` 命令（在编辑器中打开记忆文件），或者直接用对话方式告诉 Claude（例如"记住我们始终使用 TypeScript strict 模式"）。`#` 前缀方式已被废弃，不再可用。
- **Review**: README 中的 Quick memory updates 章节

### Q3
- **Category**: conceptual
- **Question**: CLAUDE.md 中 `@path/to/file` 导入语法的最大嵌套深度是多少？
- **Options**: A) 3 层 | B) 5 层 | C) 10 层 | D) 无限制
- **Correct**: B
- **Explanation**: `@import` 语法支持递归导入，最大深度为 5 层，以防止无限循环。
- **Review**: Import syntax 章节

### Q4
- **Category**: practical
- **Question**: 如何让一条规则只对 `src/api/` 目录下的文件生效？
- **Options**: A) 把规则写在 `src/api/CLAUDE.md` 中 | B) 在 `.claude/rules/*.md` 文件中添加 `paths: src/api/**` 这样的 YAML frontmatter | C) 把文件命名为 `.claude/rules/api.md` | D) 在规则文件中使用 `@scope: src/api`
- **Correct**: B
- **Explanation**: `.claude/rules/` 下的文件支持 `paths:` frontmatter 字段，用 glob 模式把规则限定在特定目录中生效。
- **Review**: Path-specific rules 章节

### Q5
- **Category**: conceptual
- **Question**: Auto Memory 的 MEMORY.md 在会话开始时会加载多少行？
- **Options**: A) 全部行 | B) 前 100 行 | C) 前 200 行 | D) 前 500 行
- **Correct**: C
- **Explanation**: MEMORY.md 的前 200 行会在会话开始时自动加载进上下文。从 MEMORY.md 引用的主题文件则按需加载。
- **Review**: Auto Memory 章节

### Q6
- **Category**: practical
- **Question**: 你想保存不提交到 git 的个人项目偏好，应该使用哪个文件？
- **Options**: A) `~/.claude/CLAUDE.md` | B) `CLAUDE.local.md` | C) `.claude/rules/personal.md` | D) `.claude/memory/personal.md`
- **Correct**: B
- **Explanation**: 项目根目录下的 `CLAUDE.local.md` 用于保存个人的项目特定偏好设置，应当被 git 忽略。
- **Review**: Memory locations comparison 章节

### Q7
- **Category**: conceptual
- **Question**: `/init` 命令的作用是什么？
- **Options**: A) 从零初始化一个新的 Claude Code 项目 | B) 根据你的项目结构生成一份模板 CLAUDE.md | C) 把所有记忆重置为默认值 | D) 创建一个新会话
- **Correct**: B
- **Explanation**: `/init` 会分析你的项目，并生成一份带有建议规则和规范的模板 CLAUDE.md。它是一次性的初始化工具。
- **Review**: /init command 章节

### Q8
- **Category**: practical
- **Question**: 如何彻底关闭 Auto Memory？
- **Options**: A) 删除 ~/.claude/projects 目录 | B) 设置 `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` | C) 在 CLAUDE.md 中添加 `auto-memory: false` | D) 使用 `/memory disable auto`
- **Correct**: B
- **Explanation**: 设置 `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` 会关闭 Auto Memory。设为 `0` 则强制开启。不设置时默认开启。
- **Review**: Auto Memory configuration 章节

### Q9
- **Category**: conceptual
- **Question**: 优先级较低的记忆层级能否覆盖优先级较高层级的规则？
- **Options**: A) 可以，最近的规则总是优先 | B) 不可以，高优先级层级始终优先 | C) 可以，如果低优先级层级使用了 `!important` 标记 | D) 取决于规则类型
- **Correct**: B
- **Explanation**: 记忆的优先级从 Managed Policy 开始向下流动。低优先级层级（如 Auto Memory）无法覆盖高优先级层级（如 Project Memory）。
- **Review**: Memory hierarchy 章节

### Q10
- **Category**: practical
- **Question**: 你同时在两个仓库中工作，希望 Claude 同时加载这两个仓库的 CLAUDE.md，应该使用哪个参数？
- **Options**: A) `--multi-repo` | B) `--add-dir /path/to/other` | C) `--include /path/to/other` | D) `--merge-context /path/to/other`
- **Correct**: B
- **Explanation**: `--add-dir` 参数会加载额外目录中的 CLAUDE.md，从而支持多仓库上下文。
- **Review**: Additional directories 章节

---

## Lesson 03：Skills

### Q1
- **Category**: conceptual
- **Question**: skill 系统的渐进式披露（progressive disclosure）分为哪 3 个层级？
- **Options**: A) Metadata、instructions、resources | B) Name、body、attachments | C) Header、content、scripts | D) Summary、details、data
- **Correct**: A
- **Explanation**: Level 1：Metadata（约 100 tokens，始终加载）；Level 2：SKILL.md 正文（低于 5k tokens，触发时加载）；Level 3：捆绑资源（scripts/references/assets，按需加载）。
- **Review**: Progressive disclosure architecture 章节

### Q2
- **Category**: practical
- **Question**: 让 Claude 自动调用某个 skill 时，最关键的因素是什么？
- **Options**: A) skill 的文件名 | B) frontmatter 中的 `description` 字段，以及其中的触发关键词 | C) skill 所在的目录位置 | D) frontmatter 中的 `auto-invoke: true` 字段
- **Correct**: B
- **Explanation**: Claude 是否自动调用一个 skill，完全取决于它的 `description` 字段。该字段必须包含具体的触发短语和使用场景。
- **Review**: Auto-invocation 章节

### Q3
- **Category**: conceptual
- **Question**: SKILL.md 文件推荐的最大长度是多少？
- **Options**: A) 100 行 | B) 250 行 | C) 500 行 | D) 1000 行
- **Correct**: C
- **Explanation**: SKILL.md 应保持在 500 行以内，更大的参考资料应放在 `references/` 子目录的文件中。
- **Review**: Content guidelines 章节

### Q4
- **Category**: practical
- **Question**: 如何让一个 skill 在拥有独立上下文的隔离子代理（subagent）中运行？
- **Options**: A) 在 frontmatter 中设置 `isolation: true` | B) 在 frontmatter 中设置 `context: fork` 并配合 `agent` 字段 | C) 在 frontmatter 中设置 `subagent: true` | D) 把该 skill 放进 `.claude/agents/`
- **Correct**: B
- **Explanation**: `context: fork` 会让该 skill 在独立的上下文中运行，`agent` 字段则指定要使用哪种 agent 类型（例如 `Explore`、`Plan`，或自定义 agent）。
- **Review**: Running skills in subagents 章节

### Q5
- **Category**: conceptual
- **Question**: skill metadata（Level 1）大约占用多少上下文预算？
- **Options**: A) 上下文窗口的 0.5% | B) 上下文窗口的 1% | C) 上下文窗口的 5% | D) 上下文窗口的 10%
- **Correct**: B
- **Explanation**: skill metadata 大约占用上下文窗口的 1%（兜底值为 8,000 字符）。可以通过 `SLASH_COMMAND_TOOL_CHAR_BUDGET` 配置。
- **Review**: Context budget 章节

### Q6
- **Category**: practical
- **Question**: 某个 skill 需要引用一份很大的 API 规范文档，应该放在哪里？
- **Options**: A) 直接写在 SKILL.md 里 | B) 放在该 skill 目录下的 `references/api-spec.md` 文件中 | C) 放在项目的 CLAUDE.md 中 | D) 放在单独的 `.claude/rules/` 文件中
- **Correct**: B
- **Explanation**: 较大的参考资料应放在 `references/` 子目录中。Claude 会按需加载 Level 3 资源，从而让 SKILL.md 保持精简。
- **Review**: Supporting files structure 章节

### Q7
- **Category**: conceptual
- **Question**: skill 中的 Reference Content 与 Task Content 有什么区别？
- **Options**: A) Reference 是只读的，Task 是可读写的 | B) Reference 为上下文补充知识，Task 提供分步操作说明 | C) Reference 用于文档，Task 用于代码 | D) 两者没有区别
- **Correct**: B
- **Explanation**: Reference Content 为 Claude 的上下文补充领域知识（例如品牌规范）。Task Content 为某个工作流提供可执行的分步操作说明。
- **Review**: Skill content types 章节

### Q8
- **Category**: practical
- **Question**: skill frontmatter 中 `name` 字段允许使用哪些字符？
- **Options**: A) 任意字符 | B) 只能是小写字母、数字和连字符（最多 64 个字符） | C) 字母和下划线 | D) 仅限字母数字
- **Correct**: B
- **Explanation**: name 必须是 kebab-case（小写、用连字符分隔），最多 64 个字符，且不能包含 "anthropic" 或 "claude"。
- **Review**: SKILL.md format 章节

### Q9
- **Category**: conceptual
- **Question**: Claude 按什么顺序搜索 skill？
- **Options**: A) User > Project > Enterprise | B) Enterprise > Personal > Project（插件使用命名空间） | C) Project > User > Enterprise | D) 按字母顺序
- **Correct**: B
- **Explanation**: 优先级顺序是：Enterprise > Personal > Project。插件 skill 使用命名空间（plugin-name:skill），因此不会产生冲突。
- **Review**: Skill types and locations 章节

### Q10
- **Category**: practical
- **Question**: 如何既阻止 Claude 自动调用某个 skill，又保留用户手动使用它的能力？
- **Options**: A) 设置 `user-invocable: false` | B) 设置 `disable-model-invocation: true` | C) 移除 description 字段 | D) 设置 `auto-invoke: false`
- **Correct**: B
- **Explanation**: `disable-model-invocation: true` 会阻止 Claude 自动调用，但该 skill 仍会保留在用户的 `/` 菜单中供手动使用。
- **Review**: Controlling invocation 章节

---

## Lesson 04：Subagents

### Q1
- **Category**: conceptual
- **Question**: 相较于内联对话，subagent 的主要优势是什么？
- **Options**: A) 速度更快 | B) 在独立、干净的上下文窗口中运行，避免上下文被污染 | C) 能使用更多工具 | D) 错误处理更好
- **Correct**: B
- **Explanation**: subagent 会获得一个全新的上下文窗口，只接收主 agent 传给它的内容。这样可以避免主对话被任务相关的细节污染。
- **Review**: Overview 章节

### Q2
- **Category**: practical
- **Question**: agent 定义的优先级顺序是怎样的？
- **Options**: A) Project > User > CLI | B) CLI > Project > User | C) User > Project > CLI | D) 三者优先级相同
- **Correct**: B
- **Explanation**: CLI 定义的 agent（`--agents` 参数）会覆盖 Project 级别（`.claude/agents/`），Project 级别又会覆盖 User 级别（`~/.claude/agents/`）。
- **Review**: File locations 章节

### Q3
- **Category**: conceptual
- **Question**: 哪个内置 subagent 使用 Haiku 模型，专门为只读的代码库探索做了优化？
- **Options**: A) general-purpose | B) Plan | C) Explore | D) Bash
- **Correct**: C
- **Explanation**: Explore subagent 使用 Haiku 模型，用于快速、只读的代码库探索。它支持三种深入程度：quick、medium、very thorough。
- **Review**: Built-in subagents 章节

### Q4
- **Category**: practical
- **Question**: 如何限制某个协调者（coordinator）agent 能生成哪些 subagent？
- **Options**: A) 使用 `allowed-agents:` 字段 | B) 在 `tools` 字段中使用 `Task(agent_name)` 语法 | C) 设置 `spawn-limit: 2` | D) 使用 `restrict-agents: [name1, name2]`
- **Correct**: B
- **Explanation**: 在 tools 字段中添加 `Task(worker, researcher)` 会创建一个白名单——该 agent 只能生成名为 "worker" 或 "researcher" 的 subagent。
- **Review**: Restrict spawnable subagents 章节

### Q5
- **Category**: conceptual
- **Question**: `isolation: worktree` 对 subagent 做了什么？
- **Options**: A) 在 Docker 容器中运行该 agent | B) 为该 agent 提供独立的 git worktree，使其改动不影响主工作树 | C) 阻止该 agent 读取任何文件 | D) 在沙箱中运行该 agent
- **Correct**: B
- **Explanation**: worktree 隔离会创建一个独立的 git worktree。如果 agent 没有做任何改动，会自动清理；如果做了改动，会返回该 worktree 的路径和分支。
- **Review**: Worktree isolation 章节

### Q6
- **Category**: practical
- **Question**: 如何让某个 subagent 在后台运行？
- **Options**: A) 在 agent 配置中设置 `background: true` | B) 在 agent 配置中使用 `async: true` | C) 启动后按 Ctrl+D | D) 使用 `--background` CLI 参数
- **Correct**: A
- **Explanation**: agent 配置中的 `background: true` 会让该 subagent 始终以后台任务方式运行。用户也可以按 Ctrl+B 把一个前台任务转到后台。
- **Review**: Background subagents 章节

### Q7
- **Category**: conceptual
- **Question**: subagent 中 scope 为 `project` 的 `memory` 字段起什么作用？
- **Options**: A) 赋予对项目 CLAUDE.md 的读取权限 | B) 创建一个绑定到当前项目的持久化记忆目录 | C) 共享主 agent 的对话历史 | D) 加载项目的 git 历史
- **Correct**: B
- **Explanation**: `memory` 字段会为该 subagent 创建一个持久化目录。scope 为 `project` 表示该记忆绑定到当前项目。该 agent MEMORY.md 的前 200 行会自动加载。
- **Review**: Persistent memory 章节

### Q8
- **Category**: practical
- **Question**: 如何在 subagent 的 description 中加入某种表述，促使 Claude 主动把任务委派给它？
- **Options**: A) 加上 "priority: high" | B) 在 description 中包含 "use PROACTIVELY" 或 "MUST BE USED" | C) 设置 `auto-delegate: true` | D) 加上 "trigger: always"
- **Correct**: B
- **Explanation**: 在 description 中包含 "use PROACTIVELY" 或 "MUST BE USED" 这类短语，会强烈促使 Claude 自动把匹配的任务委派给该 agent。
- **Review**: Automatic delegation 章节

### Q9
- **Category**: conceptual
- **Question**: subagent 有效的 `permissionMode` 取值有哪些？
- **Options**: A) read、write、admin | B) default、acceptEdits、bypassPermissions、plan、dontAsk、auto | C) safe、normal、dangerous | D) restricted、standard、elevated
- **Correct**: B
- **Explanation**: subagent 支持六种权限模式：default（对一切操作都询问）、acceptEdits（自动接受文件编辑）、bypassPermissions（跳过全部检查）、plan（只读）、dontAsk（除非预先批准，否则自动拒绝）、auto（由后台分类器决定）。
- **Review**: Configuration fields 章节

### Q10
- **Category**: practical
- **Question**: 如何恢复一个此前运行返回了 agentId 的 subagent？
- **Options**: A) 使用 `/resume agent-id` | B) 调用 Task 工具时传入 `resume` 参数并附上该 agentId | C) 使用 `claude -r agent-id` | D) subagent 无法被恢复
- **Correct**: B
- **Explanation**: 通过在调用 Task 工具时传入之前返回的 agentId 作为 `resume` 参数，可以恢复该 subagent，并完整保留之前的上下文继续执行。
- **Review**: Resumable agents 章节

---

## Lesson 05：MCP

### Q1
- **Category**: conceptual
- **Question**: MCP 有哪三种传输协议？推荐使用哪一种？
- **Options**: A) HTTP（推荐）、Stdio、SSE（已弃用） | B) WebSocket（推荐）、REST、gRPC | C) TCP、UDP、HTTP | D) Stdio（推荐）、HTTP、SSE
- **Correct**: A
- **Explanation**: 远程 server 推荐使用 HTTP。Stdio 适用于本地进程（目前最常见）。SSE 已被弃用，但仍受支持。
- **Review**: Transport protocols 章节

### Q2
- **Category**: practical
- **Question**: 如何通过 CLI 添加一个 GitHub MCP server？
- **Options**: A) `claude mcp install github` | B) `claude mcp add --transport http github https://api.github.com/mcp` | C) `claude plugin add github-mcp` | D) `claude connect github`
- **Correct**: B
- **Explanation**: 使用 `claude mcp add`，配合 `--transport` 参数、一个名称和 server 的 URL。stdio 方式则是：`claude mcp add github -- npx -y @modelcontextprotocol/server-github`。
- **Review**: MCP configuration management 章节

### Q3
- **Category**: conceptual
- **Question**: 当 MCP 工具描述超过上下文窗口的 10% 时会发生什么？
- **Options**: A) 会被截断 | B) 自动开启 Tool Search，动态挑选相关工具 | C) Claude 会报错 | D) 多余的工具会被禁用
- **Correct**: B
- **Explanation**: 当工具描述超过上下文的 10% 时，MCP Tool Search 会自动开启。它至少需要 Sonnet 4 或 Opus 4（不支持 Haiku）。
- **Review**: MCP Tool Search 章节

### Q4
- **Category**: practical
- **Question**: 如何在 MCP 配置中为环境变量设置回退值？
- **Options**: A) `${VAR || "default"}` | B) `${VAR:-default}` | C) `${VAR:default}` | D) `${VAR ? "default"}`
- **Correct**: B
- **Explanation**: `${VAR:-default}` 会在环境变量未设置时提供一个回退值。不带回退值的 `${VAR}` 在未设置时会报错。
- **Review**: Environment variable expansion 章节

### Q5
- **Category**: conceptual
- **Question**: 在数据访问方面，MCP 和 Memory 有什么区别？
- **Options**: A) MCP 更快，Memory 更慢 | B) MCP 面向实时 / 变化中的外部数据，Memory 面向持久 / 静态的偏好设置 | C) MCP 面向代码，Memory 面向文本 | D) 两者可以互换
- **Correct**: B
- **Explanation**: MCP 连接的是实时变化的外部数据源（API、数据库）。Memory 存储的是持久、静态的项目上下文和偏好设置。
- **Review**: MCP vs Memory 章节

### Q6
- **Category**: practical
- **Question**: 团队成员第一次遇到项目级 `.mcp.json` 时会发生什么？
- **Options**: A) 会自动加载 | B) 会收到一个批准提示，确认是否信任该项目的 MCP server | C) 除非用户在设置中主动开启，否则会被忽略 | D) Claude 会请求管理员批准
- **Correct**: B
- **Explanation**: 项目级 `.mcp.json` 会在团队成员第一次使用时触发一个安全批准提示。这是刻意设计的——用来防止不受信任的 MCP server。
- **Review**: MCP Scopes 章节

### Q7
- **Category**: conceptual
- **Question**: `claude mcp serve` 的作用是什么？
- **Options**: A) 启动一个 MCP server 仪表盘 | B) 让 Claude Code 本身作为 MCP server，供其他应用调用 | C) 提供 MCP 文档服务 | D) 测试 MCP server 连接
- **Correct**: B
- **Explanation**: `claude mcp serve` 会把 Claude Code 变成一个 MCP server，从而支持多 agent 编排——一个 Claude 实例可以被另一个控制。
- **Review**: Claude as MCP Server 章节

### Q8
- **Category**: practical
- **Question**: MCP 工具的默认最大输出大小是多少？
- **Options**: A) 5,000 tokens | B) 10,000 tokens | C) 25,000 tokens | D) 50,000 tokens
- **Correct**: C
- **Explanation**: 默认最大值为 25,000 tokens（`MAX_MCP_OUTPUT_TOKENS`）。达到 10k tokens 时会出现警告。落盘持久化的上限为 50k 字符。
- **Review**: MCP Output Limits 章节

### Q9
- **Category**: conceptual
- **Question**: 当托管配置中 `allowedMcpServers` 和 `deniedMcpServers` 同时匹配某个 server 时，哪个生效？
- **Options**: A) allowed 生效 | B) denied 生效 | C) 以最后配置的为准 | D) 两者都独立生效
- **Correct**: B
- **Explanation**: 在托管的 MCP 配置中，拒绝（deny）规则总是优先于允许（allow）规则。
- **Review**: Managed MCP Configuration 章节

### Q10
- **Category**: practical
- **Question**: 如何在对话中引用一个 MCP resource？
- **Options**: A) 使用 `/mcp resource-name` | B) 使用 `@server-name:protocol://resource/path` 提及语法 | C) 使用 `mcp.get("resource")` | D) resource 会自动加载
- **Correct**: B
- **Explanation**: MCP resource 是通过对话中的 `@server-name:protocol://resource/path` 提及语法来访问的。
- **Review**: MCP Resources 章节

---

## Lesson 06：Hooks

### Q1
- **Category**: conceptual
- **Question**: Claude Code 中的 hook 分为哪四种类型？
- **Options**: A) Pre、Post、Error 和 Filter hooks | B) Command、HTTP、Prompt 和 Agent hooks | C) Before、After、Around 和 Through hooks | D) Input、Output、Filter 和 Transform hooks
- **Correct**: B
- **Explanation**: Command hook 运行 shell 脚本，HTTP hook 调用 webhook 端点，Prompt hook 使用单轮 LLM 评估，Agent hook 使用基于 subagent 的校验。
- **Review**: Hook types 章节

### Q2
- **Category**: practical
- **Question**: 一个 hook 脚本以退出码 2 结束，会发生什么？
- **Options**: A) 显示一条非阻塞性的警告 | B) 阻塞性错误——stderr 会作为错误展示给 Claude，工具调用被阻止 | C) hook 会被重试 | D) 会话结束
- **Correct**: B
- **Explanation**: 退出码 0 = 成功/继续，退出码 2 = 阻塞性错误（stderr 会作为错误展示），其他非零退出码 = 非阻塞性（stderr 仅在 verbose 模式下可见）。
- **Review**: Exit codes 章节

### Q3
- **Category**: conceptual
- **Question**: PreToolUse hook 在 stdin 上会收到哪些 JSON 字段？
- **Options**: A) `tool_name` 和 `tool_output` | B) `session_id`、`tool_name`、`tool_input`、`hook_event_name`、`cwd` 等 | C) 只有 `tool_name` | D) 完整的对话历史
- **Correct**: B
- **Explanation**: hook 会在 stdin 上收到一个 JSON 对象，包含：session_id、transcript_path、hook_event_name、tool_name、tool_input、tool_use_id、cwd、permission_mode。
- **Review**: JSON input structure 章节

### Q4
- **Category**: practical
- **Question**: PreToolUse hook 如何在工具执行前修改其输入参数？
- **Options**: A) 在 stderr 上返回修改后的 JSON | B) 在 stdout 上返回带 `updatedInput` 字段的 JSON（退出码 0） | C) 写入一个临时文件 | D) hook 无法修改输入
- **Correct**: B
- **Explanation**: PreToolUse hook 可以在 stdout 输出带 `"updatedInput": {...}` 的 JSON（退出码 0），从而在 Claude 使用工具参数之前对其进行修改。
- **Review**: PreToolUse output 章节

### Q5
- **Category**: conceptual
- **Question**: 哪个 hook 事件支持使用 `CLAUDE_ENV_FILE` 把环境变量持久化写入会话？
- **Options**: A) PreToolUse | B) UserPromptSubmit | C) SessionStart | D) 所有事件
- **Correct**: C
- **Explanation**: 只有 SessionStart hook 可以使用 `CLAUDE_ENV_FILE` 把环境变量持久化写入会话。
- **Review**: SessionStart 章节

### Q6
- **Category**: practical
- **Question**: 你想要一个只在 skill 首次加载时运行一次、而不是每次工具调用都运行的 hook，应该添加哪个字段？
- **Options**: A) `run-once: true` | B) 在组件级 hook 定义中使用 `once: true` | C) `single: true` | D) `max-runs: 1`
- **Correct**: B
- **Explanation**: 组件级 hook（定义在 SKILL.md 或 agent frontmatter 中）支持 `once: true`，使其只在首次激活时运行。
- **Review**: Component-scoped hooks 章节

### Q7
- **Category**: conceptual
- **Question**: 在 subagent 的 frontmatter 中定义了一个 Stop hook，它会自动转换成什么？
- **Options**: A) 一个 PostToolUse hook | B) 一个 SubagentStop hook | C) 一个 SessionEnd hook | D) 仍然保持为 Stop hook
- **Correct**: B
- **Explanation**: 当 Stop hook 被放在某个 subagent 的 frontmatter 中时，会自动转换为 SubagentStop，从而在该特定 subagent 结束时运行。
- **Review**: Component-scoped hooks 章节

### Q8
- **Category**: practical
- **Question**: 如何让一个 hook 匹配某个特定 server 的所有 MCP 工具？
- **Options**: A) `matcher: "mcp_github"` | B) `matcher: "mcp__github__.*"`（正则表达式模式） | C) `matcher: "mcp:github:*"` | D) `matcher: "github-mcp"`
- **Correct**: B
- **Explanation**: matcher 使用正则表达式模式。MCP 工具遵循 `mcp__server__tool` 命名规范，因此 `mcp__github__.*` 能匹配全部 GitHub MCP 工具。
- **Review**: Matcher patterns 章节

### Q9
- **Category**: conceptual
- **Question**: Claude Code 总共支持多少种 hook 事件？
- **Options**: A) 10 | B) 16 | C) 25 | D) 30
- **Correct**: C
- **Explanation**: Claude Code 支持 25 种 hook 事件：PreToolUse、PostToolUse、PostToolUseFailure、UserPromptSubmit、Stop、StopFailure、SubagentStop、SubagentStart、PermissionRequest、Notification、PreCompact、PostCompact、SessionStart、SessionEnd、WorktreeCreate、WorktreeRemove、ConfigChange、CwdChanged、FileChanged、TeammateIdle、TaskCompleted、TaskCreated、Elicitation、ElicitationResult、InstructionsLoaded。
- **Review**: Hook events table 章节

### Q10
- **Category**: practical
- **Question**: 你想调试为什么某个 hook 没有触发，最佳做法是什么？
- **Options**: A) 在 hook 脚本中添加 print 语句 | B) 使用 `--debug` 参数并按 `Ctrl+O` 进入详细模式 | C) 查看系统日志 | D) hook 没有调试工具
- **Correct**: B
- **Explanation**: `--debug` 参数和 `Ctrl+O` 详细模式会展示 hook 执行的细节，包括触发了哪些 hook、它们的输入和输出。
- **Review**: Debugging 章节

---

## Lesson 07：Plugins

### Q1
- **Category**: conceptual
- **Question**: 插件的核心清单文件是什么？它存放在哪里？
- **Options**: A) 根目录下的 `plugin.yaml` | B) `.claude-plugin/plugin.json` | C) 带 "claude" 键的 `package.json` | D) `.claude/plugin.md`
- **Correct**: B
- **Explanation**: 插件清单存放在 `.claude-plugin/plugin.json`，必填字段包括：name、description、version、author。
- **Review**: Plugin definition structure 章节

### Q2
- **Category**: practical
- **Question**: 如何在发布前于本地测试一个插件？
- **Options**: A) 使用 `/plugin test ./my-plugin` | B) 使用 `claude --plugin-dir ./my-plugin` | C) 使用 `claude plugin validate ./my-plugin` | D) 把它复制到 ~/.claude/plugins/
- **Correct**: B
- **Explanation**: `--plugin-dir` 参数可以从本地目录加载插件进行测试，该参数可重复使用以加载多个插件。
- **Review**: Testing 章节

### Q3
- **Category**: conceptual
- **Question**: 在插件的 hook 和 MCP 配置中，可以用哪个环境变量引用插件的安装目录？
- **Options**: A) `$PLUGIN_HOME` | B) `${CLAUDE_PLUGIN_ROOT}` | C) `$PLUGIN_DIR` | D) `${CLAUDE_PLUGIN_PATH}`
- **Correct**: B
- **Explanation**: `${CLAUDE_PLUGIN_ROOT}` 会解析为该插件的安装目录，使 hook 和 MCP 配置中的路径引用具备可移植性。
- **Review**: Plugin directory structure 章节

### Q4
- **Category**: practical
- **Question**: "pr-review" 插件中有一个名为 "check-security" 的命令，用户如何调用它？
- **Options**: A) `/check-security` | B) `/pr-review:check-security` | C) `/plugin pr-review check-security` | D) `/pr-review/check-security`
- **Correct**: B
- **Explanation**: 插件命令使用 `plugin-name:command-name` 命名空间，以避免与用户命令及其他插件冲突。
- **Review**: Plugin commands 章节

### Q5
- **Category**: conceptual
- **Question**: 插件可以捆绑哪些组件？
- **Options**: A) 只有命令和设置 | B) 命令、agent、skill、hook、MCP server、LSP 配置、设置、模板、脚本 | C) 只有命令、hook 和 MCP server | D) 只有 skill 和 agent
- **Correct**: B
- **Explanation**: 插件可以捆绑：commands/、agents/、skills/、hooks/hooks.json、.mcp.json、.lsp.json、settings.json、templates/、scripts/、docs/、tests/。
- **Review**: Plugin directory structure 章节

### Q6
- **Category**: practical
- **Question**: 如何从 GitHub 安装一个插件？
- **Options**: A) `claude plugin add github:username/repo` | B) `/plugin install github:username/repo` | C) `npm install @claude/username-repo` | D) 先 `git clone`，再 `claude plugin register`
- **Correct**: B
- **Explanation**: 使用 `/plugin install github:username/repo` 可以直接从 GitHub 仓库安装。
- **Review**: Installation methods 章节

### Q7
- **Category**: conceptual
- **Question**: 插件 `settings.json` 中的 `agent` 键起什么作用？
- **Options**: A) 指定身份验证凭据 | B) 设置该插件的主线程 agent | C) 列出可用的 subagent | D) 配置 agent 权限
- **Correct**: B
- **Explanation**: 插件 settings.json 中的 `agent` 键指定该插件激活时，主线程使用哪个 agent 定义。
- **Review**: Plugin Settings 章节

### Q8
- **Category**: practical
- **Question**: 如何管理插件的生命周期（启用/禁用/更新）？
- **Options**: A) 手动编辑配置文件 | B) 使用 `/plugin enable`、`/plugin disable`、`/plugin update plugin-name` | C) 使用 `claude plugin-manager` | D) 重新安装插件
- **Correct**: B
- **Explanation**: Claude Code 提供了用于完整生命周期管理的 slash 命令：enable、disable、update、uninstall。
- **Review**: Installation methods 章节

### Q9
- **Category**: conceptual
- **Question**: 相较于独立的 skill/hook/MCP，插件的主要优势是什么？
- **Options**: A) 插件运行更快 | B) 单命令安装、有版本管理、通过 marketplace 分发、把一切打包在一起 | C) 插件拥有更多权限 | D) 插件可以离线工作
- **Correct**: B
- **Explanation**: 插件把多个组件打包成一个可安装单元，具备版本管理、marketplace 分发和自动更新能力——相比手动配置各个独立组件更高效。
- **Review**: Standalone vs Plugin comparison 章节

### Q10
- **Category**: practical
- **Question**: 插件的 hook 配置存放在插件目录中的哪个位置？
- **Options**: A) `.claude-plugin/hooks.json` | B) `hooks/hooks.json` | C) `plugin.json` 的 hooks 部分 | D) `.claude/settings.json`
- **Correct**: B
- **Explanation**: 插件的 hook 配置存放在插件目录结构中的 `hooks/hooks.json`。
- **Review**: Plugin hooks 章节

---

## Lesson 08：Checkpoints

### Q1
- **Category**: conceptual
- **Question**: checkpoint 会捕获哪四类内容？
- **Options**: A) Git 提交、分支、标签、stash | B) 消息、文件修改、工具使用历史、会话上下文 | C) 代码、测试、日志、配置 | D) 输入、输出、错误、耗时
- **Correct**: B
- **Explanation**: checkpoint 会捕获对话消息、Claude 工具所做的文件修改、工具使用历史，以及会话上下文。
- **Review**: Overview 章节

### Q2
- **Category**: practical
- **Question**: 如何打开 checkpoint 浏览器？
- **Options**: A) 使用 `/checkpoints` 命令 | B) 按 `Esc + Esc`（连按两次 Esc）或使用 `/rewind` | C) 使用 `/history` 命令 | D) 按 `Ctrl+Z`
- **Correct**: B
- **Explanation**: 连按两次 Esc（Esc+Esc）或使用 `/rewind` 命令，可以打开 checkpoint 浏览器来选择恢复点。
- **Review**: Accessing checkpoints 章节

### Q3
- **Category**: conceptual
- **Question**: rewind 有几种选项？分别是什么？
- **Options**: A) 3 种：Undo、Redo、Reset | B) 5 种：恢复代码+对话、只恢复对话、只恢复代码、从此处摘要、取消 | C) 2 种：完整恢复、部分恢复 | D) 4 种：代码、消息、两者都恢复、取消
- **Correct**: B
- **Explanation**: 5 种选项分别是：恢复代码和对话（完整回滚）、只恢复对话、只恢复代码、从此处摘要（压缩）、取消（放弃）。
- **Review**: Rewind options 章节

### Q4
- **Category**: practical
- **Question**: 你在 Claude Code 中通过 Bash 执行了 `rm -rf temp/`，然后想要回退。checkpoint 能恢复这些文件吗？
- **Options**: A) 能，checkpoint 会捕获一切 | B) 不能，checkpoint 不追踪 Bash 的文件系统操作（rm、mv、cp） | C) 只有用 Edit 工具执行才能恢复 | D) 只有开启了 autoCheckpoint 才能恢复
- **Correct**: B
- **Explanation**: checkpoint 只追踪由 Claude 工具（Write、Edit）所做的文件改动。像 rm、mv、cp 这类 Bash 命令的操作在 checkpoint 的追踪范围之外。
- **Review**: Limitations 章节

### Q5
- **Category**: conceptual
- **Question**: checkpoint 会保留多长时间？
- **Options**: A) 直到会话结束 | B) 7 天 | C) 30 天 | D) 永久保留
- **Correct**: C
- **Explanation**: checkpoint 会跨会话保留最长 30 天，之后会被自动清理。
- **Review**: Checkpoint persistence 章节

### Q6
- **Category**: practical
- **Question**: 回退时选择 "Summarize from here"（从此处摘要）会做什么？
- **Options**: A) 删除该处之后的对话 | B) 把对话压缩为一份 AI 生成的摘要，同时在完整记录中保留原文 | C) 生成一份变更的要点列表 | D) 把对话导出到文件
- **Correct**: B
- **Explanation**: Summarize 会把对话压缩为一份更短的 AI 生成摘要，完整的原始文本仍会保留在 transcript 文件中。
- **Review**: Summarize option 章节

### Q7
- **Category**: conceptual
- **Question**: checkpoint 会在什么时候自动创建？
- **Options**: A) 每 5 分钟 | B) 每次用户发送 prompt 时 | C) 只有手动保存时 | D) 每次工具调用之后
- **Correct**: B
- **Explanation**: 自动 checkpoint 会在每次用户发送 prompt 时创建，捕获 Claude 处理该请求之前的状态。
- **Review**: Automatic checkpoints 章节

### Q8
- **Category**: practical
- **Question**: 如何关闭自动 checkpoint 创建？
- **Options**: A) 使用 `--no-checkpoints` 参数 | B) 在设置中设置 `autoCheckpoint: false` | C) 删除 checkpoints 目录 | D) checkpoint 无法关闭
- **Correct**: B
- **Explanation**: 在配置中设置 `autoCheckpoint: false` 即可关闭自动 checkpoint 创建（默认值为 true）。
- **Review**: Configuration 章节

### Q9
- **Category**: conceptual
- **Question**: checkpoint 能替代 git commit 吗？
- **Options**: A) 能，它更强大 | B) 不能，两者是互补关系——checkpoint 是会话范围的、会过期，git 是永久的、可分享的 | C) 小项目中可以 | D) 只有单人开发时可以
- **Correct**: B
- **Explanation**: checkpoint 是临时的（保留 30 天）、局限于会话范围，且不能分享。git commit 是永久的、可审计的、可分享的。两者应配合使用。
- **Review**: Integration with git 章节

### Q10
- **Category**: practical
- **Question**: 你想对比两种不同的方案，推荐的 checkpoint 工作流是什么？
- **Options**: A) 创建两个独立会话 | B) 在方案 A 之前打 checkpoint，尝试后回退到该 checkpoint，再尝试方案 B，对比结果 | C) 改用 git 分支 | D) 没有好的对比方式
- **Correct**: B
- **Explanation**: 分支式策略：在干净状态打 checkpoint，尝试方案 A，记录结果，回退到同一个 checkpoint，尝试方案 B，对比两次结果。
- **Review**: Workflow patterns 章节

---

## Lesson 09：Advanced Features

### Q1
- **Category**: conceptual
- **Question**: Claude Code 有哪六种权限模式？
- **Options**: A) read、write、execute、admin、root、sudo | B) default、acceptEdits、plan、auto、dontAsk、bypassPermissions | C) safe、normal、elevated、admin、unrestricted、god | D) view、edit、run、deploy、full、bypass
- **Correct**: B
- **Explanation**: 六种模式分别是：default（对一切都询问）、acceptEdits（自动接受文件编辑）、plan（只读分析）、auto（由后台分类器决定）、dontAsk（除非预先批准，否则自动拒绝）、bypassPermissions（跳过所有检查）。
- **Review**: Permission Modes 章节

### Q2
- **Category**: practical
- **Question**: 如何激活规划模式（planning mode）？
- **Options**: A) 只能通过 `/plan` 命令 | B) 可通过 `/plan`、`Shift+Tab`/`Alt+M`、`--permission-mode plan` 参数，或默认配置激活 | C) 只能通过 `--planning` 参数 | D) 规划模式始终开启
- **Correct**: B
- **Explanation**: 规划模式可以通过多种方式激活：/plan 命令、Shift+Tab/Alt+M 快捷键、--permission-mode plan CLI 参数，或作为配置中的默认值。
- **Review**: Planning Mode 章节

### Q3
- **Category**: conceptual
- **Question**: `opusplan` 这个模型别名做了什么？
- **Options**: A) 全程只使用 Opus | B) 规划阶段使用 Opus，实现阶段使用 Sonnet | C) 使用一个专门为规划优化的模型 | D) 自动开启规划模式
- **Correct**: B
- **Explanation**: `opusplan` 是一个模型别名，规划阶段（更高质量的分析）使用 Opus，执行阶段（更快的实现）使用 Sonnet。
- **Review**: Planning Mode 章节

### Q4
- **Category**: practical
- **Question**: 如何在会话中开启或关闭扩展思考（extended thinking）？
- **Options**: A) 输入 `/effort max` | B) 按 `Option+T`（macOS）或 `Alt+T` | C) 在 prompt 中包含 "ultrathink" | D) 该功能始终开启，无法切换
- **Correct**: B
- **Explanation**: Option+T（macOS）或 Alt+T 会为当前会话开关扩展思考。（`Ctrl+O` 用于切换 verbose 模式，以显示/隐藏推理文本。）如需一次性的深度推理，可在 prompt 中包含 "ultrathink"；如需会话级别的控制，使用 `/effort` 命令。
- **Review**: Extended Thinking 章节

### Q5
- **Category**: conceptual
- **Question**: "ultrathink" 关键词会触发深度推理吗？
- **Options**: A) 会，它会为这一次回复触发深度推理，而不改变会话设置 | B) 不会，它会被当作普通的 prompt 文本处理 | C) 会，但仅限于 Opus 4.6 | D) 会，并且会永久改变 effort 等级
- **Correct**: A
- **Explanation**: 在 prompt 中包含 "ultrathink" 会添加一条上下文内指令，让模型在这一轮多做一些推理。它不会改变发送给 API 的 effort 等级——如需会话级别的深度推理，请使用 `/effort max`。
- **Review**: Extended Thinking 章节

### Q6
- **Category**: practical
- **Question**: 如何在 CI/CD 流水线中运行 Claude，并输出结构化 JSON、限制轮次？
- **Options**: A) `claude --ci --json --limit 3` | B) `claude -p --output-format json --max-turns 3 "review code"` | C) `claude --pipeline --format json` | D) `claude run --json --turns 3`
- **Correct**: B
- **Explanation**: print 模式（`-p`）配合 `--output-format json` 和 `--max-turns` 是标准的 CI/CD 集成方式。
- **Review**: Headless/Print Mode 章节

### Q7
- **Category**: conceptual
- **Question**: Task List 功能（Ctrl+T）提供了什么？
- **Options**: A) 正在运行的后台进程列表 | B) 一份能在上下文压缩后仍然保留、可通过 `CLAUDE_CODE_TASK_LIST_ID` 跨会话共享的持久化待办列表 | C) 过往会话的历史记录 | D) 待处理工具调用的队列
- **Correct**: B
- **Explanation**: Task List（Ctrl+T）在上下文压缩后依然持久保留，并可以通过 `CLAUDE_CODE_TASK_LIST_ID` 指定的命名任务目录跨会话共享。
- **Review**: Task List 章节

### Q8
- **Category**: practical
- **Question**: 在规划模式下，如何在你偏好的外部编辑器中编辑计划？
- **Options**: A) 从终端复制粘贴 | B) 按 `Ctrl+G`，在外部编辑器中打开该计划 | C) 使用 `/export-plan` 命令 | D) 计划无法在外部编辑
- **Correct**: B
- **Explanation**: Ctrl+G 会在你配置好的外部编辑器中打开当前计划以供修改。
- **Review**: Planning Mode 章节

### Q9
- **Category**: conceptual
- **Question**: `dontAsk` 和 `bypassPermissions` 这两种模式有什么区别？
- **Options**: A) 两者相同 | B) `dontAsk` 除非预先批准，否则自动拒绝；`bypassPermissions` 完全跳过所有检查 | C) `dontAsk` 用于文件，`bypassPermissions` 用于命令 | D) `bypassPermissions` 更安全
- **Correct**: B
- **Explanation**: dontAsk 会自动拒绝权限请求，除非匹配预先批准的模式。bypassPermissions 会完全跳过所有安全检查——日常使用中这样做很危险。
- **Review**: Permission Modes 章节

### Q10
- **Category**: practical
- **Question**: 如何把一个 CLI 会话交接给桌面应用？
- **Options**: A) 使用 `/export` 命令 | B) 使用 `/desktop` 命令 | C) 复制会话 ID，粘贴到桌面应用中 | D) 会话无法在 CLI 和桌面应用之间转移
- **Correct**: B
- **Explanation**: `/desktop` 命令会把当前 CLI 会话交接给原生桌面应用，用于可视化 diff 审阅和多会话管理。
- **Review**: Desktop App 章节

---

## Lesson 10：CLI Reference

### Q1
- **Category**: conceptual
- **Question**: Claude CLI 有哪两种主要模式？
- **Options**: A) 在线模式和离线模式 | B) 交互式 REPL（`claude`）和 Print 模式（`claude -p`） | C) GUI 模式和终端模式 | D) 单次模式和批量模式
- **Correct**: B
- **Explanation**: 交互式 REPL 是默认的对话模式。Print 模式（-p）是非交互式的，可脚本化、可管道化——回复一次后就退出。
- **Review**: CLI architecture 章节

### Q2
- **Category**: practical
- **Question**: 如何把一个文件通过管道传给 Claude，并获得 JSON 输出？
- **Options**: A) `claude --file error.log --json` | B) `cat error.log | claude -p --output-format json "explain this"` | C) `claude < error.log --format json` | D) `claude -p --input error.log --json`
- **Correct**: B
- **Explanation**: 通过 stdin 把内容管道传给 print 模式（-p），并使用 --output-format json 获得结构化输出。
- **Review**: Interactive vs Print Mode 章节

### Q3
- **Category**: conceptual
- **Question**: `-c` 和 `-r` 参数有什么区别？
- **Options**: A) 两者作用相同 | B) `-c` 继续最近的会话；`-r` 按名称或 ID 恢复指定会话 | C) `-c` 创建新会话；`-r` 恢复会话 | D) `-c` 用于代码；`-r` 用于审查
- **Correct**: B
- **Explanation**: `-c/--continue` 恢复最近的一次对话。`-r/--resume "name"` 按名称或会话 ID 恢复指定会话。
- **Review**: Session management 章节

### Q4
- **Category**: practical
- **Question**: 如何保证 Claude 输出符合 schema 的 JSON？
- **Options**: A) 只使用 `--output-format json` | B) 使用 `--output-format json --json-schema '{"type":"object",...}'` | C) 使用 `--strict-json` 参数 | D) JSON 输出始终符合 schema
- **Correct**: B
- **Explanation**: 单独使用 `--output-format json` 只能产出尽力而为（best-effort）的 JSON。再加上带有 JSON Schema 定义的 `--json-schema`，才能保证输出符合该 schema。
- **Review**: Output and format 章节

### Q5
- **Category**: conceptual
- **Question**: 哪个参数只在 print 模式（-p）下生效，在交互模式下没有作用？
- **Options**: A) `--model` | B) `--system-prompt-file` | C) `--verbose` | D) `--max-turns`
- **Correct**: B
- **Explanation**: `--system-prompt-file` 会从文件加载 system prompt，但只在 print 模式下生效。交互式会话请使用 `--system-prompt`（内联字符串）。
- **Review**: System prompt flags comparison table

### Q6
- **Category**: practical
- **Question**: 如何限制 Claude 在安全审计中只能使用只读工具？
- **Options**: A) `claude --read-only "audit code"` | B) `claude --permission-mode plan --tools "Read,Grep,Glob" "audit code"` | C) `claude --safe-mode "audit code"` | D) `claude --no-write "audit code"`
- **Correct**: B
- **Explanation**: 把 `--permission-mode plan`（只读分析）和 `--tools`（指定工具的白名单）组合使用，可以限制 Claude 只能进行读取操作。
- **Review**: Tool and permission management 章节

### Q7
- **Category**: conceptual
- **Question**: agent 定义的优先级顺序是怎样的？
- **Options**: A) Project > User > CLI | B) CLI > Project > User | C) User > CLI > Project | D) 三者优先级相同
- **Correct**: B
- **Explanation**: CLI 定义的 agent（--agents 参数）优先级最高，其次是 Project 级别（.claude/agents/），最后是 User 级别（~/.claude/agents/）。
- **Review**: Agents configuration 章节

### Q8
- **Category**: practical
- **Question**: 如何从一个已有会话 fork 出一个分支，尝试不同方案而不影响原始会话？
- **Options**: A) 使用 `/fork` 命令 | B) 使用 `--resume session-name --fork-session "branch name"` | C) 使用 `--clone session-name` | D) 使用 `/branch session-name`
- **Correct**: B
- **Explanation**: `--resume` 配合 `--fork-session` 会从被恢复的会话中创建一个新的独立分支，同时保留原始对话不受影响。
- **Review**: Session management 章节

### Q9
- **Category**: conceptual
- **Question**: 用户已登录时，`claude auth status` 返回什么退出码？
- **Options**: A) 1 | B) 0 | C) 200 | D) 它不返回退出码
- **Correct**: B
- **Explanation**: 已登录时 `claude auth status` 退出码为 0，未登录时为 1。这使得它可以用于 CI/CD 中的身份验证脚本检查。
- **Review**: CLI commands table

### Q10
- **Category**: practical
- **Question**: 如何用 Claude 批量处理多个文件？
- **Options**: A) `claude --batch *.md` | B) 使用 for 循环：`for file in *.md; do claude -p "summarize: $(cat $file)" > ${file%.md}.json; done` | C) `claude -p --files *.md "summarize all"` | D) 不支持批量处理
- **Correct**: B
- **Explanation**: 使用 shell 的 for 循环配合 print 模式，逐个处理文件。每次调用都是独立的，都可以产出结构化输出。
- **Review**: Batch processing 章节
