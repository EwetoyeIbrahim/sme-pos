from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Product

def index(request):
    return HttpResponse("You will see all products here")

def transactions(request):
    return HttpResponse("You will see all and product specific transactions here")

class ProductList(generic.ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'inventory/product_list.html'
    
class InventoryList(generic.ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'inventory/inventory_list.html'
    
class EmployeeList(generic.ListView):
    model = Product
    context_object_name = 'employee_list'
    template_name = 'inventory/user_list.html'
    
class PartnerList(generic.ListView):
    model = Product
    context_object_name = 'partner_list'
    template_name = 'inventory/partner_list.html'