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
    path('transactions/', views.transactions, name='transactions'), 
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('values/', views.InventoryList.as_view(), name='inventory_list'),
    path('employees/', views.EmployeeList.as_view(), name='employee_list'),
    path('partners/', views.PartnerList.as_view(), name='partner_list'),
]
