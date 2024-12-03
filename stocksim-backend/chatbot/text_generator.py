# text_generator.py

import re
import yfinance as yf
from transformers import pipeline
from .recommendation import recommend_stocks
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import os
from datetime import datetime, timedelta

class GRU(nn.Module):
    def __init__(self, input_size=5, hidden_size=128, num_layers=1, output_size=1):
        super(GRU, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        # GRU layer
        self.gru = nn.GRU(input_size, hidden_size, num_layers, batch_first=True)
        
        # Fully connected layer
        self.fc = nn.Linear(hidden_size, output_size)
        
    def forward(self, x):
        # Initialize hidden state with zeros
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        
        # Forward propagate GRU
        out, _ = self.gru(x, h0)
        
        # Decode the hidden state of the last time step
        out = self.fc(out[:, -1, :])
        return out
    
def load_model(model_path="deep_learning/models/gru_model.pth"):
    try:
        # Initialize the model with correct parameters
        model = GRU(input_size=5, hidden_size=128, num_layers=1, output_size=1)
        
        # Load the state dict with weights_only=True for security
        model.load_state_dict(torch.load(model_path, weights_only=True))
        
        # Set model to evaluation mode
        model.eval()
        
        return model
        
    except FileNotFoundError:
        print(f"Model file not found at {model_path}")
        return None
    except Exception as e:
        print(f"Error loading model: {str(e)}")
        return None

model = load_model()
# print("Initial model loading status:", model)  # Debug print
#if model is None:
#    print("Failed to load model - check if model file exists and path is correct")

class TextGenerationModel:
    def __init__(self, gru_model_path="deep_learning/models/gru_model.pth"):
        # Initialize both models
        self.gru_model = self._load_gru_model(gru_model_path)
        self.llm = pipeline("text-generation", model="gpt2")
        
    def _load_gru_model(self, model_path):
        model = GRU(input_size=5, hidden_size=128, num_layers=1, output_size=1)
        if os.path.exists(model_path):
            model.load_state_dict(torch.load(model_path))
        model.eval()
        return model
    
    def generate_text(self, prompt, max_length=300, max_new_tokens=50):
        """Generate text using the LLM"""
        generated_text = self.llm(
            prompt,
            max_length=max_length,
            max_new_tokens=max_new_tokens or (max_length - len(prompt.split())),
            num_return_sequences=1
        )
        return generated_text[0]['generated_text']
    
    def predict_stock_movement(self, stock_data):
        """Predict stock movement using the GRU model"""
        with torch.no_grad():
            prediction = self.gru_model(stock_data)
        return prediction

def get_stock_info(ticker):
    """Get stock information using yfinance"""
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1mo")
        stock_info = stock.info
        
        return {
            "name": stock_info.get("longName", "Unknown Company"),
            "ticker": ticker,
            "current_price": stock_info.get("currentPrice", "N/A"),
            "market_cap": stock_info.get("marketCap", "N/A"),
            "historical_data": data
        }
    except Exception as e:
        print(f"Error fetching stock info for {ticker}: {str(e)}")
        return None

class StockAnalyzer:
    def __init__(self):
        self.text_model = TextGenerationModel()
        
    def analyze_stock(self, ticker):
        """Analyze a stock using both GRU and LLM models"""
        stock_info = get_stock_info(ticker)
        if not stock_info:
            return f"Unable to analyze {ticker}"
        
        # Prepare data for GRU model
        historical_data = stock_info['historical_data']
        # Convert historical data to tensor format your GRU expects
        # This is a placeholder - adjust according to your actual data structure
        stock_tensor = torch.tensor(historical_data[['Open', 'High', 'Low', 'Close', 'Volume']]
                                  .values[-30:]).float().unsqueeze(0)
        
        # Get GRU prediction
        prediction = self.text_model.predict_stock_movement(stock_tensor)
        
        # Generate analysis text using LLM
        prompt = f"Analysis for {stock_info['name']} ({ticker}): Based on recent market data, "
        if prediction.item() > 0:
            prompt += "the stock shows positive momentum."
        else:
            prompt += "the stock shows cautionary signals."
            
        analysis = self.text_model.generate_text(prompt)
        return analysis

generator = pipeline("text-generation", model="gpt2")

def generate_text(prompt, max_length=150):
    """Generate text using the language model."""
    try:
        generated = generator(
            prompt,
            max_length=max_length,
            num_return_sequences=1,
            pad_token_id=generator.tokenizer.eos_token_id
        )
        return generated[0]['generated_text']
    except Exception as e:
        print(f"Error generating text: {str(e)}")
        return prompt

def process_question(question):
    """Process user questions about stocks"""
    analyzer = StockAnalyzer()
    
    # Find stock tickers in the question
    tickers = re.findall(r'\b[A-Z]{1,5}\b', question)
    
    # Handle different types of questions
    if 'price' in question.lower():
        responses = []
        for ticker in tickers:
            stock_info = get_stock_info(ticker)
            if stock_info:
                responses.append(f"The current price of {ticker} is {stock_info['current_price']}")
        return " ".join(responses) if responses else "Could not find stock price information."

    elif 'analyze' in question.lower() or 'analysis' in question.lower():
        responses = []
        for ticker in tickers:
            analysis = analyzer.analyze_stock(ticker)
            responses.append(analysis)
        return " ".join(responses) if responses else "Could not perform analysis."

    elif 'recommend' in question.lower() or 'tell' in question.lower():
        if model is not None:
            print("Getting recommendations...")
            recommendations = recommend_stocks(model, tickers)
            if recommendations:
                recommendations_text = ', '.join(recommendations)
                prompt = f"Based on my analysis, I recommend considering {recommendations_text}. Here's why: "
                generated_text = generate_text(prompt)
                return generated_text
            else:
                return f"After analyzing {', '.join(tickers)}, my model suggests holding off on investment at this time. Market conditions may not be optimal for these stocks."
        return "Sorry, the recommendation model is not available at this time."
    elif "help" in question.lower():
        return "I can help you with stock prices, analysis, and recommendations. Please specify what you'd like to know."
    else:
        prompt = question
        return generate_text(prompt)