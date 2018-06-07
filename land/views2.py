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
    form = LookForm(
        initial={'subjects':(('1','11'),('2','22'))}
    )
    return render(request,'look.html',
        {'form':form}
    )
