# Generated by Django 4.0.2 on 2022-05-21 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_category_product_image_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Electronics', 'Electronics'), ('Home and Decor', 'Home & Decor'), ("Men's Fashion", "Men's Fashion"), ("Women's Fashion", "Women's Fashion"), ('Furniture', 'Furniture')], default='Electronics', max_length=25),
        ),
    ]