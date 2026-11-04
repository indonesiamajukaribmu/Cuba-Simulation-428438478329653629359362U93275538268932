"""
Waterfall Chart — Neonimous Hacking Process ke 6 Akun
DANA → GoPay → BSI → BNI → BRI → Danamon → Penggunaan Aplikasi
Fasilitas Mata tetap aktif melindungi website
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

STAGES = [
    ('Neonimous\nActivate',           30,  'neon'),
    ('DANA\n→ App Mode',              45,  'penetrate'),
    ('GoPay\n→ App Mode',             40,  'penetrate'),
    ('BSI\n→ App Mode',               55,  'penetrate'),
    ('BNI\n→ App Mode',               50,  'penetrate'),
    ('BRI\n→ App Mode',               60,  'penetrate'),
    ('Danamon\n→ App Mode',           48,  'penetrate'),
    ('Fasilitas Mata\nProtected',     25,  'protect'),
    ('Website\nShield UP',            20,  'protect'),
    ('All 6 Accounts\nApp Mode ON',   15,  'complete'),
]

CAT_COLORS = {
    'neon':      '#00FF00',
    'penetrate': '#00CC00',
    'protect':   '#00e5ff',
    'complete':  '#10B981',
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
fig.patch.set_facecolor('#0a0e0a')
ax.set_facecolor('#0a0e0a')

n = len(STAGES)
x = np.arange(n + 1)
bar_width = 0.58

for i, (label, lat, cat) in enumerate(STAGES):
    h = ends[i] - starts[i]
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
ax.text(n, total + total*0.012, f'TOTAL\n{total}ms\nHACK\nCOMPLETE',
        ha='center', va='bottom', fontsize=10, color='#10B981', fontweight='bold')

labels = [s[0] for s in STAGES] + ['TOTAL\nAll 6\nApp Mode']
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=7.5, color='#00FF00', rotation=15, ha='right')

ax.set_ylim(0, total * 1.25)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f'{int(v)}ms'))
ax.tick_params(axis='y', colors='#00FF00', labelsize=9)
ax.grid(axis='y', color='#003300', alpha=0.5, linewidth=0.5)
ax.set_axisbelow(True)

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_color('#00AA00')
ax.spines['bottom'].set_color('#00AA00')

ax.set_title('Waterfall Chart — Neonimous Hacking: 6 Akun → Penggunaan Aplikasi (Fasilitas Mata Protected)',
             fontsize=13, color='#00FF00', fontweight='bold', pad=14, loc='left', family='monospace')
ax.text(0, 1.045,
        'DANA · GoPay · BSI · BNI · BRI · Danamon → App Mode · Website tetap dilindungi Fasilitas Mata',
        transform=ax.transAxes, fontsize=9.5, color='#00CC00', style='italic', family='monospace')

ax.set_ylabel('Hacking Latensi (ms)', color='#00FF00', fontsize=10, labelpad=10, family='monospace')

from matplotlib.patches import Patch
legend_elems = [
    Patch(facecolor=CAT_COLORS['neon'], edgecolor='white', label='Neonimous Activation'),
    Patch(facecolor=CAT_COLORS['penetrate'], edgecolor='white', label='Account Penetration → App Mode'),
    Patch(facecolor=CAT_COLORS['protect'], edgecolor='white', label='Fasilitas Mata + Website Shield'),
    Patch(facecolor='#10B981', edgecolor='white', label=f'Total: {total}ms — Hack Complete'),
]
ax.legend(handles=legend_elems, loc='upper left', bbox_to_anchor=(0.0, -0.08),
          ncol=2, frameon=False, labelcolor='#00FF00', fontsize=9)

ax.annotate('FASILITAS MATA\ntetap aktif melindungi\nwebsite selama peretasan',
            xy=(7, ends[7]), xytext=(8.0, ends[7] + total*0.15),
            ha='left', va='center', fontsize=9, color='#00e5ff', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#00e5ff', lw=1.2),
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#001a22', edgecolor='#00e5ff', alpha=0.95))

out = '/home/z/my-project/download/waterfall_neonimous_hacking_6accounts.png'
plt.savefig(out, dpi=200, facecolor='#0a0e0a', bbox_inches='tight')
plt.close()
print(f"OK -> {out}")
print(f"Stages: {len(STAGES)}")
print(f"Total: {total}ms")
print(f"6 accounts penetrated: DANA, GoPay, BSI, BNI, BRI, Danamon")
print(f"Fasilitas Mata: PROTECTED")
