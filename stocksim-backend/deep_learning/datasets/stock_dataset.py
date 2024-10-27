import yfinance as yf
import pandas as pd
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader

# Transforming the yfinance dataset into PyTorch dataset for model usage
class StockDataset(Dataset):
    # Initilize the stocks (tickers), sequence length (50 days), predict ahead (each monday), and the start and end date of data
    def __init__(self, tickers, seq_len=50, predict_ahead=1, start_date='2010-01-01', end_date='2023-12-31'):
        self.seq_len = seq_len
        self.predict_ahead = predict_ahead
        # Get the yfinance data and prepare the sequences
        self.data = self.download_data(tickers, start_date, end_date)
        self.X, self.y = self.prepare_sequences()

    # Download the yfinance data given the tickers, start date, and end date
    def download_data(self, tickers, start_date, end_date):
        print("Downloading stock data...")
        data = yf.download(tickers, start=start_date, end=end_date, group_by='ticker')

        if data.empty:
            raise ValueError("No data downloaded. Please check the tickers or date range.")

        resampled_data = {}
        
        # Gedt the data for each monday and get all the types
        for ticker in tickers:
            ticker_data = data[ticker].resample('W-MON').agg({
                'Open': 'first',
                'High': 'max',
                'Low': 'min',
                'Close': 'last',
                'Volume': 'sum'
            })

            resampled_data[ticker] = ticker_data

        # Combine all of the data and drop all non-existent values
        combined_data = pd.concat(resampled_data, axis=1)

        combined_data = combined_data.dropna(how='all').ffill().bfill()

        print("Data download and resampling completed.")
        return combined_data

    # Function to prepare the data for model usage
    def prepare_sequences(self):
        # Empty lists to contain the input dataset and the corresponding label         
        X, y = [], []

        # Go through each stock, getting all the values and converting them to numpy floats
        for ticker in self.data.columns.levels[0]:
            ticker_data = self.data[ticker][['Open', 'High', 'Low', 'Close', 'Volume']].values.astype(np.float32)
            
            # Get the data in a weekly manner for each stock and add it to the X and y lists
            for i in range(len(ticker_data) - self.seq_len - self.predict_ahead):
                X.append(ticker_data[i : i + self.seq_len])

                price_today = ticker_data[i + self.seq_len - 1][3] 
                price_next_week = ticker_data[i + self.seq_len + self.predict_ahead - 1][3] 

                gain = (price_next_week - price_today) / price_today
                y.append(gain)
        
        # Add the data as torch tensors for mnodel usage
        X = torch.from_numpy(np.array(X, dtype=np.float32))
        y = torch.from_numpy(np.array(y, dtype=np.float32))

        return X, y

    # Get the length of the dataset
    def __len__(self):
        return len(self.X)

    # Get the actual item (by idx) of the dataset
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]
