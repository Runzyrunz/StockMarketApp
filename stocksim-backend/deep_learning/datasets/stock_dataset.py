import yfinance as yf
import pandas as pd

tickers = ['AAPL']

data = yf.download(tickers, start='2015-01-01', end='2023-12-31')

print(data.head())