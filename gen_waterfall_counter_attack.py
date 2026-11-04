"""
Waterfall Chart — Counter-Attack Combo Process
CPU Light Speed + Airplane Mode Deception + Maps Lock + Dead-Switch Active
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

STAGES = [
    ('Attack\nDetected',              10,  'detect'),
    ('Maps Tracker\nActivate',        35,  'maps'),
    ('GPS Location\nLock',            50,  'lock'),
    ('CPU Combo\nInitiate',           25,  'combo'),
    ('Light Speed\nMode ON',          15,  'speed'),
    ('Counter-Attack\nLaunch',        80,  'attack'),
    ('Airplane Mode\nDeception',      60,  'deceive'),
    ('Dead-Switch\nActive',           40,  'dead'),
    ('Maps Secured\n& Locked',        30,  'lock'),
    ('Combo Complete\nShield UP',     20,  'confirm'),
]

CAT_COLORS = {
    'detect':  '#FFD700',
    'maps':    '#00e5ff',
    'lock':    '#0077BB',
    'combo':   '#FF8C00',
    'speed':   '#00FF00',
    'attack':  '#EF4444',
    'deceive': '#8B5CF6',
    'dead':    '#a855f7',
    'confirm': '#10B981',
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
    ax.text(i, ends[i] + total*0.015, f'+{lat}ms',
            ha='center', va='bottom', fontsize=10, color='#F1F5F9', fontweight='bold')
    if i < n - 1:
        ax.plot([i + bar_width/2, i + 1 - bar_width/2], [ends[i], ends[i]],
                color='#64748B', linewidth=0.8, linestyle='--', alpha=0.5)
    ax.text(i, starts[i] + h/2, f'{ends[i]}ms',
            ha='center', va='center', fontsize=9, color='white', fontweight='600', alpha=0.85)

ax.bar(n, total, width=bar_width, color='#10B981', edgecolor='white', linewidth=1.2, alpha=0.95)
ax.text(n, total + total*0.015, f'TOTAL\n{total}ms',
        ha='center', va='bottom', fontsize=11, color='#10B981', fontweight='bold')

labels = [s[0] for s in STAGES] + ['TOTAL\nCombo\nComplete']
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

ax.set_title('Waterfall Chart — Counter-Attack Combo (CPU Light Speed + Airplane Mode + Maps Lock)',
             fontsize=13, color='#F1F5F9', fontweight='bold', pad=14, loc='left')
ax.text(0, 1.045,
        'Sistem Kubah Simulasi · Dead-Switch Active · Light Speed Mode · Airplane Deception · Maps Secured',
        transform=ax.transAxes, fontsize=10, color='#94A3B8', style='italic')

ax.set_ylabel('Latensi kumulatif (ms)', color='#CBD5E1', fontsize=10, labelpad=10)

from matplotlib.patches import Patch
legend_elems = [
    Patch(facecolor=CAT_COLORS['maps'], edgecolor='white', label='Maps Tracker'),
    Patch(facecolor=CAT_COLORS['speed'], edgecolor='white', label='Light Speed Mode (KEY)'),
    Patch(facecolor=CAT_COLORS['attack'], edgecolor='white', label='Counter-Attack'),
    Patch(facecolor=CAT_COLORS['deceive'], edgecolor='white', label='Airplane Mode Deception'),
    Patch(facecolor=CAT_COLORS['dead'], edgecolor='white', label='Dead-Switch Active'),
    Patch(facecolor='#10B981', edgecolor='white', label=f'Total: {total}ms'),
]
ax.legend(handles=legend_elems, loc='upper left', bbox_to_anchor=(0.0, -0.08),
          ncol=3, frameon=False, labelcolor='#CBD5E1', fontsize=9)

ax.annotate('KEY: Light Speed Mode\nkecepatan cahaya maksimum\ncounter-attack instan',
            xy=(4, ends[4]), xytext=(5.2, ends[4] + total*0.18),
            ha='left', va='center', fontsize=9, color='#00FF00', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#00FF00', lw=1.3),
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#1E293B', edgecolor='#00FF00', alpha=0.95))

ax.annotate('Airplane Mode Deception\nattacker ditipu via Android\nposisi tersembunyi',
            xy=(6, ends[6]), xytext=(7.0, ends[6] + total*0.12),
            ha='left', va='center', fontsize=9, color='#8B5CF6', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#8B5CF6', lw=1.2),
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#1E293B', edgecolor='#8B5CF6', alpha=0.95))

out = '/home/z/my-project/download/waterfall_counter_attack_combo.png'
plt.savefig(out, dpi=200, facecolor='#0F172A', bbox_inches='tight')
plt.close()
print(f"OK -> {out}")
print(f"Stages: {len(STAGES)}")
print(f"Total: {total}ms")
print(f"Light Speed: {STAGES[4][1]}ms — kecepatan cahaya")
print(f"Airplane Deception: {STAGES[6][1]}ms")
print(f"Dead-Switch: {STAGES[7][1]}ms — mati daya tapi aktif")
