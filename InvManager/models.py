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
    
class Movement(models.Model):
    MOVEMENT_CHOICES = [
        ('IN', 'Entrada'),
        ('OUT', 'Salida'),
    ]

    movement_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_CHOICES)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Update product stock based on movement type
        if self.movement_type == 'IN':
            self.product.stock += self.quantity
        elif self.movement_type == 'OUT':
            self.product.stock -= self.quantity

        # Save the movement and update the product stock
        super().save(*args, **kwargs)
        self.product.save()

    def __str__(self):
        return f"{self.movement_type} - {self.product.name} - {self.quantity}"