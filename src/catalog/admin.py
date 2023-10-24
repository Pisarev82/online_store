from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin, MPTTModelAdmin
from .models import Category, Product


@admin.register(Category)
class CategoryMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass