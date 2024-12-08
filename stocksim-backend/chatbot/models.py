# written by: Renz Padlan
# tested by: Renz Padlan
# debugged by: Renz Padlan


from django.db import models
import torch
import torch.nn as nn
from transformers import pipeline
import yfinance as yf
import os

class ChatLog(models.Model):
    user_message = models.TextField()
    timestamp = models.DateTimeField()

class GRU(nn.Module):
    def __init__(self, input_size=5, hidden_size=128, num_layers=1, output_size=1):
        super(GRU, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        self.gru = nn.GRU(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
        
    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        out, _ = self.gru(x, h0)
        out = self.fc(out[:, -1, :])
        return out

class TextGenerationModel(models.Model):
    gru_model_path = models.CharField(max_length=255, default="deep_learning/models/gru_model.pth")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gru_model = self._load_gru_model(self.gru_model_path)
        self.llm = pipeline("text-generation", model="gpt2")
    
    def _load_gru_model(self, model_path):
        model = GRU(input_size=5, hidden_size=128, num_layers=1, output_size=1)
        if os.path.exists(model_path):
            model.load_state_dict(torch.load(model_path))
        model.eval()
        return model
    
    def generate_text(self, prompt, max_length=300, max_new_tokens=50):
        generated_text = self.llm(
            prompt,
            max_length=max_length,
            max_new_tokens=max_new_tokens or (max_length - len(prompt.split())),
            num_return_sequences=1
        )
        return generated_text[0]['generated_text']
    
    def predict_stock_movement(self, stock_data):
        with torch.no_grad():
            prediction = self.gru_model(stock_data)
        return prediction

class StockAnalyzer(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text_model = TextGenerationModel()
    
    def analyze_stock(self, ticker):
        stock_info = self.get_stock_info(ticker)
        if not stock_info:
            return f"Unable to analyze {ticker}"
        
        historical_data = stock_info['historical_data']
        stock_tensor = torch.tensor(historical_data[['Open', 'High', 'Low', 'Close', 'Volume']]
                                  .values[-30:]).float().unsqueeze(0)
        
        prediction = self.text_model.predict_stock_movement(stock_tensor)
        
        prompt = f"Analysis for {stock_info['name']} ({ticker}): Based on recent market data, "
        if prediction.item() > 0:
            prompt += "the stock shows positive momentum."
        else:
            prompt += "the stock shows cautionary signals."
            
        analysis = self.text_model.generate_text(prompt)
        return analysis
    
    @staticmethod
    def get_stock_info(ticker):
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