from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("You will see all products here")

def transactions(request):
    return HttpResponse("You will see all and product specific transactions here")