import csv
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

with open('campaign_data_week1_china.csv', 'r', encoding='utf-8') as f:
    content = f.read()

# Split by lines and parse
lines = content.strip().split('\n')
header_line = lines[0]
header = header_line.split('、')

data_rows = lines[1:]

# Parse data
parsed_rows = []
for row in data_rows:
    if row.strip():
        values = row.split(',')
        if len(values) == len(header):
            parsed_rows.append(dict(zip(header, values)))

print('=' * 80)
print('营销活动数据分析报告 (Marketing Campaign Data Analysis)')
print('=' * 80)

print('\n【数据质量检查】(Data Quality Check)')
print(f'总数据行数 (Total rows): {len(parsed_rows)}')
print(f'\n缺失值检查 (Missing values):')
missing_impr = sum(1 for r in parsed_rows if not r.get('展示次数') or r.get('展示次数').strip() == '')
print(f'  展示次数 (Impressions): {missing_impr} 个缺失值')
print(f'  Note: 小程序推送渠道无展示次数数据 (Mini Program has no impression data)')

print('\n' + '=' * 80)
print('【漏斗分析】(Funnel Analysis)')
print('=' * 80)

# Calculate metrics by channel
benchmarks = {
    '微信广告': {'ctr': 2.5, 'cvr': 3.8},
    '百度推广': {'ctr': 5.0, 'cvr': 4.5},
    '抖音广告': {'ctr': 2.0, 'cvr': 0.9},
    '小程序推送': {'ctr': 15.0, 'cvr': 2.1}
}

channel_metrics = defaultdict(lambda: {'impressions': 0, 'clicks': 0, 'conversions': 0, 'count': 0})

for row in parsed_rows:
    channel = row['渠道']
    channel_metrics[channel]['count'] += 1

    try:
        impr = row.get('展示次数', '').strip()
        clicks = float(row.get('点击次数', 0))
        conv = float(row.get('转化次数', 0))

        if impr:
            channel_metrics[channel]['impressions'] += int(impr)
        channel_metrics[channel]['clicks'] += clicks
        channel_metrics[channel]['conversions'] += conv
    except:
        pass

# Calculate and display metrics
for channel in ['微信广告', '百度推广', '抖音广告', '小程序推送']:
    metrics = channel_metrics[channel]
    print(f'\n--- {channel} ---')

    if metrics['impressions'] > 0:
        ctr = (metrics['clicks'] / metrics['impressions']) * 100
        cvr = (metrics['conversions'] / metrics['clicks']) * 100

        benchmark_ctr = benchmarks[channel]['ctr']
        benchmark_cvr = benchmarks[channel]['cvr']

        print(f'活动数量 (Campaigns): {metrics["count"]}')
        print(f'展示次数 (Impressions): {metrics["impressions"]:,}')
        print(f'点击次数 (Clicks): {metrics["clicks"]:,}')
        print(f'转化次数 (Conversions): {metrics["conversions"]:,}')
        print(f'\nCTR (点击率): {ctr:.2f}% (目标: {benchmark_ctr}%) ', end='')
        if ctr >= benchmark_ctr:
            print('✓ 达标')
        else:
            print(f'✗ 未达标 (差距: {benchmark_ctr - ctr:.2f}%)')

        print(f'CVR (转化率): {cvr:.2f}% (目标: {benchmark_cvr}%) ', end='')
        if cvr >= benchmark_cvr:
            print('✓ 达标')
        else:
            print(f'✗ 未达标 (差距: {benchmark_cvr - cvr:.2f}%)')
    else:
        print(f'活动数量 (Campaigns): {metrics["count"]}')
        print(f'点击次数 (Clicks): {metrics["clicks"]:,}')
        print(f'转化次数 (Conversions): {metrics["conversions"]:,}')

        if metrics['clicks'] > 0:
            cvr = (metrics['conversions'] / metrics['clicks']) * 100
            benchmark_cvr = benchmarks[channel]['cvr']
            print(f'\nCVR (转化率): {cvr:.2f}% (目标: {benchmark_cvr}%) ', end='')
            if cvr >= benchmark_cvr:
                print('✓ 达标')
            else:
                print(f'✗ 未达标 (差距: {benchmark_cvr - cvr:.2f}%)')
        print('  Note: 无展示次数数据，无法计算CTR (No impression data for CTR)')
