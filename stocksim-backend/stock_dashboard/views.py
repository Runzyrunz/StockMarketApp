# written by: Renz Padlan
# tested by: Renz Padlan
# debugged by: Renz Padlan

from django.http import JsonResponse
import yfinance as yf

def get_stock_data(request):
    stock_symbols = ["AAPL", "MSFT", "GOOGL"]
    data = {}
    for symbol in stock_symbols:
        stock = yf.Ticker(symbol)
        info = stock.info
        data[symbol] = {
            "name": info.get("longName"),
            "price": info.get("regularMarketPrice"),
            "change": info.get("regularMarketChangePercent"),
        }
    return JsonResponse(data)
