from django.db import models
from django.contrib import admin

class OrderDB(models.Model):
    Order_No=models.IntegerField(primary_key=True);
    Name=models.CharField(max_length=10);
    Address=models.CharField(max_length=100);
    Restraunt_Name=models.CharField(max_length=25);
    Food=models.CharField(max_length=25);
    Quantity=models.IntegerField();
    Total_amt=models.FloatField();

class OrderDBAdmin(admin.ModelAdmin):
    list_display=['Order_No','Name', 'Address','Restraunt_Name','Food','Quantity','Total_amt']