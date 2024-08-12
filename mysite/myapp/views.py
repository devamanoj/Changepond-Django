from django.shortcuts import render
from django.http import *
def home(request):
    return HttpResponse("Home Page")

def about(request):
    return HttpResponse("About")

def contact(request):
    return HttpResponse("contact")
