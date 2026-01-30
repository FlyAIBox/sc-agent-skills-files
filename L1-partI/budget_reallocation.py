#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
预算调整分析脚本
Budget Reallocation Analysis
"""

# 读取数据
data = []
with open('skill/zh/campaign_data_week1_china.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()

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
print("预算调整分析报告")
print("=" * 100)
print()

# ===== 配置参数 =====
TARGET_ROAS = 4.0
MAX_CPA = 50.0
SHIPPING_COST_PER_ORDER = 8.0
PRODUCT_COST_PERCENT = 0.35

# 用户指定参数
USER_REALLOCATION_LIMIT = 10000.0  # 1万元
PER_CHANNEL_INCREASE_CAP = 0.15    # 15%

# ===== 按渠道汇总数据 =====
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

    roas = (total_revenue / total_spend) if total_spend > 0 else None
    cpa = (total_spend / total_conversions) if total_conversions > 0 else None
    shipping_cost = total_orders * SHIPPING_COST_PER_ORDER
    product_cost = total_revenue * PRODUCT_COST_PERCENT
    total_cost = total_spend + shipping_cost + product_cost
    net_profit = total_revenue - total_cost

    channel_stats[channel] = {
        'conversions': total_conversions,
        'spend': total_spend,
        'roas': roas,
        'cpa': cpa,
        'net_profit': net_profit
    }

# ===== 规则0：最低数据门槛 =====
print("\n【规则0：最低数据门槛检查】")
print("-" * 100)

MIN_CONVERSIONS = 50
eligible_channels = []

for channel, stats in channel_stats.items():
    eligible = stats['conversions'] >= MIN_CONVERSIONS
    status = "✓ 符合资格" if eligible else "✗ 数据不足"
    print(f"{channel}: {stats['conversions']:,.0f} 次转化 - {status}")
    if eligible:
        eligible_channels.append(channel)

print(f"\n具备调整预算资格的渠道: {len(eligible_channels)}/{len(channels)}")

# ===== 规则1：渠道分类 =====
print("\n\n【规则1：渠道分类】")
print("-" * 100)

classifications = {}

for channel in eligible_channels:
    stats = channel_stats[channel]

    # 计算比率
    roas_ratio = (stats['roas'] / TARGET_ROAS * 100) if stats['roas'] else 0
    cpa_ratio = (stats['cpa'] / MAX_CPA * 100) if stats['cpa'] else 0

    # 分类逻辑（按顺序）
    classification = "MAINTAIN"
    change_percent = 0

    # 1. PAUSE (-100%) - 用户陈述的连续3周以上负向（此处无用户陈述，跳过）

    # 2. DECREASE_HEAVY (-45%)
    if (stats['roas'] < TARGET_ROAS * 0.5 and stats['net_profit'] <= 0) or \
       (stats['cpa'] > MAX_CPA * 1.5 and stats['net_profit'] <= 0) or \
       (stats['roas'] < TARGET_ROAS and stats['cpa'] > MAX_CPA and stats['net_profit'] <= 0):
        classification = "DECREASE_HEAVY"
        change_percent = -0.45

    # 3. INCREASE (+15% cap)
    elif stats['roas'] >= TARGET_ROAS * 1.15 and stats['cpa'] <= MAX_CPA * 0.8 and stats['net_profit'] > 0:
        classification = "INCREASE"
        change_percent = 0.15

    # 4. DECREASE_LIGHT (-25%)
    elif stats['roas'] < TARGET_ROAS * 0.8 or stats['cpa'] > MAX_CPA * 1.2:
        classification = "DECREASE_LIGHT"
        change_percent = -0.25

    # 5. MAINTAIN (0%)
    else:
        classification = "MAINTAIN"
        change_percent = 0

    classifications[channel] = {
        'classification': classification,
        'change_percent': change_percent
    }

# ===== 分类表输出 =====
print("\n{:<15} {:>12} {:>18} {:>12} {:>18} {:>14} {:<20}".format(
    "渠道", "ROAS", "目标达成率(%)", "CPA", "达到上限率(%)", "净利润", "分类结果"
))
print("-" * 110)

for channel in eligible_channels:
    stats = channel_stats[channel]
    cls = classifications[channel]

    roas_ratio = (stats['roas'] / TARGET_ROAS * 100) if stats['roas'] else 0
    cpa_ratio = (stats['cpa'] / MAX_CPA * 100) if stats['cpa'] else 0

    print("{:<15} {:>12.2f} {:>18.2f} {:>12.2f} {:>18.2f} {:>14.2f} {:<20}".format(
        channel,
        stats['roas'],
        roas_ratio,
        stats['cpa'],
        cpa_ratio,
        stats['net_profit'],
        f"{cls['classification']} ({cls['change_percent']:+.0%})"
    ))

# ===== 规则2：计算预算变更 =====
print("\n\n【规则2：计算预算变更】")
print("-" * 100)

# 第1步：计算削减额
decrease_channels = [c for c in eligible_channels if classifications[c]['change_percent'] < 0]
total_freed_budget = 0

print("\n第1步：计算削减额")
for channel in decrease_channels:
    stats = channel_stats[channel]
    change = classifications[channel]['change_percent']
    decrease_amount = stats['spend'] * abs(change)
    total_freed_budget += decrease_amount
    print(f"  {channel}: ¥{stats['spend']:,.2f} × {abs(change):.0%} = ¥{decrease_amount:,.2f}")

print(f"\n释放预算总计: ¥{total_freed_budget:,.2f}")

# 第2步：释放的预算
print(f"\n第2步：释放预算 = ¥{total_freed_budget:,.2f}")

# 第3步：分配给"增加"类别的渠道
increase_channels = [c for c in eligible_channels if classifications[c]['change_percent'] > 0]

if increase_channels:
    print(f"\n第3步：按净利润比例分配给 {len(increase_channels)} 个'增加'渠道")

    # 计算权重
    total_profit_for_increase = sum(channel_stats[c]['net_profit'] for c in increase_channels)

    proposed_increases = {}
    for channel in increase_channels:
        stats = channel_stats[channel]
        weight = stats['net_profit'] / total_profit_for_increase
        proposed = total_freed_budget * weight
        proposed_increases[channel] = proposed
        print(f"  {channel}: 权重 = {weight:.2%}, 建议增加额 = ¥{proposed:,.2f}")

    # 第4步：应用上限限制
    print(f"\n第4步：应用上限限制（单渠道上限: {PER_CHANNEL_INCREASE_CAP:.0%}）")

    max_increases = {}
    for channel in increase_channels:
        stats = channel_stats[channel]
        max_inc = stats['spend'] * PER_CHANNEL_INCREASE_CAP
        max_increases[channel] = max_inc
        proposed = proposed_increases[channel]
        capped = min(proposed, max_inc)
        print(f"  {channel}: 建议额 ¥{proposed:,.2f} vs 上限额 ¥{max_inc:,.2f} {'→ 受限' if proposed > max_inc else '→ OK'}")

    # 应用用户总调配限额
    print(f"\n第4步续：应用用户总调配限额 (¥{USER_REALLOCATION_LIMIT:,.2f})")

    # 先按单渠道上限调整
    capped_increases = {}
    for channel in increase_channels:
        capped_increases[channel] = min(proposed_increases[channel], max_increases[channel])

    total_capped_increases = sum(capped_increases.values())

    if total_capped_increases > USER_REALLOCATION_LIMIT:
        scale_factor = USER_REALLOCATION_LIMIT / total_capped_increases
        print(f"  所有增加额总计 (¥{total_capped_increases:,.2f}) > 用户限额")
        print(f"  缩放因子 = {scale_factor:.4f}")

        final_increases = {}
        for channel in increase_channels:
            final_increases[channel] = capped_increases[channel] * scale_factor
            print(f"  {channel}: ¥{capped_increases[channel]:,.2f} × {scale_factor:.4f} = ¥{final_increases[channel]:,.2f}")
    else:
        final_increases = capped_increases.copy()
        print(f"  所有增加额总计 (¥{total_capped_increases:,.2f}) <= 用户限额，无需缩放")
        for channel, amt in final_increases.items():
            print(f"  {channel}: ¥{amt:,.2f}")

    # 第5步：计算未分配结余
    print(f"\n第5步：计算未分配结余")
    total_final_increases = sum(final_increases.values())
    unallocated = total_freed_budget - total_final_increases
    print(f"  未分配金额 = ¥{total_freed_budget:,.2f} - ¥{total_final_increases:,.2f} = ¥{unallocated:,.2f}")

# ===== 最终调整表 =====
print("\n\n【最终调整表】")
print("-" * 100)

print("\n{:<15} {:>14} {:>14} {:>14} {:<20}".format(
    "渠道", "当前预算", "变更额", "新预算", "分类"
))
print("-" * 80)

for channel in channels:
    if channel not in eligible_channels:
        continue

    stats = channel_stats[channel]
    cls = classifications[channel]

    if cls['change_percent'] > 0 and channel in final_increases:
        change = final_increases[channel]
    elif cls['change_percent'] < 0:
        change = stats['spend'] * cls['change_percent']
    else:
        change = 0

    new_budget = stats['spend'] + change

    print("{:<15} {:>14,} {:>14,} {:>14,} {:<20}".format(
        channel,
        int(stats['spend']),
        int(change),
        int(new_budget),
        cls['classification']
    ))

if increase_channels and unallocated > 0:
    print("-" * 80)
    print("{:<15} {:>14} {:>14} {:>14} {:<20}".format(
        "储备金 (Reserve)", "-", "-", int(unallocated), "可用储备"
    ))

# ===== 汇总统计 =====
print("\n\n【汇总统计】")
print("-" * 100)

total_current = sum(channel_stats[c]['spend'] for c in eligible_channels)
total_change = sum(final_increases.get(c, 0) if classifications[c]['change_percent'] > 0
                  else channel_stats[c]['spend'] * classifications[c]['change_percent']
                  for c in eligible_channels)
total_new = total_current + total_change

print(f"\n当前总预算: ¥{total_current:,.2f}")
print(f"削减总额: ¥{sum(channel_stats[c]['spend'] * abs(classifications[c]['change_percent']) for c in decrease_channels):,.2f}")
print(f"增加总额: ¥{sum(final_increases.values()):,.2f}")
print(f"新总预算: ¥{total_new:,.2f}")
print(f"储备金: ¥{unallocated:,.2f}")

# 分类统计
print(f"\n分类统计:")
cls_counts = {}
for cls in classifications.values():
    name = cls['classification']
    cls_counts[name] = cls_counts.get(name, 0) + 1

for name, count in sorted(cls_counts.items()):
    print(f"  {name}: {count} 个渠道")

print("\n" + "=" * 100)
