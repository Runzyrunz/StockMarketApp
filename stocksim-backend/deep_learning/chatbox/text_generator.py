# text_generator.py

import re
import yfinance as yf
from transformers import pipeline

# Initialize the language model pipeline
generator = pipeline("text-generation", model="gpt2")

def process_question(question):
    """
    Processes the user's question to determine if it contains a stock ticker and relevant keywords,
    and then generates an appropriate response.
    """
    # Find all uppercase words that look like ticker symbols (1-5 uppercase letters)
    tickers = re.findall(r'\b[A-Z]{1,5}\b', question)
    print("Identified possible tickers:", tickers)  # Debugging

    for possible_ticker in tickers:
        stock = yf.Ticker(possible_ticker)
        stock_info = stock.info
        if 'currentPrice' in stock_info:  # Check if it's a valid ticker
            # Check if the question specifically asks about the "current price"
            if "current price" in question.lower() or "price" in question.lower():
                # Get and return the current price information
                stock_data = get_stock_info(possible_ticker)
                return stock_data

    # If no valid ticker or relevant keywords were found, provide feedback
    return "Please provide a valid stock ticker symbol and specify what information you need."

def get_stock_info(ticker):
    """Fetches specific stock information: name, ticker, current price, and market cap."""
    stock = yf.Ticker(ticker)
    info = stock.info
    
    # Extract only the required fields
    name = info.get("longName", "Unknown Company")
    current_price = info.get("currentPrice", "N/A")
    market_cap = info.get("marketCap", "N/A")
    
    return f"{name}\n({ticker})\nCurrent Price: ${current_price}\nMarket Cap: {market_cap}"
