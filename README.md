# AI Agent Skills 课程材料

[![Claude AI](https://img.shields.io/badge/Claude-AI-blue)](https://claude.ai)
[![Python](https://img.shields.io/badge/Python-3.8+-green)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Educational-orange)](LICENSE)

## 项目概述

本仓库为 **AI Agent Skills** 系列课程的完整学习资料库，包含从基础概念到高级应用的全套教学内容。课程主要聚焦于 Claude AI 的 Agent Skills 技术体系，涵盖理论讲解、代码示例、实战项目和最佳实践。

**Agent Skills** 是一种开放标准，允许开发者为 AI 代理定义可复用的专业技能模块，使其能够高效执行特定领域的复杂任务。本课程通过系统化的学习路径，帮助开发者掌握 Agent Skills 的设计、开发和部署方法。

## 核心特性

- 📚 **系统化课程体系**：从基础到高级，循序渐进的7个课程模块
- 💻 **实战驱动**：每个课程包含完整的代码示例和实际应用场景
- 🎯 **技能导向**：涵盖营销分析、任务管理、文档研究等多个实用领域
- 🔧 **工具集成**：支持 Claude.ai、Claude Desktop、Claude API 和 Claude Agent SDK
- 🌐 **开放标准**：所有技能遵循开放标准，可在任何兼容的 AI 应用中使用

## 技术栈

### 核心技术
- **AI 平台**：Claude AI (Sonnet 4.5, Haiku 4.5)
- **开发语言**：Python 3.8+, JavaScript
- **框架与工具**：
  - Claude Agent SDK
  - Model Context Protocol (MCP)
  - Notion API
  - MinerU (文档处理)

### 开发工具
- **包管理器**：uv (Python)
- **测试框架**：pytest
- **数据处理**：pandas, numpy
- **可视化**：matplotlib, seaborn

## 项目结构

```
sc-agent-skills-files/
│
├── course_materials.md          # 课程材料总览
│
├── L1-partI/                    # 第一课（上）：Agent Skills 简介
│   ├── skill/                   # 技能定义文件
│   │   └── analyzing-marketing-campaign/
│   ├── campaign_data_week1.csv  # 示例数据
│   ├── budget_reallocation_rules.md
│   └── reading_material_1_I.md  # 阅读材料
│
├── L1-partII/                   # 第一课（下）：Agent Skills 深入
│   ├── skill/
│   └── reading_material_1_II.md
│
├── L2/                          # 第二课：技能结构与设计
│   └── reading_material_2.md
│
├── L3/                          # 第三课：提示词工程
│   └── [课程材料]
│
├── L4/                          # 第四课：自定义技能开发
│   └── custom_skills/
│       └── analyzing-time-series/
│           └── scripts/         # Python 工具脚本
│
├── L5/                          # 第五课：高级技能实现
│   ├── custom_skills/
│   ├── data/                    # 示例数据集
│   ├── lesson_5.ipynb           # Jupyter Notebook 教程
│   └── reading_material_5.md
│
├── L6/                          # 第六课：任务管理 CLI 项目
│   ├── src/
│   │   └── task/                # 任务管理核心模块
│   ├── tests/                   # 单元测试
│   ├── pyproject.toml
│   └── README.md
│
├── L7/                          # 第七课：多代理系统
│   ├── agent.py                 # 代理实现
│   ├── main.py                  # 主程序入口
│   ├── utils.py                 # 工具函数
│   ├── prompts/                 # 提示词模板
│   ├── pyproject.toml
│   └── README.md
│
├── L6_notes/                    # 第六课补充资料
└── L7_notes/                    # 第七课补充资料
    └── learning-mineru/         # MinerU 学习资料
        └── code-examples/
```

## 课程内容详解

### L1: 为什么需要 Agent Skills？

**课程目标**：理解 Agent Skills 的价值和应用场景

#### Part I - 基础概念
- Agent Skills 的设计理念
- 技能定义的标准格式
- 实战案例：营销活动分析技能
  - 多渠道数据分析
  - 漏斗指标计算（CTR、CVR）
  - 效率指标评估（ROAS、CPA、净利润）
  - 基于规则的预算重新分配

#### Part II - 深入探讨
- 技能的模块化设计
- 上下文与参考文件管理
- 技能的版本控制与迭代

**关键文件**：
- `skill/analyzing-marketing-campaign/SKILL.md` - 技能定义
- `budget_reallocation_rules.md` - 业务规则文档

---

### L2: 技能的结构与组成

**课程目标**：掌握技能文件的标准结构

**核心内容**：
- 技能清单（Skill Manifest）
- 指令（Instructions）
- 参考文件（References）
- 最佳实践与设计模式

---

### L3: 提示词工程与技能优化

**课程目标**：学习如何编写高效的技能指令

**核心内容**：
- 提示词设计原则
- 上下文管理策略
- 技能调试与测试方法

---

### L4: 自定义技能开发

**课程目标**：从零开发专属技能

**实战项目**：时间序列分析技能
- 数据可视化工具 (`visualize.py`)
- 异常诊断脚本 (`diagnose.py`)
- 时间序列工具库 (`ts_utils.py`)

**应用场景**：
- 金融数据分析
- 业务指标监控
- 趋势预测与异常检测

---

### L5: 高级技能实现

**课程目标**：掌握复杂技能的设计与实现

**核心内容**：
- 多步骤任务编排
- 外部 API 集成
- 数据持久化与状态管理
- Jupyter Notebook 交互式教程

---

### L6: 实战项目 - 任务管理 CLI

**项目简介**：基于 Python 的命令行任务管理工具

**功能特性**：
- ✅ 任务增删改查
- 🎯 优先级管理（低/中/高）
- 📅 截止日期设置
- 💾 本地 JSON 存储
- 🧪 完整的单元测试覆盖

**技术实现**：
- 使用 `typer` 构建现代化 CLI
- 采用模块化架构设计
- 支持 `uv` 工具链管理

**快速开始**：
```bash
cd L6
uv sync                        # 安装依赖
uv run task add "学习 Agent Skills"  # 添加任务
uv run task list               # 查看任务列表
```

**详细文档**：[L6/README.md](L6/README.md)

---

### L7: 多代理系统构建

**项目简介**：基于 Claude Agent SDK 的多代理协作系统

**系统能力**：
- 📖 文档研究与知识提取
- 🔍 代码仓库分析
- 🌐 网络搜索集成
- 📝 Notion 笔记管理（通过 MCP）

**架构设计**：
- 多代理协同工作流
- 工具链扩展机制
- 异步任务处理

**环境配置**：
```bash
cd L7
uv sync

# 创建 .env 文件
echo "ANTHROPIC_API_KEY=your_api_key" > .env
echo "NOTION_TOKEN=your_notion_token" >> .env  # 可选

# 运行代理
uv run python agent.py
```

**MCP 集成**：
- 支持 Notion 本地 MCP 服务器
- 可扩展其他 MCP 协议服务

**详细文档**：[L7/README.md](L7/README.md)

**补充资料**：
- `L7_notes/learning-mineru/` - MinerU 文档处理框架学习资料
  - 文档解析与提取
  - 多语言处理
  - API 服务器实现
  - RAG 流水线集成

---

## 快速开始

### 环境要求

- **操作系统**：Linux, macOS, Windows (WSL)
- **Python**：3.8 或更高版本
- **Node.js**：16+ (仅 L7 的 MCP 功能需要)
- **Claude 账号**：免费账号即可试用技能功能

### 安装 Python 依赖管理工具

本项目使用 `uv` 作为现代化的 Python 包管理器：

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 使用 Claude.ai 试用技能

1. 访问 [Claude.ai](https://claude.ai)（免费账号可用）
2. 导航到「技能」(Skills) 设置
3. 上传技能文件（如 `L1-partI/skill/analyzing-marketing-campaign/SKILL.md`）
4. 在对话中使用该技能处理任务

**支持的模型**：
- Claude Sonnet 4.5
- Claude Haiku 4.5

### 运行本地项目

#### 示例：L6 任务管理器

```bash
# 1. 进入项目目录
cd L6

# 2. 安装依赖
uv sync

# 3. 使用工具
uv run task add "第一个任务" -p high -d 2026-02-15
uv run task list

# 4. （可选）全局安装
uv tool install -e .
task list  # 直接使用
```

#### 示例：L7 多代理系统

```bash
# 1. 进入项目目录
cd L7

# 2. 安装依赖
uv sync

# 3. 配置环境变量
cat > .env << EOL
ANTHROPIC_API_KEY=sk-ant-your-api-key
NOTION_TOKEN=secret_your-notion-token  # 可选
EOL

# 4. 运行代理
uv run python agent.py
```

**获取 API Key**：
- Anthropic API Key: [console.anthropic.com](https://console.anthropic.com)
- Notion Token: [notion.so/my-integrations](https://www.notion.so/my-integrations)

---

## 技能开发指南

### 技能文件结构

一个标准的 Agent Skill 由以下部分组成：

```markdown
---
name: skill-name
description: 简短的技能描述，说明何时使用此技能
---

# 技能标题

## 输入要求
定义技能所需的输入数据格式和必填字段

## 处理步骤
详细说明技能的执行流程和算法逻辑

## 输出格式
规定技能返回结果的结构和呈现方式

## 参考文件
列出技能依赖的外部文档和数据源
```

### 设计原则

1. **单一职责**：每个技能专注于一个明确的任务领域
2. **可重用性**：设计通用的技能模板，支持参数化配置
3. **清晰的输入输出**：明确定义数据格式和预期结果
4. **完善的文档**：提供详细的使用说明和示例
5. **错误处理**：考虑边界情况和异常处理逻辑

### 最佳实践

- ✅ 使用描述性的技能名称（kebab-case）
- ✅ 在 description 中明确说明何时使用该技能
- ✅ 提供具体的数据格式示例
- ✅ 将复杂规则拆分到独立的参考文件
- ✅ 定义清晰的成功/失败指标
- ⚠️ 避免过度复杂的单一技能
- ⚠️ 避免硬编码业务逻辑（使用配置文件）

---

## 技能生态系统

### 支持的平台

由于 Agent Skills 是开放标准，您可以在多个平台使用本课程开发的技能：

- **Claude.ai** - 网页版（免费）
- **Claude Desktop** - 桌面应用
- **Claude API** - 编程接口
- **Claude Agent SDK** - 开发框架
- **其他兼容平台** - [查看完整列表](https://agentskills.io/home#adoption)

### 扩展开发

您可以基于本课程的示例技能进行扩展：

**营销分析技能增强方向**：
- 添加数据质量修复指南
- 扩展营销指标计算库
- 集成数据库查询能力
- 支持实时数据流分析

**时间序列分析技能增强方向**：
- 添加机器学习预测模型
- 集成季节性分解算法
- 支持多变量时间序列
- 实现自动化异常告警

---

## 测试与调试

### 单元测试

本项目使用 `pytest` 进行单元测试：

```bash
# 运行所有测试
cd L6
uv run pytest

# 运行特定测试文件
uv run pytest tests/test_add.py

# 显示详细输出
uv run pytest -v

# 查看测试覆盖率
uv run pytest --cov=src/task
```

### 技能调试

在 Claude.ai 或 Claude Desktop 中调试技能：

1. **启用详细输出模式**：在技能中添加调试信息
2. **逐步测试**：从简单输入开始，逐步增加复杂度
3. **验证参考文件**：确保所有引用的文件路径正确
4. **检查数据格式**：验证输入数据符合技能定义的要求

---

## 常见问题 (FAQ)

### Q: 我可以免费使用 Claude Skills 吗？

**A**: 可以。自 2026 年 1 月 26 日起，Claude.ai 免费用户可以使用 Sonnet 4.5 和 Haiku 4.5 模型的 Skills 功能。

### Q: Agent Skills 与传统 AI 工具有何不同？

**A**: Agent Skills 将专业知识模块化，使 AI 能够执行特定领域的复杂任务，而不是单纯的对话。技能可以被共享、复用和组合，形成强大的工作流。

### Q: 如何将技能部署到生产环境？

**A**: 您可以：
1. 通过 Claude API 集成技能到应用程序
2. 使用 Claude Agent SDK 构建自定义代理系统
3. 将技能文件部署到支持的第三方平台

### Q: 技能可以访问外部 API 吗？

**A**: 可以。通过 Claude Agent SDK 和 MCP (Model Context Protocol)，技能可以集成各种外部服务和 API。

### Q: 如何处理敏感数据？

**A**: 
- 在技能中避免硬编码敏感信息
- 使用环境变量管理 API 密钥
- 遵循数据最小化原则
- 参考 Anthropic 的安全最佳实践文档

---

## 学习资源

### 官方文档

- [Agent Skills 官网](https://agentskills.io/home)
- [Anthropic Agent Skills 文档](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Claude Skills 博客](https://claude.com/blog/skills)
- [Model Context Protocol](https://modelcontextprotocol.io/)

### 相关工具

- [uv - Python 包管理器](https://github.com/astral-sh/uv)
- [MinerU - 文档处理框架](https://github.com/opendatalab/MinerU)
- [Notion MCP Server](https://github.com/makenotion/notion-mcp-server)

### 社区与支持

- [Anthropic 开发者社区](https://community.anthropic.com/)
- [GitHub Discussions](https://github.com/https-deeplearning-ai/sc-agent-skills-files/discussions)

---

## 贡献指南

本课程材料旨在教育目的，我们欢迎社区贡献改进建议：

1. **报告问题**：发现错误或有疑问时，请提交 Issue
2. **改进建议**：对课程内容或代码有改进想法，欢迎讨论
3. **技能分享**：开发了有趣的技能，欢迎分享到社区

**注意**：所有课程中展示的技能均为教育示例，在生产使用前需要进一步优化和测试。

---

## 许可证

本仓库内容仅供教育学习使用。使用 Claude AI 服务时，请遵守 [Anthropic 服务条款](https://www.anthropic.com/legal/terms)。

---

## 致谢

本课程材料由 DeepLearning.AI 和 Anthropic 联合制作，感谢所有贡献者的努力。

特别感谢：
- Claude AI 团队提供的强大技术支持
- Agent Skills 社区的宝贵反馈
- 所有参与课程开发的工程师和教育专家

---

## 更新日志

- **2026-01-30**: 创建项目 README 文档
- **2026-01-26**: Claude.ai 免费用户开放 Skills 功能

---

<div align="center">

**🚀 开始你的 Agent Skills 学习之旅！**

[查看课程材料](course_materials.md) | [访问 Claude.ai](https://claude.ai) | [官方文档](https://agentskills.io/home)

</div>

