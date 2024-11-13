# stock_data_fetcher.py

import yfinance as yf

def fetch_stock_data(stock_symbol):
    try:
        stock = yf.Ticker(stock_symbol)
        stock_info = stock.history(period="1d")  # Get latest stock data for 1 day
        latest_price = stock_info['Close'].iloc[-1]
        return f"The latest closing price of {stock_symbol} is ${latest_price:.2f}"
    except Exception as e:
        return f"Error fetching data for {stock_symbol}: {str(e)}"
