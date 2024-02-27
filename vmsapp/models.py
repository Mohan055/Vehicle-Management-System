
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_security_department = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
   

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    vehicle_name = models.CharField(max_length=50)
    vehicle_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=50)
    delivery_challan_number = models.CharField(max_length=50)
    purchase_order_number = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)  # Associate vehicle with product based on PO number
    vehicle_image = models.ImageField(upload_to='vehicle_images/')
    date_and_time = models.DateTimeField(auto_now_add=True)
    checked_out = models.BooleanField(default=False) 
    
    def __str__(self):
        return self.vehicle_number

class QualityCheck(models.Model):
    STATUS_CHOICES = (
        ('Processing', 'Processing'),
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
    )

    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE, related_name='quality_check')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Processing')
