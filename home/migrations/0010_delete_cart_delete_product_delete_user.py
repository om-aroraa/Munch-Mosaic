# Generated by Django 4.2.3 on 2023-10-26 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_cart_quantity_cart_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
