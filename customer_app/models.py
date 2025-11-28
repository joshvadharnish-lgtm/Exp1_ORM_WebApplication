from django.db import models
from django.contrib import admin

class Customer(models.Model):
    customer_name=models.CharField(max_length=100,help_text="Enter Customer Name")
    customer_number=models.IntegerField(help_text="Enter Customer Number")
    customer_email=models.CharField(max_length=100,help_text="Enter Customer Email")

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_number', 'customer_email')