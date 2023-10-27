# Generated by Django 4.2.6 on 2023-10-26 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0004_alter_category_parent_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
        migrations.AddField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='carts', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ProductsInCardQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('carts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_in_cart', to='catalog.cart', verbose_name='cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_in_cart', to='catalog.product', verbose_name='product')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(through='catalog.ProductsInCardQuantity', to='catalog.product'),
        ),
    ]