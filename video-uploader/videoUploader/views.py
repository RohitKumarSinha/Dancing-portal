from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from sprout.client import SproutClient
from .models import upload_video
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

        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        print(name,email,desc)
        # Upload video
        response =  sprout.video.upload('media/'+ filename, title="Rohitt!")
        for key, value in response.items(): 
            if (str(key) == "id"):
                print("id") 
                print(value)
                id = value
            if (str(key) == "security_token"): 
                print("token")
                print(value)
                token = value
            if (str(key) == 'embed_code'): 
                print(value)
        print(id,token)
        url = "https://videos.sproutvideo.com/embed/" + id + "/" + token
        print(url)
        video_data = upload_video(name=name, email=email, desc=desc, url = url, )
        video_data.save()
    return render(request,'index.html')

def view(request):
    return render(request,'view.html')