import pandas as pd
from datetime import datetime
from pathlib import Path

def scrape_amazon():
    # PoC: simulated fixed values (safe for resume/demo)
    data = [
        {"product_id": 1, "product_name": "Sports Shoes", "price": 1499, "currency": "INR", "source": "Amazon", "timestamp": datetime.now().strftime("%Y-%m-%d")},
        {"product_id": 2, "product_name": "Running T-Shirt", "price": 699, "currency": "INR", "source": "Amazon", "timestamp": datetime.now().strftime("%Y-%m-%d")},
        {"product_id": 3, "product_name": "Backpack", "price": 1599, "currency": "INR", "source": "Amazon", "timestamp": datetime.now().strftime("%Y-%m-%d")},
    ]
    df = pd.DataFrame(data)
    out = Path("data/raw/amazon.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    print(f"✅ Wrote {out}")
    return df

if __name__ == "__main__":
    scrape_amazon()
