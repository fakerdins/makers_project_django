from django.db import router
from django.urls import path, include
from rest_framework import urlpatterns
from .views import OrderViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('orders', OrderViewset)

urlpatterns = [
    path("", include(router.urls)),
]