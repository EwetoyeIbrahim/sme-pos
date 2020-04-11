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

app_name = 'users'

urlpatterns = [
    path('', views.UserList.as_view(), name='user-list'),
    path('', views.UserList.as_view(), name='user-list'),
    path('add', views.UserCreate.as_view(), name='user-add'),
    path('<int:pk>/', views.UserUpdate.as_view(), name='user-update'),
    path('<int:pk>/delete', views.UserDelete.as_view(), name='user-delete'),

]
