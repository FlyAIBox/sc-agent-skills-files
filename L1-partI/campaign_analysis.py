#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
营销活动数据分析脚本
Marketing Campaign Data Analysis
"""

# 读取数据 - 处理中文标点问题
data = []
with open('skill/zh/campaign_data_week1_china.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 跳过第一行标题（使用中文顿号），从第二行开始
# 列名按顺序：日期、营销活动名称、渠道、受众分群、展示次数、点击次数、转化次数、支出、收入、订单数
for line in lines[1:]:
    line = line.strip()
    if not line:
        continue
    # 使用逗号分割数据行
    parts = line.split(',')
    if len(parts) >= 10:
        data.append({
            '日期': parts[0].strip(),
            '营销活动名称': parts[1].strip(),
            '渠道': parts[2].strip(),
            '受众分群': parts[3].strip(),
            '展示次数': parts[4].strip() if parts[4].strip() else '',
            '点击次数': parts[5].strip(),
            '转化次数': parts[6].strip(),
            '支出': parts[7].strip(),
            '收入': parts[8].strip(),
            '订单数': parts[9].strip()
        })

print("=" * 80)
print("营销活动数据分析报告")
print("=" * 80)
print()

# ===== 1. 数据质量检查 =====
print("【数据质量检查】")
print("-" * 80)

# 统计缺失值
total_rows = len(data)
columns = ['日期', '营销活动名称', '渠道', '受众分群', '展示次数', '点击次数', '转化次数', '支出', '收入', '订单数']

print("\n1. 缺失数据检查:")
for col in columns:
    missing = sum(1 for r in data if not r.get(col, '').strip())
    if missing > 0:
        pct = (missing / total_rows) * 100
        print(f"   ⚠️  {col}: {missing} 条缺失 ({pct:.1f}%)")

# 特别检查：小程序推送的展示次数列
mini_program_rows = [r for r in data if r['渠道'] == '小程序推送']
if mini_program_rows:
    missing_imp = sum(1 for r in mini_program_rows if not r.get('展示次数', '').strip())
    if missing_imp == len(mini_program_rows):
        print(f"\n   ⚠️  重要发现: 小程序推送渠道的【展示次数】列完全缺失")
        print(f"   影响的记录数: {len(mini_program_rows)} 条")
        print(f"   说明: 无法计算小程序推送的CTR，因为缺少分母数据")

# 检查数值异常（负值）
print("\n2. 数值异常检查:")
numeric_cols = ['展示次数', '点击次数', '转化次数', '支出', '收入', '订单数']
for col in numeric_cols:
    neg_count = 0
    for row in data:
        val = row.get(col, '').strip()
        if val:
            try:
                if float(val) < 0:
                    neg_count += 1
            except:
                pass
    if neg_count > 0:
        print(f"   ⚠️  {col} 包含 {neg_count} 个负值")
    else:
        print(f"   ✓ {col}: 无负值")

print()

# ===== 2. 漏斗分析 =====
print("\n【漏斗分析】")
print("-" * 80)

# 基准数据
benchmarks = {
    '微信广告': {'ctr': 2.5, 'cvr': 3.8},
    '百度推广': {'ctr': 5.0, 'cvr': 4.5},
    '抖音广告': {'ctr': 2.0, 'cvr': 0.9},
    '小程序推送': {'ctr': 15.0, 'cvr': 2.1}
}

# 按渠道汇总数据
channel_stats = {}
for channel in benchmarks.keys():
    channel_data = [r for r in data if r['渠道'] == channel]

    total_impressions = 0
    total_clicks = 0
    total_conversions = 0
    total_spend = 0
    total_revenue = 0
    total_orders = 0

    for row in channel_data:
        imp = row.get('展示次数', '').strip()
        if imp:
            try:
                total_impressions += float(imp)
            except:
                pass

        try:
            total_clicks += float(row.get('点击次数', 0))
            total_conversions += float(row.get('转化次数', 0))
            total_spend += float(row.get('支出', 0))
            total_revenue += float(row.get('收入', 0))
            total_orders += float(row.get('订单数', 0))
        except:
            pass

    # 计算CTR和CVR
    ctr = (total_clicks / total_impressions * 100) if total_impressions > 0 else None
    cvr = (total_conversions / total_clicks * 100) if total_clicks > 0 else None
    roi = ((total_revenue - total_spend) / total_spend * 100) if total_spend > 0 else None
    roas = (total_revenue / total_spend) if total_spend > 0 else None
    aov = (total_revenue / total_orders) if total_orders > 0 else None

    channel_stats[channel] = {
        'impressions': total_impressions,
        'clicks': total_clicks,
        'conversions': total_conversions,
        'spend': total_spend,
        'revenue': total_revenue,
        'orders': total_orders,
        'ctr': ctr,
        'cvr': cvr,
        'roi': roi,
        'roas': roas,
        'aov': aov
    }

# 输出表格
print("\n{:<15} {:>12} {:>10} {:>10} {:>10} {:>10} {:>12} {:>10}".format(
    "渠道", "展示次数", "点击次数", "转化次数", "CTR%", "目标CTR%", "CVR%", "目标CVR%"
))
print("-" * 95)

for channel, stats in channel_stats.items():
    imp = f"{stats['impressions']:,.0f}" if stats['impressions'] > 0 else "N/A"
    clicks = f"{stats['clicks']:,.0f}"
    conv = f"{stats['conversions']:,.0f}"
    ctr = f"{stats['ctr']:.2f}%" if stats['ctr'] is not None else "N/A*"
    target_ctr = f"{benchmarks[channel]['ctr']:.1f}%"
    cvr = f"{stats['cvr']:.2f}%" if stats['cvr'] is not None else "N/A"
    target_cvr = f"{benchmarks[channel]['cvr']:.1f}%"

    # 根据表现添加标记
    ctr_symbol = ""
    cvr_symbol = ""
    if stats['ctr'] is not None:
        diff = stats['ctr'] - benchmarks[channel]['ctr']
        if diff >= 0:
            ctr_symbol = " ✓"
        else:
            ctr_symbol = " ✗"
    if stats['cvr'] is not None:
        diff = stats['cvr'] - benchmarks[channel]['cvr']
        if diff >= 0:
            cvr_symbol = " ✓"
        else:
            cvr_symbol = " ✗"

    print("{:<15} {:>12} {:>10} {:>10} {:>10} {:>10} {:>12} {:>10}".format(
        channel, imp, clicks, conv, ctr + ctr_symbol, target_ctr, cvr + cvr_symbol, target_cvr
    ))

print("\n* 注: 小程序推送的CTR无法计算，因为缺少展示次数数据")
print("✓ = 达到或超过基准 | ✗ = 低于基准")

# ===== 3. 详细对比分析 =====
print("\n\n【详细对比分析】")
print("-" * 80)

for channel, stats in channel_stats.items():
    print(f"\n{channel}:")

    if stats['ctr'] is not None:
        ctr_diff = stats['ctr'] - benchmarks[channel]['ctr']
        print(f"  CTR表现: {stats['ctr']:.2f}% vs 目标 {benchmarks[channel]['ctr']:.1f}%", end="")
        if ctr_diff >= 0:
            print(f" (超出 +{ctr_diff:.2f}%) ✓")
        else:
            print(f" (低于 {ctr_diff:.2f}%) ✗")
    else:
        print(f"  CTR表现: N/A (无法计算 - 缺少展示次数数据)")

    if stats['cvr'] is not None:
        cvr_diff = stats['cvr'] - benchmarks[channel]['cvr']
        print(f"  CVR表现: {stats['cvr']:.2f}% vs 目标 {benchmarks[channel]['cvr']:.1f}%", end="")
        if cvr_diff >= 0:
            print(f" (超出 +{cvr_diff:.2f}%) ✓")
        else:
            print(f" (低于 {cvr_diff:.2f}%) ✗")

    if stats['roi'] is not None:
        print(f"  ROI: {stats['roi']:.2f}% | ROAS: {stats['roas']:.2f}")
    if stats['aov'] is not None:
        print(f"  平均订单价值 (AOV): ¥{stats['aov']:.2f}")

# ===== 4. 总结 =====
print("\n\n【关键发现总结】")
print("-" * 80)

# 统计达标情况
ctr_channels = [c for c, s in channel_stats.items() if s['ctr'] is not None]
cvr_channels = [c for c, s in channel_stats.items() if s['cvr'] is not None]

ctr_pass = sum(1 for c, s in channel_stats.items()
               if s['ctr'] is not None and s['ctr'] >= benchmarks[c]['ctr'])
cvr_pass = sum(1 for c, s in channel_stats.items()
               if s['cvr'] is not None and s['cvr'] >= benchmarks[c]['cvr'])

print(f"\nCTR 达标率: {ctr_pass}/{len(ctr_channels)} 个渠道达到或超过目标")
print(f"CVR 达标率: {cvr_pass}/{len(cvr_channels)} 个渠道达到或超过目标")

# 找出表现最好和最差的渠道
print("\n各渠道表现排名:")

# 按CTR排序
ctr_rank = sorted([(c, s['ctr']) for c, s in channel_stats.items() if s['ctr'] is not None],
                  key=lambda x: x[1], reverse=True)
if ctr_rank:
    print("\n  CTR排名:")
    for i, (ch, ctr_val) in enumerate(ctr_rank, 1):
        print(f"    {i}. {ch}: {ctr_val:.2f}%")

# 按CVR排序
cvr_rank = sorted([(c, s['cvr']) for c, s in channel_stats.items() if s['cvr'] is not None],
                  key=lambda x: x[1], reverse=True)
if cvr_rank:
    print("\n  CVR排名:")
    for i, (ch, cvr_val) in enumerate(cvr_rank, 1):
        print(f"    {i}. {ch}: {cvr_val:.2f}%")

# 按收入排序
revenue_rank = sorted([(c, s['revenue']) for c, s in channel_stats.items()],
                      key=lambda x: x[1], reverse=True)
print("\n  收入排名:")
for i, (ch, rev) in enumerate(revenue_rank, 1):
    print(f"    {i}. {ch}: ¥{rev:,.2f}")

print("\n" + "=" * 80)
