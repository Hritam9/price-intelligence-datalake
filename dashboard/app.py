import streamlit as st
import pandas as pd

st.title("💰 Competitive Price Intelligence Dashboard")

df = pd.read_csv("data/processed/recommendations.csv")
st.dataframe(df)

st.subheader("📈 Pricing Insights")
avg_gap = ((df['avg_price'] - df['recommended_price']) / df['avg_price'] * 100).mean()
st.metric("Avg Recommended Discount", f"{avg_gap:.2f}%")

st.bar_chart(df.set_index('product_name')[['avg_price', 'recommended_price']])
