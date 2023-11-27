from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
# Create your views here.


@login_required(login_url='user-login')
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'orders':orders,   
        'form':form,
        'products':products,
    }
    return render(request, 'dashboard/index.html', context)

@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    order_count = Order.objects.all().count()
    items_count = Product.objects.all().count()
    context = {
        'workers' : workers,
        'workers_count': workers_count,
        'order_count':order_count,
        'items_count':items_count
    }
    return render(request, 'dashboard/staff.html', context)

@login_required(login_url='user-login')
def staff_detail(request, pk):
    workers = User.objects.get(id = pk)
    context = {
        'workers' : workers,
    }
    return render(request, 'dashboard/staff_detail.html', context)

@login_required(login_url='user-login')
def product(request):
    workers = User.objects.all()
    workers_count = workers.count()
    order_count = Order.objects.all().count()
    items = Product.objects.raw("SELECT * FROM dashboard_product")
    items_count = Product.objects.all().count()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'items' : items,
        'form' : form,
        'workers_count':workers_count,
        'order_count':order_count,
        'items_count':items_count,
    }
    return render(request, 'dashboard/product.html', context)

@login_required(login_url='user-login')
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

@login_required(login_url='user-login')
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form' : form,
    }
    return render(request, 'dashboard/product_update.html', context)
   

@login_required(login_url='user-login')
def order(request):
    orders = Order.objects.all()
    order_count = Order.objects.all().count()
    workers = User.objects.all()
    workers_count = workers.count()
    items_count = Product.objects.all().count()
    context = {
        'orders':orders,
        'workers_count':workers_count,
        'order_count':order_count,
        'items_count':items_count,
    }
    return render(request, 'dashboard/order.html', context)




