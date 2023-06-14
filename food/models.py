from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField(default=0)
    item_image = models.CharField(max_length=500, null=True)
