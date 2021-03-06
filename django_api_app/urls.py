from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('books', views.BookViewSet)
router.register('products', views.ProductViewSet)
router.register('carts', views.CartViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
]
