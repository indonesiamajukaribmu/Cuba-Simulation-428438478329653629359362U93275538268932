"""
Waterfall Chart — Robot Destroyer + Building Controller Defense Process
Sistem Kubah Simulasi · Anti-Bot Self-Destruct + Premium Building Protection
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

STAGES = [
    ('Robot\nDetection',           25,  'detect'),
    ('Bot Signature\nAnalysis',    60,  'analyze'),
    ('AI\nClassification',         80,  'analyze'),
    ('Auto-Lock\nRobot',           100, 'lock'),
    ('Self-Destruct\nTrigger',     120, 'destroy'),
    ('EMP\nPulse',                 90,  'destroy'),
    ('Robot\nNeutralized',         50,  'confirm'),
    ('Building Alert\nBroadcast',  40,  'building'),
    ('Building Lockdown\nCheck',   70,  'building'),
    ('All Buildings\nSecured',     35,  'confirm'),
]

CAT_COLORS = {
    'detect':   '#FFD700',   # gold — detection
    'analyze':  '#3AAFA9',   # teal — analysis
    'lock':     '#FF8C00',   # orange — lock
    'destroy':  '#EF4444',   # red — destruction (KEY)
    'building': '#00e5ff',   # cyan — building control
    'confirm':  '#10B981',   # green — confirmation
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

fig, ax = plt.subplots(figsize=(16, 9), constrained_layout=True)
fig.patch.set_facecolor('#0F172A')
ax.set_facecolor('#0F172A')

n = len(STAGES)
x = np.arange(n + 1)
bar_width = 0.6

for i, (label, lat, cat) in enumerate(STAGES):
    h = ends[i] - starts[i]
    color = CAT_COLORS[cat]
    ax.bar(i, h, bottom=starts[i], width=bar_width,
           color=color, edgecolor='white', linewidth=0.8, alpha=0.92)
    ax.text(i, ends[i] + total*0.012, f'+{lat}ms',
            ha='center', va='bottom', fontsize=10, color='#F1F5F9', fontweight='bold')
    if i < n - 1:
        ax.plot([i + bar_width/2, i + 1 - bar_width/2], [ends[i], ends[i]],
                color='#64748B', linewidth=0.9, linestyle='--', alpha=0.55)
    ax.text(i, starts[i] + h/2, f'{ends[i]}ms',
            ha='center', va='center', fontsize=9, color='white', fontweight='600', alpha=0.85)

ax.bar(n, total, width=bar_width, color='#10B981', edgecolor='white', linewidth=1.2, alpha=0.95)
ax.text(n, total + total*0.012, f'TOTAL\n{total}ms',
        ha='center', va='bottom', fontsize=11, color='#10B981', fontweight='bold')

labels = [s[0] for s in STAGES] + ['TOTAL\nDefenses\nActive']
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

ax.set_title('Waterfall Chart — Robot Destroyer + Building Controller Defense (Anti-Bot Self-Destruct)',
             fontsize=13.5, color='#F1F5F9', fontweight='bold', pad=14, loc='left')
ax.text(0, 1.045,
        'Sistem Kubah Simulasi · 10 Tahap · Robot musnah otomatis + Bangunan Perdana Terproteksi',
        transform=ax.transAxes, fontsize=10, color='#94A3B8', style='italic')

ax.set_ylabel('Latensi kumulatif (ms)', color='#CBD5E1', fontsize=10, labelpad=10)

from matplotlib.patches import Patch
legend_elems = [
    Patch(facecolor=CAT_COLORS['detect'], edgecolor='white', label='Robot Detection'),
    Patch(facecolor=CAT_COLORS['analyze'], edgecolor='white', label='AI Analysis'),
    Patch(facecolor=CAT_COLORS['lock'], edgecolor='white', label='Auto-Lock'),
    Patch(facecolor=CAT_COLORS['destroy'], edgecolor='white', label='Self-Destruct + EMP (KEY)'),
    Patch(facecolor=CAT_COLORS['building'], edgecolor='white', label='Building Control'),
    Patch(facecolor=CAT_COLORS['confirm'], edgecolor='white', label='Confirmation'),
    Patch(facecolor='#10B981', edgecolor='white', label=f'Total: {total}ms'),
]
ax.legend(handles=legend_elems, loc='upper left', bbox_to_anchor=(0.0, -0.08),
          ncol=4, frameon=False, labelcolor='#CBD5E1', fontsize=9)

# Highlight Self-Destruct Trigger (KEY)
ax.annotate('KEY: Self-Destruct Trigger\nRobot musnah otomatis\n— tidak bisa ditembus\napapun jenis robotnya',
            xy=(4, ends[4]), xytext=(5.2, ends[4] + total*0.20),
            ha='left', va='center', fontsize=9, color='#EF4444', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#EF4444', lw=1.4),
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#1E293B', edgecolor='#EF4444', alpha=0.95))

# Highlight Building Lockdown
ax.annotate('Building Lockdown\nBangunan perdana tinggi\nterproteksi otomatis',
            xy=(8, ends[8]), xytext=(9.0, ends[8] + total*0.12),
            ha='left', va='center', fontsize=9, color='#00e5ff', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#00e5ff', lw=1.2),
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#1E293B', edgecolor='#00e5ff', alpha=0.95))

out = '/home/z/my-project/download/waterfall_robot_destroyer_building.png'
plt.savefig(out, dpi=200, facecolor='#0F172A', bbox_inches='tight')
plt.close()
print(f"OK -> {out}")
print(f"Stages: {len(STAGES)}")
print(f"Total: {total}ms")
print(f"Self-Destruct: {STAGES[4][1]}ms ({STAGES[4][1]/total*100:.1f}%)")
print(f"Building Lockdown: {STAGES[8][1]}ms ({STAGES[8][1]/total*100:.1f}%)")
