from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render (request,'home.html')

def contact(request):
    return render(request,'contact.html')

def index(reqest):
    return render(reqest,'index.html')

def view(request):
    return render(request,'view.html')