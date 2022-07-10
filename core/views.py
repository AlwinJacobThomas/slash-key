from django.shortcuts import render





def merchant_dashboard(request):
    return render(request, 'merchant_dashboard.html')