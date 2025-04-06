from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    user_role = [
        ('worker', 'Worker'),
        ('employer', 'Employer')
    ]
    role = models.CharField(max_length=20, choices=user_role)
    email_verified = models.BooleanField(default = False)
class WorkerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name = 'worker_profile')
    skills = models.CharField(max_length=500)
    experience = models.CharField(max_length= 250)
    portfolio = models.URLField(blank=True, null=True)
class EmployerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name ='employer_profile')
    company  = models.CharField(max_length=250)
    industry = models.CharField(max_length=250)
    is_hiring = models.BooleanField(default=False)