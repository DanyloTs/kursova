from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group

admin.site.site_header = 'Курсова робота'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quanity',)
    list_filter = ('category', 'quanity')

   

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'staff', 'date', 'order_quanity')
    


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

