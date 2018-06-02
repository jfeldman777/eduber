from django.shortcuts import render
from django.http import HttpResponse

# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def index(request):
    return render(request,'index.html')

def xin(request):
    return render(request,'in.html')

def about(request):
    return render(request,'about.html')

def map(request):
    return render(request,'map.html')

def gps(request):
    return render(request,'gps.html')

def demo(request,lat,lng):
    request.session["lat"] = lat;
    request.session["lng"] = lng;
    return render(request,'demo.html')

def demo_map(request):
    d = {}
    d['lat'] = request.session.get('lat',0)
    d['lng'] = request.session.get('lng',0)
    return render(request,'demo_map.html',d)
