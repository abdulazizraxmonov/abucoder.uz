from django.contrib import admin
from .models import Message

# Регистрируем модели в административной панели

admin.site.register(Message)
