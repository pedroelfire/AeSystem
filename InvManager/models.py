from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    color =  models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    stock = models.IntegerField()

    def __str__(self):
        return self.name
