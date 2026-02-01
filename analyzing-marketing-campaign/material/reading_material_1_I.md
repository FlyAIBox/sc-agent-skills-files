以下是该内容的中文翻译，保持了专业性和严谨性：

# 为什么选择 Agent Skills？- 第一部分 (Part I)

## 课程文件 (Lesson Files)

**初始对话 (Initial Conversation)：** 以下是初始对话中使用的提示词和文件：

* <a href="[https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L1-partI/prompts_initial_conversation.md](https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L1-partI/prompts_initial_conversation.md)" target="_blank">提示词 (prompts)</a>
* <a href="[https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L1-partI/campaign_data_week1.csv](https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L1-partI/campaign_data_week1.csv)" target="_blank">CSV 文件</a>
* <a href="[https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L1-partI/budget_reallocation_rules.md](https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L1-partI/budget_reallocation_rules.md)" target="_blank">预算重新分配规则</a>

**技能文件 (Skill Files)：** 您可以在<a href="[https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L1-partI/skill/analyzing-marketing-campaign/](https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L1-partI/skill/analyzing-marketing-campaign/)" target="_blank">此处</a>找到 `analyzing-marketing-campaign`（营销活动分析）技能的相关文件。

**上传技能后的对话：**

* <a href="[https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L1-partI/prompts_with_skills.md](https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L1-partI/prompts_with_skills.md)" target="_blank">提示词 (prompts)</a>
* <a href="[https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L1-partI/campaign_data_week1.csv](https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L1-partI/campaign_data_week1.csv)" target="_blank">CSV 文件</a>
* <a href="[https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L1-partI/output_report_example/Marketing_Campaign_Report_Dec9-15.xlsx](https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L1-partI/output_report_example/Marketing_Campaign_Report_Dec9-15.xlsx)" target="_blank">录制期间生成的 Excel 报告</a>

## 如何尝试 Skills？

如果您没有订阅 Claude，您仍然可以通过免费计划（使用 Sonnet 4.5 或 Haiku 4.5）在 Claude.ai 中尝试该技能。截至 1 月 26 日，Claude.ai 的免费用户已可以使用 Skills 功能。

由于 Skills 是一种开放标准，您也可以在任何其他兼容 Skills 的 AI 应用程序中进行尝试。您可以在<a href="[https://agentskills.io/home#adoption](https://agentskills.io/home#adoption)" target="_blank">此处</a>找到支持该标准的平台列表。

## 如何扩展 `analyzing-marketing-campaign` 技能？

您可以添加以下内容：

* 关于如何分析和修复数据质量问题的参考文件
* 包含您可能有兴趣计算的所有营销指标的参考文件
* 利用现有数据可进行的额外分析
* 当未提供 CSV 文件时，从数据库查询数据的说明指令

我们也邀请您思考自己的工作流程：

* 是否有您反复要求智能体 (Agent) 遵循的指令？
* 您是否考虑将这些指令整合为一个技能？
* 对于特定任务，是否有您希望智能体始终遵循的特定准则？

**注意**：本课程中展示的所有技能仅供教学使用。每个展示的技能都有进一步增强和迭代的空间。

## 参考资料 (References)

* <a href="[https://agentskills.io/home](https://agentskills.io/home)" target="_blank">Agent Skills</a>
* <a href="[https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)" target="_blank">Agent Skills Anthropic 文档</a>
* <a href="[https://claude.com/blog/skills](https://claude.com/blog/skills)" target="_blank">博客：Agent Skills 介绍</a>