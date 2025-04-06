from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UpdateStatusView, ApplyView
router = DefaultRouter()
router.register(r'update', UpdateStatusView)
router.register(r'Apply', ApplyView)
urlpatterns = [
    path('api/', include(router.urls))
]