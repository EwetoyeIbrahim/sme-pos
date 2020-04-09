from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import CustomUser
# Create your views here.



class UserList(generic.ListView):
    model = CustomUser
    context_object_name = 'user_list'
    template_name = 'users/user_list.html'


class User_(LoginRequiredMixin,):
    model = CustomUser
    fields = ['photo', 'name', 'description', 'code', 'quantity',
                'cost', 'price',]
    success_url = reverse_lazy('users:user-list')


class UserCreate(User_, generic.CreateView):
    
    def form_valid(self, form):
        form.instance.responsible = self.request.user
        form.instance.date = datetime.now()

        return super().form_valid(form)


class UserUpdate(User_, generic.UpdateView):
    pass


class UserDelete(User_, generic.DeleteView):
    pass
