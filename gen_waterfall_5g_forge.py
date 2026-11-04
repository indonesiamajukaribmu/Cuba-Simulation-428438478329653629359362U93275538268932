"""
Waterfall Chart — 5G Network Speed Boost Process
4G→5G Forge Upgrade · No Lag · Continuous · Fasilitas Mata Defense
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

STAGES = [
    ('Network\nDetected (4G)',     20,  'detect'),
    ('Speed\nLow (Lambat)',        45,  'slow'),
    ('Forge\nInitiate',            30,  'forge'),
    ('4G → 5G\nJump',              25,  'jump'),
    ('5G\nConnected',              15,  'g5'),
    ('Speed\nBoost ON',            10,  'boost'),
    ('No Lag\nNo Tolakan',         20,  'nolag'),
    ('Continuous\nStreaming',      35,  'stream'),
    ('Live Kurs\nSpeed Update',    40,  'kurs'),
    ('Fasilitas Mata\nDefense ON', 30,  'defense'),
]

CAT_COLORS = {
    'detect':  '#FFD700',
    'slow':    '#EF4444',
    'forge':   '#FF8C00',
    'jump':    '#8B5CF6',
    'g5':      '#00FF00',
    'boost':   '#00CC00',
    'nolag':   '#00e5ff',
    'stream':  '#0077BB',
    'kurs':    '#3AAFA9',
    'defense': '#10B981',
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

fig, ax = plt.subplots(figsize=(15, 8.5), constrained_layout=True)
fig.patch.set_facecolor('#0F172A')
ax.set_facecolor('#0F172A')

n = len(STAGES)
x = np.arange(n + 1)
bar_width = 0.6

for i, (label, lat, cat) in enumerate(STAGES):
    h = ends[i] - starts[i]
    color = CAT_COLORS[cat]
    ax.bar(i, h, bottom=starts[i], width=bar_width,
           color=color, edgecolor='white', linewidth=0.6, alpha=0.92)
    ax.text(i, ends[i] + total*0.012, f'+{lat}ms',
            ha='center', va='bottom', fontsize=10, color='#F1F5F9', fontweight='bold')
    if i < n - 1:
        ax.plot([i + bar_width/2, i + 1 - bar_width/2], [ends[i], ends[i]],
                color='#64748B', linewidth=0.8, linestyle='--', alpha=0.5)
    ax.text(i, starts[i] + h/2, f'{ends[i]}ms',
            ha='center', va='center', fontsize=9, color='white', fontweight='600', alpha=0.85)

ax.bar(n, total, width=bar_width, color='#10B981', edgecolor='white', linewidth=1.2, alpha=0.95)
ax.text(n, total + total*0.012, f'TOTAL\n{total}ms\n5G\nFORGE',
        ha='center', va='bottom', fontsize=10, color='#10B981', fontweight='bold')

labels = [s[0] for s in STAGES] + ['TOTAL\n5G\nForge\nComplete']
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=8, color='#CBD5E1')

ax.set_ylim(0, total * 1.25)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f'{int(v)}ms'))
ax.tick_params(axis='y', colors='#CBD5E1', labelsize=9)
ax.grid(axis='y', color='#1E293B', alpha=0.5, linewidth=0.6)
ax.set_axisbelow(True)

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_color('#334155')
ax.spines['bottom'].set_color('#334155')

ax.set_title('Waterfall Chart — 5G Network Forge: 4G→5G Speed Boost (No Lag, Continuous)',
             fontsize=13.5, color='#F1F5F9', fontweight='bold', pad=14, loc='left')
ax.text(0, 1.045,
        'Kubah Simutret · 4G lambat → langsung lompat 5G · Tanpa gangguan · Live Kurs speed update',
        transform=ax.transAxes, fontsize=10, color='#94A3B8', style='italic')

ax.set_ylabel('Network Process Latensi (ms)', color='#CBD5E1', fontsize=10, labelpad=10)

from matplotlib.patches import Patch
legend_elems = [
    Patch(facecolor=CAT_COLORS['slow'], edgecolor='white', label='4G Lambat (Slow)'),
    Patch(facecolor=CAT_COLORS['forge'], edgecolor='white', label='5G Forge Initiate'),
    Patch(facecolor=CAT_COLORS['jump'], edgecolor='white', label='4G → 5G Jump'),
    Patch(facecolor=CAT_COLORS['g5'], edgecolor='white', label='5G Connected'),
    Patch(facecolor=CAT_COLORS['nolag'], edgecolor='white', label='No Lag / No Tolakan'),
    Patch(facecolor='#10B981', edgecolor='white', label=f'Total: {total}ms → 5G Forge'),
]
ax.legend(handles=legend_elems, loc='upper left', bbox_to_anchor=(0.0, -0.08),
          ncol=3, frameon=False, labelcolor='#CBD5E1', fontsize=9)

ax.annotate('KEY: 4G → 5G Jump\njaringan lambat (4G)\nlangsung lompat menjadi 5G\ntanpa tolakan, langsung lanjut',
            xy=(3, ends[3]), xytext=(4.2, ends[3] + total*0.18),
            ha='left', va='center', fontsize=9, color='#8B5CF6', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#8B5CF6', lw=1.3),
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#1E293B', edgecolor='#8B5CF6', alpha=0.95))

ax.annotate('5G Connected\nkecepatan maksimum\ntanpa gangguan\nlangsung lancar',
            xy=(4, ends[4]), xytext=(5.0, ends[4] + total*0.10),
            ha='left', va='center', fontsize=9, color='#00FF00', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#00FF00', lw=1.2),
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#1E293B', edgecolor='#00FF00', alpha=0.95))

out = '/home/z/my-project/download/waterfall_5g_network_forge.png'
plt.savefig(out, dpi=200, facecolor='#0F172A', bbox_inches='tight')
plt.close()
print(f"OK -> {out}")
print(f"Stages: {len(STAGES)}")
print(f"Total: {total}ms")
print(f"4G→5G Jump: {STAGES[3][1]}ms")
print(f"5G Connected: {STAGES[4][1]}ms")
