from django.contrib import admin
from django.urls import path
from core.views import index,contact,login,cart
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index),  
    path('contact/', contact , name = 'contact'),
    path('login/', login , name = 'login'),
    path('admin/', admin.site.urls),
    path('cart/', cart , name = 'cart'),
      
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
