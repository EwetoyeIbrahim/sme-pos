from django.contrib import admin

from .models import Parner, Product, Transaction
# Register your models here.

admin.site.register([Parner, Product, Transaction])