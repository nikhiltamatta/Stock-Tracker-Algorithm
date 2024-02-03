# Stock Tracker Algorithm 📈

This Python script tracks the stock prices of a given list of companies using the Alpha Vantage API. It continuously fetches the latest prices for the specified stocks and prints them out at regular intervals.

## Usage 🚀

1. **Sign up for Alpha Vantage API Key**
   
   Before using this script, you need to sign up for a free API key from Alpha Vantage. You can sign up [here](https://www.alphavantage.co/support/#api-key).

2. **Clone the Repository**

   ```bash
   git clone https://github.com/nikhiltamatta/stock-tracker.git
   ```

3. **Install Dependencies**

   Make sure you have Python installed on your system. You can download it from [here](https://www.python.org/downloads/). Install the requests library if you haven't already:

   ```bash
   pip install requests
   ```

4. **Set up API Key**

   Replace `'your_api_key_here'` in the script (`stock_tracker.py`) with your actual Alpha Vantage API key.

5. **Specify Stock Symbols**

   Adjust the `SYMBOLS` list in the script to include the stock symbols you want to track.

6. **Run the Script**

   Navigate to the directory where the script is located and run:

   ```bash
   python stock_tracker.py
   ```

   The script will continuously fetch and print the latest prices for the specified stocks.

## Integration 🛠️

You can integrate this script into your project by importing the `track_stocks` function from `stock_tracker.py`. You can then call this function from your own code to track stock prices.

```python
from stock_tracker import track_stocks

if __name__ == "__main__":
    track_stocks()
```

## Note 📝

- The script fetches stock prices every minute by default. You can adjust the interval by changing the sleep time in the `track_stocks` function.
- Alpha Vantage API has usage limits for free accounts. Make sure to check their [documentation](https://www.alphavantage.co/documentation/) for more information.
```
