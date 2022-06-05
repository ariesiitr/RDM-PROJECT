from django.db import models
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class DETAIL(models.Model):

    image = models.ImageField(upload_to="images", blank=True, null=True)
    detail=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    product_name=models.CharField(max_length=100,default="")
    final=models.IntegerField(default=0)
    type=models.CharField(max_length=100,default="")

class Cart(models.Model):
    username =models.CharField(max_length=100,default="")
    product_id=models.CharField(max_length=100,default="")
    quantity=models.IntegerField(default=0)
    total_cost=models.IntegerField(default=0)
    userid=models.CharField(max_length=100,default="")

