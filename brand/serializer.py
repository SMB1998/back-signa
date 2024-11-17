# brands/serializers.py

from rest_framework import serializers
from .model import Brand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'owner', 'status']  
