from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Catagory, Product, Merchant



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