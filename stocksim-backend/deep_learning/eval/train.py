import torch
import torch.nn as nn
from tqdm import tqdm

def train_model(model, dataloader, num_epochs=200, learning_rate=0.0001):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)

    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(num_epochs):
        model.train()
        total_loss = 0.0

        progress_bar = tqdm(dataloader, desc=f'Epoch [{epoch + 1}/{num_epochs}]', leave=False)

        for X, y in dataloader:
            
            X, y = X.to(device), y.to(device)

            optimizer.zero_grad()
            predictions = model(X).squeeze()
            loss = criterion(predictions, y)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()

            total_loss += loss.item()

            progress_bar.set_postfix(loss=loss.item())


        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {total_loss / len(dataloader):.4f}')