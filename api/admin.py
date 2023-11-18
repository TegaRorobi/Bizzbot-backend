from django.contrib import admin
from .models import *
from .models2 import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product 
    list_display = 'seller', 'name', 'price', 'inventory', 'delivery_time'

    @admin.display()
    def seller(self, obj):
        return obj.seller.full_name
    

@admin.register(OpeningDay)
class OpeningDayAdmin(admin.ModelAdmin):
    model = OpeningDay
    list_display = 'day', 'opening_time', 'closing_time'