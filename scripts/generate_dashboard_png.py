import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv("data/processed/recommendations.csv")
df = df.sort_values("product_name").reset_index(drop=True)
df['avg_price'] = df['avg_price'].astype(float)
df['recommended_price'] = df['recommended_price'].astype(float)

avg_discount = ((df["avg_price"] - df["recommended_price"]) / df["avg_price"]).mean() * 100

# layout: table (top), metric, chart
fig = plt.figure(figsize=(10,8))
gs = fig.add_gridspec(3, 1, height_ratios=[0.8, 0.3, 3], hspace=0.4)

ax_table = fig.add_subplot(gs[0,0])
ax_table.axis("off")
table_df = df.copy()
table_df['avg_price'] = table_df['avg_price'].astype(int)
table_df['recommended_price'] = table_df['recommended_price'].round(2)
table = ax_table.table(cellText=table_df.values, colLabels=table_df.columns, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1,1.6)

ax_metric = fig.add_subplot(gs[1,0])
ax_metric.axis("off")
ax_metric.text(0.5,0.6,"Avg Recommended Discount", ha="center", va="center", fontsize=12, fontweight="bold")
ax_metric.text(0.5,0.1,f"{avg_discount:.2f}%", ha="center", va="center", fontsize=18, fontweight="bold")

ax_chart = fig.add_subplot(gs[2,0])
x = np.arange(len(df))
width = 0.35
colors = ["#2B6CB0", "#ED8936"]
bars1 = ax_chart.bar(x - width/2, df['avg_price'], width, label='Avg price', color=colors[0])
bars2 = ax_chart.bar(x + width/2, df['recommended_price'], width, label='Recommended price', color=colors[1])
ax_chart.set_xticks(x)
ax_chart.set_xticklabels(df['product_name'])
ax_chart.set_ylabel("Price (INR)")
ax_chart.set_ylim(0, max(df['avg_price']) * 1.2)
ax_chart.legend()

for b in bars1:
    h = b.get_height()
    ax_chart.annotate(f"{int(h)}", xy=(b.get_x()+b.get_width()/2, h), xytext=(0,8), textcoords="offset points", ha='center')

for b in bars2:
    h = b.get_height()
    ax_chart.annotate(f"{h:.2f}", xy=(b.get_x()+b.get_width()/2, h), xytext=(0,8), textcoords="offset points", ha='center')

Path("docs").mkdir(parents=True, exist_ok=True)
out = Path("docs/price_intelligence_report.png")
fig.savefig(out, dpi=200, bbox_inches="tight")
plt.close(fig)
print(f"Saved dashboard image to {out}")
