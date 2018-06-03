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

def profile(request):
    return render(request,'profile.html')    

def xin(request):
    return render(request,'in.html')

def about(request):
    return render(request,'about.html')

def demo1(request):
    return render(request,'demo1.html')

def demo2(request):
    return render(request,'demo2.html')

def demo3(request):
    return render(request,'demo3.html')
