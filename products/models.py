from django.db import models

# Create your models here.

class Upload(models.Model):
    productname = models.CharField(max_length = 50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField(max_length=100)
    image = models.FileField(upload_to="pics/")    
    category = models.CharField(max_length = 50)
    user_id = models.IntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

from django.db import models

# Create your models here.

class Upload(models.Model):
    productname = models.CharField(max_length = 50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField(max_length=100)
    image = models.FileField(upload_to="pics/")    
    category = models.CharField(max_length = 50)
    user_id = models.IntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=50)


   


   