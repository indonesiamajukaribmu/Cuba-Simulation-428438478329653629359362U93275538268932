"""
Waterfall Chart — Radar Coverage Detection + Small Android Robot Defense
4 Radius: 1m, 10m, 45m, 10001+ Km² (Global Earth) · External & Internal Attacks
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

STAGES = [
    ('Radar 1m\nSweep',              15,  'radar1'),
    ('Radar 10m\nSweep',             25,  'radar2'),
    ('Radar 45m\nSweep',             40,  'radar3'),
    ('Radar 10001+Km\nGlobal Earth', 80,  'radar4'),
    ('Small Robot\nDetection',       35,  'detect'),
    ('Android Device\nScan',         90,  'scan'),
    ('Hardware Access\nCheck',       120, 'check'),
    ('Identity\nVerification',       150, 'identity'),
    ('Robot\nQuarantine',            70,  'block'),
    ('Ext/Int\nClassification',      60,  'classify'),
    ('Defense\nResponse',            80,  'response'),
    ('All Clear\nSignal',            30,  'confirm'),
]

CAT_COLORS = {
    'radar1':   '#00e5ff',   # cyan — 1m radar (closest)
    'radar2':   '#0077BB',   # blue — 10m radar
    'radar3':   '#3AAFA9',   # teal — 45m radar
    'radar4':   '#8B5CF6',   # purple — global Earth radar
    'detect':   '#FFD700',   # gold — detection
    'scan':     '#3AAFA9',   # teal — scanning
    'check':    '#FF8C00',   # orange — hardware check
    'identity': '#FFD700',   # gold — identity (KEY)
    'block':    '#EF4444',   # red — quarantine
    'classify': '#a855f7',   # purple — classification
    'response': '#0077BB',   # blue — defense response
    'confirm':  '#10B981',   # green — all clear
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
bar_width = 0.58

for i, (label, lat, cat) in enumerate(STAGES):
    h = ends[i] - starts[i]
    color = CAT_COLORS[cat]
    ax.bar(i, h, bottom=starts[i], width=bar_width,
           color=color, edgecolor='white', linewidth=0.8, alpha=0.92)
    ax.text(i, ends[i] + total*0.012, f'+{lat}ms',
            ha='center', va='bottom', fontsize=9.5, color='#F1F5F9', fontweight='bold')
    if i < n - 1:
        ax.plot([i + bar_width/2, i + 1 - bar_width/2], [ends[i], ends[i]],
                color='#64748B', linewidth=0.9, linestyle='--', alpha=0.55)
    ax.text(i, starts[i] + h/2, f'{ends[i]}ms',
            ha='center', va='center', fontsize=8.5, color='white', fontweight='600', alpha=0.85)

ax.bar(n, total, width=bar_width, color='#10B981', edgecolor='white', linewidth=1.2, alpha=0.95)
ax.text(n, total + total*0.012, f'TOTAL\n{total}ms',
        ha='center', va='bottom', fontsize=11, color='#10B981', fontweight='bold')

labels = [s[0] for s in STAGES] + ['TOTAL\nAll\nClear']
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=7.5, color='#CBD5E1')

ax.set_ylim(0, total * 1.22)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f'{int(v)}ms'))
ax.tick_params(axis='y', colors='#CBD5E1', labelsize=9)
ax.grid(axis='y', color='#1E293B', alpha=0.5, linewidth=0.6)
ax.set_axisbelow(True)

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_color('#334155')
ax.spines['bottom'].set_color('#334155')

ax.set_title('Waterfall Chart — Radar Coverage (1m/10m/45m/10001+Km) + Small Android Robot Defense',
             fontsize=13, color='#F1F5F9', fontweight='bold', pad=14, loc='left')
ax.text(0, 1.045,
        'Sistem Kubah Simulasi · 4 Radius Radar · External & Internal Attack Detection via Android Devices',
        transform=ax.transAxes, fontsize=10, color='#94A3B8', style='italic')

ax.set_ylabel('Latensi kumulatif (ms)', color='#CBD5E1', fontsize=10, labelpad=10)

from matplotlib.patches import Patch
legend_elems = [
    Patch(facecolor=CAT_COLORS['radar1'], edgecolor='white', label='Radar 1m'),
    Patch(facecolor=CAT_COLORS['radar2'], edgecolor='white', label='Radar 10m'),
    Patch(facecolor=CAT_COLORS['radar3'], edgecolor='white', label='Radar 45m'),
    Patch(facecolor=CAT_COLORS['radar4'], edgecolor='white', label='Radar 10001+Km (Global Earth)'),
    Patch(facecolor=CAT_COLORS['identity'], edgecolor='white', label='Identity Verification (KEY)'),
    Patch(facecolor=CAT_COLORS['block'], edgecolor='white', label='Robot Quarantine'),
    Patch(facecolor='#10B981', edgecolor='white', label=f'Total: {total}ms → All Clear'),
]
ax.legend(handles=legend_elems, loc='upper left', bbox_to_anchor=(0.0, -0.08),
          ncol=4, frameon=False, labelcolor='#CBD5E1', fontsize=9)

# Highlight Global Earth radar (largest radar range)
ax.annotate('GLOBAL EARTH COVERAGE\n10001+ Km² — radar menjangkau\nseluruh permukaan bumi\ndari serangan luar',
            xy=(3, ends[3]), xytext=(4.2, ends[3] + total*0.22),
            ha='left', va='center', fontsize=9, color='#8B5CF6', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#8B5CF6', lw=1.4),
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#1E293B', edgecolor='#8B5CF6', alpha=0.95))

# Highlight Identity Verification
ax.annotate('KEY: Identity Verification\npenerimaan identitas baru\nuntuk menyetujui pihak\nProses Pencairan Ke Akun',
            xy=(7, ends[7]), xytext=(8.2, ends[7] + total*0.15),
            ha='left', va='center', fontsize=9, color='#FFD700', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#FFD700', lw=1.2),
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#1E293B', edgecolor='#FFD700', alpha=0.95))

out = '/home/z/my-project/download/waterfall_radar_small_robot_defense.png'
plt.savefig(out, dpi=200, facecolor='#0F172A', bbox_inches='tight')
plt.close()
print(f"OK -> {out}")
print(f"Stages: {len(STAGES)}")
print(f"Total: {total}ms")
print(f"Radar 4 ranges: 1m+10m+45m+10001Km = {STAGES[0][1]+STAGES[1][1]+STAGES[2][1]+STAGES[3][1]}ms")
print(f"Identity Verification: {STAGES[7][1]}ms ({STAGES[7][1]/total*100:.1f}%)")
