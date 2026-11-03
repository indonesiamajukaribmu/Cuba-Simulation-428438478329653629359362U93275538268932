"""
Waterfall Chart — Pelindung Data Protection Lifecycle
Sistem Kubah Simulasi · Anti-Hacker/Anti-Peretas Defense Process
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

# Data protection lifecycle stages (anti-hacker defense)
STAGES = [
    ('Hacker\nDetection',          25,  'detect'),
    ('Firewall\nBlock',            45,  'block'),
    ('Encryption\nVerify',         80,  'verify'),
    ('Intrusion\nPrevention',      120, 'block'),
    ('Threat\nAnalysis',           95,  'analyze'),
    ('Auto\nQuarantine',           60,  'block'),
    ('Log\nArchive',               35,  'confirm'),
    ('Alert\nNotification',        40,  'confirm'),
]

CAT_COLORS = {
    'detect':  '#FFD700',  # gold — detection
    'block':   '#EF4444',  # red — blocking/quarantine (hacker defense)
    'verify':  '#8B5CF6',  # purple — encryption/verification
    'analyze': '#3AAFA9',  # teal — analysis
    'confirm': '#009988',  # green-teal — confirmation
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
bar_width = 0.62

for i, (label, lat, cat) in enumerate(STAGES):
    h = ends[i] - starts[i]
    color = CAT_COLORS[cat]
    ax.bar(i, h, bottom=starts[i], width=bar_width,
           color=color, edgecolor='white', linewidth=0.8, alpha=0.92)
    ax.text(i, ends[i] + total*0.015, f'+{lat}ms',
            ha='center', va='bottom', fontsize=10, color='#F1F5F9', fontweight='bold')
    if i < n - 1:
        ax.plot([i + bar_width/2, i + 1 - bar_width/2], [ends[i], ends[i]],
                color='#64748B', linewidth=0.9, linestyle='--', alpha=0.55)
    ax.text(i, starts[i] + h/2, f'{ends[i]}ms',
            ha='center', va='center', fontsize=9, color='white', fontweight='600', alpha=0.85)

ax.bar(n, total, width=bar_width, color='#10B981', edgecolor='white', linewidth=1.2, alpha=0.95)
ax.text(n, total + total*0.015, f'TOTAL\n{total}ms',
        ha='center', va='bottom', fontsize=11, color='#10B981', fontweight='bold')

labels = [s[0] for s in STAGES] + ['TOTAL\nEnd-to-End']
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=9, color='#CBD5E1')

ax.set_ylim(0, total * 1.20)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f'{int(v)}ms'))
ax.tick_params(axis='y', colors='#CBD5E1', labelsize=9)
ax.grid(axis='y', color='#1E293B', alpha=0.5, linewidth=0.6)
ax.set_axisbelow(True)

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_color('#334155')
ax.spines['bottom'].set_color('#334155')

ax.set_title('Waterfall Chart — Pelindung Data Protection Lifecycle (Anti-Hacker Defense)',
             fontsize=14, color='#F1F5F9', fontweight='bold', pad=14, loc='left')
ax.text(0, 1.045,
        'Sistem Kubah Simulasi · Pelindung Data · 8 Tahap Pertahanan Anti-Peretas (SLA < 600ms)',
        transform=ax.transAxes, fontsize=10, color='#94A3B8', style='italic')

ax.set_ylabel('Latensi kumulatif (ms)', color='#CBD5E1', fontsize=10, labelpad=10)

from matplotlib.patches import Patch
legend_elems = [
    Patch(facecolor=CAT_COLORS['detect'], edgecolor='white', label='Hacker Detection'),
    Patch(facecolor=CAT_COLORS['block'], edgecolor='white', label='Firewall Block / Quarantine'),
    Patch(facecolor=CAT_COLORS['verify'], edgecolor='white', label='Encryption Verify'),
    Patch(facecolor=CAT_COLORS['analyze'], edgecolor='white', label='Threat Analysis'),
    Patch(facecolor=CAT_COLORS['confirm'], edgecolor='white', label='Log & Alert Confirmation'),
    Patch(facecolor='#10B981', edgecolor='white', label=f'Total: {total}ms'),
]
ax.legend(handles=legend_elems, loc='upper left', bbox_to_anchor=(0.0, -0.08),
          ncol=3, frameon=False, labelcolor='#CBD5E1', fontsize=9.5)

# Highlight the heaviest stage
max_idx = deltas.index(max(deltas))
ax.annotate(f'Heaviest stage:\n{STAGES[max_idx][1]}ms',
            xy=(max_idx, ends[max_idx]), xytext=(max_idx + 1.2, ends[max_idx] + total*0.15),
            ha='left', va='center', fontsize=9.5, color='#EF4444', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#EF4444', lw=1.2),
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#1E293B', edgecolor='#EF4444', alpha=0.95))

out = '/home/z/my-project/download/waterfall_pelindung_data_protection.png'
plt.savefig(out, dpi=200, facecolor='#0F172A', bbox_inches='tight')
plt.close()
print(f"OK -> {out}")
print(f"Stages: {len(STAGES)}")
print(f"Total end-to-end: {total}ms (SLA 600ms: {'PASS' if total < 600 else 'OVER'})")
print(f"Heaviest stage: {STAGES[max_idx][0].replace(chr(10),' ')} = {STAGES[max_idx][1]}ms")
