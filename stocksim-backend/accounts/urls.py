# accounts/urls.py
from django.urls import path
from .views import create_account, sign_in

urlpatterns = [
    path('create-account/', create_account, name='create_account'),
    path('sign-in/', sign_in, name='sign_in'),
]
