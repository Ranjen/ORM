# Ex01 Django ORM Web Application
## Date: 22-11-2025

## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
models.py

from django.db import models
from django.contrib import admin
class Flipkart(models.Model):
    Serial_Number=models.IntegerField()
    Product_Name=models.CharField(max_length=30)
    Brand_Name=models.CharField(max_length=50)
    Product_Code=models.IntegerField(primary_key=True)
    Category=models.CharField(max_length=20)
    Description=models.TextField()
    Price=models.FloatField()
class FlipkartAdmin(admin.ModelAdmin):
    list_display=["Serial_Number","Product_Name","Brand_Name","Product_Code","Category","Description","Price"]

admin.py

from django.contrib import admin
from .models import Flipkart,FlipkartAdmin
admin.site.register(Flipkart,FlipkartAdmin)
```

## OUTPUT
![alt text](<Screenshot (15).png>)


## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
