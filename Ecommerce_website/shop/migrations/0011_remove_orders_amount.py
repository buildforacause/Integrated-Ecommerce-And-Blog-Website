# Generated by Django 4.0.2 on 2022-06-02 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_orders_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='amount',
        ),
    ]
