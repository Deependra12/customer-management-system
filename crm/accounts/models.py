from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    profile_pic=models.ImageField(default="download.png",null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.name)

class Tag(models.Model):
    name=models.CharField(max_length=100,null=True)

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('Out door','Out door')
    )
    name=models.CharField(max_length=100,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=100,null=True,choices=CATEGORY)
    description=models.CharField(max_length=100,null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    tag=models.ManyToManyField(Tag)

    def __str__(self):
        return str(self.name)



class Order(models.Model):
    STATUS=(
        ('pending','pending'),
        ('out of delivery','out of delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=100,null=True,choices=STATUS)
    note=models.CharField(max_length=100,null=True)
    
