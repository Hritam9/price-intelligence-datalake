import pandas as pd
from datetime import datetime
import random
from pathlib import Path

def scrape_flipkart():
    """
    Simulated Flipkart price extractor for 3 demo products.
    Generates pseudo-random prices around a base value to imitate daily fluctuations.
    """

    # Define base product catalog (you can add more products easily)
    catalog = [
        {"product_name": "Sports Shoes", "base_price": 1550},
        {"product_name": "Running T-Shirt", "base_price": 750},
        {"product_name": "Backpack", "base_price": 1499},
    ]

    data = []
    for idx, item in enumerate(catalog, start=1):
        # add a random ±5% price fluctuation
        fluctuation = random.uniform(-0.05, 0.05)
        price = round(item["base_price"] * (1 + fluctuation), 2)
        data.append({
            "product_id": idx,
            "product_name": item["product_name"],
            "price": price,
            "currency": "INR",
            "source": "Flipkart",
            "timestamp": datetime.now().strftime("%Y-%m-%d")
        })

    df = pd.DataFrame(data)

    # ensure directories exist
    output_path = Path("data/raw/flipkart.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"✅ Flipkart data scraped and saved to {output_path}")
    return df


if __name__ == "__main__":
    scrape_flipkart()
