import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw")
OUT_PATH = Path("data/processed/merged_prices.csv")

frames = [pd.read_csv(f) for f in RAW_PATH.glob("*.csv")]
merged = pd.concat(frames)
merged['price'] = merged['price'].astype(float)
merged = merged.groupby('product_name', as_index=False).agg({
    'price': 'mean', 'currency': 'first'
})
merged['avg_price'] = merged['price'].round(2)
merged.to_csv(OUT_PATH, index=False)
print(f"✅ Merged data saved to {OUT_PATH}")
