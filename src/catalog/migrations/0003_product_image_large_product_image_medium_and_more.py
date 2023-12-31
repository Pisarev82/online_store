# Generated by Django 4.2.6 on 2023-10-24 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_large',
            field=models.ImageField(blank=True, null=True, upload_to='categories/large/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_medium',
            field=models.ImageField(blank=True, null=True, upload_to='categories/medium/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_small',
            field=models.ImageField(blank=True, null=True, upload_to='categories/small/'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
