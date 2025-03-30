from django.shortcuts import render
from rest_framework import viewsets
from .models import WorkerProfile, EmployerProfile
from .serializers import EmployerProfileSerializer, WorkerProfileSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class EmployerProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    querryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileSerializer
class WorkerProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = WorkerProfile.objects.all()
    serializer_class = WorkerProfileSerializer
