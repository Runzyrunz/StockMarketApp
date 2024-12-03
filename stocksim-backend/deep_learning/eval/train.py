import torch
import torch.nn as nn
from tqdm import tqdm

# Function to train the GRU model given the chosen training dataset
def train_model(model, dataloader, num_epochs=10, learning_rate=0.01):
    # Add model to GPU or CPU
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)

    # Define the loss function and optimizer for training
    criterion = nn.HuberLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    # Used to look at progress whle model trains
    epoch_pbar = tqdm(range(num_epochs), desc='Training', unit='epoch')
    
    # For each training iteration, get the data from X, y in a sequential manner,
    # make a prediction, compute loss, then do a backward pass for the gradients,
    # and finally, update the weights
    for epoch in epoch_pbar:
        model.train()
        total_loss = 0.0
        batch_pbar = tqdm(dataloader, leave=False, desc=f'Epoch {epoch + 1}', unit='batch')

        # Using batches, calculate the loss for each batch and get a running total
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

    return model