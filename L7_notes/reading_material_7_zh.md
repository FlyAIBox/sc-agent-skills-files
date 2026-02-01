# Claude Agent SDK 技能

## 课程文件

你可以在 <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L7" target="_blank">这里</a> 找到 L7 的所有文件，与视频中显示的有一些不同：
- 每个子智能体使用 `haiku` 作为模型
- 指定了要使用的确切 MCP 工具列表

以下是一些值得探索的关键文件：
- <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L7/prompts" target="_blank">主智能体和子智能体的系统提示词</a>
- <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L7/.claude/skills/learning-a-tool/" target="_blank">`learning-a-tool` 技能的相关文件</a>
- <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L7/utils.py" target="_blank">utils.py</a> (消息格式化)
- <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L7/agent.py" target="_blank">agent.py</a>
- <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L7_notes/learning-mineru/" target="_blank">录制期间生成的学习指南</a>

要运行智能体，请按照 <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L7/README.md" target="_blank">README 文件</a> 中的说明进行操作。你需要一个 Anthropic API 密钥（无需订阅）。

**关于成本：** 如果使用 `haiku` 作为子智能体模型（并使用 `sonnet` 作为主智能体），运行具有相同请求的智能体大约花费 $3.43 API 额度，如果子智能体也使用 `sonnet`，则大约花费 $6.35。

### 课程中使用的提示词

**步骤 1:** 开始研究过程
```
Help me get started with MinerU. Create a learning guide. Show me your plan first.
```
（译文：帮助我开始学习 MinerU。创建一个学习指南。先给我看看你的计划。）

**注意：** 智能体可能需要大约 15 分钟才能完成。如果你想要更快的研究或更简单的学习指南，可以随时更新技能的说明和智能体定义。

**步骤 2:** 审查并批准计划

你可以同意该计划或提供反馈和建议。

**步骤 3（可选）:** 导出到 Notion

如果你想尝试与 Notion 的 MCP 集成：
```
Write ./learning-mineru/resources.md to the "Resources" subpage under Learning in Notion. The subpage already exists. Use rich formatting. For Notion MCP: You can use the full range of Notion block types for proper formatting.
```
（译文：将 ./learning-mineru/resources.md 写入 Notion 中 Learning 下的 "Resources" 子页面。子页面已存在。使用富文本格式。对于 Notion MCP：你可以使用各种 Notion 块类型来进行正确的格式化。）

**注意：** 在课程中使用的 Notion 账户中，我们创建了一个名为 `Learning` 的页面，其中包含一个名为 `Resources` 的子页面。

## 更多高级选项

- <a href="https://platform.claude.com/docs/en/agent-sdk/python#example-advanced-permission-control" target="_blank">高级权限控制</a>
- <a href="https://platform.claude.com/docs/en/agent-sdk/python#building-a-continuous-conversation-interface" target="_blank">构建连续对话界面</a> (中断、新对话、退出)

## 参考资料

- <a href="https://platform.claude.com/docs/en/agent-sdk/overview" target="_blank">Claude Agent SDK 文档</a>
- <a href="https://platform.claude.com/docs/en/agent-sdk/python" target="_blank">Python Agent SDK</a>
- <a href="https://platform.claude.com/docs/en/agent-sdk/skills" target="_blank">SDK 中的 Agent 技能</a>
- <a href="https://github.com/anthropics/claude-agent-sdk-demos" target="_blank">Claude Agent SDK 演示</a>
