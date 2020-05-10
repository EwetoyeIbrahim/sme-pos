from inventory_models import Partner, Product, Transaction
from users.models import CustomUser as User
from django.db import transaction
prod_id_list = [2,1,3]
trade_list_qty = [11,2,4]
unit_price_list = [100,120,310]
partner = Partner.objects.get(pk=1)