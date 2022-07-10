from django.urls import path

from .views import ProductList, MerchantList, CatagoryList

urlpatterns = [
    path('productlist/', ProductList.as_view()),
    path('merchantslist/', MerchantList.as_view()),
    path('catagory/', CatagoryList.as_view())
]
