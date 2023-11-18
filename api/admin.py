from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product 
    list_display = 'seller', 'price', 'inventory', 'delivery_time'

    @admin.display()
    def seller(self, obj):
        return obj.owner.full_name