from django.shortcuts import render
from .models import Product
from .models import Order

# Create your views here.
def catalog(request):
    products = Product.objects.all()
    return render(request,'magazin/catalog.html', {'products':products})

def product_ditail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'magazin/product_ditail.html', {'product':product})

def order(request):
    order = Order.objects.all()
    return render(request, 'magazin/order.html', {'order':order})

def create_order(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'magazin/create_order.html', {'product':product})
