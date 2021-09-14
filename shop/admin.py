from django.contrib import admin
from .models import Contact,Order,Product

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)