from django import forms
from .models import Product, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'quanity']
        labels = {
            'quanity': 'Кількість',
            'name': 'Назва',
            'category':'Категорія'
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'order_quanity']
        labels = {
            'product':'Товар',
            'order_quanity':'Кількість'
        }

        
