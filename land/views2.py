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
from math import sqrt

def xy2t(x1,y1,x2,y2):
  dx = x1 - x2
  dy = y1 - y2
  d2 = dx*dx + dy*dy
  d = sqrt(d2)
  me = 0.04075509311105271
  t = d*40/me
  return t

def map11(request):
    return render(request,'map11.html')

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

def choices(user):
    qs = Location.objects.filter(user=user)
    qq = [(x.id,x.name+"("+ x.address +")") for x in qs]
    return qq

def look(request):
    addr_list = choices(request.user)
    if request.method == "POST":
        form = LookForm(request.POST,my_choices=addr_list)
        if form.is_valid():
            sbj = form.cleaned_data['subjects']
            a = form.cleaned_data['addr']
            ad = Location.objects.get(id=a)
            qs = Course.objects.filter(subject__in=sbj)
            rr = []
            for q in qs:
                x = Location.objects.filter(name__in=q.locations,user=q.user)[0]
                t = xy2t(x.lat, x.lng, ad.lat, ad.lng)
                rr.append(
                {'code':q.code,
                'name':q.name,
                'letter':q.letter,
                'user':q.user,
                'time':round(t)}
                )

            return render(request,'see.html',
                {'qs':rr}
            )
    else:
        form = LookForm(my_choices=addr_list)

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
