from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.db.models import Max
from django.http import JsonResponse
#from django.core import serializers

from django import forms

import json

from .models import Partner, Product, Transaction
from datetime import datetime

from search_listview.list import SearchableListView

def index(request):
    return HttpResponse("You will see all products here")


class Product_(PermissionRequiredMixin):
    model = Product
    permission_required = ('inventory.add_product')
    fields = ['photo', 'name', 'description', 'code', 'quantity',
                'cost', 'price',]
    success_url = reverse_lazy('inventory:product-list')


class ProductList(Product_, generic.ListView):
    context_object_name = 'product_list'
    permission_required = ('inventory.view_product')
    template_name = 'inventory/product_list.html'


class ProductCreate(Product_, generic.CreateView):
    
    def form_valid(self, form):
        form.instance.responsible = self.request.user
        form.instance.date = datetime.now()

        return super().form_valid(form)


class ProductUpdate(Product_, generic.UpdateView):
    pass


class ProductDelete(Product_, generic.DeleteView):
    pass


class Partner_(PermissionRequiredMixin,):
    model = Partner
    permission_required = ('inventory.add_partner')
    fields = ['photo', 'name', 'phone_number', 'mobile_number',
                'address', 'email', 'is_vendor', 'is_customer',]
    success_url = reverse_lazy('inventory:partner-list')
    
    
class PartnerList(Partner_, generic.ListView):
    context_object_name = 'partner_list'
    permission_required = ('inventory.view_partner')
    template_name = 'inventory/partner_list.html'


class PartnerCreate(Partner_, generic.CreateView):
    
    def form_valid(self, form):
        form.instance.responsible = self.request.user
        form.instance.date = datetime.now()

        return super().form_valid(form)


class PartnerUpdate(Partner_, generic.UpdateView):
    pass


class PartnerDelete(Partner_, generic.DeleteView):
    pass


#class TransactionList(generic.ListView):
class TransactionList(SearchableListView):
    model = Transaction
    template_name = "inventory/transaction_list.html"
    paginate_by = 10
    searchable_fields = ["product__name"]
    specifications = {
    }
    '''model = Transaction
    context_object_name = 'transaction_list'
    #permission_required = ('inventory.view_transaction')
    template_name = 'inventory/transaction_list.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(name__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list
    '''


class InventoryList(Partner_, generic.ListView):
    context_object_name = 'product_list'
    template_name = 'inventory/inventory_list.html'


class IssueProduct(PermissionRequiredMixin, generic.ListView):
    model = Product
    permission_required = ('inventory.add_product')
    fields = ['photo', 'name', 'code', 'quantity', 'price',]
    context_object_name = 'products'
    template_name = 'inventory/transact_in.html'

    
    def get_context_data(self, **kwargs):
        '''
        Convertion of the default query set to dictionary,
        is the most efficient way, known to me for now, I could get the
        selected items properties which will be used to populate the form
        '''
        customers = Partner.objects.filter(is_customer=1)
        #qs = Product.objects.all()
        context = super(IssueProduct, self).get_context_data(**kwargs)
        context['customers'] = customers
        #context = json.loads(serializers.serialize('json', qs))
        print(context)
        return context

    def post(self, request):
        print("Thank you")

class TestForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ('reference',)

def test_form(request):
    form = TestForm(initial=dict(foo=request.__))
    context = dict(form=form)
    template_name = 'testapp/test.html'
    return render(request, template_name, context)
'''
class ExecuteTransaction(generic.View):
    def get(self, request):
        product_name = request.GET.get('product_name', None)
        product = Product.objects.filter(name=product_name).first().id
        trade_qty = request.GET.get('trade_qty', None)
        unit_price = request.GET.get('unit_price', None)
        partner = request.GET.get('customer', None)
'''

def transact_api(request):
    if request.method == 'POST':
        prod_id_list = request.POST.getlist('prod_id_list[]', None)
        trade_qty_list=request.POST.getlist('trade_qty_list[]', None)
        unit_price_list=request.POST.getlist('unit_price_list[]', None)
        partner = Partner.objects.get(pk=request.POST.get('partner', None))
        reference = 'Ref'+str(Transaction.objects.aggregate(id_max=Max('id'))['id_max']+1)
        new_transact = [Transaction(
                            product=Product.objects.get(pk=prod_id_list[i]),
                            trade_qty=trade_qty_list[i],
                            unit_price=unit_price_list[i], 
                            partner=partner, 
                            reference=reference, 
                            responsible= request.user, 
                            date=timezone.now(),
                            ) for i in range(len(prod_id_list))]
        Transaction.objects.bulk_create(new_transact)
        report = {"Successful Transaction": prod_id_list}
        return JsonResponse(report)

    


        



