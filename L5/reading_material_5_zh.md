# 使用 Claude API 的 Skills

## 课程文件

你可以在 <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L5" target="_blank">这里</a> 找到课程的 Notebook 和所有必需的输入文件。

要运行 Notebook，你需要创建一个包含 Anthropic API 密钥的 `.env` 文件（不需要 Claude 订阅）：

`ANTHROPIC_API_KEY="your-key"`

你可以从 <a href="https://platform.claude.com/dashboard" target="_blank">Claude 开发者平台</a> 获取密钥。

**关于成本：** 请注意，运行一次所有 Notebook 单元格将在 API 额度中花费大约 0.67 美元。

如果你不想运行 Notebook，你可以：
- 查看 <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L5/lesson_5.ipynb" target="_blank">带有预运行输出的 Notebook</a>（与视频中显示的完全一致）
- 查看 <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L5/sample_outputs/" target="_blank">生成的示例输出</a>

你也可以在 Claude.ai 中尝试相同的自定义 Skills。

## 注意事项
- 这里是 <a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#pre-installed-libraries" target="_blank">沙箱环境中预安装库的列表</a>
- 流式传输（Streaming）：课程的 Notebook 没有使用 Messages API 实现流式传输。因此，当你运行单元格以获取响应时，可能需要等待几分钟。如果你想实现流式传输，可以查看 <a href="https://platform.claude.com/docs/en/build-with-claude/streaming" target="_blank">文档</a>。
- 要查看更多关于如何在 API 中使用 Agent Skills（如多轮对话）的示例，请务必查看此 <a href="https://platform.claude.com/docs/en/build-with-claude/skills-guide" target="_blank">指南</a>。

## 其他参考资料
- <a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool" target="_blank">代码执行工具 (Code Execution Tool)</a>
- <a href="https://platform.claude.com/docs/en/build-with-claude/files" target="_blank">Files API</a>
- <a href="https://github.com/anthropics/claude-cookbooks/tree/main/skills" target="_blank">Claude Cookbook: Skills</a>
