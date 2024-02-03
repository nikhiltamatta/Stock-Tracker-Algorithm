import requests
import time

API_KEY = 'your_api_key_here'
SYMBOLS = ['AAPL', 'GOOGL', 'MSFT']  # Example list of stock symbols

def get_stock_price(symbol):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    if 'Global Quote' in data:
        return data['Global Quote']['05. price']
    else:
        return None

def track_stocks():
    while True:
        for symbol in SYMBOLS:
            price = get_stock_price(symbol)
            if price:
                print(f'{symbol}: ${price}')
            else:
                print(f'Error retrieving data for {symbol}')
        time.sleep(60)  # Adjust the interval here (in seconds) for how often you want to check the prices

if __name__ == "__main__":
    track_stocks()
