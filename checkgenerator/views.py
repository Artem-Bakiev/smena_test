from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create_checks(request):
    if request.POST:
        return HttpResponse({})

def new_checks(request):
    return HttpResponse({})

def check(request):
    return HttpResponse({})