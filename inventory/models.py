from django.db import models
from django.core.validators import MinValueValidator
from users.models import CustomUser as User

# Create your models here.

class Partner(models.Model):
    name = models.CharField(max_length=100, unique=True,)
    phone_number = models.CharField(max_length=100, unique=True, blank=True, null=True,)
    mobile_number = models.CharField(max_length=100, unique=True, blank=True, null=True,)
    address = models.CharField(max_length=100, blank=True, null=True,)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True,)
    is_vendor = models.BooleanField(default=False,)
    is_customer = models.BooleanField(default=False,)
    photo = models.ImageField(upload_to='avatars/partners', null=True, blank=True)
    responsible = models.ForeignKey(User, on_delete=models.PROTECT,)
    date = models.DateTimeField()

   
class Product(models.Model):
    name = models.CharField(max_length=200, unique=True, db_index=True, help_text="Product name is required: It must be unique",)
    description = models.CharField(max_length=200, db_index=True, blank=True, help_text="Optional information about the product",)
    code = models.CharField(max_length=50, unique=True, db_index=True, blank=True, null=True,)
    quantity = models.PositiveIntegerField()
    cost = models.DecimalField(decimal_places=2, max_digits=11, default=0.00, validators=[MinValueValidator(0.00)])
    price = models.DecimalField(decimal_places=2, max_digits=11, default=0.00, validators=[MinValueValidator(0.00)])
    photo = models.ImageField(upload_to='avatars/products', null=True, blank=True)
    responsible = models.ForeignKey(User, on_delete=models.PROTECT,)
    date = models.DateTimeField()
 

class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT,)
    reference = models.CharField(max_length=200)
    trade_qty = models.IntegerField(default=0)
    unit_price = models.FloatField(default=0.00, validators=[MinValueValidator(0.00)])
    partner = models.ForeignKey(Partner, on_delete=models.PROTECT,)
    responsible = models.ForeignKey(User, on_delete=models.PROTECT,)
    date = models.DateTimeField()
