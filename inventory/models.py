from django.db import models
from django.core.validators import MinValueValidator
from users.models import CustomUser as User

# Create your models here.

class Parner(models.Model):
    company_name = models.CharField(max_length=100, unique=True,)
    phone_number = models.CharField(max_length=100, unique=True, blank=True, null=True,)
    mobile_number = models.CharField(max_length=100, unique=True, blank=True, null=True,)
    address = models.CharField(max_length=100, blank=True, null=True,)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True,)
    is_vendor = models.BooleanField(default=False,)
    is_customer = models.BooleanField(default=False,)
    responsible = models.ForeignKey(User, on_delete=models.PROTECT,)
    date = models.DateTimeField()

   
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True, db_index=True, help_text="Product name is required: It must be unique",)
    product_description = models.CharField(max_length=200, db_index=True, blank=True, help_text="Optional information about the product",)
    product_code = models.CharField(max_length=50, unique=True, db_index=True, blank=True, null=True,)
    product_qty = models.PositiveIntegerField()
    responsible = models.ForeignKey(User, on_delete=models.PROTECT,)
    date = models.DateTimeField()
 

class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT,)
    reference = models.CharField(max_length=200)
    trade_qty = models.IntegerField(default=0)
    unit_price = models.FloatField(default=0.00, validators=[MinValueValidator(0.00)])
    partner = models.ForeignKey(Parner, on_delete=models.PROTECT,)
    responsible = models.ForeignKey(User, on_delete=models.PROTECT,)
    date = models.DateTimeField()
