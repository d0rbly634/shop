from django.db import models

# Create your models here.
class Product(models.Model):
    price = models.PositiveIntegerField()
    name = models.CharField(max_length=15)
    stok = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    discount = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0)
    is_availabol = models.BooleanField(default=True)



class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    number = models.CharField(max_length=16)
    email = models.EmailField()
    addres = models.CharField(max_length=60)
    quantity = models.PositiveIntegerField(default=1)