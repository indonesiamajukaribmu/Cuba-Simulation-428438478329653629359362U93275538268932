"""
Waterfall Chart — Proses Pencairan Coin dengan Identity Verification
Sistem Kubah Simulasi · S5·COIN Reward Sensor · Multi-Currency Redemption Flow
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

# ===== Redemption process stages with identity verification =====
# Each stage: (label, latency_ms, category)
# category: 'verify' = identity/account verification, 'process' = processing, 'confirm' = confirmation
STAGES = [
    ('Coin\nBalance\nCheck',           15,  'process'),
    ('Identity\nVerification',         180, 'verify'),
    ('Account Match\n(Phone/Rekening)', 85, 'verify'),
    ('Tier Selection\n& Conversion',    95, 'process'),
    ('Bank/E-wallet\nTransfer',         220, 'process'),
    ('QRIS Scan\n(Merchant)',           140, 'process'),
    ('Confirmation\nReceipt',           35,  'confirm'),
    ('Cloud Archive\nWrite',            45,  'confirm'),
]

# Colors per category (low-saturation palette per charts skill)
CAT_COLORS = {
    'verify':   '#EE7733',  # orange — verification stages (highlight)
    'process':  '#0077BB',  # blue — processing stages
    'confirm':  '#009988',  # teal — confirmation stages
}

# Compute waterfall cumulative
deltas = [s[1] for s in STAGES]
running = 0
starts = []
ends = []
for d in deltas:
    starts.append(running)
    running += d
    ends.append(running)
total = running

# ===== Plot =====
fig, ax = plt.subplots(figsize=(15, 8.5), constrained_layout=True)
fig.patch.set_facecolor('#0F172A')
ax.set_facecolor('#0F172A')

n = len(STAGES)
x = np.arange(n + 1)  # +1 for total
bar_width = 0.62

# Draw waterfall bars
for i, (label, lat, cat) in enumerate(STAGES):
    h = ends[i] - starts[i]
    color = CAT_COLORS[cat]
    ax.bar(i, h, bottom=starts[i], width=bar_width,
           color=color, edgecolor='white', linewidth=0.8, alpha=0.92)
    # Value label on top of bar
    ax.text(i, ends[i] + total*0.012, f'+{lat}ms',
            ha='center', va='bottom', fontsize=10, color='#F1F5F9', fontweight='bold')
    # Connector dashed line to next bar
    if i < n - 1:
        ax.plot([i + bar_width/2, i + 1 - bar_width/2], [ends[i], ends[i]],
                color='#64748B', linewidth=0.9, linestyle='--', alpha=0.55)
    # Cumulative running label inside bar
    ax.text(i, starts[i] + h/2, f'{ends[i]}ms',
            ha='center', va='center', fontsize=9, color='white', fontweight='600', alpha=0.85)

# Total bar
ax.bar(n, total, width=bar_width, color='#10B981', edgecolor='white', linewidth=1.2, alpha=0.95)
ax.text(n, total + total*0.012, f'TOTAL\n{total}ms',
        ha='center', va='bottom', fontsize=11, color='#10B981', fontweight='bold')

# X-axis labels
labels = [s[0] for s in STAGES] + ['TOTAL\nEnd-to-End']
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=9, color='#CBD5E1')

# Y-axis
ax.set_ylim(0, total * 1.18)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f'{int(v)}ms'))
ax.tick_params(axis='y', colors='#CBD5E1', labelsize=9)
ax.grid(axis='y', color='#1E293B', alpha=0.5, linewidth=0.6)
ax.set_axisbelow(True)

# Spines
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_color('#334155')
ax.spines['bottom'].set_color('#334155')

# Title
ax.set_title('Waterfall Chart — Proses Pencairan Coin dengan Identity Verification',
             fontsize=14, color='#F1F5F9', fontweight='bold', pad=14, loc='left')
ax.text(0, 1.045, 'Sistem Kubah Simulasi · S5·COIN · 8 Tahap Pencairan (E-wallet/Bank/QRIS Merchant)',
        transform=ax.transAxes, fontsize=10, color='#94A3B8', style='italic')

# Y label
ax.set_ylabel('Latensi kumulatif (ms)', color='#CBD5E1', fontsize=10, labelpad=10)

# Legend
from matplotlib.patches import Patch
legend_elems = [
    Patch(facecolor=CAT_COLORS['verify'], edgecolor='white', label='Identity & Account Verification'),
    Patch(facecolor=CAT_COLORS['process'], edgecolor='white', label='Processing & Transfer'),
    Patch(facecolor=CAT_COLORS['confirm'], edgecolor='white', label='Confirmation & Archive'),
    Patch(facecolor='#10B981', edgecolor='white', label='Total End-to-End Latency'),
]
ax.legend(handles=legend_elems, loc='upper left', bbox_to_anchor=(0.0, -0.10),
          ncol=4, frameon=False, labelcolor='#CBD5E1', fontsize=9.5)

# Annotation: SLA line at 300ms
ax.axhline(y=300, color='#FFB74D', linewidth=1.2, linestyle=':', alpha=0.7)
ax.text(n - 0.2, 305, 'SLA target: 300ms', color='#FFB74D', fontsize=8.5, ha='right', va='bottom', style='italic')

# Highlight identity verification as key new stage
ax.annotate('NEW: Identity\nVerification stage',
            xy=(1, ends[1]), xytext=(1.8, ends[1] + total*0.18),
            ha='left', va='center', fontsize=9.5, color='#EE7733', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#EE7733', lw=1.2),
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#1E293B', edgecolor='#EE7733', alpha=0.95))

# Save
out = '/home/z/my-project/download/waterfall_redemption_process_with_identity.png'
plt.savefig(out, dpi=200, facecolor='#0F172A', bbox_inches='tight')
plt.close()
print(f"OK -> {out}")
print(f"Stages: {len(STAGES)}")
print(f"Total end-to-end: {total}ms (SLA 300ms: {'PASS' if total < 300 else 'OVER — but multi-stage async'})")
print(f"Identity verification contributes: {STAGES[1][1]}ms ({STAGES[1][1]/total*100:.1f}%)")
