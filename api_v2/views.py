from . import models, serializers
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, viewsets
from rest_framework.exceptions import NotAcceptable
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class ListProfitView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        income = 0
        total_quantity = 0
        carts = models.Cart.objects.all()
        cart_items = models.CartItem.objects.all()
        for cart in carts:
            income += cart.total
        for item in cart_items:
            total_quantity += item.quantity
        return Response(
            {
                "The total income is": income,
                "The total quantity of items sold is": total_quantity,
            },
            status = status.HTTP_200_OK
        )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CartItemSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = models.CartItem.objects.filter(cart__user=user)
        return queryset

    def create(self, request, *args, **kwargs):
        user = request.user
        cart = get_object_or_404(models.Cart, user=user)
        product = get_object_or_404(models.Product, pk=request.data['product'])
        quantity = int(request.data['quantity'])
        current_item = models.CartItem.objects.filter(cart=cart, product=product)
        if current_item.count() > 0:
            raise NotAcceptable('You already have this item in your list')
        elif quantity > product.quantity:
            raise NotAcceptable("Your order quantity exceeds our shop's stock")

        cart_item = models.CartItem(cart=cart, product=product, quantity=quantity)
        cart_item.save()
        serializer = serializers.CartItemSerializer(cart_item)

        total = float(product.price) * float(quantity)
        cart.total = float(cart.total) + float(total)
        cart.save()

        product.quantity = int(product.quantity) - quantity
        product.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        user = request.user
        cart_item = self.get_object()
        cart = get_object_or_404(models.Cart, user=user)
        product = get_object_or_404(models.Product, pk=request.data['product'])
        quantity = int(request.data['quantity'])
        if quantity > product.quantity:
            raise NotAcceptable("Your order quantity exceeds our shop's stock")
        elif quantity > cart_item.quantity:
            product.quantity -= quantity - cart_item.quantity
            cart.total = float(cart.total) + float(product.price) * float(
                quantity - cart_item.quantity
            )
        elif quantity < cart_item.quantity:
            product.quantity += cart_item.quantity - quantity
            cart.total = float(cart.total) -  float(product.price) * float(
                cart_item.quantity - quantity
            )
        product.save()
        cart.save()

        serializer = serializers.CartUpdateSerializer(cart_item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        cart_item = self.get_object()
        cart = get_object_or_404(models.Cart, user=user)
        product = get_object_or_404(models.Product, pk=cart_item.product.id)
        product.quantity += cart_item.quantity
        cart.total = float(cart.total) - float(product.price) * float(
            cart_item.quantity
        )
        cart_item.delete()
        product.save()
        cart.save()
        return Response(
            {'detail': ('your item has been deleted.')},
            status=status.HTTP_204_NO_CONTENT
        )
