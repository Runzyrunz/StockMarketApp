import torch
import torch.nn as nn
from tqdm import tqdm

def train_model(model, dataloader, num_epochs=10, learning_rate=0.0001):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)

    criterion = nn.HuberLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    epoch_pbar = tqdm(range(num_epochs), desc='Training', unit='epoch')
    
    for epoch in epoch_pbar:
        model.train()
        total_loss = 0.0
        batch_pbar = tqdm(dataloader, leave=False, desc=f'Epoch {epoch + 1}', unit='batch')

        for X, y in batch_pbar:
            X, y = X.to(device), y.to(device)

            optimizer.zero_grad()
            predictions = model(X).squeeze()
            loss = criterion(predictions, y)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()

            total_loss += loss.item()
            batch_pbar.set_postfix({'batch_loss': f'{loss.item():.4f}'})

        avg_loss = total_loss / len(dataloader)
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {avg_loss:.4f}')
