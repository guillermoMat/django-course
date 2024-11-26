from rest_framework.serializers import ModelSerializer
from .models import Product
from rest_framework.serializers import ModelSerializer


class ProductSerializer(ModelSerializer):
    class Meta:
        model=Product
        fields=[
            'name',
            'description',
            'price',
            'available',
            'photo',]
