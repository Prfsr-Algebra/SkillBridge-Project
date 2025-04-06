from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UpdateStatusView, ApplyView
router = DefaultRouter()
router.register(r'update', UpdateStatusView, basename= 'update')
router.register(r'Apply', ApplyView, basename= 'Apply')
urlpatterns = [
    path('', include(router.urls)),
]