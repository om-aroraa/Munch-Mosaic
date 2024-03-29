from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    productName = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to="home/static/imgs", default="")
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")

class User (models.Model):
    user_id = models.AutoField
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Cart (models.Model):
    cart_id = models.AutoField
    productName = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to="home/static/imgs", default="")
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    quantity = models.IntegerField()
    user = models.CharField(max_length=100)