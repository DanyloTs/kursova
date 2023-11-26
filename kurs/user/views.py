from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUser

# Create your views here.
def register(request):
    if request.method == 'POST':

        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    else:
        form = CreateUser()
    context = {
        'form' : form,

    }
    return render(request, 'user/register.html', context)

def profile(request):
    return render(request, 'user/profile.html')
