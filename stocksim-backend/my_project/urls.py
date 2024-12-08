# written by: Renz Padlan
# tested by: Renz Padlan
# debugged by: Renz Padlan

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('chatbot.urls')),
]
