"""
Waterfall Chart — Neonimous Conversation Process
Android Guardian ↔ Human Chat · Message Exchange · Agreement · Comment Insertion
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

STAGES = [
    ('Topen\nOpened',               30,  'trigger'),
    ('Neonimous\nMessage Sent',     50,  'neon'),
    ('Human\nReads Message',        80,  'human'),
    ('Human\nTypes Reply',          120, 'human'),
    ('Reply\nProcessing',           60,  'process'),
    ('Neonimous\nResponse Gen',     90,  'neon'),
    ('Conversation\nTurn Complete', 40,  'turn'),
    ('Agreement\nCheck',            70,  'check'),
    ('Comment\nInsertion',          45,  'insert'),
    ('Session\nEnd',                25,  'confirm'),
]

CAT_COLORS = {
    'trigger':  '#FFD700',   # gold — trigger
    'neon':     '#00FF00',   # green — Neonimous (Android guardian)
    'human':    '#00e5ff',   # cyan — human
    'process':  '#3AAFA9',   # teal — processing
    'turn':     '#0077BB',   # blue — turn complete
    'check':    '#FF8C00',   # orange — agreement check
    'insert':   '#8B5CF6',   # purple — comment insertion (KEY)
    'confirm':  '#10B981',   # green — session end
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

labels = [s[0] for s in STAGES] + ['TOTAL\nConversation\nComplete']
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

ax.set_title('Waterfall Chart — Neonimous ↔ Human Conversation Process',
             fontsize=14, color='#F1F5F9', fontweight='bold', pad=14, loc='left')
ax.text(0, 1.045,
        'Android Guardian Chat · Topen Trigger → Message Exchange → Agreement → Comment Insertion',
        transform=ax.transAxes, fontsize=10, color='#94A3B8', style='italic')

ax.set_ylabel('Latensi kumulatif (ms)', color='#CBD5E1', fontsize=10, labelpad=10)

from matplotlib.patches import Patch
legend_elems = [
    Patch(facecolor=CAT_COLORS['trigger'], edgecolor='white', label='Topen Trigger'),
    Patch(facecolor=CAT_COLORS['neon'], edgecolor='white', label='Neonimous (Android Guardian)'),
    Patch(facecolor=CAT_COLORS['human'], edgecolor='white', label='Human'),
    Patch(facecolor=CAT_COLORS['check'], edgecolor='white', label='Agreement Check'),
    Patch(facecolor=CAT_COLORS['insert'], edgecolor='white', label='Comment Insertion (KEY)'),
    Patch(facecolor='#10B981', edgecolor='white', label=f'Total: {total}ms'),
]
ax.legend(handles=legend_elems, loc='upper left', bbox_to_anchor=(0.0, -0.08),
          ncol=3, frameon=False, labelcolor='#CBD5E1', fontsize=9)

# Highlight Comment Insertion
ax.annotate('KEY: Comment Insertion\nhasil percakapan disisipkan\ndi HTML antara korban\ndengan manusia',
            xy=(8, ends[8]), xytext=(9.0, ends[8] + total*0.18),
            ha='left', va='center', fontsize=9, color='#8B5CF6', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#8B5CF6', lw=1.3),
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#1E293B', edgecolor='#8B5CF6', alpha=0.95))

out = '/home/z/my-project/download/waterfall_neonimous_conversation.png'
plt.savefig(out, dpi=200, facecolor='#0a0e0a', bbox_inches='tight')
plt.close()
print(f"OK -> {out}")
print(f"Stages: {len(STAGES)}")
print(f"Total: {total}ms")
print(f"Comment Insertion: {STAGES[8][1]}ms ({STAGES[8][1]/total*100:.1f}%)")
