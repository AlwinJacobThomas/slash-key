from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Merchant)
admin.site.register(Catagory)
admin.site.register(Product)