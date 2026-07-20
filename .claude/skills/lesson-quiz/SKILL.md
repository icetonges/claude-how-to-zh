---
name: lesson-quiz
description: "针对 Claude Code 教程中的某一节课（01-10）对学习者进行测验，10 道题，评分并标出薄弱环节。可在学习课程之前、期间或之后使用。不要用于整个教程的综合评估，也不要用于讲解某个主题而非测验。"
effort: high
metadata:
  version: 1.1.0
  author: Luong NGUYEN
---

# Lesson Quiz（课程测验）

针对某一节 Claude Code 课程的互动测验，8-10 道题检验理解程度，逐题给出反馈，并指出需要复习的地方。

## 前置条件

本技能需要：

- 已检出（checked out）教程仓库，使得课程目录 `01-slash-commands/` … `10-cli/` 及其各自的 `README.md` 可读取。
- 本技能目录下存在 `references/question-bank.md`（所有题目的来源）。

开始前，先确认目标课程的 `README.md` 存在。如果缺失，不要编造题目——应提醒用户并请他们检查仓库结构（见「边界情况与错误处理」）。

**护栏（Guardrails）：**

- **绝不臆造题目或答案。** 只能从 `references/question-bank.md` 中提取所选课程对应的题目；如果题库中没有该课程的条目，应如实告知，而不是自己编。
- **准确评分。** 对每道题都要记录打乱顺序后正确答案所在的位置，并据此校验每个作答——绝不能靠猜测给分。
- **评分前先确认测验时机。** 课前 / 课中 / 课后的选择会影响结果的呈现方式，不要跳过这一步。

## 操作步骤

### 步骤 1：确定课程

如果用户以参数形式提供了课程（例如 `/lesson-quiz hooks` 或 `/lesson-quiz 03`），将其映射到对应的课程目录：

**课程映射：**
- `01`、`slash-commands`、`commands` → 01-slash-commands
- `02`、`memory` → 02-memory
- `03`、`skills` → 03-skills
- `04`、`subagents`、`agents` → 04-subagents
- `05`、`mcp` → 05-mcp
- `06`、`hooks` → 06-hooks
- `07`、`plugins` → 07-plugins
- `08`、`checkpoints`、`checkpoint` → 08-checkpoints
- `09`、`advanced`、`advanced-features` → 09-advanced-features
- `10`、`cli` → 10-cli

如果没有提供参数，使用 AskUserQuestion 呈现选择：

**问题 1**（header："Lesson"）：
"你想测验哪节课？"
选项：
1. "Slash Commands (01)" —— 自定义命令、skill、frontmatter、参数
2. "Memory (02)" —— CLAUDE.md、记忆层级、规则、Auto Memory
3. "Skills (03)" —— 渐进式披露、自动触发、SKILL.md
4. "Subagents (04)" —— 任务委派、agent 配置、隔离性

**问题 2**（header："Lesson"）：
"你想测验哪节课？（续）"
选项：
1. "MCP (05)" —— 外部集成、传输协议、server、工具搜索
2. "Hooks (06)" —— 事件自动化、PreToolUse、退出码、JSON 输入输出
3. "Plugins (07)" —— 打包解决方案、marketplace、plugin.json
4. "More lessons..." —— Checkpoints、Advanced Features、CLI

如果选择了 "More lessons..."，则呈现：

**问题 3**（header："Lesson"）：
"选择你要测验的课程："
选项：
1. "Checkpoints (08)" —— 回溯、恢复、安全实验
2. "Advanced Features (09)" —— 规划模式、权限、print 模式、思考模式
3. "CLI Reference (10)" —— 命令行参数、输出格式、脚本化、管道

### 步骤 2：阅读课程内容

阅读课程的 README.md 文件以刷新上下文：
- 读取文件：`<lesson-directory>/README.md`

然后使用 `references/question-bank.md` 中该课程对应的题库（10 道预先写好的题目，含答案与解释）。为控制上下文预算，只读取所选的那一节课的 README——不要读全部十节。

### 步骤 3：呈现测验

询问用户本次测验的时机背景：

使用 AskUserQuestion（header："Timing"）：
"你是在什么时候进行这次测验的？"
选项：
1. "Before (pre-test)" —— 我还没读这节课，想测一下已有的知识水平
2. "During (progress check)" —— 我正在学这节课，学到一半
3. "After (mastery check)" —— 我已经学完这节课，想确认自己是否掌握了

这个时机背景会影响结果的呈现方式（见步骤 5）。

### 步骤 4：分轮呈现题目

将题库中的 10 道题分 5 轮呈现，每轮 2 道题。每道题都通过一次 AskUserQuestion 调用，附带题目文本和 3-4 个答案选项。

**重要**：每次 AskUserQuestion 调用最多 4 个选项，每轮 2 道题。

