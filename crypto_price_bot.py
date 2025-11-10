import requests
import time

API_URL = "https://api.coingecko.com/api/v3/simple/price"
COINS = ["bitcoin", "ethereum", "toncoin"]
CURRENCY = "usd"

def fetch_prices():
    response = requests.get(API_URL, params={
        "ids": ",".join(COINS),
        "vs_currencies": CURRENCY
    })
    data = response.json()
    for coin, price in data.items():
        print(f"{coin.capitalize()}: ${price[CURRENCY]:,.2f}")

if __name__ == "__main__":
    print("💰 Crypto Price Bot Started (Ctrl+C to stop)\n")
    while True:
        fetch_prices()
        print("-" * 30)
        time.sleep(30)
