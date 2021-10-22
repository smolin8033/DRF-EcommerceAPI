from django.urls import path, include, re_path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('books', views.BookViewSet)
router.register('products', views.ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
]