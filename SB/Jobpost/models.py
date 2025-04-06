from django.db import models
from users.models import EmployerProfile
# Create your models here.
class Jobpost(models.Model):
    employer_id = models.ForeignKey(EmployerProfile, on_delete=models.SET_NULL, null = True, related_name= "job_posted_by")
    title = models.CharField(max_length= 250)
    description = models.TextField
    created_at = models.DateTimeField(auto_now_add = True)