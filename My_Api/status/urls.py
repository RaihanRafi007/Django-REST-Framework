from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import StatusViewSet

# status/ -> List, Create => Get, Post
# status/<id>/ Details, Delete, Update => Get, Delete, Put/Patch

router = DefaultRouter()
router.register(r"status", StatusViewSet, basename="status")

urlpatterns = []+router.urls
