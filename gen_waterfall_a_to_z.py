"""
Waterfall Chart — Full A-Z Pencairan Process
Play Store Apps → Download → Install → Coin Convert → 34 Tier Multi-Currency → Uang Tunai
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

STAGES = [
    ('Play Store\nOpen',                30,  'app'),
    ('DANA App\nDownload',              45,  'download'),
    ('DANA App\nInstall',               35,  'install'),
    ('GoPay App\nDownload+Install',     70,  'download'),
    ('BSI Mobile\nDownload+Install',    65,  'download'),
    ('BNI Mobile\nDownload+Install',    60,  'download'),
    ('BRI Mobile\nDownload+Install',    55,  'download'),
    ('Danamon\nDownload+Install',       50,  'download'),
    ('Coin → Tunai\nConvert',           80,  'convert'),
    ('34 Tier\nMulti-Currency',         90,  'tier'),
    ('Uang Tunai\nReceived',            40,  'cash'),
    ('A-Z Process\nComplete',           20,  'complete'),
]

CAT_COLORS = {
    'app':       '#00FF00',
    'download':  '#00e5ff',
    'install':   '#0077BB',
    'convert':   '#FFD700',
    'tier':      '#FF8C00',
    'cash':      '#10B981',
    'complete':  '#00FF00',
}

deltas = [s[1] for s in STAGES]
running = 0
starts = []
ends = []
for d in deltas:
    starts.append(running)
    running += d
    ends.append(running)
total = running

fig, ax = plt.subplots(figsize=(17, 9), constrained_layout=True)
fig.patch.set_facecolor('#0F172A')
ax.set_facecolor('#0F172A')

n = len(STAGES)
x = np.arange(n + 1)
bar_width = 0.55

for i, (label, lat, cat) in enumerate(STAGES):
    h = ends[i] - starts[i]
    color = CAT_COLORS[cat]
    ax.bar(i, h, bottom=starts[i], width=bar_width,
           color=color, edgecolor='white', linewidth=0.6, alpha=0.92)
    ax.text(i, ends[i] + total*0.010, f'+{lat}ms',
            ha='center', va='bottom', fontsize=9, color='#F1F5F9', fontweight='bold')
    if i < n - 1:
        ax.plot([i + bar_width/2, i + 1 - bar_width/2], [ends[i], ends[i]],
                color='#64748B', linewidth=0.7, linestyle='--', alpha=0.5)
    ax.text(i, starts[i] + h/2, f'{ends[i]}',
            ha='center', va='center', fontsize=8, color='white', fontweight='600', alpha=0.85)

ax.bar(n, total, width=bar_width, color='#10B981', edgecolor='white', linewidth=1.2, alpha=0.95)
ax.text(n, total + total*0.010, f'TOTAL\n{total}ms\nA-Z\nCOMPLETE',
        ha='center', va='bottom', fontsize=10, color='#10B981', fontweight='bold')

labels = [s[0] for s in STAGES] + ['TOTAL\nA-Z\nPencairan\nComplete']
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=7, color='#CBD5E1', rotation=15, ha='right')

ax.set_ylim(0, total * 1.22)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f'{int(v)}ms'))
ax.tick_params(axis='y', colors='#CBD5E1', labelsize=9)
ax.grid(axis='y', color='#1E293B', alpha=0.5, linewidth=0.5)
ax.set_axisbelow(True)

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_color('#334155')
ax.spines['bottom'].set_color('#334155')

ax.set_title('Waterfall Chart — Full A-Z Pencairan Process (Play Store Apps → Coin → Tunai)',
             fontsize=13.5, color='#F1F5F9', fontweight='bold', pad=14, loc='left')
ax.text(0, 1.045,
        'Kubah Simutret · 6 Apps via Play Store · Coin → Tunai · 34 Tier Multi-Currency (Rp/$/RM/SR/¥/₹)',
        transform=ax.transAxes, fontsize=10, color='#94A3B8', style='italic')

ax.set_ylabel('Process Latensi (ms)', color='#CBD5E1', fontsize=10, labelpad=10)

from matplotlib.patches import Patch
legend_elems = [
    Patch(facecolor=CAT_COLORS['app'], edgecolor='white', label='Play Store'),
    Patch(facecolor=CAT_COLORS['download'], edgecolor='white', label='App Download/Install'),
    Patch(facecolor=CAT_COLORS['convert'], edgecolor='white', label='Coin → Tunai Convert'),
    Patch(facecolor=CAT_COLORS['tier'], edgecolor='white', label='34 Tier Multi-Currency'),
    Patch(facecolor=CAT_COLORS['cash'], edgecolor='white', label='Uang Tunai Received'),
    Patch(facecolor='#10B981', edgecolor='white', label=f'Total: {total}ms → A-Z Complete'),
]
ax.legend(handles=legend_elems, loc='upper left', bbox_to_anchor=(0.0, -0.08),
          ncol=3, frameon=False, labelcolor='#CBD5E1', fontsize=9)

ax.annotate('KEY: Coin → Tunai\nkonversi coin menjadi\nuang tunai via\n34 tier multi-currency',
            xy=(8, ends[8]), xytext=(9.2, ends[8] + total*0.15),
            ha='left', va='center', fontsize=9, color='#FFD700', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#FFD700', lw=1.3),
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#1E293B', edgecolor='#FFD700', alpha=0.95))

ax.annotate('34 Tier Multi-Currency\nRp / $ / RM / SR / ¥ / ₹\nkonversi otomatis\nke mata uang terbaik',
            xy=(9, ends[9]), xytext=(10.2, ends[9] + total*0.08),
            ha='left', va='center', fontsize=9, color='#FF8C00', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#FF8C00', lw=1.2),
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#1E293B', edgecolor='#FF8C00', alpha=0.95))

out = '/home/z/my-project/download/waterfall_a_to_z_pencairan.png'
plt.savefig(out, dpi=200, facecolor='#0F172A', bbox_inches='tight')
plt.close()
print(f"OK -> {out}")
print(f"Stages: {len(STAGES)}")
print(f"Total: {total}ms")
print(f"6 apps: DANA, GoPay, BSI, BNI, BRI, Danamon")
print(f"34 tier multi-currency: Rp/$/RM/SR/¥/₹")
