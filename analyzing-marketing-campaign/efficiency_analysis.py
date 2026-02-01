#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
营销活动效率分析脚本
Marketing Campaign Efficiency Analysis
"""

# 读取数据 - 处理中文标点问题
data = []
with open('skill/zh/campaign_data_week1_china.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 跳过第一行标题（使用中文顿号），从第二行开始
for line in lines[1:]:
    line = line.strip()
    if not line:
        continue
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

print("=" * 100)
print("营销活动效率分析报告")
print("=" * 100)
print()

# 目标值
TARGET_ROAS = 4.0  # 最低4倍
MAX_CPA = 50.0     # 最大50元
SHIPPING_COST_PER_ORDER = 8.0  # 每单8元
PRODUCT_COST_PERCENT = 0.35    # 产品成本35%

# 按渠道汇总数据
channels = ['微信广告', '百度推广', '抖音广告', '小程序推送']
channel_stats = {}

for channel in channels:
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

        total_clicks += float(row.get('点击次数', 0))
        total_conversions += float(row.get('转化次数', 0))
        total_spend += float(row.get('支出', 0))
        total_revenue += float(row.get('收入', 0))
        total_orders += float(row.get('订单数', 0))

    # 计算核心指标
    roas = (total_revenue / total_spend) if total_spend > 0 else None
    cpa = (total_spend / total_conversions) if total_conversions > 0 else None

    # 计算总成本和净利润
    shipping_cost = total_orders * SHIPPING_COST_PER_ORDER
    product_cost = total_revenue * PRODUCT_COST_PERCENT
    total_cost = total_spend + shipping_cost + product_cost
    net_profit = total_revenue - total_cost
    profit_margin = (net_profit / total_revenue * 100) if total_revenue > 0 else None

    # 计算CTR和CVR（用于参考）
    ctr = (total_clicks / total_impressions * 100) if total_impressions > 0 else None
    cvr = (total_conversions / total_clicks * 100) if total_clicks > 0 else None

    channel_stats[channel] = {
        'impressions': total_impressions,
        'clicks': total_clicks,
        'conversions': total_conversions,
        'spend': total_spend,
        'revenue': total_revenue,
        'orders': total_orders,
        'roas': roas,
        'cpa': cpa,
        'shipping_cost': shipping_cost,
        'product_cost': product_cost,
        'total_cost': total_cost,
        'net_profit': net_profit,
        'profit_margin': profit_margin,
        'ctr': ctr,
        'cvr': cvr
    }

# ===== 汇总表格 =====
print("\n【效率指标汇总】")
print("-" * 100)

# 表头
print("\n{:<15} {:>12} {:>12} {:>14} {:>14} {:>14} {:>14}".format(
    "渠道", "ROAS", "目标ROAS", "CPA(元)", "最大CPA", "净利润(元)", "利润率(%)"
))
print("-" * 100)

for channel, stats in channel_stats.items():
    roas = f"{stats['roas']:.2f}" if stats['roas'] is not None else "N/A"
    roas_symbol = " ✓" if stats['roas'] and stats['roas'] >= TARGET_ROAS else " ✗"

    cpa = f"¥{stats['cpa']:.2f}" if stats['cpa'] is not None else "N/A"
    cpa_symbol = " ✓" if stats['cpa'] and stats['cpa'] <= MAX_CPA else " ✗"

    profit = f"¥{stats['net_profit']:,.2f}"
    profit_symbol = " ✓" if stats['net_profit'] > 0 else " ✗"
    margin = f"{stats['profit_margin']:.2f}%" if stats['profit_margin'] is not None else "N/A"

    print("{:<15} {:>12} {:>12} {:>14} {:>14} {:>14} {:>14}".format(
        channel,
        roas + roas_symbol,
        f"≥{TARGET_ROAS}",
        cpa + cpa_symbol,
        f"≤{MAX_CPA}",
        profit + profit_symbol,
        margin
    ))

print("\n✓ = 达到目标 | ✗ = 未达标")

# ===== 详细成本分析 =====
print("\n\n【详细成本与利润分析】")
print("-" * 100)

print("\n{:<15} {:>14} {:>14} {:>14} {:>14} {:>14} {:>14}".format(
    "渠道", "广告支出", "物流成本", "产品成本", "总成本", "收入", "净利润"
))
print("-" * 100)

for channel, stats in channel_stats.items():
    print("{:<15} {:>14} {:>14} {:>14} {:>14} {:>14} {:>14}".format(
        channel,
        f"¥{stats['spend']:,.2f}",
        f"¥{stats['shipping_cost']:,.2f}",
        f"¥{stats['product_cost']:,.2f}",
        f"¥{stats['total_cost']:,.2f}",
        f"¥{stats['revenue']:,.2f}",
        f"¥{stats['net_profit']:,.2f}"
    ))

# ===== 目标达成情况总结 =====
print("\n\n【目标达成情况总结】")
print("-" * 100)

roas_pass = sum(1 for c, s in channel_stats.items() if s['roas'] and s['roas'] >= TARGET_ROAS)
cpa_pass = sum(1 for c, s in channel_stats.items() if s['cpa'] and s['cpa'] <= MAX_CPA)
profit_pass = sum(1 for c, s in channel_stats.items() if s['net_profit'] > 0)

print(f"\nROAS 达标 (≥{TARGET_ROAS}): {roas_pass}/{len(channels)} 个渠道")
print(f"CPA 达标 (≤¥{MAX_CPA}): {cpa_pass}/{len(channels)} 个渠道")
print(f"净利润为正: {profit_pass}/{len(channels)} 个渠道")

# 全部达标检查
all_pass = []
for channel, stats in channel_stats.items():
    roas_ok = stats['roas'] and stats['roas'] >= TARGET_ROAS
    cpa_ok = stats['cpa'] and stats['cpa'] <= MAX_CPA
    profit_ok = stats['net_profit'] > 0
    all_ok = roas_ok and cpa_ok and profit_ok
    all_pass.append((channel, all_ok, roas_ok, cpa_ok, profit_ok))

print("\n各渠道综合达标情况:")
for channel, all_ok, roas_ok, cpa_ok, profit_ok in all_pass:
    status = "✓ 全部达标" if all_ok else "✗ 部分未达标"
    details = []
    if not roas_ok:
        details.append(f"ROAS({channel_stats[channel]['roas']:.2f}<{TARGET_ROAS})")
    if not cpa_ok:
        details.append(f"CPA(¥{channel_stats[channel]['cpa']:.2f}>¥{MAX_CPA})")
    if not profit_ok:
        details.append(f"净利润(¥{channel_stats[channel]['net_profit']:.2f}<0)")

    detail_str = " - " + ", ".join(details) if details else ""
    print(f"  {channel}: {status}{detail_str}")

# ===== 效率排名 =====
print("\n\n【效率排名】")
print("-" * 100)

# ROAS排名
roas_rank = sorted([(c, s['roas']) for c, s in channel_stats.items() if s['roas'] is not None],
                   key=lambda x: x[1], reverse=True)
print("\n  ROAS 排名:")
for i, (ch, val) in enumerate(roas_rank, 1):
    print(f"    {i}. {ch}: {val:.2f}x")

# CPA排名 (越低越好)
cpa_rank = sorted([(c, s['cpa']) for c, s in channel_stats.items() if s['cpa'] is not None],
                  key=lambda x: x[1])
print("\n  CPA 排名 (成本越低越好):")
for i, (ch, val) in enumerate(cpa_rank, 1):
    print(f"    {i}. {ch}: ¥{val:.2f}")

# 净利润排名
profit_rank = sorted([(c, s['net_profit']) for c, s in channel_stats.items()],
                     key=lambda x: x[1], reverse=True)
print("\n  净利润排名:")
for i, (ch, val) in enumerate(profit_rank, 1):
    margin = channel_stats[ch]['profit_margin']
    print(f"    {i}. {ch}: ¥{val:,.2f} (利润率: {margin:.2f}%)")

# ===== 综合建议 =====
print("\n\n【优化建议】")
print("-" * 100)

print("\n1. ROAS优化:")
for channel, stats in channel_stats.items():
    if stats['roas'] and stats['roas'] < TARGET_ROAS:
        gap = TARGET_ROAS - stats['roas']
        current_revenue = stats['revenue']
        needed_revenue = stats['spend'] * TARGET_ROAS
        increase = needed_revenue - current_revenue
        print(f"   - {channel}: ROAS {stats['roas']:.2f}x，需提升 {gap:.2f}x 达标")
        print(f"     需增加收入 ¥{increase:,.2f} 或优化支出策略")

print("\n2. CPA控制:")
for channel, stats in channel_stats.items():
    if stats['cpa'] and stats['cpa'] > MAX_CPA:
        excess = stats['cpa'] - MAX_CPA
        print(f"   - {channel}: CPA ¥{stats['cpa']:.2f}，超出 ¥{excess:.2f}")
        print(f"     建议优化定向策略或提升转化率")

print("\n3. 成本结构分析:")
for channel, stats in channel_stats.items():
    spend_pct = (stats['spend'] / stats['total_cost'] * 100)
    shipping_pct = (stats['shipping_cost'] / stats['total_cost'] * 100)
    product_pct = (stats['product_cost'] / stats['total_cost'] * 100)
    print(f"   - {channel}: 广告{spend_pct:.1f}% | 物流{shipping_pct:.1f}% | 产品{product_pct:.1f}%")

print("\n" + "=" * 100)
