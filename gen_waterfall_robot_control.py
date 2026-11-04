"""
Waterfall Chart — Robot Entry/Exit Control Process
ChatGPT.AI Robot + Gemini.AI Robot + Arduino Robot + Master Switch (Mode Bahaya)
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

STAGES = [
    ('Master Switch\nON',              15,  'master'),
    ('ChatGPT.AI\nRobot Allowed',      40,  'chatgpt'),
    ('ChatGPT.AI\nRemote Control',     55,  'chatgpt'),
    ('ChatGPT.AI\nEnter Fasilitas',    45,  'chatgpt'),
    ('Gemini.AI\nRobot Allowed',       35,  'gemini'),
    ('Gemini.AI\nRemote Control',      50,  'gemini'),
    ('Gemini.AI\nEnter Fasilitas',     40,  'gemini'),
    ('Arduino\nRobot Entry',           30,  'arduino'),
    ('Arduino\nRobot Exit',            25,  'arduino'),
    ('All Robots\nActive (Bahaya)',    20,  'bahaya'),
]

CAT_COLORS = {
    'master':   '#00FF00',
    'chatgpt':  '#00e5ff',
    'gemini':   '#FFD700',
    'arduino':  '#FF8C00',
    'bahaya':   '#EF4444',
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

fig, ax = plt.subplots(figsize=(16, 8.5), constrained_layout=True)
fig.patch.set_facecolor('#0F172A')
ax.set_facecolor('#0F172A')

n = len(STAGES)
x = np.arange(n + 1)
bar_width = 0.58

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
ax.text(n, total + total*0.012, f'TOTAL\n{total}ms\nALL\nROBOTS',
        ha='center', va='bottom', fontsize=10, color='#10B981', fontweight='bold')

labels = [s[0] for s in STAGES] + ['TOTAL\nAll Robots\nActive']
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=7.5, color='#CBD5E1', rotation=12, ha='right')

ax.set_ylim(0, total * 1.25)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f'{int(v)}ms'))
ax.tick_params(axis='y', colors='#CBD5E1', labelsize=9)
ax.grid(axis='y', color='#1E293B', alpha=0.5, linewidth=0.6)
ax.set_axisbelow(True)

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_color('#334155')
ax.spines['bottom'].set_color('#334155')

ax.set_title('Waterfall Chart — Robot Entry/Exit Control (ChatGPT.AI + Gemini.AI + Arduino + Master Switch)',
             fontsize=13, color='#F1F5F9', fontweight='bold', pad=14, loc='left')
ax.text(0, 1.045,
        'Kubah Simutret · Fasilitas Mata · Master Switch On/Off · Mode Bahaya · Remote Control',
        transform=ax.transAxes, fontsize=10, color='#94A3B8', style='italic')

ax.set_ylabel('Control Latensi (ms)', color='#CBD5E1', fontsize=10, labelpad=10)

from matplotlib.patches import Patch
legend_elems = [
    Patch(facecolor=CAT_COLORS['master'], edgecolor='white', label='Master Switch (On/Off All)'),
    Patch(facecolor=CAT_COLORS['chatgpt'], edgecolor='white', label='ChatGPT.AI Robot'),
    Patch(facecolor=CAT_COLORS['gemini'], edgecolor='white', label='Gemini.AI Robot'),
    Patch(facecolor=CAT_COLORS['arduino'], edgecolor='white', label='Arduino Robot (Entry/Exit)'),
    Patch(facecolor=CAT_COLORS['bahaya'], edgecolor='white', label='Mode Bahaya (All Active)'),
    Patch(facecolor='#10B981', edgecolor='white', label=f'Total: {total}ms'),
]
ax.legend(handles=legend_elems, loc='upper left', bbox_to_anchor=(0.0, -0.08),
          ncol=3, frameon=False, labelcolor='#CBD5E1', fontsize=9)

ax.annotate('Master Switch ON\nmengaktifkan SEMUA robot\nsekaligus — Mode Bahaya\nFasilitas Mata',
            xy=(0, ends[0]), xytext=(1.2, ends[0] + total*0.15),
            ha='left', va='center', fontsize=9, color='#00FF00', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#00FF00', lw=1.3),
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#1E293B', edgecolor='#00FF00', alpha=0.95))

out = '/home/z/my-project/download/waterfall_robot_control_switch.png'
plt.savefig(out, dpi=200, facecolor='#0F172A', bbox_inches='tight')
plt.close()
print(f"OK -> {out}")
print(f"Stages: {len(STAGES)}")
print(f"Total: {total}ms")
