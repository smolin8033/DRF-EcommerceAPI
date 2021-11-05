from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('carts', views.CartItemViewSet, basename='carts')


urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
    path('profits/', views.ListProfitView.as_view(), name='list_profit'),
    path('register/', views.CreateUserView.as_view(), name='register'),
]
