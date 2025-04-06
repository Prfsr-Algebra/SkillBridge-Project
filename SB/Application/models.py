from django.db import models
from django.contrib.auth import get_user_model
from Jobpost.models import JobPost
# Create your models here.
User = get_user_model()
class Application(models.Model):
    application_status = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ]
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    applied_since = models.DateTimeField(auto_now_add= True)
    status = models.CharField(max_length=100, choices=application_status, default='pending')
    class meta:
        unique_together = ('Jobpost', 'Applicant') # this is to ensure an applicant can only submit an application
        

