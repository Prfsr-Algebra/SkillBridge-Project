from django.db import models
from rest_framework import generics, permissions
from users.models import EmployerProfile
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()
class Jobpost(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "job_posted_by", null = True)
    title = models.CharField(max_length= 250)
    description = models.TextField
    created_at = models.DateTimeField(auto_now_add = True)