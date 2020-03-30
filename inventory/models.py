from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
   
class Right(models.Model):
    name = models.CharField(max_length=100, unique=True)


class User(models.Model):
    first_name = models.CharField(max_length=100,)
    last_name = models.CharField(max_length=100,)
    email = models.EmailField(max_length=100, unique=True,)
    password = models.CharField(max_length=100,)
    phone_number = models.CharField(max_length=100,)
    right = models.ManyToManyField(Right,)
    responsible = models.CharField(max_length=100,)


class Parner(models.Model):
    company_name = models.CharField(max_length=100, unique=True,)
    phone_number = models.CharField(max_length=100, unique=True,)
    mobile_number = models.CharField(max_length=100, unique=True,)
    address = models.CharField(max_length=100,)
    email = models.EmailField(max_length=100, unique=True,)
    is_vendor = models.BooleanField(default=False,)
    is_customer = models.BooleanField(default=False,)
    responsible = models.ForeignKey(User, on_delete=models.PROTECT,)

   
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True, db_index=True, help_text="Product name is required: It must be unique")
    product_description = models.CharField(max_length=200, db_index=True, help_text="Optional information about the product")
    product_code = models.CharField(max_length=50, unique=True,)
    product_qty = models.PositiveIntegerField()
    responsible = models.ForeignKey(User, on_delete=models.PROTECT,)
 

class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT,)
    reference = models.CharField(max_length=200)
    trade_qty = models.IntegerField(default=0)
    unit_price = models.FloatField(default=0.00, validators=[MinValueValidator(0.00)])
    partner = models.ForeignKey(Parner, on_delete=models.PROTECT,)
    responsible = models.ForeignKey(User, on_delete=models.PROTECT,)
    date = models.DateTimeField()