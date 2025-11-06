import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw")
OUT_PATH = Path("data/processed/merged_prices.csv")
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

def run():
    frames = []
    for f in RAW_PATH.glob("*.csv"):
        try:
            df = pd.read_csv(f)
            frames.append(df)
        except Exception as e:
            print(f"skipping {f} due to {e}")

    if not frames:
        print("No raw files found in data/raw/")
        return

    merged = pd.concat(frames, ignore_index=True)
    merged['price'] = pd.to_numeric(merged['price'], errors='coerce')
    # Basic normalization: group by product_name and compute mean price
    grouped = merged.groupby('product_name', as_index=False).agg({
        'price': 'mean',
        'currency': 'first'
    })
    grouped = grouped.rename(columns={'price': 'avg_price'})
    grouped['avg_price'] = grouped['avg_price'].round(2)
    grouped.to_csv(OUT_PATH, index=False)
    print(f"✅ Wrote merged processed file to {OUT_PATH}")

if __name__ == "__main__":
    run()
