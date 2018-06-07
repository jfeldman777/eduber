from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.utils.text import slugify
from django.contrib.auth.models import User
from .models import Profile, Reference, Location, Kid, Place, Course, Subject
from .forms2 import LookForm

def look(request):
    
    if request.method == "POST":
        form = LookForm(request.POST)
        if form.is_valid():
            return render(request,'see.html',
                {}
            )
    else:
        form = LookForm()
        return render(request,'look.html',
            {'form':form}
        )
