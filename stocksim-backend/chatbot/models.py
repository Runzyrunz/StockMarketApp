from django.db import models

# Create your models here.

#chatbot app stores data
class ChatLog(models.Model):
    user_message = models.TextField()
    timestamp = models.DateTimeField