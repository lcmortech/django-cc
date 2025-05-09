from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

# functional view
def hello_world(request):
    return HttpResponse("Hello World")

# class-based view

class HelloNYC(View): # inherits from the view class
    def get(self, request):
        return HttpResponse("Hello NYC")
