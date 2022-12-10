from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import requests 
import json 
from .forms import NameForm 
# Create your views here.
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
     
    return "%d:%02d:%02d" % (hour, minutes, seconds)
def index(request): 
    if request.method=="POST":
        form = NameForm(request.POST)
        if form.is_valid(): 
            city = form.cleaned_data['location']
            url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + ",uk&APPID={YOUR_API_KEY}"
            request_API = requests.get(url)
            data = json.loads(request_API.text) 
            if len(data) > 2:
                time = convert(data['dt'])

                return render(request,'components/index.html',{'time' : time, 'data' : data, 'form' : form})
            else:
                form = NameForm()
                return render(request,"components/index.html",{'form' : form , 'errorMessage' : 'City not listed!!'})

    else: 
        form = NameForm() 
    
    return render(request,"components/index.html",{'form' : form})
