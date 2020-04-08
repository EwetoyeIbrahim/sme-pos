from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Product
from datetime import datetime

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

class ProductCreate(LoginRequiredMixin, generic.CreateView):
    model = Product
    fields = ['name', 'description', 'code', 'quantity',
                'cost', 'price', 'photo',]
    success_url = reverse_lazy('inventory:product-list')
    
    def form_valid(self, form):
        form.instance.responsible = self.request.user
        form.instance.date = datetime.now()

        return super().form_valid(form)


class ProductUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Product
    fields = ['name', 'description', 'code', 'quantity',
                'cost', 'price', 'photo',]
    success_url = reverse_lazy('inventory:product-list')
    

class ProductDelete(LoginRequiredMixin, generic.DeleteView):
    model = Product
    success_url = reverse_lazy('inventory:product-list')
    