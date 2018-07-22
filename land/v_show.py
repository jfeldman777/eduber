from django.shortcuts import render, redirect
from .models import Profile
from .forms3 import AdmForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.utils.text import slugify
from django.contrib.auth.models import User
from math import sqrt
from .models import Location, Place, Kid, Course, Reference, Claim, Prop, Subject, Event, Invite
from .forms import PlaceForm, KidForm, CourseForm, MyletterForm
from .forms2 import GoodForm, ClaimForm, PropForm, EventForm
from .views3 import msg, obj, xy2t


def f2s(f):
    return str(f).replace(',' , '.')

def qs2lopos(qs):
    res = []
    for q in qs:
        s1 = f2s(q.lat)
        s2 = f2s(q.lng)
        p = (s1,s2)
        res.append(p)
    return res

def lopos2js(qs):
    lopos = qs2lopos(qs)
    res = ''
    for x,y in lopos:
        res += '['+ x + ',' + y + '],'
    res = res[:-1]
    return res

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
    js = lopos2js(qs)
    return render(request,'map9.html',
        {'lopos':js}
    )

def show_kids(request):
    qs = Location.objects.exclude(kid = None).distinct()
    js = lopos2js(qs)
    return render(request,'map9.html',
        {'lopos':js}
    )

def show_places(request):
    qs = Location.objects.exclude(place = None).distinct()
    js = lopos2js(qs)
    return render(request,'map9.html',
        {'lopos':js}
    )

def show_claims(request):
    qs = Location.objects.exclude(claim = None).distinct()
    js = lopos2js(qs)
    return render(request,'map9.html',
        {'lopos':js}
    )

def show_prop(request):
    qs = Location.objects.exclude(prop = None).distinct()
    js = lopos2js(qs)
    return render(request,'map9.html',
        {'lopos':js}
    )

def show_courses(request):
    qs = Location.objects.exclude(course = None).distinct()
    js = lopos2js(qs)
    return render(request,'map9.html',
        {'lopos':js}
    )

def show_events(request):
    qs = Location.objects.exclude(event = None).distinct()
    js = lopos2js(qs)
    return render(request,'map9.html',
        {'lopos':js}
    )

def event_show(request,event_id):
    event = Event.objects.get(id=event_id)
    form = EventForm(
            user=event.user,instance=event
        )

    qs = Invite.objects.filter(event=event).exclude(user=request.user).exclude(status='0').order_by('-status')

    return render(request,'event_show.html',
        {'form':form,
        'qs':qs
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
