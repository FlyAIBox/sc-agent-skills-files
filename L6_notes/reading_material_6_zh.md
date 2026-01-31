# Claude Code 中的 Skills

## 课程的代码库和文件

课程文件链接：
- <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L6" target="_blank">课程中使用的代码库</a>
- <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L6/.claude/skills/" target="_blank">课程 Skills 的文件</a>
- <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L6/.claude/agents" target="_blank">Subagent 定义</a>
- <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L6_notes/prompts.md" target="_blank">对话中使用的提示词</a>
- <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L6_notes/clear.py" target="_blank">clear.py</a>

当你首次在终端中运行应用程序时：
- 从 `uv sync` 开始
- 激活虚拟环境：`source .venv/bin/activate`
- 尝试以下命令：
   - `task –help`
   - `task add "write the final report" -p high -d 2025-01-15`
   - `task list`
   - `task done 1`
   - `task list -a`

这是一个待办事项列表 CLI 应用程序的入门代码库。在课程中，我们演示了如何添加编辑和清除命令。你还可以通过添加删除和撤销命令，或更改存储和显示任务的底层逻辑来扩展应用程序。

## Claude Code

如果这是你第一次尝试 Claude Code，你可以查看这些课程：
- <a href="https://www.deeplearning.ai/short-courses/claude-code-a-highly-agentic-coding-assistant/" target="_blank">Claude Code: A Highly Agentic Coding Assistant</a>
- <a href="https://anthropic.skilljar.com/claude-code-in-action" target="_blank">Claude Code in Action</a>

如果你完成了这些课程中的任何一个，并希望看到关于 Claude Code 的高级课程，请向我们反馈你希望我们涵盖的主题。

如果你没有 Anthropic 订阅，你可以选择使用 API 密钥运行 Claude Code。使用 Sonnet 4.5 运行相同的练习花费大约 1.57 美元。

## Claude Code 中的 Skills

在课程中，你看到了如何在项目级别添加 Skills。这里是 Skills 可以存放的其他位置的 <a href="https://code.claude.com/docs/en/skills#where-skills-live" target="_blank">列表</a>。


### 你可以在 Frontmatter 中添加哪些额外字段？

除了 `name` 和 `description`，在 Claude Code 中工作时，你还可以向 Skills 添加其他几个字段，例如 `allowed-tools`、`model`、`disable-model-invocation`、`user-invocable`、`argument-hint`、`context` 和 `agent`。由于这些字段大多是在我们拍摄课程后添加的，因此我们没有机会在视频中介绍它们。你可以在 <a href="https://code.claude.com/docs/en/skills#frontmatter-reference" target="_blank">这里</a> 找到每个字段的描述文档。

### Claude Code 中的 Skills 调用

Claude Code 中的任何 Skill 都可以是被模型调用的（如本课程所示）或被用户调用的。例如，如果你想调用 Skill `adding-cli-command`，你可以输入 `/adding-cli-command`，然后描述要添加什么命令。`disable-model-invocation` 和 `user-invocable` 字段允许你进一步控制此行为，详情见 <a href="https://code.claude.com/docs/en/skills#control-who-invokes-a-skill" target="_blank">此处</a>。

如果你发现 Claude Code 在需要时没有调用预期的 Skill，请确保：
- 你在添加 Skills 后重启了 Claude Code
- 你的 Skill 描述包含足够的细节，以便 Claude 理解何时使用它

你总是可以手动调用 Skill，或明确指示 Claude 使用特定的 Skill。


### Skills 和 Slash Commands 已合并

在作为 Skills 推出之前，Claude Code 有一个名为 Slash 命令的功能。此功能允许你通过在 `.claude` 下的 `commands` 文件夹中保存 Markdown 文件来创建自定义命令。

截至 1 月 23 日，自定义 Slash 命令已合并到 Skills 中。此次合并是因为 `.claude/commands/review.md` 处的文件和 `.claude/skills/review/SKILL.md` 处的 Skill 都会创建 `/review` 命令，并且工作方式相同。但是，Skills 提供了额外的可选功能：用于支持文件的专用目录（可以在 `SKILL.md` 中引用），以及用于控制是你还是 Claude 调用它们的 Frontmatter 选项。

### Subagents 和 Skills

在课程中，你看到了如何创建自定义 Subagents。Claude Code 还包括内置 Subagents，如 `Explore`、`Plan` 和 `General-Purpose` (<a href="https://code.claude.com/docs/en/sub-agents#built-in-subagents" target="_blank">内置 Subagents</a>)。

在 Subagents 中使用 Skills 有两种方法：

- **方法 1**：定义一个使用 Skills 的自定义 Subagent（如课程所示）

    当你创建 Subagent 时，可以使用 `skills` 字段在启动时将 Skill 内容注入 Subagent 的上下文。由于 Subagents 不会从父对话继承 Skills，因此必须显式列出 Skills。当调用 Subagent 时，`SKILL.md` 文件的全部内容都会注入到 Subagent 的上下文中。

    `code-reviewer` Subagent 的定义：
    ```
    ---
    name: code-reviewer
    description: "Review code for quality, security, and convention compliance. Use when user asks to review, check, or verify code"
    tools: Bash, Glob, Grep, Read
    model: inherit
    color: purple
    skills: reviewing-cli-command
    ---
    ```

    在这种情况下，`reviewing-cli-command` Skill 对你的主 Agent 和 Subagent 都可用。Skill 可以在需要时加载到主 Agent 的上下文中，或者在调用 Subagent 时指导 `code-reviewer` Subagent。

    你还可以为你的 `code-reviewer` Subagent 列出多个 Skill。例如，你可以添加另一个 Skill 来审查用不同语言或框架编写的 CLI 命令。你还可以添加一个审查 SQL 查询的 Skill（如果你希望应用程序的任务存储在数据库中而不是本地 JSON 文件中）。

- **方法 2**：在 Subagent 中运行 Skills（课程中未展示）

    如果你希望 Skill 始终在隔离的上下文中运行，则需要在 Skill 的 Frontmatter 中使用 `context: fork` 字段。当 Skill 运行时，默认情况下，内置的 `general-purpose` Subagent 接收 Skill 内容作为其提示词或任务，按照 Skill 的指示在隔离的上下文中运行，然后返回结果。如果你希望特定的 Subagent（内置或自定义）与 Skill 一起使用，则需要在 Skill 的 Frontmatter 中指定 `agent` 字段。

    例如，这里是一个示例 `SKILL.md` 文件：
    ```
    ---
    name: deep-research
    description: Research a topic thoroughly
    context: fork
    agent: Explore
    ---

    Research $ARGUMENTS thoroughly:

    1. Find relevant files using Glob and Grep
    2. Read and analyze the code
    3. Summarize findings with specific file references
    ```

    参考资料：<a href="https://code.claude.com/docs/en/skills#run-skills-in-a-subagent" target="_blank">在 Subagent 中运行 Skills</a>


## 参考资料

- 有关如何在 Claude Code 中使用 Skills 的更全面指南，请查看此 <a href="https://code.claude.com/docs/en/skills" target="_blank">文档</a>。

- 要了解更多关于 Claude Code 中 Subagents 的信息，请查看此 <a href="https://code.claude.com/docs/en/sub-agents" target="_blank">指南</a>。

- <a href="https://code.claude.com/docs/en/skills#troubleshooting" target="_blank">故障排除指南</a>。
