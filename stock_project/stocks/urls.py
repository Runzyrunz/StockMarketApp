from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/<int:user_id>/', views.get_portfolio, name='portfolio'),
]
