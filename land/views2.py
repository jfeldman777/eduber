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
    return render(request,'myletter.html',
        {'form':form
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

def course_show(request,course_id):
    course = Course.objects.get(id=course_id)
    form = CourseForm(
            user=course.user,instance=course
        )
    return render(request,'course3.html',
        {'form':form
        }
    )

def place_show(request,place_id):
    place = Place.objects.get(id=place_id)
    form = PlaceForm(instance=place,user=place.user
    )

    url1 = None
    if place.face1:
        url1 = place.face1.url

    url2 = None
    if place.face2:
        url2 = place.face2.url

    url3 = None
    if place.face3:
        url3 = place.face3.url

    return render(request,'place3.html',
        {'form':form,
            'face1':url1,    'face2':url2,     'face3':url3
        }
    )

def kid_show(request,kid_id):
    kid = Kid.objects.get(id=kid_id)
    form = KidForm(instance=kid,user=kid.parent)

    url = None
    if kid.face:
        url = kid.face.url

    return render(request,'kid3.html',
        {'form':form,
        'face':url
        }
    )

def prop_show(request,prop_id):
    prop = Prop.objects.get(id=prop_id)
    form = PropForm(instance=prop,user=prop.user)

    return render(request,'form_show.html',
        {'form':form,
        }
    )

def claim_show(request,claim_id):
    claim = Claim.objects.get(id=claim_id)
    form = ClaimForm(instance=claim,user=claim.user)

    return render(request,'form_show.html',
        {'form':form,
        }
    )
