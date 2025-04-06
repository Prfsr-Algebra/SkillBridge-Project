from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError, PermissionDenied
from .models import Application
from .serializers import ApplicationSerializer
from Jobpost.models import JobPost
# Create your views here.
class ApplyView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        job_id = self.kwargs['id']
        job = JobPost.objects.all(id = job_id)
        if Application.objects.filter(job = job, applicant = self.request.user).exist:
            raise ValidationError("you've already applied to this job")
        serializer.save(applicant = self.request.user, job = job)
class UpdateStatusView(generics.UpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        application = super().get_object()

        # Ensure that the current user is the employer who owns the job
        if application.job.employer != self.request.user:
            raise PermissionDenied("You are not allowed to modify this application.")

        return application