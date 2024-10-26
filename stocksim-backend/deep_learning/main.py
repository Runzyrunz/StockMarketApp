from datasets.stock_dataset import StockDataset
from models.gru import GRU
from torch.utils.data import DataLoader
from eval.train import train_model

tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
dataset = StockDataset(tickers)

model = GRU()

dataloader = DataLoader(dataset, batch_size=128, shuffle=True, drop_last=True)
print(len(dataloader))
train_model(model, dataloader)

print(f"Total sequences: {len(dataset)}")  # Total samples

# Print the number of batches in the DataLoader
print(f"Number of batches: {len(dataloader)}")

# Print the shape of one batch to confirm data structure
X_batch, y_batch = next(iter(dataloader))
print(f"Batch X shape: {X_batch.shape}, Batch y shape: {y_batch.shape}")