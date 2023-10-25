# Generated by Django 4.2.3 on 2023-10-24 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=300)),
                ('image', models.ImageField(default='', upload_to='home/static/imgs')),
                ('category', models.CharField(default='', max_length=50)),
                ('subcategory', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='home/static/imgs'),
        ),
    ]
