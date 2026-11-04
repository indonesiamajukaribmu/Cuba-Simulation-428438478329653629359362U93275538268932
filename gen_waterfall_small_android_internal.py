"""
Waterfall Chart — Small Android Robot Internal Attack Defense
Serangan Dalam via Android Device · View-Only Mode · Malware Block
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

STAGES = [
    ('Android Robot\nDetected (Internal)',  20,  'detect'),
    ('Android Device\nScan',                45,  'scan'),
    ('Hardware Access\nCheck',              55,  'check'),
    ('Malware Payload\nDetect',             50,  'scan'),
    ('Virus/Malware\nBlock',                40,  'block'),
    ('View-Only\nMode ON',                  30,  'viewonly'),
    ('Robot\nQuarantine',                   35,  'quarantine'),
    ('Hardware\nLockdown',                  25,  'lock'),
    ('Safe Internal\nViewing',              15,  'safe'),
    ('Robot\nNeutralized',                  10,  'neutralize'),
]

CAT_COLORS = {
    'detect':     '#FFD700',
    'scan':       '#00e5ff',
    'check':      '#FF8C00',
    'block':      '#EF4444',
    'viewonly':   '#00FF00',
    'quarantine': '#a855f7',
    'lock':       '#0077BB',
    'safe':       '#10B981',
    'neutralize': '#8B5CF6',
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
ax.text(n, total + total*0.012, f'TOTAL\n{total}ms\nROBOT\nNEUTRALIZED',
        ha='center', va='bottom', fontsize=10, color='#10B981', fontweight='bold')

labels = [s[0] for s in STAGES] + ['TOTAL\nInternal\nDefense\nComplete']
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=7, color='#CBD5E1')

ax.set_ylim(0, total * 1.25)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f'{int(v)}ms'))
ax.tick_params(axis='y', colors='#CBD5E1', labelsize=9)
ax.grid(axis='y', color='#1E293B', alpha=0.5, linewidth=0.6)
ax.set_axisbelow(True)

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_color('#334155')
ax.spines['bottom'].set_color('#334155')

ax.set_title('Waterfall Chart — Small Android Robot Internal Attack Defense (Serangan Dalam)',
             fontsize=13.5, color='#F1F5F9', fontweight='bold', pad=14, loc='left')
ax.text(0, 1.045,
        'Kubah Simutret · Robot Android serangan dalam · View-Only + Malware Block + Hardware Lockdown',
        transform=ax.transAxes, fontsize=10, color='#94A3B8', style='italic')

ax.set_ylabel('Defense Latensi (ms)', color='#CBD5E1', fontsize=10, labelpad=10)

from matplotlib.patches import Patch
legend_elems = [
    Patch(facecolor=CAT_COLORS['detect'], edgecolor='white', label='Android Robot Detection'),
    Patch(facecolor=CAT_COLORS['scan'], edgecolor='white', label='Device + Malware Scan'),
    Patch(facecolor=CAT_COLORS['block'], edgecolor='white', label='Virus/Malware Block'),
    Patch(facecolor=CAT_COLORS['viewonly'], edgecolor='white', label='View-Only Mode (KEY)'),
    Patch(facecolor=CAT_COLORS['quarantine'], edgecolor='white', label='Robot Quarantine'),
    Patch(facecolor='#10B981', edgecolor='white', label=f'Total: {total}ms → Neutralized'),
]
ax.legend(handles=legend_elems, loc='upper left', bbox_to_anchor=(0.0, -0.08),
          ncol=3, frameon=False, labelcolor='#CBD5E1', fontsize=9)

ax.annotate('KEY: View-Only Mode\nrobot internal cukup\nlihat tampilan saja\nmalware diblokir',
            xy=(5, ends[5]), xytext=(6.2, ends[5] + total*0.18),
            ha='left', va='center', fontsize=9, color='#00FF00', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#00FF00', lw=1.3),
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#1E293B', edgecolor='#00FF00', alpha=0.95))

ax.annotate('Malware Block\nvirus dari Android\ndiblokir untuk cegah\nkerusakan',
            xy=(4, ends[4]), xytext=(3.0, ends[4] + total*0.25),
            ha='left', va='center', fontsize=9, color='#EF4444', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#EF4444', lw=1.2),
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#1E293B', edgecolor='#EF4444', alpha=0.95))

out = '/home/z/my-project/download/waterfall_small_android_internal_defense.png'
plt.savefig(out, dpi=200, facecolor='#0F172A', bbox_inches='tight')
plt.close()
print(f"OK -> {out}")
print(f"Stages: {len(STAGES)}")
print(f"Total: {total}ms")
print(f"View-Only Mode: {STAGES[5][1]}ms ({STAGES[5][1]/total*100:.1f}%)")
print(f"Malware Block: {STAGES[4][1]}ms")
