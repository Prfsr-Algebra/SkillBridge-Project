from django.urls import path, include
from .views import EmployerProfileViewSet
from .views import WorkerProfileViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'EmployerProfile', EmployerProfileViewSet, basename= "my_profile")
router.register(r'Worker_profile', WorkerProfileViewSet, basename="profile")
urlpatterns = [
    path('', include(router.urls)),
]