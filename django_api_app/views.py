from . import models, serializers
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets

# Create your views here.


class CreateUserView(generics.CreateAPIView):
    model = User
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = serializers.RegisterSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer
