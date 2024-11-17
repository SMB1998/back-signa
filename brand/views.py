# brands/views.py

from rest_framework import viewsets
from .model import Brand
from .serializer import BrandSerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
