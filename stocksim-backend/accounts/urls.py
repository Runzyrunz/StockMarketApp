# accounts/urls.py
from django.urls import path
from .views import create_account, sign_in
from .views import AccountListCreate, AccountDetail, user_portfolio


urlpatterns = [
    path('create-account/', create_account, name='create_account'),
    path('sign-in/', sign_in, name='sign_in'),
    path('portfolio/', user_portfolio, name='user_portfolio'),
]
