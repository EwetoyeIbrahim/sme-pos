from datetime import datetime

from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import CustomUser as User

class User_(PermissionRequiredMixin):
    model = User
    permission_required = ('users.add_user')
    fields = ['photo', 'email', 'user_name', 'first_name', 'last_name',
                'phone_number', 'address', 'is_staff', 'is_active',]
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:user-list')


class UserList(User_, generic.ListView):
    permission_required = ('users.view_user')
    context_object_name = 'user_list'
    template_name = 'users/user_list.html'


class UserCreate(User_, generic.CreateView):
    
    def form_valid(self, form):
        form.instance.responsible = self.request.user
        form.instance.date = datetime.now()

        return super().form_valid(form)


class UserUpdate(User_, generic.UpdateView):
    pass


class UserDelete(User_, generic.DeleteView):
    pass
