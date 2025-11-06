import requests
from bs4 import BeautifulSoup

def get_price_from_html(html, selector):
    """Extracts a numeric price from an HTML element using a CSS selector."""
    try:
        soup = BeautifulSoup(html, "html.parser")
        el = soup.select_one(selector)
        text = el.text.strip().replace(",", "")
        price = float("".join([ch for ch in text if ch.isdigit() or ch == "."]))
        return price
    except Exception:
        return None
