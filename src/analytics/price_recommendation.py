import pandas as pd
from pathlib import Path

INPUT = Path("data/processed/merged_prices.csv")
OUT = Path("data/processed/recommendations.csv")
OUT.parent.mkdir(parents=True, exist_ok=True)

def run():
    df = pd.read_csv(INPUT)
    # Simple rule: recommended = avg_price * 0.95 (5% below market avg)
    df['recommended_price'] = (df['avg_price'] * 0.95).round(2)
    df.to_csv(OUT, index=False)
    print(f"✅ Wrote recommendations to {OUT}")

if __name__ == "__main__":
    run()
