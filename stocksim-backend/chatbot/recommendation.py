# recommendation.py

import torch
import yfinance as yf
import pandas as pd
import numpy as np
from typing import List, Tuple, Optional

def fetch_historical_data(ticker: str, period: str = "1y") -> pd.DataFrame:
    """
    Fetch historical stock data with error handling.
    
    Args:
        ticker (str): Stock ticker symbol
        period (str): Time period for historical data
    
    Returns:
        pd.DataFrame: Historical stock data
    """
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period)
        if data.empty:
            raise ValueError(f"No data found for ticker {ticker}")
        return data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {str(e)}")
        return pd.DataFrame()

def preprocess_data(data: pd.DataFrame) -> torch.Tensor:
    try:
        # Ensure we only select these 5 specific features
        essential_features = ['Open', 'High', 'Low', 'Close', 'Volume']
        df = data[essential_features].copy()
        
        # Update fillna syntax to avoid warning
        df = df.ffill().bfill()
        
        # Normalize the data
        df = (df - df.mean()) / df.std()
        
        # Convert to tensor with correct dimensions
        tensor_data = torch.tensor(df.values, dtype=torch.float32)
        
        # Ensure correct shape (batch_size, sequence_length, features)
        tensor_data = tensor_data.unsqueeze(0)  # Add batch dimension
        
        print(f"Tensor shape after processing: {tensor_data.shape}")  # Debug print
        return tensor_data
        
    except Exception as e:
        print(f"Error in preprocessing data: {str(e)}")
        return None

def calculate_rsi(prices: pd.Series, periods: int = 14) -> pd.Series:
    """Calculate Relative Strength Index."""
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=periods).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=periods).mean()
    
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def get_stock_score(prediction: float, confidence: float) -> float:
    """
    Calculate a composite score for stock recommendation.
    
    Args:
        prediction (float): Model's prediction value
        confidence (float): Confidence score of the prediction
    
    Returns:
        float: Composite score between 0 and 1
    """
    # Combine prediction and confidence into a single score
    score = (prediction * 0.7) + (confidence * 0.3)
    return max(0, min(1, score))  # Clamp between 0 and 1

def recommend_stocks(model, tickers):
    recommendations = []
    
    for ticker in tickers:
        try:
            print(f"Processing ticker: {ticker}")
            
            # Fetch stock data
            stock_data = fetch_historical_data(ticker)
            if stock_data.empty:
                print(f"No data available for {ticker}")
                continue
            
            # Preprocess the data
            processed_data = preprocess_data(stock_data)
            if processed_data is None:
                print(f"Failed to process data for {ticker}")
                continue
                
            print(f"Processed data shape: {processed_data.shape}")
            
            # Make prediction
            with torch.no_grad():
                try:
                    prediction = model(processed_data)
                    raw_score = prediction.item()
                    score = torch.sigmoid(prediction).item()
                    print(f"Raw prediction for {ticker}: {raw_score}")
                    print(f"Sigmoid score for {ticker}: {score}")
                    
                    # Lower threshold for testing
                    if score > 0.3:  # Lowered from 0.5
                        recommendations.append(ticker)
                        print(f"Added {ticker} to recommendations with score {score}")
                    else:
                        print(f"Score {score} below threshold for {ticker}")
                        
                except Exception as e:
                    print(f"Error making prediction for {ticker}: {str(e)}")
                    continue
                
        except Exception as e:
            print(f"Error processing {ticker}: {str(e)}")
            continue
    
    print(f"Final recommendations: {recommendations}")
    return recommendations

def generate_recommendation_summary(recommendations: List[Tuple[str, float]]) -> str:
    """
    Generate a summary of stock recommendations.
    
    Args:
        recommendations (List[Tuple[str, float]]): List of recommendations with scores
    
    Returns:
        str: Formatted summary string
    """
    if not recommendations:
        return "No stocks meet the recommendation criteria at this time."
    
    summary = "Stock Recommendations:\n"
    for ticker, score in recommendations:
        confidence_level = "High" if score > 0.8 else "Medium" if score > 0.6 else "Low"
        summary += f"- {ticker}: {confidence_level} confidence (score: {score:.2f})\n"
    
    return summary
