"""
Waterfall Chart — Robot Avatar Transition Process
Neonimous Topen → Robot Avatar Display → Mouth Animation → Setuju → Image Transition
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

STAGES = [
    ('Topen\nOpened',              25,  'trigger'),
    ('Robot Avatar\nDisplay',      40,  'display'),
    ('Mouth\nAnimation Start',     30,  'anim'),
    ('Neonimous\nSpeaking',        200, 'speak'),
    ('Human\nListen',              80,  'human'),
    ('Human\nSetuju Click',        15,  'click'),
    ('Image\nTransition 1→2',      60,  'transition'),
    ('Avatar 2\nDisplay',          40,  'display'),
    ('Mouth Anim\nContinue',       150, 'anim'),
    ('Conversation\nComplete',     35,  'confirm'),
]

CAT_COLORS = {
    'trigger':    '#FFD700',
    'display':    '#00FF00',
    'anim':       '#00CC00',
    'speak':      '#00FF00',
    'human':      '#00e5ff',
    'click':      '#FF8C00',
    'transition': '#8B5CF6',
    'confirm':    '#10B981',
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
fig.patch.set_facecolor('#0a0e0a')
ax.set_facecolor('#0a0e0a')

n = len(STAGES)
x = np.arange(n + 1)
bar_width = 0.6

for i, (label, lat, cat) in enumerate(STAGES):
    h = ends[i] - starts[i]
    color = CAT_COLORS[cat]
    ax.bar(i, h, bottom=starts[i], width=bar_width,
           color=color, edgecolor='white', linewidth=0.6, alpha=0.9)
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

labels = [s[0] for s in STAGES] + ['TOTAL\nAvatar\nComplete']
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

ax.set_title('Waterfall Chart — Robot Avatar Transition (Topen → Mouth Animation → Setuju → Image Switch)',
             fontsize=13, color='#F1F5F9', fontweight='bold', pad=14, loc='left')
ax.text(0, 1.045,
        'Neonimous Chat · Robot Avatar 1041 → Setuju → Avatar 1042 · Green Theme · Animated Mouth',
        transform=ax.transAxes, fontsize=10, color='#94A3B8', style='italic')

ax.set_ylabel('Latensi kumulatif (ms)', color='#CBD5E1', fontsize=10, labelpad=10)

from matplotlib.patches import Patch
legend_elems = [
    Patch(facecolor=CAT_COLORS['trigger'], edgecolor='white', label='Topen Trigger'),
    Patch(facecolor=CAT_COLORS['display'], edgecolor='white', label='Avatar Display'),
    Patch(facecolor=CAT_COLORS['anim'], edgecolor='white', label='Mouth Animation'),
    Patch(facecolor=CAT_COLORS['speak'], edgecolor='white', label='Neonimous Speaking'),
    Patch(facecolor=CAT_COLORS['human'], edgecolor='white', label='Human'),
    Patch(facecolor=CAT_COLORS['transition'], edgecolor='white', label='Image Transition (KEY)'),
    Patch(facecolor='#10B981', edgecolor='white', label=f'Total: {total}ms'),
]
ax.legend(handles=legend_elems, loc='upper left', bbox_to_anchor=(0.0, -0.08),
          ncol=4, frameon=False, labelcolor='#CBD5E1', fontsize=9)

ax.annotate('KEY: Image Transition\nAvatar 1041 → 1042\nsaat klik "setuju"',
            xy=(6, ends[6]), xytext=(7.0, ends[6] + total*0.18),
            ha='left', va='center', fontsize=9, color='#8B5CF6', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#8B5CF6', lw=1.3),
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#1E293B', edgecolor='#8B5CF6', alpha=0.95))

out = '/home/z/my-project/download/waterfall_robot_avatar_transition.png'
plt.savefig(out, dpi=200, facecolor='#0a0e0a', bbox_inches='tight')
plt.close()
print(f"OK -> {out}")
print(f"Stages: {len(STAGES)}")
print(f"Total: {total}ms")
