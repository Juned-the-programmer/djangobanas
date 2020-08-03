from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Bill(models.Model):
    name = models.CharField(max_length=100)
    cooler = models.IntegerField()
    rate = models.IntegerField()
    amount = models.IntegerField()
    pending_amount = models.IntegerField()
    subtotal = models.IntegerField()
    task = models.CharField(max_length=100)


class Customer(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name =  models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10)
    email = models.CharField(max_length=50,null=True,blank=True)
    pwd = models.CharField(max_length=100)
    pwd1 = models.CharField(max_length=100)

class DailyEntry(models.Model):
    name = models.CharField(max_length=100)
    cooler = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    # date = models.DateField(auto_now=False , auto_now_add=False , null = True)

class Payment(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    pay = models.IntegerField()
    pending = models.IntegerField()
    date_payed = models.DateTimeField(auto_now_add=True)