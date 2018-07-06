from django.shortcuts import render
from django.contrib.auth.models import User
from .views3 import msg

def show_users(request):
    qs = User.objects.exclude(last_name="").order_by('last_name')
    
    return render(request,'show_users.html',
        {'qs':qs}
    )

def show_adr(request):
    return msg(request,'adr')

def show_kids(request):
    return msg(request,'kids')

def show_places(request):
    return msg(request,'places')

def show_claims(request):
    return msg(request,'claims')

def show_prop(request):
    return msg(request,'prop')

def show_courses(request):
    return msg(request,'courses')
