from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.utils.text import slugify
from django.contrib.auth.models import User
from .models import Profile, Reference, Location, Kid, Place, Course, Subject
from .forms2 import LookForm
from .forms import Course2Form

def scan(request):
    xusers = User.objects.all().count()
    xaddr = Location.objects.all().count()
    xkids = Kid.objects.all().count()
    xplaces = Place.objects.all().count()
    xcrs = Course.objects.all().count()
    return render(request,'scan.html',
        {
        'xusers':xusers,
        'xaddr':xaddr,
        'xkids':xkids,
        'xplaces':xplaces,
        'xcrs':xcrs
        }
    )

def look(request):
    if request.method == "POST":
        form = LookForm(request.POST)
        if form.is_valid():
            sbj = form.cleaned_data['subjects']
            qs = Course.objects.filter(subject__in=sbj)
            print(qs)
            return render(request,'see.html',
                {'qs':qs}
            )
    else:
        form = LookForm()
        return render(request,'look.html',
            {'form':form}
        )

def course3(request,uname,code):
    user = User.objects.get(username=uname)
    course = Course.objects.get(user=user.id,code=code)
    form = Course2Form(
    initial={
    'name':course.name,
    'locations':course.locations,
    'letter':course.letter,
    'web':course.web,
    'level':course.level,
    'age':course.age
    }
    )
    return render(request,'course3.html',
        {'form':form,
         'code':code,
         'uname':uname
        }
    )
