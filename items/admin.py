from django.contrib import admin

from .models import Category, Item, User, Cart, ItemHasCart

admin.site.register(Category)  
admin.site.register(Item) 
admin.site.register(User)
admin.site.register(Cart)
admin.site.register(ItemHasCart)