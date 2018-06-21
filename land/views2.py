from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.utils.text import slugify
from django.contrib.auth.models import User
from math import sqrt
from .models import Location, Place, Kid, Course, Reference, Claim, Prop
from .forms import PlaceForm, KidForm, CourseForm
from .forms2 import GoodForm
from .views3 import msg, obj, choices, xy2t


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


    return render(request,'scan.html',
        {
        'xusers':xusers,
        'xaddr':xaddr,
        'xkids':xkids,
        'xplaces':xplaces,
        'xcrs':xcrs,
        'xclaim':xclaim,
        'xprop':xprop
        }
    )

def look4course(request):
    rr = []
    addr_list = choices(request.user)
    if request.method == "POST":
        form = LookATSForm(request.POST,choices=addr_list)
        if form.is_valid():
            sbj = form.cleaned_data['subjects']
            a = form.cleaned_data['addr']
            ad = Location.objects.get(id=a)

            tx = form.cleaned_data['time_minutes']
            qs = Course.objects.filter(subject__in=sbj).distinct()

            for q in qs:
                qx = Location.objects.filter(course=q.id)
                for x in qx:
                    t = xy2t(x.lat, x.lng, ad.lat, ad.lng)
                    if t <= tx:
                        rr.append(
                            {'id':q.id,
                            'code':q.code,
                            'name':q.name,
                            'letter':q.letter,
                            'user':q.user,
                            'time':round(t),
                            'lat':x.lat,
                            'lng':x.lng
                            }
                        )

        return render(request,'see_course.html',
            {'qs':rr}
        )
    else:
        form = LookATSForm(choices=addr_list)

        return render(request,'look4course.html',
            {'form':form}
        )

def look4place(request):
    addr_list = choices(request.user)
    if request.method == "POST":
        form = LookATForm(request.POST,choices=addr_list)
        if form.is_valid():
            a = form.cleaned_data['addr']
            ad = Location.objects.get(id=a)

            tx = form.cleaned_data['time_minutes']
            qs = Place.objects.all()
            rr = []
            for q in qs:
                try:
                    x = Location.objects.get(place=q.id)
                    if x:
                        t = xy2t(x.lat, x.lng, ad.lat, ad.lng)
                        if t <= tx:
                            rr.append(
                                {'id':q.id,
                                'code':q.code,
                                'name':q.name,
                                'letter':q.letter,
                                'user':q.user,
                                'time':round(t),
                                'lat':x.lat,
                                'lng':x.lng,
                                'web':q.web
                                }
                            )
                except:
                    pass
            return render(request,'see_place.html',
                {'qs':rr}
            )
    else:
        form = LookATForm(choices=addr_list)

        return render(request,'look4kid.html',
            {'form':form}
        )

from datetime import timedelta, date

def look4kid(request):
    addr_list = choices(request.user)
    if request.method == "POST":
        form = LookATGForm(request.POST,choices=addr_list)
        if form.is_valid():
            a = form.cleaned_data['addr']
            ad = Location.objects.get(id=a)
            tx = form.cleaned_data['time_minutes']
            age = form.cleaned_data['age']
            age_dif = form.cleaned_data['age_dif']

            dif = timedelta(days=age_dif*365)
            back = timedelta(days=age*365)
            now = date.today()

            qs = Kid.objects.filter(
                birth_date__range=(now-back-dif, now-back+dif)
                )

            rr = []
            for q in qs:
                qx = Location.objects.filter(kid=q.id)

                for x in qx:
                    t = xy2t(x.lat, x.lng, ad.lat, ad.lng)
                    if True or t <= tx:
                        rr.append(
                            {'id':q.id,
                            'username':q.username,
                            'first_name':q.first_name,
                            'letter':q.letter,
                            'parent':q.parent,
                            'birth_date':q.birth_date,
                            'time':round(t),
                            'lat':x.lat,
                            'lng':x.lng
                            }
                        )

            return render(request,'see_kid.html',
                {'qs':rr}
            )
    else:
        form = LookATGForm(choices=addr_list)

        return render(request,'look4kid.html',
            {'form':form}
        )



def course_show(request,course_id):
    course = Course.objects.get(id=course_id)
    form = CourseForm(
        course_id=course_id,
        user=request.user,
        initial={
            'code':course.code,
            'name':course.name,
            'locations':course.locations,
            'letter':course.letter,
            'web':course.web,
            'level':course.level,
            'age':course.age
            }
        )
    return render(request,'course3.html',
        {'form':form
        }
    )

def place_show(request,place_id):
    place = Place.objects.get(id=place_id)

    form = PlaceForm(
    initial={
    'code':place.code,
    'name':place.name,
    'location':place.location,
    'letter':place.letter,
    'web':place.web
    },user=request.user
    )

    return render(request,'place3.html',
        {'form':form
        }
    )

def kid_show(request,kid_id):
    kid = Kid.objects.get(id=kid_id)
    form = KidForm(
    initial={
    'username':kid.username,
    'first_name':kid.first_name,
    'birth_date':kid.birth_date,
    'locations':kid.locations,
    'letter':kid.letter
    },user=request.user,kid_id=kid_id
    )

    url = None
    if kid.face:
        url = kid.face.url

    return render(request,'kid3.html',
        {'form':form,
        'face':url
        }
    )
