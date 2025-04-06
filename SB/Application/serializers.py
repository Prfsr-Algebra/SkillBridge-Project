from rest_framework import serializers
from .models import Application
class ApplicationSerializer(serializers.ModelSerializer):
    class meta:
        model = Application
        fields = '__all__'
        read_only_fields = ['applicant', 'job, created_at'] #this is to ensure only the status field is editable by the employer

 