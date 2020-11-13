from django.contrib import admin

# Register your models here.
from .models import Store, Store_set, Allitem, Today_lineup

admin.site.register(Store)
admin.site.register(Store_set)
admin.site.register(Allitem)
admin.site.register(Today_lineup)