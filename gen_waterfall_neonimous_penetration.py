"""
Waterfall Chart — Neonimous Forces Entry into All Payment Accounts
9 Accounts: DANA, GoPay, BSI, BNI, BRI, Danamon, Alfamaret, Indomaret, Alfamidi
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

ACCOUNTS = [
    ('DANA',       'e-wallet',  45),
    ('GoPay',      'e-wallet',  40),
    ('BSI',        'Bank',      55),
    ('BNI',        'Bank',      50),
    ('BRI',        'Bank',      60),
    ('Danamon',    'Bank',      48),
    ('Alfamaret',  'Merchant',  35),
    ('Indomaret',  'Merchant',  38),
    ('Alfamidi',   'Merchant',  42),
]

CAT_COLORS = {
    'e-wallet': '#00FF00',
    'Bank':     '#00e5ff',
    'Merchant': '#FFD700',
}

deltas = [a[2] for a in ACCOUNTS]
running = 0
starts = []
ends = []
for d in deltas:
    starts.append(running)
    running += d
    ends.append(running)
total = running

fig, ax = plt.subplots(figsize=(16, 8.5), constrained_layout=True)
fig.patch.set_facecolor('#0a0e0a')
ax.set_facecolor('#0a0e0a')

n = len(ACCOUNTS)
x = np.arange(n + 1)
bar_width = 0.58

for i, (name, cat, lat) in enumerate(ACCOUNTS):
    h = deltas[i]
    color = CAT_COLORS[cat]
    ax.bar(i, h, bottom=starts[i], width=bar_width,
           color=color, edgecolor='white', linewidth=0.6, alpha=0.9)
    ax.text(i, ends[i] + total*0.012, f'+{lat}ms',
            ha='center', va='bottom', fontsize=9.5, color='#00FF00', fontweight='bold')
    if i < n - 1:
        ax.plot([i + bar_width/2, i + 1 - bar_width/2], [ends[i], ends[i]],
                color='#00AA00', linewidth=0.8, linestyle='--', alpha=0.5)
    ax.text(i, starts[i] + h/2, f'{ends[i]}ms',
            ha='center', va='center', fontsize=8.5, color='white', fontweight='600', alpha=0.85)

ax.bar(n, total, width=bar_width, color='#10B981', edgecolor='white', linewidth=1.2, alpha=0.95)
ax.text(n, total + total*0.012, f'TOTAL\n{total}ms\nALL 9\nPENETRATED',
        ha='center', va='bottom', fontsize=10, color='#10B981', fontweight='bold')

labels = [f'{a[0]}\n({a[1]})' for a in ACCOUNTS] + ['TOTAL\nAll Accounts\nPenetrated']
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=8, color='#00FF00', rotation=20, ha='right')

ax.set_ylim(0, total * 1.25)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f'{int(v)}ms'))
ax.tick_params(axis='y', colors='#00FF00', labelsize=9)
ax.grid(axis='y', color='#003300', alpha=0.5, linewidth=0.5)
ax.set_axisbelow(True)

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_color('#00AA00')
ax.spines['bottom'].set_color('#00AA00')

ax.set_title('Waterfall Chart — Neonimous Forces Entry into All 9 Payment Accounts',
             fontsize=13.5, color='#00FF00', fontweight='bold', pad=14, loc='left',
             family='monospace')
ax.text(0, 1.045,
        'Neonimous GREEN MODE · Auto-penetration: DANA · GoPay · BSI · BNI · BRI · Danamon · Alfamaret · Indomaret · Alfamidi',
        transform=ax.transAxes, fontsize=9.5, color='#00CC00', style='italic', family='monospace')

ax.set_ylabel('Penetration Latensi (ms)', color='#00FF00', fontsize=10, labelpad=10, family='monospace')

from matplotlib.patches import Patch
legend_elems = [
    Patch(facecolor=CAT_COLORS['e-wallet'], edgecolor='white', label='E-Wallet (DANA, GoPay)'),
    Patch(facecolor=CAT_COLORS['Bank'], edgecolor='white', label='Bank (BSI, BNI, BRI, Danamon)'),
    Patch(facecolor=CAT_COLORS['Merchant'], edgecolor='white', label='Merchant (Alfamaret, Indomaret, Alfamidi)'),
    Patch(facecolor='#10B981', edgecolor='white', label=f'Total: {total}ms — All 9 penetrated'),
]
ax.legend(handles=legend_elems, loc='upper left', bbox_to_anchor=(0.0, -0.10),
          ncol=2, frameon=False, labelcolor='#00FF00', fontsize=9)

out = '/home/z/my-project/download/waterfall_neonimous_payment_penetration.png'
plt.savefig(out, dpi=200, facecolor='#0a0e0a', bbox_inches='tight')
plt.close()
print(f"OK -> {out}")
print(f"Accounts: {len(ACCOUNTS)}")
print(f"Total penetration: {total}ms")
for name, cat, lat in ACCOUNTS:
    print(f"  {name} ({cat}): {lat}ms")
