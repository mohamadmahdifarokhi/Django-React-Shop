from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'photo',
            'description',
            'price',
            'discount_price',
            'count',
            'sold',
            'created',
            'get_thumbnail',
        ]
