from django.contrib.auth.models import AbstractUser, User
from django.db import models
from mptt.models import MPTTModel
from slugify import slugify


class Category(MPTTModel):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='subcategory',
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
    )
    image = models.ImageField(
        upload_to='categories/',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name = 'Category for products'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
    )
    image_small = models.ImageField(
        upload_to='categories/small/',
        null=True,
        blank=True,
    )
    image_medium = models.ImageField(
        upload_to='categories/medium/',
        null=True,
        blank=True,
    )
    image_large = models.ImageField(
        upload_to='categories/large/',
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)


class Cart(models.Model):
    title = models.CharField(max_length=255, default='Корзина')
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='carts',
    )
    products = models.ManyToManyField(Product, through='CartItem', related_name='cart_items',)

    class Meta:
        verbose_name = 'Cart'


class CartItem(models.Model):
    cart = models.ForeignKey(
        'Cart',
        on_delete=models.CASCADE,
        verbose_name='cart',
        related_name='product_in_cart'
    )
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        verbose_name='product',
        related_name='carts_with_product'
    )
    quantity = models.IntegerField(default=0)
