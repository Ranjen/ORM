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
