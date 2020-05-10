"""smepos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.index, name='index'),
    path('issuing/', views.IssueProduct.as_view(), name='issue-products'),
    path('receiving/', views.ReceiveProduct.as_view(), name='receive-products'),
    path('transact_api/', views.transact_api, name='transact-api'),
    path('transactions/', views.TransactionList.as_view(), name='transactions'),
    path('values/', views.InventoryList.as_view(), name='inventory-list'),

    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/add', views.ProductCreate.as_view(), name='product-add'),
    path('products/<int:pk>/', views.ProductUpdate.as_view(), name='product-update'),
    path('products/<int:pk>/delete', views.ProductDelete.as_view(), name='product-delete'),

    path('partners/', views.PartnerList.as_view(), name='partner-list'),
    path('partners/add', views.PartnerCreate.as_view(), name='partner-add'),
    path('partners/<int:pk>/', views.PartnerUpdate.as_view(), name='partner-update'),
    path('partners/<int:pk>/delete', views.PartnerDelete.as_view(), name='partner-delete'),
    
]
