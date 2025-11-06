import pandas as pd

df = pd.read_csv("data/processed/merged_prices.csv")
df['recommended_price'] = (df['avg_price'] * 0.95).round(2)
df.to_csv("data/processed/recommendations.csv", index=False)

print("💡 Recommended prices saved to data/processed/recommendations.csv")
