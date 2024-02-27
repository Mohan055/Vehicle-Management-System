from django.contrib import admin
from .models import UserProfile,Vehicle,Vendor,Product, QualityCheck

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Vehicle)
admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(QualityCheck)


