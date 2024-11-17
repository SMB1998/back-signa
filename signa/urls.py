# sigma/urls.py

from django.urls import path, include

urlpatterns = [
    path('api/', include('brand.urls')), 
]
