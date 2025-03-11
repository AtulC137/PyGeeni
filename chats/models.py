# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Each chat belongs to a user
    title = models.CharField(max_length=255, blank=True, null=True)  # Chat name
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when chat started

    def __str__(self):
        return self.title if self.title else f"Chat {self.id}"  # Display title or ID

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")  # Each message belongs to a chat
    user_input = models.TextField()  # User's message
    bot_response = models.TextField()  # Bot's reply
    timestamp = models.DateTimeField(auto_now_add=True)  # Message time

    def __str__(self):
        return f"Message in Chat {self.chat.id} at {self.timestamp}"
