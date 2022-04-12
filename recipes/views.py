import re
from django.http import Http404, HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    return HttpResponse('Contacts')

def about(request):
    return HttpResponse('About')