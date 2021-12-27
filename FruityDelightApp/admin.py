from django.contrib import admin

from FruityDelightApp.models import Complaint, Order

# Register your models here.
admin.site.register(Order)
admin.site.register(Complaint)