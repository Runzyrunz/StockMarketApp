from django.urls import path
from . import views
from .views import recommend_stocks_view


urlpatterns = [
    path("chat/", views.chat, name="chat"),
    path("recommend/", views.recommend_stocks_view, name="recommend_stocks"),

]
