from rest_framework import serializers
from .models import Category, Product, Cart, CartItem


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'parent',
            'slug',
            'image',
        )


class CategoryForProductSerializer(serializers.ModelSerializer):
    parent = serializers.StringRelatedField()
    class Meta:
        model = Category
        fields = (
            'parent',
            'title',
        )


class ProductSerializer(serializers.ModelSerializer):
    category = CategoryForProductSerializer(read_only=True)
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'title',
            'slug',
            'category',
            'price',
            'images',
        )

    def get_images(self, obj):
        return {
            'small': obj.image_small.url if obj.image_small else None,
            'medium': obj.image_medium.url if obj.image_medium else None,
            'large': obj.image_large.url if obj.image_large else None,
        }


class CartItemsSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.title')

    class Meta:
        model = CartItem
        fields = (
            'cart',
            'product',
            'product_name',
            'quantity',
        )


class CartSerializer(serializers.ModelSerializer):
    owner_name = serializers.ReadOnlyField(source='owner.username')
    products_in_cart = CartItemsSerializer(source='product_in_cart', many=True, read_only=True)
    total = serializers.SerializerMethodField()

    def get_total(self, obj):

        products = obj.products.values()
        prices = [i.get('price') for i in products]
        cart_items = obj.product_in_cart.values()
        quantity = [i.get('quantity') for i in cart_items]
        total_price = sum([x * y for x, y in zip(prices, quantity)])
        return {
            'price': total_price,
            'quantity': sum(quantity),
        }

    class Meta:
        model = Cart
        fields = (
            'id',
            'title',
            'owner',
            'owner_name',
            'total',
            'products_in_cart',
        )
