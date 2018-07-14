from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from .models import Profile, Reference, Location, Kid, Place, Course, Claim, Prop
from .forms import UserForm, ProfileForm, ReferenceForm, FaceForm, Face2Form
from .forms import KidForm, Face31Form, Face32Form, Face33Form
from .forms import LocationForm, PlaceForm, CourseForm
from .forms import C2SForm
from .forms2 import UnameForm, ClaimForm, PropForm
from .views3 import msg, obj
from .views import index, viewref

def reference(request,uname):
    if request.method == "POST":
        form = ReferenceForm(request.POST)
        if form.is_valid():
            ref = form.save(commit=False)
            ref.person_from = request.user
            ref.person_to = User.objects.get(username=uname)
            ref.save()
        return viewref(request,uname)
    else:
        form = ReferenceForm()
        return render(request,
            'form.html',
            {   'form':form, 'title':'написать рекомендацию'    }
        )

def profile(request):
    user = request.user
    profile = user.profile##Profile.objects.get(user=user)
    if request.method == "POST":
        uform = UserForm(data = request.POST)
        pform = ProfileForm(data = request.POST)
        if uform.is_valid() and pform.is_valid():
            profile.birth_date = pform.cleaned_data['birth_date']
            profile.phone = pform.cleaned_data['phone']
            profile.web = pform.cleaned_data['web']

            user.first_name = uform.cleaned_data['first_name']
            user.last_name = uform.cleaned_data['last_name']
            user.email = uform.cleaned_data['email']

            user.save()
            profile.save()

        return index(request)
    else:
        uform = UserForm(initial={
        'first_name':user.first_name,
        'last_name':user.last_name,
        'email':user.email})
        pform = ProfileForm(
            initial={
            'birth_date':profile.birth_date,
            'phone':profile.phone,
            'web':profile.web
            })
        return render(request,'profile.html',
            {'uform': uform,
             'pform': pform,
            })

def obj22(request,uname):#какого пользователя мы хотим проверить?
        user = User.objects.get(username=uname)
        return obj2(request,user)

def obj12(request):#какого пользователя мы хотим проверить?
    if request.method == 'POST':
        form = UnameForm(data = request.POST)
        if form.is_valid():
            u = form.cleaned_data['uname']
            user = User.objects.get(username=u)
            return obj2(request,user)
        return msg(request,'bad form')
    else:
        form = UnameForm()
        return render(request,
        'form.html',
        {'form':form, 'title':'username to check objects'}
        )

def obj2(request,user):#показать все объекты ДРУГОГО пользователя
    profile = user.profile##Profile.objects.get(user=user)
    q_adr = Location.objects.filter(user=user)
    q_kid = Kid.objects.filter(parent=user)
    q_place = Place.objects.filter(user=user)
    q_crs = Course.objects.filter(user=user)
    q_claim = Claim.objects.filter(user=user)
    q_prop = Prop.objects.filter(user=user)

    return render(request,'obj2.html',
    {
    'profile':profile,
    'q_adr':q_adr,
    'q_kid':q_kid,
    'q_place':q_place,
    'q_crs':q_crs,
    'q_claim':q_claim,
    'q_prop':q_prop
    })
