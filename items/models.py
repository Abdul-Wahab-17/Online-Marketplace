from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    Category = models.ForeignKey(Category, on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank = True , null = True)
    price = models.FloatField()
    image = models.ImageField(upload_to = 'items_images', blank = True, null = True)
    is_sold = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name