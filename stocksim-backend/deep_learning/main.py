from datasets.stock_dataset import StockDataset
from models.gru import GRU
from torch.utils.data import DataLoader
from eval.train import train_model

# Initialize the training data (tickers) and create dataset
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
dataset = StockDataset(tickers)

# Initialize randomized model
model = GRU()

# Dataloader class for PyTorch to speed up training
dataloader = DataLoader(dataset, batch_size=128, shuffle=True, drop_last=True)
print(len(dataloader))

# Train model with the training dataset
train_model(model, dataloader)

print(f"Total sequences: {len(dataset)}") 


print(f"Number of batches: {len(dataloader)}")


X_batch, y_batch = next(iter(dataloader))
print(f"Batch X shape: {X_batch.shape}, Batch y shape: {y_batch.shape}")