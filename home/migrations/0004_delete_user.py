# Generated by Django 4.2.3 on 2023-10-24 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]