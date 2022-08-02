from django.db import models

# Create your models here.
class Customer(models.Model):
    c_name = models.CharField(max_length=30)
    c_address = models.CharField(max_length=50)
    c_email = models.EmailField()
    phone = models.IntegerField()
    def __str__(self):
        return self.c_name
    
class Plan(models.Model):
 name = models.CharField(max_length=50)
 price = models.IntegerField() 
 days = models.IntegerField() 
 offer = models.CharField(max_length=50)
 def __str__(self):
        return self.name
 
 
class Subscription(models.Model):
 plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
 customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
 a_date = models.DateField(("date"), auto_now=False, auto_now_add=False)