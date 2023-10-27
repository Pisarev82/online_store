# Generated by Django 4.2.6 on 2023-10-26 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_cart_product_remove_cart_quantity_cart_owner_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_in_cart', to='catalog.cart', verbose_name='cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts_with_product', to='catalog.product', verbose_name='product')),
            ],
        ),
        migrations.DeleteModel(
            name='ProductsInCardQuantity',
        ),
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(through='catalog.CartItem', to='catalog.product'),
        ),
    ]