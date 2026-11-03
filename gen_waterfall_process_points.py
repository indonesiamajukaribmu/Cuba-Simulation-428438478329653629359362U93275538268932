"""
Waterfall Chart — Process Points → Coin Conversion
5 Process Event Types (Sensor/Gateway/Cloud/Intercept/Breach) × 9 Level Tiers
Each event type has its own currency: Rp, RM, SR, $, BTC(Satoshi)
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

# Exchange rates to IDR
RATES = {'Rp':1, '$':15500, 'RM':3500, 'SR':4100, '₿':15}  # BTC as Satoshi: 1₿=Rp15

# Process tiers from screenshot (9 levels × 5 event types)
PROCESS_TIERS = [
    # level, sensor(Rp),  gateway(RM), cloud(SR),  intercept($), breach(₿)
    (1, 1000),   (1, 1000),    # level 1
    (2, 2000),   (2, 2000),    # level 2
    (3, 5000),   (5, 5000),    # level 3 (cloud starts 5,10,50...)
    (4, 10000),  (10, 10000),  # level 4
    (5, 20000),  (20, 20000),  # level 5
    (6, 25000),  (25, 25000),  # level 6
    (7, 50000),  (50, 50000),  # level 7
    (8, 100000), (100, 100000),# level 8
    (9, 200000), (200, 200000),# level 9
]

# Re-structure properly: 9 levels, each with 5 event type values
LEVELS = [
    # (sensor_rp, gateway_rm, cloud_sr, intercept_$, breach_btc)
    (1000,   1,    1,    1,    1000),    # L1
    (2000,   2,    5,    2,    2000),    # L2
    (5000,   5,    10,   10,   5000),    # L3
    (10000,  10,   50,   50,   10000),   # L4
    (20000,  20,   100,  100,  20000),   # L5
    (25000,  25,   200,  200,  25000),   # L6
    (50000,  50,   300,  300,  50000),   # L7
    (100000, 100,  400,  400,  100000),  # L8
    (200000, 200,  500,  500,  200000),  # L9
]

# Sample: show conversion at Level 5 for all 5 types
SAMPLE_LEVEL = 5
lvl_idx = SAMPLE_LEVEL - 1
sensor_rp, gateway_rm, cloud_sr, intercept_usd, breach_btc = LEVELS[lvl_idx]

# Compute IDR equivalent for each
events = [
    ('Sensor\nTriggers',  'Rp', sensor_rp,   RATES['Rp']),
    ('Gateway\nRelays',   'RM', gateway_rm,  RATES['RM']),
    ('Cloud\nWrites',     'SR', cloud_sr,    RATES['SR']),
    ('Intercepts',        '$',  intercept_usd, RATES['$']),
    ('Breaches',          'BTC', breach_btc, RATES['₿']),
]

# IDR equivalents
idr_values = [amt * rate for _, _, amt, rate in events]
coins = [int(idr / 1000) for idr in idr_values]  # 1 coin = Rp 1,000

# Waterfall data (cumulative IDR)
running = 0
starts = []
ends = []
deltas = []
for v in idr_values:
    starts.append(running)
    running += v
    ends.append(running)
    deltas.append(v)
total_idr = running
total_coins = sum(coins)

# Colors per event type
EVENT_COLORS = ['#0077BB', '#3AAFA9', '#8B5CF6', '#EE7733', '#FFD700']

# ===== Plot =====
fig, ax = plt.subplots(figsize=(14, 8), constrained_layout=True)
fig.patch.set_facecolor('#0F172A')
ax.set_facecolor('#0F172A')

n = len(events)
x = np.arange(n + 1)
bar_width = 0.6

# Draw waterfall bars
for i, (label, curr, amt, rate) in enumerate(events):
    h = deltas[i]
    color = EVENT_COLORS[i]
    ax.bar(i, h, bottom=starts[i], width=bar_width,
           color=color, edgecolor='white', linewidth=0.8, alpha=0.92)
    # Value annotation on top
    orig_str = f'{curr} {amt:,.0f}' if curr in ('$',) else f'{curr} {amt:,.0f}'
    idr_str = f'Rp {h/1e3:.0f}K' if h < 1e6 else f'Rp {h/1e6:.2f}M'
    coin_str = f'{coins[i]} coins'
    ax.text(i, ends[i] + total_idr*0.015,
            f'{orig_str}\n≈ {idr_str}\n→ {coin_str}',
            ha='center', va='bottom', fontsize=8.5, color='#F1F5F9', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#1E293B', edgecolor=color, alpha=0.9))
    # Connector
    if i < n - 1:
        ax.plot([i + bar_width/2, i + 1 - bar_width/2], [ends[i], ends[i]],
                color='#64748B', linewidth=0.9, linestyle='--', alpha=0.55)
    # Running total inside bar
    ax.text(i, starts[i] + h/2, f'{idr_str}',
            ha='center', va='center', fontsize=8.5, color='white', fontweight='600', alpha=0.85)

# Total bar
ax.bar(n, total_idr, width=bar_width, color='#10B981', edgecolor='white', linewidth=1.2, alpha=0.95)
ax.text(n, total_idr + total_idr*0.015,
        f'TOTAL\nRp {total_idr/1e6:.2f}M\n→ {total_coins} coins',
        ha='center', va='bottom', fontsize=10, color='#10B981', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#064E3B', edgecolor='#10B981', alpha=0.95))

# X-axis
labels = [e[0] for e in events] + ['TOTAL\nConvert All']
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=10, color='#CBD5E1')

# Y-axis
ax.set_ylim(0, total_idr * 1.30)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(
    lambda v, _: f'Rp {v/1e6:.1f}M' if v >= 1e6 else f'Rp {v/1e3:.0f}K'))
ax.tick_params(axis='y', colors='#CBD5E1', labelsize=9)
ax.grid(axis='y', color='#1E293B', alpha=0.5, linewidth=0.6)
ax.set_axisbelow(True)

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_color('#334155')
ax.spines['bottom'].set_color('#334155')

# Title
ax.set_title(f'Waterfall Chart — Process Points → Coin Conversion (Sample: Level {SAMPLE_LEVEL})',
             fontsize=14, color='#F1F5F9', fontweight='bold', pad=14, loc='left')
ax.text(0, 1.045,
        f'Sistem Kubah Simulasi · 5 Event Types × 9 Levels · 1 coin = Rp 1.000 IDR equivalent',
        transform=ax.transAxes, fontsize=10, color='#94A3B8', style='italic')

ax.set_ylabel('Nilai IDR kumulatif (Rp)', color='#CBD5E1', fontsize=10, labelpad=10)

# Legend
from matplotlib.patches import Patch
legend_elems = [
    Patch(facecolor=EVENT_COLORS[0], edgecolor='white', label='Sensor Triggers (Rp)'),
    Patch(facecolor=EVENT_COLORS[1], edgecolor='white', label='Gateway Relays (RM)'),
    Patch(facecolor=EVENT_COLORS[2], edgecolor='white', label='Cloud Writes (SR)'),
    Patch(facecolor=EVENT_COLORS[3], edgecolor='white', label='Intercepts ($)'),
    Patch(facecolor=EVENT_COLORS[4], edgecolor='white', label='Breaches (BTC)'),
    Patch(facecolor='#10B981', edgecolor='white', label=f'Total → {total_coins} coins'),
]
ax.legend(handles=legend_elems, loc='upper left', bbox_to_anchor=(0.0, -0.08),
          ncol=3, frameon=False, labelcolor='#CBD5E1', fontsize=9)

out = '/home/z/my-project/download/waterfall_process_points_conversion.png'
plt.savefig(out, dpi=200, facecolor='#0F172A', bbox_inches='tight')
plt.close()
print(f"OK -> {out}")
print(f"Sample Level {SAMPLE_LEVEL}:")
for i, (label, curr, amt, rate) in enumerate(events):
    idr = amt * rate
    print(f"  {label.replace(chr(10),' ')}: {curr} {amt} = Rp {idr:,.0f} = {coins[i]} coins")
print(f"Total: Rp {total_idr:,.0f} = {total_coins} coins")
