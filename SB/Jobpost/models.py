from django.db import models
from rest_framework import generics, permissions
from users.models import EmployerProfile
from users.models import CustomUser
# Create your models here.
class Jobpost(models.Model):
    employer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name= "job_posted_by", null = True)
    title = models.CharField(max_length= 250)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)