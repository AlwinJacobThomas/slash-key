from dataclasses import dataclass

from django.shortcuts import render
from core.models import Product
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

# import requests


from core.models import Product, Merchant, Catagory
from core.serializers import CatagorySerializer, MerchantSerializer, ProductSerializer, UserSerializer


class RegisterUser(APIView):

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            view = TokenObtainPairView.as_view()
            # breakpoint()
            # return Response(view(request._request))
            return Response(serializer.data)
        return Response(serializer.errors)

class ProductList(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):
        try:
            if (Merchant.objects.get(user=request.user).exist()):
                user = Merchant.objects.get(user=request.user)
                obj = Product.objects.filter(seller=user)
                serialiser = ProductSerializer(obj, many=True)

                return Response(serialiser.data, status=status. HTTP_200_OK)

        except Exception as e:
            return Response("NOt a merchant user")

    def post(self, request):

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductEditDel(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, id):
        try:
            # breakpoint()
            if(Merchant.objects.get(user=request.user)):
                product = Product.objects.filter(id=id)
                #     "title" : request.data['title'],
                #     "catagory":request.data["catagory"],
                #     "price":request.data["price"],
                #     "stock":request.data["stock"],

                # )
                data = request.data
                serializer = ProductSerializer(product, data=   data)

                if serializer.is_valid():
                    serializer.save()
                    return Response("Updated Successfullyy", status=status.HTTP_201_CREATED)
                return Response(serializer.errors)
        except Exception as e:
            return Response(e)

class MerchantList(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):
        obj = Merchant.objects.all()
        serialzier = MerchantSerializer(obj, many=True)
        return Response(serialzier.data, status=status.HTTP_200_OK)


class MerchantRegistration(APIView):

    permission_classes = (IsAuthenticated,)
    def post(self, request):
        data = request.data
        data["user"] = request.user.id

        serializer = MerchantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

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



class AllProduct(APIView):

    def get(self, request):
        obj = Product.objects.all()
        serializer = ProductSerializer(obj, many=True)
        return Response(serializer.data)