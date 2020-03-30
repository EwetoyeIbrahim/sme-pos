from django.contrib import admin

# Register your models here.
from .models import User, Parner, Product, Transaction

admin.site.register([User, Parner, Product, Transaction])