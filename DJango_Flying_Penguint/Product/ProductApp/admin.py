from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['P_image','P_price','P_name']

admin.site.register(Product,ProductAdmin)