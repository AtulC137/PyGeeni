from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Chat, Message  # Import the models

# Register the models
admin.site.register(Chat)
admin.site.register(Message)
