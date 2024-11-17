

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BrandViewSet

router = DefaultRouter()
router.register(r'brand', BrandViewSet)

urlpatterns = [
    path('', include(router.urls)), 
]
