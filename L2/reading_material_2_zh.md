# Skills 与 Tools、MCP 和 Subagents 的对比

## 幻灯片摘要

### Skills vs MCP

| 特性 | MCP | Skills |
|--------|-----|--------|
| **目的** | 将你的 Agent 连接到外部系统和数据（数据库、API、服务） | 教你的 Agent 如何使用这些数据 |
| **示例** | MCP 服务器连接到数据库 | Skill 指示“使用该表的 A 列和 B 列计算指标 X” |

MCP 提供*访问权限*，Skills 提供*专业知识*。


### Skills vs Tools

| 特性 | Tools | Skills |
|--------|-------|--------|
| **目的** | 为 Agent 提供完成任务的基本能力 | 用专业知识扩展 Agent 的能力 |
| **上下文** | Tool 定义（名称、描述、参数）始终存在于上下文窗口中 | Skills 根据需要动态加载 |
| **灵活性** | 固定的能力集 | Skills 可以包含脚本作为 Tool，在需要时使用（“按需工具”） |



### Skills vs Subagents

| 特性 | Subagents | Skills |
|--------|-----------|--------|
| **目的** | 拥有自己独立的上下文和 Tool 权限 | 为主 Agent 或其任何 Subagent 提供专业知识 |
| **操作** | Agent 将任务委派给专门的 Subagent，Subagent 独立工作（可能并行）并返回结果 | Skills 告知工作应如何完成 |
| **示例** | 代码审查员 Subagent | 特定语言或框架的最佳实践 Skill |

Skills 可以用专业知识同时增强主 Agent *和* 其 Subagents。



### 融会贯通

**示例：客户洞察分析器**

| 组件 | 角色 |
|-----------|------|
| **Skill** | 关于如何分类反馈以及如何总结发现的指南 |
| **MCP Server** | Google Drive MCP 服务器，用于访问包含客户访谈记录和调查回复的 Drive 文件夹 |
| **Subagents** | 访谈分析器、调查分析器 |





## 参考资料
* <a href="https://www.claude.com/blog/skills-explained" target="_blank">Skills 详解</a>
* <a href="https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills" target="_blank">教 Claude 使用 Skills 掌握你的工作方式</a>
