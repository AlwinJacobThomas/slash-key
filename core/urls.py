from django.urls import path

from .views import merchant_dashboard

urlpatterns = [
    path('', merchant_dashboard, name="merchant_dashboard")
]
