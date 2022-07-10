from itertools import product
from urllib import response
from django.shortcuts import render
from core.models import Product
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Product, Merchant, Catagory
from .serializers import CatagorySerializer, MerchantSerializer, ProductSerializer

class ProductList(APIView):

    def get(self, request):
        # breakpoint()
        breakpoint()
        user = Merchant.objects.get(user=request.user)
        obj = Product.objects.filter(seller=user)
        serialiser = ProductSerializer(obj, many=True)

        return Response(serialiser.data, status=status.HTTP_200_OK)


class MerchantList(APIView):
    
    def get(self, request):
        obj = Merchant.objects.all()
        serialzier = MerchantSerializer(obj, many=True)
        return Response(serialzier.data, status=status.HTTP_200_OK)


class CatagoryList(APIView):

    def get(self, request):
        obj = Catagory.objects.all()
        serializer = CatagorySerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CatagorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



# orm views

def merchant_dashboard(request):
    return render(request, 'merchant_dashboard.html')