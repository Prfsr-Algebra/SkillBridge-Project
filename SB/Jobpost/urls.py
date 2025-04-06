from .models import Jobpost
from rest_framework.routers import DefaultRouter
from .views import JobPostViews
from django.urls import path, include
router = DefaultRouter()
router.register(r'jobs', JObPostViews)
urlpatterns = [
    path('jobs/', include (router.urls))
]