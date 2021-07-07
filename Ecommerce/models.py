from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    description = models.CharField(max_length=64, null=False)

    def __str__(self):
        return f"{self.description}"

class Product(models.Model):
    titulo = models.CharField(max_length=250, null=False)
    imagen = models.FileField(upload_to='imagenes/')
    description = models.CharField(max_length=2000, null=False)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="clasification_category")
    def __str__(self):
        return f"{self.titulo}"

class Cart(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return f"{self.usuario} - {self.product}"