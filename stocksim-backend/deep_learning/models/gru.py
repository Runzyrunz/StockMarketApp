import torch.nn as nn
import torch

# Gated Recurrent Unit model for sequential data, such as stock data
class GRU(nn.Module):
    # Initialize the sequence input size, hidden unit size, number of layers, and what the output will be
    def __init__(self, input_size=5, hidden_size=128, num_layers=4, output_size=1):
        super().__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        # Use dropout to make model more robust
        self.dropout = nn.Dropout(0.2)
        # GRU unit and linear unit for the neural network
        self.gru = nn.GRU(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
    
    # Forward pass of the model
    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        out, _ = self.gru(x, h0)
        out = self.dropout(out[:, -1, :])
        out = self.fc(out)
        return out