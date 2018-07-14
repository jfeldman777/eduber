from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.utils.text import slugify
from django.contrib.auth.models import User
from math import sqrt
from .models import Location, Place, Kid, Course, Reference, Claim, Prop, Subject
from .forms import PlaceForm, KidForm, CourseForm, MyletterForm
from .forms2 import GoodForm, ClaimForm, PropForm
from .views3 import msg, obj, xy2t
from .models import Profile
from .forms3 import AdmForm

def adm(request,user_id):
    form = None
    if request.method == "POST":
        form = AdmForm(request.POST)
        if form.is_valid():
            profile = Profile.objects.get(user_id = user_id)
            profile.adm_comment = form.cleaned_data['adm_comment']
            profile.save()
            return redirect('/')
        else:
            print(form.errors.as_data())
            return msg(request,'bad adm form')
    else:
        form = AdmForm()

    return render(request,
            'form.html',
            {   'form':form, 'title':'администратор - пользователю'    }

    )

def friend_down(request,user_id):
    u = User.objects.get(pk=user_id)
    p = request.user.profile
    p.friends.remove(u)
    return redirect('/')

def friend_up(request,user_id):
    u = User.objects.get(pk=user_id)
    p = request.user.profile
    p.friends.add(u)
    return redirect('/')

def myletter(request):
    if request.method == "POST":
        form = MyletterForm(request.POST,instance = request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return msg(request,'myletter bad form')
    form = MyletterForm(instance = request.user.profile)
    return render(request,'form.html',
        {'form':form,'title':'о чем я думаю'
        }
    )

def good(request):
    jf = User.objects.get(username='jacobfeldman')
    if request.method == "POST":
        form = GoodForm(request.POST)
        if form.is_valid():
            letter = form.cleaned_data['letter']
            ref = Reference()
            ref.letter = letter
            ref.person_to = jf
            ref.person_from = request.user
            ref.save()

    form = GoodForm()
    qs = Reference.objects.filter(person_to=jf).order_by('-edited')
    return render(request,'good.html',
        {'form':form,
        'qs':qs
        }
    )

def scan(request):
    xusers = User.objects.all().count()
    xaddr = Location.objects.all().count()
    xkids = Kid.objects.all().count()
    xplaces = Place.objects.all().count()
    xcrs = Course.objects.all().count()

    xclaim = Claim.objects.all().count()
    xprop = Prop.objects.all().count()
    xref = Reference.objects.all().count()

    xsubj = Subject.objects.all().count()

    return render(request,'scan.html',
        {
        'xusers':xusers,
        'xaddr':xaddr,
        'xkids':xkids,
        'xplaces':xplaces,
        'xcrs':xcrs,
        'xclaim':xclaim,
        'xprop':xprop,
        'xref':xref,
        'xsubj':xsubj
        }
    )
