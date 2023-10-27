from rest_framework import mixins, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from .models import Category, Product, Cart, CartItem
from .serializers import (CategorySerializer,
                          ProductSerializer,
                          CartSerializer,
                          CartItemsSerializer
                          )


class IsOwnerUserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class CategoryViewSet(mixins.ListModelMixin,
                      GenericViewSet
                      ):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(mixins.ListModelMixin,
                     GenericViewSet
                     ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet
                  ):

    permission_classes = (
        IsAuthenticated,
        IsOwnerUserPermission,
    )

    pagination_class = None
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(owner=self.request.user)


class CartItemsViewSet(#mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       GenericViewSet
                     ):
    queryset = CartItem.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsOwnerUserPermission,
    )
    pagination_class = None
    serializer_class = CartItemsSerializer
