import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def scrape_amazon():
    products = [
        {"name": "Sports Shoes", "url": "https://www.amazon.in/s?k=sports+shoes"},
        {"name": "Backpack", "url": "https://www.amazon.in/s?k=backpack"},
    ]
    data = []
    for product in products:
        data.append({
            "product_id": len(data)+1,
            "product_name": product["name"],
            "price": 1499 + len(data)*100,  # dummy value
            "currency": "INR",
            "source": "Amazon",
            "timestamp": datetime.now().strftime("%Y-%m-%d")
        })
    df = pd.DataFrame(data)
    df.to_csv("data/raw/amazon.csv", index=False)
    print("✅ Amazon data saved")

if __name__ == "__main__":
    scrape_amazon()
