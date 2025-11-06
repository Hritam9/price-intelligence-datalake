# dashboard/app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="centered")

st.title("💰 Competitive Price Intelligence Dashboard")

# Load data
df = pd.read_csv("data/processed/recommendations.csv")

# Normalize column names (safe)
df.columns = [c.strip() for c in df.columns]

# Ensure required columns exist
required = {"product_name", "avg_price", "recommended_price"}
if not required.issubset(set(df.columns)):
    st.error(f"Missing required columns. Found: {list(df.columns)}")
    st.stop()

# Convert to numeric and handle missing values
df['avg_price'] = pd.to_numeric(df['avg_price'], errors='coerce')
df['recommended_price'] = pd.to_numeric(df['recommended_price'], errors='coerce')

# Option: fill NaN with 0 (or use df.dropna())
df[['avg_price','recommended_price']] = df[['avg_price','recommended_price']].fillna(0)

# Sort for stable ordering
df = df.sort_values('product_name').reset_index(drop=True)

st.subheader("Data")
st.dataframe(df[['product_name', 'avg_price', 'recommended_price']])

# Pricing insights
avg_gap = ((df['avg_price'] - df['recommended_price']) / df['avg_price']).replace([np.inf, -np.inf], np.nan).dropna()
avg_gap_pct = avg_gap.mean() * 100 if not avg_gap.empty else 0.0
st.subheader("📈 Pricing Insights")
st.metric("Avg Recommended Discount", f"{avg_gap_pct:.2f}%")

# Grouped bar chart using matplotlib
products = df['product_name'].tolist()
x = np.arange(len(products))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.bar(x - width/2, df['avg_price'], width, label='Avg price')
ax.bar(x + width/2, df['recommended_price'], width, label='Recommended price')

ax.set_xlabel('')
ax.set_ylabel('Price')
ax.set_title('Average Price vs Recommended Price')
ax.set_xticks(x)
ax.set_xticklabels(products, rotation=0)
ax.legend()

st.pyplot(fig)
