# written by: Renz Padlan
# tested by: Renz Padlan
# debugged by: Renz Padlan

from .models import GRU, StockAnalyzer
import torch
from django.conf import settings

class ModelService:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def __init__(self):
        self.model = self._load_model()
        self.stock_analyzer = StockAnalyzer()

    def _load_model(self):
        try:
            model = GRU(input_size=5, hidden_size=128, num_layers=1, output_size=1)
            # Update path to match your actual file structure
            model_path = settings.BASE_DIR / 'deep_learning' / 'models' / 'gru_model.pth'
            print(f"Looking for model at: {model_path}")  # Debug print
            if model_path.exists():
                model.load_state_dict(torch.load(str(model_path)), strict=False)
                model.eval()
                print("Model loaded successfully")
                return model
            else:
                print(f"Model file not found at {model_path}")
                return None
        except Exception as e:
            print(f"Error loading model: {str(e)}")
            return None

model_service = ModelService.get_instance()