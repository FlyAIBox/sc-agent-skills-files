---
name: analyzing-time-series_zh
description: 全面的时间序列数据诊断分析工具。当用户提供 CSV 格式的时间序列数据并希望在预测之前了解其特征（平稳性、季节性、趋势、可预测性和变换建议）时使用。
---

# 时间序列诊断

在进行预测之前分析时间序列数据特征的综合诊断工具包。

## 输入格式

输入的 CSV 文件应包含两列：
- **日期列** - 时间戳或日期（例如：`date`, `timestamp`, `time`）
- **数值列** - 要分析的数值（例如：`value`, `sales`, `temperature`）

## 工作流程

**第 1 步：运行诊断**

```bash
python scripts/diagnose.py data.csv --output-dir results/
```

这将运行所有统计测试和分析。输出包含所有指标的 `diagnostics.json` 和包含人类可读结果的 `summary.txt`。程序会自动检测列名，或者可以使用 `--date-col` 和 `--value-col` 选项指定。

**第 2 步：生成图表（可选）**

```bash
python scripts/visualize.py data.csv --output-dir results/
```

在 `results/plots/` 中生成诊断图表以供视觉检查。请在运行 `diagnose.py` 之后运行此步骤，以确保 ACF/PACF 图与平稳性结果同步。程序 Automatically detects column names, or can be specified with `--date-col` and `--value-col` options.

**第 3 步：向用户报告**

总结 `summary.txt` 中的发现并展示相关图表。请参阅 `references/interpretation.md` 以获取以下方面的指导：
- 数据是否可预测？
- 数据是否平稳？需要多少阶差分？
- 是否存在季节性？周期是多少？
- 是否存在趋势？什么方向？
- 是否需要变换？

## 脚本选项

两个脚本都接受：
- `--date-col NAME` - 日期列（如果省略则自动检测）
- `--value-col NAME` - 数值列（如果省略则自动检测）
- `--output-dir PATH` - 输出目录（默认：`diagnostics/`）
- `--seasonal-period N` - 季节性周期（如果省略则自动检测）

## 输出文件

```
results/
├── diagnostics.json       # 所有测试结果和统计数据
├── summary.txt            # 人类可读的发现
├── diagnostics_state.json # 图表同步的内部状态
└── plots/
    ├── timeseries.png
    ├── histogram.png
    ├── rolling_stats.png
    ├── box_by_dayofweek.png  # 按星期几（如适用）
    ├── box_by_month.png      # 按月份（如适用）
    ├── box_by_quarter.png    # 按季度（如适用）
    ├── acf_pacf.png
    ├── decomposition.png
    └── lag_scatter.png
```

## 参考资料

请参阅 `references/interpretation.md` 了解：
- 统计测试阈值和解释
- 不同数据频率的季节性周期指南
- 变换建议

## 依赖项

`pandas`, `numpy`, `matplotlib`, `statsmodels`, `scipy`
