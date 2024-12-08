# written by: Renz Padlan
# tested by: Renz Padlan
# debugged by: Renz Padlan

from django.urls import path
from . import views
from .views import recommend_stocks_view

urlpatterns = [
    # Existing routes
    path('chat/', views.chat, name='chat'),
    path('recommend/', views.recommend_stocks_view, name='recommend_stocks'),
    
    # New routes for text generation and stock analysis
    path('analyze/<str:ticker>/', views.analyze_stock, name='analyze_stock'),
    path('generate/', views.generate_text, name='generate_text'),
    path('process/', views.process_question, name='process_question'),
    path('stock-info/<str:ticker>/', views.get_stock_info, name='stock_info'),
]