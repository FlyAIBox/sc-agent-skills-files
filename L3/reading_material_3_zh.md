# 探索预构建的 Skills

## 预构建的 Skills

* <a href="https://github.com/anthropics/skills/tree/main/skills" target="_blank">Anthropic Skills 列表</a>
* <a href="https://github.com/anthropics/skills/tree/main/skills/pptx" target="_blank">pptx</a>
* <a href="https://github.com/anthropics/skills/tree/main/skills/skill-creator" target="_blank">Skill creator</a>

## 第 1 部分：更新 Marketing Skill

在视频中，我们更新了 Marketing Skill，使其使用 BigQuery MCP Server 从 BigQuery 表中获取数据，而不是要求提供 CSV 文件：

- <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L3/prompts.md#part-1-updating-the-marketing-skill" target="_blank">第 1 部分中使用的提示词</a>
- <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L3/updated_marketing_skill/analyzing-marketing-campaign/" target="_blank">拍摄期间获得的 Marketing Skill 更新后文件</a>

你可以设置一个 BigQuery 表来尝试这一部分（说明链接如下），或者你可以设置一个本地数据库作为替代。例如，你可以设置一个本地 SQLite 数据库，将此 <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L3/campaign_performance_4weeks.csv" target="_blank">CSV 文件</a> 导入数据库，并使用此 <a href="https://github.com/modelcontextprotocol/servers-archived/tree/main/src/sqlite" target="_blank">MCP Server</a>。或者你可以完全跳过这一部分。

- 选做：<a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L3/additional_references/table_setup.md#bigquery-setup" target="_blank">设置 BigQuery 表的说明</a>
- 选做替代方案：<a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L3/additional_references/table_setup.md#sqlite-setup" target="_blank">设置 SQLite 表的说明</a>

**注意**：由于 BigQuery MCP Server 是一个本地 MCP Server，我们使用了 Claude Desktop（而不是 Claude.ai）。在 Claude.ai 上，你只能使用远程 MCP Server。

## 第 2 部分：创建 Brand Guidelines Skill

- <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L3/brand_guidelines_files/" target="_blank">品牌指南文件</a>
- <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L3/prompts.md#part-2--creating-the-brand-guideline-skill" target="_blank">第 2 部分中使用的提示词</a>
- <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L3/brand_guidelines_skill/craftedwell-brand/" target="_blank">拍摄期间获得的 Skill 文件</a>

## 第 3 部分：实现整个工作流

- <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L3/prompts.md#part-3-implementing-the-entire-workflow" target="_blank">第 3 部分中使用的提示词</a>
- <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L3/output_report_example/CraftedWell_Weekly_Report_Dec16-22.pptx" target="_blank">拍摄期间获得的幻灯片</a>

幻灯片生成可能需要几分钟时间，而且它们看起来可能与视频中的完全不同。
