from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('carts', views.CartItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
]
