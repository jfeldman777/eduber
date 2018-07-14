from django.shortcuts import render
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

##########################################################
def face31(request,place_id):
    place = Place.objects.get(id=place_id)
    if request.method == 'POST':
        form = Face31Form(request.POST, request.FILES)
        if form.is_valid():
            place.face1 = form.cleaned_data['face1']
            place.save()
        return obj(request)
    else:
        form = Face31Form(
            initial={'face1':place.face1}
                )
        url = None
        if place.face1:
            url = place.face1.url
        return render(request, 'face.html',
            {'form': form,
            'face':url,
            })

def face32(request,place_id):
    place = Place.objects.get(id=place_id)
    if request.method == 'POST':
        form = Face32Form(request.POST, request.FILES)
        if form.is_valid():
            place.face2 = form.cleaned_data['face2']
            place.save()
        return obj(request)

    else:
        form = Face32Form(
            initial={'face2':place.face2}
                )
        url = None
        if place.face2:
            url = place.face2.url
        return render(request, 'face.html',
            {'form': form,
            'face':url,
            })

def face33(request,place_id):
    place = Place.objects.get(id=place_id)
    if request.method == 'POST':
        form = Face32Form(request.POST, request.FILES)
        if form.is_valid():
            place.face3 = form.cleaned_data['face3']
            place.save()
        return obj(request)

    else:
        form = Face33Form(
            initial={'face3':place.face3}
                )
        url = None
        if place.face3:
            url = place.face3.url
        return render(request, 'face.html',
            {'form': form,
            'face':url,
            })

def face2(request):
    profile = request.user.profile##Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = Face2Form(request.POST, request.FILES)
        if form.is_valid():
            profile.face = form.cleaned_data['face']
            profile.save()
        return index(request)

    else:
        form = Face2Form(
            initial={'face':profile.face}
                )
        url = None
        if profile.face:
            url = profile.face.url
        return render(request, 'face.html',
            {'form': form,
            'face':url,
            })

def face(request,kid_id):
    kid = Kid.objects.get(id=kid_id)
    if request.method == 'POST':
        form = FaceForm(request.POST, request.FILES)
        if form.is_valid():
            kid.face = form.cleaned_data['face']
            kid.save()
        return obj(request)

    else:
        form = FaceForm(
            initial={'face':kid.face}
                )
        url = None
        if kid.face:
            url = kid.face.url
        return render(request, 'face.html',
            {'form': form,
            'face':url,
            })
