from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=models.Product.objects.all(),
        source = 'product.title'
    )

    class Meta:
        model = models.CartItem
        fields = [
            'id',
            'product',
            'quantity',
        ]


class CartUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartItem
        fields = [
            'product',
            'quantity'
        ]
