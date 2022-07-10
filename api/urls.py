from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from .views import ProductList, MerchantList, CatagoryList, MerchantRegistration, ProductEditDel, RegisterUser, AllProduct

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('register/', RegisterUser.as_view()),
    path('productlist/', ProductList.as_view()),
    path('product/<str:id>', ProductEditDel.as_view()),
    path('merchantslist/', MerchantList.as_view()),
    path("merchant-register/", MerchantRegistration.as_view()),
    path('catagory/', CatagoryList.as_view()),
    path('all-product/', AllProduct.as_view())
]
