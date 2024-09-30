from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products (models.Model):
    productName = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True, default="null.jpg", )
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
class Orders (models.Model):
    User = models.ForeignKey(User , on_delete=models.CASCADE, null=True)
    orders = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    