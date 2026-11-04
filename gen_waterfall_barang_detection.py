"""
Waterfall Chart — Barang Detection Process
Kubah Simutret · Pusat Keluar Masuk Barang · Deteksi Barang Menghindari Robot
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

STAGES = [
    ('Barang\nEnter Zone',            20,  'enter'),
    ('Radar\nScan 1m',                15,  'radar'),
    ('Radar\nScan 10m',               25,  'radar'),
    ('Radar\nScan 45m',               35,  'radar'),
    ('Radar\nScan 10001Km',           50,  'radar'),
    ('Robot Evasion\nDetect',         80,  'evasion'),
    ('Barang\nIdentify',              60,  'identify'),
    ('Prohibited\nCheck',             45,  'check'),
    ('Entry\nBlock/Allow',            30,  'decision'),
    ('Log &\nArchive',                25,  'log'),
]

CAT_COLORS = {
    'enter':     '#FFD700',
    'radar':     '#00e5ff',
    'evasion':   '#EF4444',
    'identify':  '#00FF00',
    'check':     '#FF8C00',
    'decision':  '#8B5CF6',
    'log':       '#10B981',
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
ax.text(n, total + total*0.012, f'TOTAL\n{total}ms',
        ha='center', va='bottom', fontsize=11, color='#10B981', fontweight='bold')

labels = [s[0] for s in STAGES] + ['TOTAL\nDetection\nComplete']
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=8, color='#CBD5E1')

ax.set_ylim(0, total * 1.22)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f'{int(v)}ms'))
ax.tick_params(axis='y', colors='#CBD5E1', labelsize=9)
ax.grid(axis='y', color='#1E293B', alpha=0.5, linewidth=0.6)
ax.set_axisbelow(True)

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_color('#334155')
ax.spines['bottom'].set_color('#334155')

ax.set_title('Waterfall Chart — Barang Detection Process (Kubah Simutret)',
             fontsize=14, color='#F1F5F9', fontweight='bold', pad=14, loc='left')
ax.text(0, 1.045,
        'Pusat Keluar Masuk Barang · Deteksi barang menghindari robot berkebolehan tinggi · 4 Radius Radar',
        transform=ax.transAxes, fontsize=10, color='#94A3B8', style='italic')

ax.set_ylabel('Detection Latensi (ms)', color='#CBD5E1', fontsize=10, labelpad=10)

from matplotlib.patches import Patch
legend_elems = [
    Patch(facecolor=CAT_COLORS['enter'], edgecolor='white', label='Barang Enter Zone'),
    Patch(facecolor=CAT_COLORS['radar'], edgecolor='white', label='Radar Scan (4 radius)'),
    Patch(facecolor=CAT_COLORS['evasion'], edgecolor='white', label='Robot Evasion Detection (KEY)'),
    Patch(facecolor=CAT_COLORS['identify'], edgecolor='white', label='Barang Identify'),
    Patch(facecolor=CAT_COLORS['check'], edgecolor='white', label='Prohibited Check'),
    Patch(facecolor=CAT_COLORS['decision'], edgecolor='white', label='Block/Allow Decision'),
    Patch(facecolor='#10B981', edgecolor='white', label=f'Total: {total}ms'),
]
ax.legend(handles=legend_elems, loc='upper left', bbox_to_anchor=(0.0, -0.08),
          ncol=3, frameon=False, labelcolor='#CBD5E1', fontsize=9)

ax.annotate('KEY: Robot Evasion Detect\nbarang baru menghindari\nrobot berkebolehan tinggi\ndidetect di tahap ini',
            xy=(5, ends[5]), xytext=(6.2, ends[5] + total*0.20),
            ha='left', va='center', fontsize=9, color='#EF4444', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#EF4444', lw=1.3),
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#1E293B', edgecolor='#EF4444', alpha=0.95))

out = '/home/z/my-project/download/waterfall_barang_detection.png'
plt.savefig(out, dpi=200, facecolor='#0F172A', bbox_inches='tight')
plt.close()
print(f"OK -> {out}")
print(f"Stages: {len(STAGES)}")
print(f"Total: {total}ms")
print(f"Robot Evasion Detect: {STAGES[5][1]}ms ({STAGES[5][1]/total*100:.1f}%)")
