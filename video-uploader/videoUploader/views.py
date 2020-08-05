from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from sprout.client import SproutClient
# from urlparse import urljoin

# Create your views here.
def home(request):
    return render (request,'home.html')

def contact(request):
    return render(request,'contact.html')

def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        sprout = SproutClient("948ea6bdb9ac2b12a1b045108b13c648")
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        # Upload video
        response =  sprout.video.upload('media/'+ filename, title="Rohitt!")
        for key, value in response.items(): 
            if (str(key) == "id"):
                print("id") 
                print(value)
            if (str(key) == "security_token"): 
                print("token")
                print(value)  
            if (str(key) == 'embed_code'): 
                print(value) 
    return render(request,'index.html')

def view(request):
    return render(request,'view.html')