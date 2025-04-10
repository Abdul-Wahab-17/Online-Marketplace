from django.shortcuts import render

from items.models import Item, Category

def index(request):
    items = Item.objects.filter(is_sold_out = False)[0:5]
    categories = Category.objects.all()

    return render(request, 'core/index.html' , {'items': items, 'categories': categories})

def contact(request):
    return render(request, 'core/contact.html')

def login(request):
    return render(request , 'core/login.html')

def cart(request):
    return render(request , 'core/cart.html')