import pandas as pd
from datetime import datetime
import random
from pathlib import Path

def scrape_myntra():
    catalog = [
        {"product_name": "Sports Shoes", "base_price": 1600},
        {"product_name": "Running T-Shirt", "base_price": 725},
        {"product_name": "Backpack", "base_price": 1650},
    ]

    data = []
    for idx, item in enumerate(catalog, start=1):
        fluctuation = random.uniform(-0.05, 0.05)
        price = round(item["base_price"] * (1 + fluctuation), 2)
        data.append({
            "product_id": idx,
            "product_name": item["product_name"],
            "price": price,
            "currency": "INR",
            "source": "Myntra",
            "timestamp": datetime.now().strftime("%Y-%m-%d")
        })

    df = pd.DataFrame(data)
    out = Path("data/raw/myntra.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    print(f"✅ Wrote {out}")
    return df

if __name__ == "__main__":
    scrape_myntra()
