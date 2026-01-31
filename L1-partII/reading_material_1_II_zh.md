# 为什么需要 Agent Skills？- 第二部分

## 幻灯片摘要

### 什么是 Agent Skills？

Agent Skills 是一种轻量级、开放的格式，用于扩展 AI Agent 的能力。Skill 是一个包含指令、脚本、资产和资源的文件夹，Agent 可以通过发现这些 Skill 来准确执行特定任务。

### 我们过去如何看待 Agent

- 专用 Agent：研究 Agent、编程 Agent、金融 Agent、营销 Agent
- 每个 Agent 都有自己狭窄的关注点、自己的脚手架（scaffolding）和特定的工具

### 新范式

- **通用 Agent** 使用代码作为通用接口
- 简单的脚手架：bash 和文件系统
- 但它们需要**上下文和领域专业知识**才能可靠地完成工作
- Skills 提供程序性知识和公司/团队/用户特定的上下文，Agent 可以按需加载

### Skills 能赋能什么

| 类别 | 示例 |
|----------|----------|
| **领域专业知识** | 品牌指南和模板、法律审查流程、数据分析方法论 |
| **可重复的工作流** | 每周营销活动审查、客户通话准备工作流、季度业务审查 |
| **新能力** | 创建演示文稿、生成 Excel 表格或 PDF 报告、构建 MCP 服务器 |

### 如果没有 Skills

- 每次都要描述你的指令和要求
- 每次都要打包所有的参考资料和支持文件
- 手动确保工作流或输出始终一致

### Skills 的关键特征

1. **可移植：** 你可以在不同的兼容 Skill 的 Agent 之间重用同一个 Skill：
    - Claude Code
    - Claude.ai
    - Claude Agent SDK
    - Claude API

    Agent Skills 现在是一个**开放标准**，正被越来越多的 Agent 产品采用。

2. **可组合：** Skills 可以组合起来构建复杂的工作流。例如：
    - **公司品牌 Skill**：提供品牌指南（字体、颜色、Logo）
    - **PowerPoint Skill**：创建幻灯片
    - **BigQuery Skill**：提供营销相关的 Schema
    - **营销活动分析 Skill**：分析营销数据

### Skills 如何工作？- 渐进式披露

Skills 可能包含大量信息，你可能有数百个 Skill。为了保护上下文窗口，Skills 是**渐进式披露**的：

| 层级 | 何时加载 |
|-------|-------------|
| **元数据** (YAML frontmatter: 名称, 描述) | 始终加载 |
| **指令** (主 SKILL.md 内容) | 触发时加载 |
| **资源** (参考文件, 脚本) | 按需加载 |

### Skill 结构示例

根据 Agent Skills 规范：
- SKILL.md 是必需的
- 可选目录：references, scripts, 和 assets

由于一些 Skill 是在 Agent Skills 成为开放标准之前开发的，你会看到有些 Skill（如下面的 PDF Skill）并未严格遵循标准格式。
```
analyzing-marketing-campaign/
├── SKILL.md
└── references/
    └── budget_reallocation_rules.md
```
```
pdf/
├── SKILL.md
├── forms.md
├── reference.md
└── scripts/
    ├── check_fillable_fields.py
    ├── convert_pdf_to_images.py
    ├── extract_form_field_info.py
    └── fill_pdf_form_with_annotations.py
```
```
designing-newsletters/
├── SKILL.md
├── references/
│   └── style-guide.md
└── assets/
    ├── header.png
    ├── icons/
    └── templates/
        ├── newsletter.html
        └── layout.docx
```

## 参考资料

- <a href="https://agentskills.io/what-are-skills" target="_blank">什么是 Skills?</a>
- <a href="https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#how-skills-work" target="_blank">Skills 如何工作</a>
- <a href="https://www.youtube.com/watch?v=CEvIs9y1uog" target="_blank">Barry Zhang & Mahesh Murag 在 AI 工程师博览会上的演讲</a>
