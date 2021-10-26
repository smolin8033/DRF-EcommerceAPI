from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
            'email',
        ]
        write_only_fields = ['password']

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data.get('username', None),
            email = validated_data.get('email', None),
            first_name = validated_data.get('first_name', None),
            last_name = validated_data.get('last_name', None)
        )
        if User.objects.filter(email=user.email).exists():
            raise serializers.ValidationError('Not unique email')
        elif User.objects.filter(username=user.username).exists():
            raise serializers.ValidationError('Not unique username')
        else:
            user.set_password(validated_data.get('password'))
            user.save()
            return user


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
        fields = ['username']


class CartSerializer(serializers.ModelSerializer):
    cart_id = CartUserSerializer(read_only=True)
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
