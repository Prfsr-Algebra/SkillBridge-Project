from django.shortcuts import render
from rest_framework import viewsets
from .serializers import JobpostSerializers
from .models import Jobpost
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
class JObPostViews(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    querryset = Jobpost.objects.all()
    serializer_class = JobpostSerializers
    def perform_created(self, serializer):
        serializer.save(employer = self.request.user)
# Create your views here.
