from django.db import models

# Create your models here.


class Subscription(models.Model):
    SubscriptionType= models.CharField(max_length=300, unique=True)
    NumberofDuration=models.IntegerField(max_length=5)
    TotalAmount=models.IntegerField(max_length=5)
    description=models.CharField(max_length=300)
   
class Payment(models.Model):
    
    User_id=models.IntegerField(max_length=10)
    Subscription_id= models.CharField(max_length=300)
    TotalAmount=models.IntegerField(max_length=5)
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

#class Category(models.Model):
  #  name = models.CharField(max_length=50)


   
    

