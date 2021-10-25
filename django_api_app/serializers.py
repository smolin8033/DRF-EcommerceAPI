from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class CartUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'username'


class CartSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = models.Cart
        fields = [
            'cart_id',
            'created_at',
            'books',
            'products'
        ]
