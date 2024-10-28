from datasets.stock_dataset import StockDataset
from models.gru import GRU
from torch.utils.data import DataLoader
from eval.train import train_model

# Initialize the training data (tickers) and create dataset
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'NFLX']
dataset = StockDataset(tickers)

# Initialize randomized model
model = GRU()

# Dataloader class for PyTorch to speed up training
dataloader = DataLoader(dataset, batch_size=128, shuffle=True, drop_last=True)

# Train model with the training dataset
trained_model = train_model(model, dataloader)