from django.contrib import admin

from .models import Partner, Product, Transaction
# Register your models here.

admin.site.register([Partner, Product, Transaction])