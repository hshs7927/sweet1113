from django.contrib import admin

# Register your models here.
from .models import Orderlist, Order, Customer, Review
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Orderlist)
admin.site.register(Review)