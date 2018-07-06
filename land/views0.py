from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .views3 import msg
from .models import Location, Kid, Place, Subject

def adm(request,user_id):
    return msg(request,'adm')

def show_users(request):
    qs = User.objects.exclude(last_name="").order_by('last_name')
    return render(request,'show_users.html',
        {'qs':qs}
    )

def show_subj(request):
    qs = Subject.objects.all().order_by('name')
    return render(request,'show_subj.html',
    {'qs':qs}
    )

def show_adr(request):
    qs = Location.objects.all()
    return msg(request,'adr')

def show_kids(request):
    qs = Location.objects.exclude(kid = None).distinct()
    return msg(request,'kids')

def show_places(request):
    qs = Location.objects.exclude(place = None).distinct()
    return msg(request,'places')

def show_claims(request):
    qs = Location.objects.exclude(claim = None).distinct()
    return msg(request,'claims')

def show_prop(request):
    qs = Location.objects.exclude(prop = None).distinct()
    return msg(request,'prop')

def show_courses(request):
    qs = Location.objects.exclude(course = None).distinct()
    return msg(request,'courses')
