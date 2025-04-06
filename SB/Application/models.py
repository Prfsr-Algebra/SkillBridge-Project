from django.db import models
from users.models import CustomUser
from Jobpost.models import Jobpost
# Create your models here.
class Application(models.Model):
    application_status = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ]
    job = models.ForeignKey(Jobpost, on_delete=models.CASCADE)
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    applied_since = models.DateTimeField(auto_now_add= True)
    status = models.CharField(max_length=100, choices=application_status, default='pending')
    class Meta:
        unique_together = ('job', 'applicant') # this is to ensure an applicant can only submit an application