每一轮呈现 2 道题。用户回答完每一轮后，立即展示逐题反馈：每道题是否答对，如果答错则展示正确答案和简要解释。然后进入下一轮。5 轮全部结束后，进行最终评分。

**每轮的题目格式：**

题库中的每道题包含：
- `question`：题目文本
- `options`：3-4 个答案选项（其中一个为正确答案，在题库中已标注）
- `correct`：正确答案的标签
- `explanation`：为什么该答案是正确的
- `category`："conceptual"（概念）或 "practical"（实操）

**关键——打乱答案选项顺序**：对每道题，你**必须**在通过 AskUserQuestion 呈现之前随机打乱答案选项的顺序。不要按题库中原有的顺序（A、B、C、D）呈现，也不要把正确答案放在第一位。每道题使用不同的随机排列方式。要记录打乱后正确答案所在的位置，以便准确评分。

示例：如果题库中列出的选项是 A（正确）、B、C、D——你呈现时可能是：C、A、D、B。这时正确答案就在第 2 个位置。

通过 AskUserQuestion 呈现每道题，并记录用户对每道题的作答。

### 步骤 5：评分并呈现结果

所有轮次结束后，计算分数并呈现结果。

**评分方式：**
- 每答对一题 = 1 分
- 满分 = 10 分

**等级划分：**
- 9-10 分：精通（Mastered）—— 理解非常出色
- 7-8 分：熟练（Proficient）—— 掌握良好，有少量疏漏
- 5-6 分：发展中（Developing）—— 基础已理解，需要复习
- 3-4 分：入门（Beginning）—— 存在明显差距，建议复习
- 0-2 分：尚未掌握（Not yet）—— 建议从这节课开头重新学习

**输出格式：** 遵循 `references/results-template.md` 中的报告模板。该模板定义了分数行、逐题结果表格、"答错的题目——请复习" 板块、按时机区分的提示信息，以及 "建议的后续步骤" 板块。用本次测验的数据填充其中带方括号的占位符。

### 步骤 6：提供后续选项

呈现结果后，使用 AskUserQuestion：

"接下来你想做什么？"
选项：
1. "Retake this quiz" —— 重新测验同一节课
2. "Quiz another lesson" —— 切换到另一节课测验
3. "Explain a topic I missed" —— 详细讲解一道你答错的题目
4. "Done" —— 结束本次测验

如果选择**重新测验（Retake）**：回到步骤 4（跳过时机问题，沿用相同的时机设定）。
如果选择**测验另一节课（Quiz another lesson）**：回到步骤 1。
如果选择**讲解某个主题（Explain a topic）**：询问是第几题，然后阅读课程 README.md 中对应的章节并结合示例进行讲解。

## 验收标准

一次完整的测验流程必须满足以下全部条件——在呈现最终结果前逐项核对：

- 在提出任何问题之前，已确定唯一一节课程（01-10）。
- 已通过 AskUserQuestion 采集了时机背景（课前 / 课中 / 课后）。
- 已呈现该课程 `references/question-bank.md` 中的 10 道题，分 5 轮、每轮 2 题，且每题的答案选项都经过打乱。
- 每个作答都已对照记录下来的正确位置进行评分，最终得出一个 0-10 的整数分数。
- **预期输出**：一份 `## Lesson Quiz Results` 报告，包含分数行（`Score: N/10` 并附等级标签）、逐题结果表格、每道错题对应的 "答错的题目——请复习" 板块，以及一条按时机定制的提示信息。
- 已提供后续选项提示（重测 / 换课 / 讲解 / 结束）。

示例：对 Hooks 这节课进行的一次 "课后"（after）测验得了 7/10 分，报告中应写明 `Score: 7/10 — Proficient`，列出结果表格中的全部 10 行，并对答错的 3 道题展开说明，给出正确答案、解释与复习指引。

## 边界情况与错误处理

### 无效的课程参数
如果参数不匹配任何课程，展示有效的课程列表并让用户选择。

### 用户想在测验中途退出
如果用户在任意一轮中表示想要停止，展示已作答题目的部分结果（按已作答题数计分，而非按 10 分计）。

### 找不到课程 README
如果对应路径下的 README.md 文件不存在，告知用户并建议其检查仓库结构。不要用编造的内容继续进行。

### 题库中缺少该课程的题目
如果 `references/question-bank.md` 中没有已解析课程对应的题目，告知用户并停止——绝不能为了填补空缺而臆造题目。

## 验证

### 触发测试集

**应当触发：**
- "quiz me on hooks"
- "lesson quiz"
- "test my knowledge of lesson 3"
- "practice quiz for MCP"
- "do I understand skills"
- "quiz me on slash commands"
- "lesson-quiz 06"
- "test me on checkpoints"
- "how well do I know the CLI"
- "quiz me before I start the memory lesson"

**不应触发：**
- "assess my overall level"（应使用 /self-assessment）
- "explain hooks to me"
- "create a hook"
- "what is MCP"
- "review my code"
