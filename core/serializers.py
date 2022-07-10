from attr import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Catagory, Product, Merchant


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'catagory', 'price', 'stock', 'seller']

class MerchantSerializer(serializers.ModelSerializer):
    product_list = []
    class Meta:
        model = Merchant
        fields = ['id', 'user', 'shop_name', 'location']

class CatagorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Catagory
        fields = ['id', 'name']