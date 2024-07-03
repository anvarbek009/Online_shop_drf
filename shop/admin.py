from django.contrib import admin
from .models import  Product,Categories,Order
# Register your models here.
admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(Order)