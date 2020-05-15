from django.test import TestCase
from django.urls import reverse

from users.models import CustomUser as User
from inventory.models import Partner, Product, Transaction
from inventory.views import transact_api
# Create your tests here.

# custom entries into the database
product_insert = [Product(
        name = prod_name_list[i],
        description = prod_des[i],
        code = code_list[i],
        quantity = qty_list[i],
        cost = cost_list[i],
        price = price_list[i],
        responsible = User.objects.get(pk=1),
    ) for i in range(len(prod_name_list[i]))]

Product.objects.bulk_create(product_insert)


class TransactionViewTestCase(TestCase):
    partner = 1
    prod_id_list = [2,1,3]
    trade_list_qty = [11,2,4]
    unit_price_list = [100,120,310]

    def test_perfect_receiving(self):
        response = self.client.post(reverse('inventory:transact-api'),
                    data={'trigger':'receiving',
                            'pro_id_list[]':prod_id_list, 
                            'trade_qty_list[]':trade_qty_list, 
                            'unit_price_list[]':unit_price_list, 
                            'partner':partner})
        self.assertIs(response.status_code, 200)

    def test_perfect_issuing(self):
        response = self.client.post(reverse('inventory:transact-api'),
                    data={'trigger':'issuing',
                            'pro_id_list[]':prod_id_list, 
                            'trade_qty_list[]':trade_qty_list, 
                            'unit_price_list[]':unit_price_list, 
                            'partner':partner})
        self.assertIs(response.status_code, 200)
