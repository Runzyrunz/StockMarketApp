# written by: Renz Padlan
# tested by: Renz Padlan
# debugged by: Renz Padlan

from django.apps import AppConfig

class ChatbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatbot'

    def ready(self):
        from .models import TextGenerationModel, StockAnalyzer
        from .text_generator import generator