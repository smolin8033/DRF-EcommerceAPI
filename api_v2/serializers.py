from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
        write_only_fields = ['password']

    def create(self, validated_data):
        user = User(
            username=validated_data.get('username', None),
        )
        if User.objects.filter(username=user.username).exists():
            raise serializers.ValidationError('Not unique username')
        else:
            user.set_password(validated_data.get('password'))
            user.save()
            cart = models.Cart(user=user, total=0)
            cart.save()
            return user


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
