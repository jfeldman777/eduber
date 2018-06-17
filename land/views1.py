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
from . import views,views2

def prop_ed(request,prop_id):
    prop = Prop.objects.get(id=prop_id)
    if request.method == "POST":
        form = PropForm(request.POST, user=request.user, initial=None, prop_id=None)
        if form.is_valid():
            prop.choices = form.cleaned_data['choices']
            prop.letter = form.cleaned_data['letter']
            prop.subjects.set(form.cleaned_data['subjects'])
            prop.locations.set(form.cleaned_data['locations'])
            prop.save()
            return obj(request)
        else:
            print(form.errors.as_data())
            return msg(request,'bad form')
    else:
        initial = {
        'choices':prop.choices,
        'letter':prop.letter
        }
        form = PropForm(user=request.user,initial=initial, prop_id=prop_id)

        return render(request,
            'prop_cre.html',
            {
            'form':form
            })

def claim_ed(request,claim_id):
    claim = Claim.objects.get(id=claim_id)
    if request.method == "POST":
        form = ClaimForm(request.POST, user=request.user,initial=None,claim_id=None)
        if form.is_valid():
            claim.choices = form.cleaned_data['choices']
            claim.letter = form.cleaned_data['letter']
            claim.subjects.set(form.cleaned_data['subjects'])
            claim.locations.set(form.cleaned_data['locations'])
            claim.kids.set(form.cleaned_data['kids'])
            claim.save()
            return obj(request)
        else:
            print(form.errors.as_data())
            return msg(request,'bad form')
    else:
        initial = {
            'choices':claim.choices,
            'letter':claim.letter
        }
        form = ClaimForm(user=request.user,initial=initial,claim_id=claim_id)
        return render(request,
            'claim_cre.html',
            {
            'form':form
            })
def prop_del(request,prop_id):
    prop = Prop.objects.get(id=prop_id)
    prop.delete()
    return obj(request)

def claim_del(request,claim_id):
    claim = Claim.objects.get(id=claim_id)
    claim.delete()
    return obj(request)

def prop_cre(request):
    if request.method == "POST":
        form = PropForm(request.POST, user=request.user)
        if form.is_valid():
            prop = Prop()
            prop.user = request.user
            prop.choices = form.cleaned_data['choices']
            prop.letter = form.cleaned_data['letter']
            prop.save()
            prop.subjects.set(form.cleaned_data['subjects'])
            prop.locations.set(form.cleaned_data['locations'])
            prop.save()
            return obj(request)
        else:
            print(form.errors.as_data())
            return msg(request,'bad form')
    else:
        form = PropForm(user=request.user)
        return render(request,
            'prop_cre.html',
            {
            'form':form
            })

def claim_cre(request):
    if request.method == "POST":
        form = ClaimForm(request.POST, user=request.user, initial=None,claim_id=None)
        if form.is_valid():
            claim = Claim()
            claim.user = request.user
            claim.choices = form.cleaned_data['choices']
            claim.letter = form.cleaned_data['letter']
            claim.save()
            claim.subjects.set(form.cleaned_data['subjects'])
            claim.locations.set(form.cleaned_data['locations'])
            claim.kids.set(form.cleaned_data['kids'])
            claim.save()
            return obj(request)
        else:
            print(form.errors.as_data())
            return msg(request,'bad form')
    else:
        form = ClaimForm(user=request.user, initial=None,claim_id=None)
        return render(request,
            'claim_cre.html',
            {
            'form':form
            })

def reference(request):
    if request.method == "POST":
        form = ReferenceForm(request.POST)
        if form.is_valid():
            ref = Reference()
            ref.person_from = request.user
            ref.letter = form.cleaned_data['letter']
            email = form.cleaned_data['email']
            try:
                person_to = form.cleaned_data['uname_to']
                user_to = User.objects.filter(username = person_to, email = email)[0]
                ref.person_to = user_to
                ref.save()
            except:
                return msg(request,'неправильные реквизиты, сохранить отзыв не удалось')

        return index(request)
    else:
        form = ReferenceForm()
        return render(request,'reference.html',{'form':form})

def profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
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

def obj(request):#показать все объекты
    profile = Profile.objects.get(user=request.user)
    q_adr = Location.objects.filter(user=request.user)
    q_kid = Kid.objects.filter(parent=request.user)
    q_place = Place.objects.filter(user=request.user)
    q_crs = Course.objects.filter(user=request.user)
    q_claim = Claim.objects.filter(user=request.user)
    q_prop = Prop.objects.filter(user=request.user)
    return render(request,'obj.html',
    {
    'profile':profile,
    'q_adr':q_adr,
    'q_kid':q_kid,
    'q_place':q_place,
    'q_crs':q_crs,
    'q_claim':q_claim,
    'q_prop':q_prop
    })

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
        return render(request,'uform.html',{'form':form})

def obj2(request,user):#показать все объекты ДРУГОГО пользователя
    profile = Profile.objects.get(user=user)
    q_adr = Location.objects.filter(user=user)
    q_kid = Kid.objects.filter(parent=user)
    q_place = Place.objects.filter(user=user)
    q_crs = Course.objects.filter(user=user)
    return render(request,'obj.html',
    {
    'profile':profile,
    'q_adr':q_adr,
    'q_kid':q_kid,
    'q_place':q_place,
    'q_crs':q_crs
    })
