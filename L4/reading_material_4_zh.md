# 创建自定义 Skills

## 自定义 Skills 链接
- <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L4/custom_skills/analyzing-time-series/" target="_blank">分析时间序列</a>
- <a href="https://github.com/https-deeplearning-ai/sc-agent-skills-files/tree/main/L4/custom_skills/generating-practice-questions/" target="_blank">生成练习题</a>

## 参考资料
有关 Skills 创建最佳实践和规范的完整列表，请务必查看：
- <a href="https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices" target="_blank">Skill 编写最佳实践</a>
- <a href="https://agentskills.io/specification" target="_blank">规范</a>

## 如何在 Claude Code 中禁用插件？

插件设计为根据需要开启和关闭。你可以在需要特定功能时启用它们，并在不需要时禁用它们，以减少系统提示词的上下文和复杂性。

- 使用 `/plugin` 命令：导航到 `installed` 标签页，然后选择你要禁用的插件。
- 使用命令行：
`claude plugin disable <plugin-name>`


## 幻灯片摘要

### SKILL.md 文件结构

一个 Skill 文件有两个主要部分：
1. **YAML Frontmatter** — 顶部的元数据
2. **正文内容** — 下方的 Markdown 指令

### Frontmatter 必填字段

| 字段 | 约束 |
|-------|-------------|
| **name** | 最多 64 个字符；仅限小写字母、数字和连字符；不得以连字符开头/结尾；必须与父目录名称匹配；推荐：动名词形式（动词+-ing） |
| **description** | 最多 1024 个字符；非空；应描述 Skill 做什么**以及**何时使用它；包含特定关键字以帮助 Agent 识别相关任务 |

### Frontmatter 可选字段

| 字段 | 约束 |
|-------|-------------|
| **license** | 许可证名称或对许可证文件的引用 |
| **compatibility** | 最多 500 个字符；指示环境要求 |
| **metadata** | 任意键值对（例如，作者、版本） |
| **allowed-tools** | 预先批准的 Tool 的空格分隔列表（实验性） |


### 正文内容

**没有格式限制**，但这里有一些建议：

#### 推荐部分
- 分步说明
- 输入格式 / 输出格式 / 示例
- 常见边缘情况

#### 实践指南
- 保持在 **500 行以内**
- 将详细的参考资料移至单独的文件（展示基本内容，链接到高级内容）
- 保持参考资料与 SKILL.md **同一层级**（避免嵌套文件引用）
- 清晰简洁，使用一致的术语
- 在文件路径中使用正斜杠，即使在 Windows 上也是如此

#### 自由度

| 级别 | 描述 |
|-------|-------------|
| **高自由度** | 通用的基于文本的指导；多种方法均有效 |
| **中等自由度** | 指令包含可定制的伪代码、代码示例或模式；存在首选模式，但允许一定变体 |
| **低自由度** | 指令引用特定脚本；必须遵循特定顺序 |

#### 复杂工作流
- 将复杂操作分解为清晰、顺序的步骤
- 如果工作流变得很大且步骤很多，请考虑将它们放入单独的文件中

### 可选目录

#### `/assets`
- **模板：** 文档模板、配置模板
- **图像：** 图表、Logo
- **数据文件：** 查找表、Schema

#### `/references`
- 包含 Agent 在需要时可以阅读的额外文档
- 保持单个参考文件专注
- **注意：** 对于超过 100 行的参考文件，请在顶部包含目录，以便 Agent 可以看到完整范围

#### `/scripts`
- 清晰记录依赖关系
- 脚本应有清晰的文档
- 错误处理应明确且有帮助
- **注意：** 在指令中明确说明 Claude 应该执行脚本还是将其作为参考阅读


### 评估

#### 单元测试

定义测试用例，包含：
- **skills**: 要测试哪些 Skill
- **queries**: 要运行的测试提示词
- **files**: 要使用的输入文件
- **expected_behavior**: 成功的标准

#### 测试用例示例
```json
{
  "skills": ["generating-practice-questions"],
  "queries": [
    "Generate practice questions from this lecture note and save it to output.md",
    "Generate practice questions from this lecture note and save it to output.tex",
    "Generate practice questions from this lecture note and save it to output.pdf"
  ],
  "files": ["test-files/notes.pdf", "test-files/notes.tex", "test-files/notes.pdf"],
  "expected_behavior": [
    "Successfully reads and extracts the input file. For pdf input, uses pdfplumber.",
    "Successfully extracts all the learning objectives.",
    "Generates the 4 types of questions.",
    "Follows the guidelines for each question.",
    "Uses the output structure and the correct output templates.",
    "The latex output successfully compiles.",
    "Saves the generated questions to a file named output."
  ]
}
```
**其他评估提示**:

- 获取 **人工反馈**
- 使用你计划使用的 **所有模型** 进行测试
