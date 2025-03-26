from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    user_role = [
        ('worker', 'Worker'),
        ('employer', 'Employer')
    ]
    role = models.CharField(max_length=20, choices=user_role)