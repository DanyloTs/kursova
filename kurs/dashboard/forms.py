from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'quanity']
        labels = {
            'quanity': 'Кількість',
            'name': 'Назва',
            'category':'Категорія'
        }

     

        
