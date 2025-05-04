from django.shortcuts import render
from django.http import HttpResponse
from django.views import view

# Create your views here.

# functional view
def hell_world(request):
    return HttpResponse("Hello World")

# class-based view

class HelloNYC(View): # inherits from the view class
    
