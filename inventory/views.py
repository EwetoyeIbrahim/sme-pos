from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Partner, Product
from datetime import datetime

def index(request):
    return HttpResponse("You will see all products here")

def transactions(request):
    return HttpResponse("You will see all and product specific transactions here")

class ProductList(generic.ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'inventory/product_list.html'


class Product_(LoginRequiredMixin):
    model = Product
    fields = ['photo', 'name', 'description', 'code', 'quantity',
                'cost', 'price',]
    success_url = reverse_lazy('inventory:product-list')


class ProductCreate(Product_, generic.CreateView):
    
    def form_valid(self, form):
        form.instance.responsible = self.request.user
        form.instance.date = datetime.now()

        return super().form_valid(form)


class ProductUpdate(Product_, generic.UpdateView):
    pass


class ProductDelete(Product_, generic.DeleteView):
    pass


class PartnerList(generic.ListView):
    model = Product
    context_object_name = 'partner_list'
    template_name = 'inventory/partner_list.html'

class Partner_(LoginRequiredMixin,):
    model = Partner
    fields = ['photo', 'name', 'description', 'code', 'quantity',
                'cost', 'price',]
    success_url = reverse_lazy('inventory:product-list')


class PartnerCreate(Partner_, generic.CreateView):
    
    def form_valid(self, form):
        form.instance.responsible = self.request.user
        form.instance.date = datetime.now()

        return super().form_valid(form)


class PartnerUpdate(Partner_, generic.UpdateView):
    pass


class PartnerDelete(Partner_, generic.DeleteView):
    pass


class InventoryList(generic.ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'inventory/inventory_list.html'
