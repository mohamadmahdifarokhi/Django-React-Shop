from rest_framework import serializers
from .models import Order, OrderItem


class ListOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'user',
            'coupon',
            'transaction_id',
            'full_name',
            'address',
            'city',
            'price',
            'discount_price',
            'shipping_name',
            'shipping_price',
            'shipping_time',
            'status',
        ]


class ListOrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'user',
            'coupon',
            'transaction_id',
            'full_name',
            'address',
            'city',
            'price',
            'discount_price',
            'shipping_name',
            'shipping_price',
            'shipping_time',
            'status',
            'order_items',
        ]
