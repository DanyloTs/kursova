from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class CreateUser(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields =  ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Логін', 
            'email': 'Ел. Пошта',
            'password1': 'Пароль',
            'password2': 'Підвердити пароль',
        }



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'email':'Пошта',
            'username': 'Логін',
            }
       
        

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone', 'image']
        labels = {
            'address': 'Адреса', 
            'phone': 'Телефон',  
            'image': 'Зоображення',  
            
        }