from django.urls import path, include
from .views import EmployerProfileViewSet, WorkerProfileViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter
router.register(r'EmployerProfile', EmployerProfileViewSet)
router.register('Worker_profile', WorkerProfileViewSet)
urlspatterns = [
    path('api/', include(router.urls))
]