from django.contrib import admin

# Register your models here.
from .models import Orderlist, Order, Customer
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Orderlist)