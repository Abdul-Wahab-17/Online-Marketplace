from django.shortcuts import render

from items.models import Item, Category

def index(request):
    items = Item.objects.filter(is_sold = False)[0:5]
    categories = Category.objects.all()

    return render(request, 'core/index.html' , {'items': items, 'categories': categories})

def contact(request):
    return render(request, 'core/contact.html')



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to homepage
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'core/login.html')

def logout(request):
    logout(request)
    return redirect('login')