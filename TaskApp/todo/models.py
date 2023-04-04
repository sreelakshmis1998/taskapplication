from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tasks(models.Model):
    task_name=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    status=models.BooleanField(default=False)

class Vehicle(models.Model):
    vehicle_name=models.CharField(max_length=50)
    vehicle_number=models.CharField(max_length=50)
    model=models.CharField(max_length=50)
    owner=models.CharField(max_length=50)
    km_driven=models.PositiveIntegerField()
    purchase_date=models.DateField(null=True)
    options=(('petrol','petrol'),('diesel','diesel'),('ev','ev'))
    fuel_type=models.CharField(max_length=50,choices=options,default="petrol")
    
    def __str__(self):
        return super.vehicle_name