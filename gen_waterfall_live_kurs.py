"""
Waterfall Chart — Live Kurs Exchange Rate Movements
Sistem Kubah Simulasi · 6 Currency Pairs · Portfolio Value Change
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

# Base portfolio positions (in each currency)
POSITIONS = [
    ('USD', '$',  1000,   15500,  +1.2),   # amount, base_rate, weekly_change%
    ('MYR', 'RM', 500,    3500,   -0.5),
    ('SAR', 'SR', 200,    4100,   +0.3),
    ('JPY', '¥',  10000,  105,    -0.8),
    ('INR', '₹',  5000,   190,    +0.6),
    ('BTC', '₿',  50,     15,     +3.5),   # Satoshi
]

# Base portfolio value in IDR
BASE_PORTFOLIO = 100_000_000  # Rp 100 juta

# Compute each position's IDR value and change
deltas = []
labels = []
colors = []
for curr, sym, amt, rate, pct in POSITIONS:
    base_idr = amt * rate
    delta_idr = base_idr * pct / 100
    deltas.append(delta_idr)
    labels.append(f'{sym} {amt:,.0f}\n({curr}/IDR)\n{pct:+.1f}%')
    colors.append('#10B981' if delta_idr >= 0 else '#EF4444')

# Build waterfall cumulative
running = BASE_PORTFOLIO
starts = []
ends = []
for d in deltas:
    starts.append(running)
    running += d
    ends.append(running)
final_total = running
total_change = sum(deltas)

fig, ax = plt.subplots(figsize=(15, 8.5), constrained_layout=True)
fig.patch.set_facecolor('#0F172A')
ax.set_facecolor('#0F172A')

n = len(POSITIONS)
x = np.arange(n + 2)  # +1 for base, +1 for final
bar_width = 0.58

# Base portfolio bar (starting point)
ax.bar(0, BASE_PORTFOLIO, width=bar_width, color='#00e5ff', edgecolor='white', linewidth=1, alpha=0.9)
ax.text(0, BASE_PORTFOLIO + total_change*0.03, f'BASE\nRp {BASE_PORTFOLIO/1e6:.0f}M',
        ha='center', va='bottom', fontsize=9, color='#00e5ff', fontweight='bold')

# Waterfall bars (each currency change)
for i in range(n):
    h = deltas[i]
    bottom = starts[i]
    # For negative deltas, the bar goes down
    if h >= 0:
        ax.bar(i + 1, h, bottom=bottom, width=bar_width, color=colors[i], edgecolor='white', linewidth=0.8, alpha=0.92)
        ax.text(i + 1, ends[i] + abs(total_change)*0.05, f'+Rp {h/1e3:.0f}K',
                ha='center', va='bottom', fontsize=8.5, color='#10B981', fontweight='bold')
    else:
        ax.bar(i + 1, abs(h), bottom=ends[i], width=bar_width, color=colors[i], edgecolor='white', linewidth=0.8, alpha=0.92)
        ax.text(i + 1, ends[i] - abs(total_change)*0.05, f'-Rp {abs(h)/1e3:.0f}K',
                ha='center', va='top', fontsize=8.5, color='#EF4444', fontweight='bold')
    # Connector
    if i < n - 1:
        ax.plot([i + 1 + bar_width/2, i + 2 - bar_width/2], [ends[i], ends[i]],
                color='#64748B', linewidth=0.9, linestyle='--', alpha=0.55)

# Final total bar
ax.bar(n + 1, final_total, width=bar_width, color='#10B981' if total_change >= 0 else '#EF4444', edgecolor='white', linewidth=1.2, alpha=0.95)
ax.text(n + 1, final_total + abs(total_change)*0.03,
        f'FINAL\nRp {final_total/1e6:.2f}M\n({total_change/BASE_PORTFOLIO*100:+.2f}%)' if False else
        f'FINAL\nRp {final_total/1e6:.2f}M\n(+{total_change/BASE_PORTFOLIO*100:.3f}%)',
        ha='center', va='bottom', fontsize=9, color='#10B981', fontweight='bold')

# X-axis
all_labels = ['BASE\nPortfolio'] + labels + [f'FINAL\nRp {final_total/1e6:.2f}M']
ax.set_xticks(x)
ax.set_xticklabels(all_labels, fontsize=8, color='#CBD5E1')

# Y-axis
ax.set_ylim(BASE_PORTFOLIO * 0.998, final_total * 1.005)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f'Rp {v/1e6:.2f}M'))
ax.tick_params(axis='y', colors='#CBD5E1', labelsize=9)
ax.grid(axis='y', color='#1E293B', alpha=0.5, linewidth=0.6)
ax.set_axisbelow(True)

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_color('#334155')
ax.spines['bottom'].set_color('#334155')

ax.set_title('Waterfall Chart — Live Kurs Exchange Rate Movements (Weekly Portfolio Change)',
             fontsize=14, color='#F1F5F9', fontweight='bold', pad=14, loc='left')
ax.text(0, 1.045,
        'Sistem Kubah Simulasi · 6 Currency Pairs · Base Rp 100M · Real-time IDR equivalent',
        transform=ax.transAxes, fontsize=10, color='#94A3B8', style='italic')

ax.set_ylabel('Portfolio Value (IDR)', color='#CBD5E1', fontsize=10, labelpad=10)

from matplotlib.patches import Patch
legend_elems = [
    Patch(facecolor='#00e5ff', edgecolor='white', label='Base Portfolio'),
    Patch(facecolor='#10B981', edgecolor='white', label='Currency Gain (▲)'),
    Patch(facecolor='#EF4444', edgecolor='white', label='Currency Loss (▼)'),
    Patch(facecolor='#10B981', edgecolor='white', label=f'Final: +Rp {total_change/1e3:.0f}K ({total_change/BASE_PORTFOLIO*100:.3f}%)'),
]
ax.legend(handles=legend_elems, loc='upper left', bbox_to_anchor=(0.0, -0.08),
          ncol=4, frameon=False, labelcolor='#CBD5E1', fontsize=9)

# Highlight BTC (biggest mover)
btc_idx = 5
ax.annotate(f'BTC biggest move\n+{POSITIONS[5][4]:.1f}%',
            xy=(btc_idx + 1, ends[btc_idx]), xytext=(btc_idx + 0.3, ends[btc_idx] + abs(total_change)*0.5),
            ha='left', va='center', fontsize=9, color='#FFD700', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#FFD700', lw=1.2),
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#1E293B', edgecolor='#FFD700', alpha=0.95))

out = '/home/z/my-project/download/waterfall_live_kurs_movements.png'
plt.savefig(out, dpi=200, facecolor='#0F172A', bbox_inches='tight')
plt.close()
print(f"OK -> {out}")
print(f"Base: Rp {BASE_PORTFOLIO/1e6:.0f}M")
for curr, sym, amt, rate, pct in POSITIONS:
    delta = amt * rate * pct / 100
    print(f"  {sym} {amt}: {pct:+.1f}% → {delta:+,.0f} IDR")
print(f"Total change: +Rp {total_change:,.0f} (+{total_change/BASE_PORTFOLIO*100:.3f}%)")
print(f"Final: Rp {final_total:,.0f}")
