from django.shortcuts import render
from django import HttpResponse
# Create your views here.

def my_blog(request):
    return HttpResponse("Hello, Blog!")