from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin)
    pass