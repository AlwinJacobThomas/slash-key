from operator import le
from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField

# Create your models here.


class Catagory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name



class Merchant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    def __str__(self) -> str:
        return self.shop_name

class Product(models.Model):
    title = models.CharField(max_length=255)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    seller = models.ForeignKey(Merchant, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

