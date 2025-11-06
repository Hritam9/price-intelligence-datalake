import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="centered", page_title="Price Intelligence")

st.title("💰 Competitive Price Intelligence Dashboard")

CSV = "data/processed/recommendations.csv"
try:
    df = pd.read_csv(CSV)
except Exception as e:
    st.error(f"Cannot load recommendations CSV: {e}")
    st.stop()

# Ensure numeric
df['avg_price'] = pd.to_numeric(df['avg_price'], errors='coerce')
df['recommended_price'] = pd.to_numeric(df['recommended_price'], errors='coerce')
df = df.sort_values('product_name').reset_index(drop=True)

st.subheader("Data")
st.dataframe(df)

# Insights
avg_gap = ((df['avg_price'] - df['recommended_price']) / df['avg_price']).mean() * 100
st.subheader("📈 Pricing Insights")
st.metric("Avg Recommended Discount", f"{avg_gap:.2f}%")

# Plot using matplotlib for consistent visuals
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(len(df))
width = 0.35
fig, ax = plt.subplots(figsize=(8,4.5))

ax.bar(x - width/2, df['avg_price'], width, label='Avg price')
ax.bar(x + width/2, df['recommended_price'], width, label='Recommended price')
ax.set_xticks(x)
ax.set_xticklabels(df['product_name'], rotation=0)
ax.set_ylabel("Price (INR)")
ax.legend()

# annotate
for i,(a,b) in enumerate(zip(df['avg_price'], df['recommended_price'])):
    ax.text(i - width/2, a + 20, f"{int(a)}", ha='center')
    ax.text(i + width/2, b + 20, f"{b:.2f}", ha='center')

st.pyplot(fig)
