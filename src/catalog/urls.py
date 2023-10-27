from django.urls import path, include
from rest_framework import routers
from .views import (
    CategoryViewSet,
    ProductViewSet,
    CartViewSet,
    CartItemsViewSet
)

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'cart-item', CartItemsViewSet, basename='cart_item')

urlpatterns = [
    path(r'', include(router.urls)),
]
