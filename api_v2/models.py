from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.OneToOneField(
        User, related_name='user_cart', on_delete=models.CASCADE
    )
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.user}'


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='categories', on_delete=models.CASCADE
    )
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    imageUrl = models.URLField()
    status = models.BooleanField(default=True)
    quantity = models.IntegerField(default=1)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return f'{self.title}'


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, related_name='cart_item', on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name='cart_product', on_delete=models.CASCADE
    )
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.product}: {self.quantity} items'