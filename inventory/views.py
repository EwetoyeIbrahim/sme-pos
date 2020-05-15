from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.db.models import Sum ,Max , F, FloatField
from django.db import transaction
from django.http import HttpResponse
from django import forms

from search_listview.list import SearchableListView
from .models import Partner, Product, Transaction

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
        form.instance.date = timezone.now()
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
        form.instance.date = timezone.now()

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
    searchable_fields = ["product__name", "partner__name", "reference"]
    specifications = {
        "product__name": "__icontains",
        "partner__name": "__icontains",
        "reference": "__icontains",
        }
    
    def get_context_data(self, **kwargs):
        '''
        Convertion of the default query set to dictionary,
        is the most efficient way, known to me for now, I could get the
        selected items properties which will be used to populate the form
        '''
        transaction_list = Transaction.objects.annotate(total=Sum(F('trade_qty')*F('unit_price')))
        context = super(TransactionList, self).get_context_data(**kwargs)
        context['transaction_list'] = transaction_list
        print({"context":context})
        return context
    
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
    template_name = 'inventory/transact_base.html'

    
    def get_context_data(self, **kwargs):
        '''
        Convertion of the default query set to dictionary,
        is the most efficient way, known to me for now, I could get the
        selected items properties which will be used to populate the form
        '''
        trigger = "issuing"
        customers = Partner.objects.filter(is_customer=1)
        context = super(IssueProduct, self).get_context_data(**kwargs)
        context['other_params'] = {"partners":customers, "trigger":trigger}
        print({"context":context})
        return context

    def post(self, request):
        print("Thank you")

class ReceiveProduct(IssueProduct):

    def get_context_data(self, **kwargs):
        '''
        Convertion of the default query set to dictionary,
        is the most efficient way, known to me for now, I could get the
        selected items properties which will be used to populate the form
        '''
        trigger = "receiving"
        vendors = Partner.objects.filter(is_vendor=1)
        context = super(ReceiveProduct, self).get_context_data(**kwargs)
        context['other_params'] = {"partners":vendors, "trigger":trigger}
        print({"context":context})
        return context
    
@require_POST
def transact_api(request):
    ''' It is expected that the validation handling must have handle by
    the javascripts thus validation may not be neccessary here.'''
    # getting the result data
    trigger = partner = request.POST.get('trigger')
    prod_id_list = request.POST.getlist('prod_id_list[]')
    trade_qty_list=request.POST.getlist('trade_qty_list[]')
    unit_price_list=request.POST.getlist('unit_price_list[]')
    partner = Partner.objects.get(pk=request.POST.get('partner'))
    # computing the reference number
    if trigger=="receiving":
        ref_ = "IN"
    if trigger=="issuing":
        ref_ = "OUT"
    reference = ref_ + str(Transaction.objects.aggregate(id_max=Max('id'))['id_max']+1)
    # instantiate the new transaction list for later creation in bulk
    new_transact = [Transaction(
                        product=Product.objects.get(pk=prod_id_list[i]),
                        trade_qty=trade_qty_list[i],
                        unit_price=unit_price_list[i], 
                        partner=partner, 
                        reference=reference, 
                        responsible= request.user, 
                        date=timezone.now(),
                        ) for i in range(len(prod_id_list))]
    # select and lock the concerned product untill end of transaction
    prod_update = Product.objects.select_for_update().filter(pk__in=prod_id_list)
    #print(prod_update)
    with transaction.atomic():
        # Atomicity guarantees that an case an error is encountred
        # all pending transactions are rolled back
        Transaction.objects.bulk_create(new_transact)
        for i in range(len(prod_id_list)):
            if trigger=="receiving":
                prod_update.filter(pk=prod_id_list[i]).update(
                    quantity=F('quantity')+trade_qty_list[i])
            if trigger=="issuing":
                prod_update.filter(pk=prod_id_list[i]).update(
                    quantity=F('quantity')-trade_qty_list[i])
    return HttpResponse('Successful')
