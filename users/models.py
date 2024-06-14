from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    image=models.ImageField(upload_to="user/images")
    phone=models.CharField(max_length=13)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone']

    def str(self):
        return self.username
    