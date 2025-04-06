from rest_framework import serializers
from .models import Jobpost
class JobpostSerializers(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField
    class meta:
        model = Jobpost
        fields = ['title', 'description', 'days_since_created']
    def validate(self, data):
        if len(data['title']) < 10:
            raise serializers.ValidationError('title must be at least 10 characters long')
        return data
    def get_days_since_created(self, obj):
        from datetime import datetime, timezone
        return (datetime.now(timezone.utc) - obj.created_at).days
    