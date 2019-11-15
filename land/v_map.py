from django.shortcuts import render
from django.utils.translation import gettext as _
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from .models import Profile, Reference, Location, Kid, Place, Course, Prop
from .forms import UserForm, ProfileForm, ReferenceForm, FaceForm, Face2Form
from .forms import KidForm, Face31Form, Face32Form, Face33Form
from .forms import LocationForm, PlaceForm, CourseForm
from .forms import C2SForm
from .forms2 import UnameForm
from .views3 import obj
from .views3 import msg

def map20(request,location_id):
    location = Location.objects.get(id=location_id)
    return render(request,'map112.html',
        {
            'lat':str(location.lat).replace( ',' , '.'),
            'lng':str(location.lng).replace(',' , '.')
        }
    )

def map2(request,location_id):
    location = Location.objects.get(id=location_id)
    if request.method == 'POST':
        form = LocationForm(request.POST,instance=location)
        if form.is_valid():
            form.save()
            return obj(request)
        else:
            return msg(request,'bad form map2')
    else:
        form = LocationForm(instance=location)
        return render(request,'map.html',
            {
                'form':form,
                'lat':str(location.lat).replace( ',' , '.'),
                'lng':str(location.lng).replace(',' , '.')
            }
        )

def map(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.user = request.user
            location.save()
        return obj(request)
    else:
        form = LocationForm()
        return render(request,'map.html',
            {
                'form':form,
                'lat':'59.93863',
                'lng':'30.31413',
            }
        )

def map112(request,lat,lng):
    return render(request,'map112.html',
        {
        'lat':str(lat).replace(',','.'),
        'lng':str(lng).replace(',','.')
        }
    )

def map11(request):
    return render(request,'map11.html')
