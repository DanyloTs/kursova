from django.contrib import admin
from .models import Product
from django.contrib.auth.models import Group

admin.site.site_header = 'Курсова робота'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quanity',)
    list_filter = ('category', 'quanit')

admin.site.register(Product, ProductAdmin)

