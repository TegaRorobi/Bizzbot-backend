from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product 
    list_display = 'seller', 'name', 'price', 'inventory', 'delivery_time'

    @admin.display()
    def seller(self, obj):
        return obj.seller.full_name