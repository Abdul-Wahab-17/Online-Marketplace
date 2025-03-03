from django.db import models
from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name or f"User {self.id}"


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    items = models.CharField(max_length=45, null=True)

    def __str__(self):
        return f"Cart of {self.user}"


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=True)
    price = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True)
    image = models.BinaryField(null=True)
    is_sold_out = models.BooleanField(null=True)
    created_at = models.CharField(max_length=45, null=True)
    created_by = models.CharField(max_length=45, null=True)

    def __str__(self):
        return self.name


class ItemHasCart(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('item', 'cart')

    def __str__(self):
        return f"{self.item} in {self.cart}"
