# CLAUDE.md

教程仓库。产出是编号模块 `01-` 到 `10-` 下的 Markdown 文档，而不是一个应用程序。`scripts/` 下的脚本仅用于校验文档和构建 EPUB。

另请参阅 `.claude/CLAUDE.md` 了解技术栈和常用命令，以及 `STYLE_GUIDE.md` 了解课程结构规范。

## 关键命令

```bash
# 质量门禁（也会在提交时通过 pre-commit hooks 自动运行）
pre-commit run --all-files

# 测试
pytest scripts/tests/ -v

# 构建 EPUB（调用 Kroki.io API 渲染 Mermaid，需要联网）
uv run scripts/build_epub.py

# Python 工具链
ruff check scripts/ && ruff format scripts/
mypy scripts/ --ignore-missing-imports
bandit -c scripts/pyproject.toml -r scripts/ --exclude scripts/tests/
```

Pre-commit 会运行 5 项检查：markdown-lint、cross-references、mermaid-syntax、link-check、build-epub（在 `.md` 文件变更时触发）。全部必须通过。

## 架构地图

- `01-` … `10-` —— 教程模块。**编号前缀代表学习顺序**，不是字母顺序。不要重新编排。
- 每个模块：`README.md` + 可直接复制使用的模板（`.md`、`.json`、`.sh`）。
- `scripts/` —— 工具脚本（EPUB 构建器、链接/Mermaid/交叉引用校验器）。不是产品本身。
- `02-memory/*.md` —— 用户可复制到自己项目中的 CLAUDE.md 模板。不要与本文件混淆。
- `openspec/` —— 基于规范驱动的变更提案。

## 硬性规则

- **未经用户明确要求，禁止提交（commit）或推送（push）。**
- **禁止在任何提交信息中添加 `Co-Authored-By: Claude`。**
- 运行 Python 脚本前务必先激活 `.venv`（检查 `venv/`、`.venv/`、`env/`）。
- 内部链接使用**相对路径**（例如 `01-slash-commands/README.md`）；锚点使用 `#heading-name`。
- 代码块**必须**声明语言（`bash`、`python`、`json` 等）——否则交叉引用检查会失败。
- 外部 URL 必须可访问且保持稳定，不使用临时性链接。
- Mermaid 图表必须能被解析（pre-commit 会校验）。EPUB 构建失败通常是因为 Mermaid 语法错误，或无法连接 Kroki。
- 提交信息格式：`type(scope): subject`，其中 `scope` 对应模块目录名（例如 `feat(slash-commands):`、`docs(memory):`、`fix(README):`）。
- 不要重新编排 `01-`–`10-` 的编号顺序，这个顺序就是课程大纲。

## 工作流偏好

- 修改课程内容时，遵循 `STYLE_GUIDE.md` 中关于结构、命名、图表的规范。
- 小修改 → 最小化 diff。不要为了修一个错别字而重写整节内容。
- 新增模块页面时：先写 README + 模板，再更新根目录 `README.md` 索引，如顺序或课时有变化，也要更新 `LEARNING-ROADMAP.md`。
- 教程优先于库：优先追求清晰的讲解和可直接复制运行的示例，而非可复用的抽象。
- 如果质量检查失败，修复根本问题，不要用 `--no-verify` 绕过。

## Token 效率

- 不要重复读取你刚写入或编辑过的文件，你已经知道其内容。
- 除非结果不确定，否则不要重复运行命令去"验证"。
- 除非用户要求，否则不要把大段代码或文件内容原样回显出来。
- 把相关的编辑合并为一次操作，不要用 5 次编辑做 1 次就能完成的事。
- 跳过"我继续了…"之类的确认语句，直接执行。
- 如果一个任务只需要 1 次工具调用，就不要用 3 次。先规划，再动手。
- 除非结果存在歧义或还需要用户提供更多信息，否则不要总结你刚做了什么。
