from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.utils.text import slugify
from django.contrib.auth.models import User
from math import sqrt
from . import views, views1
from .models import Location, Place, Kid, Course
from .forms import PlaceForm, KidForm, CourseForm
from .forms2 import Look3Form, LookForm

def chat2me(request):
    return render(request,'chat2me.html')

def kid9(request,user,code):
    return msg(request,'мне интересен ваш ребенок (заготовка)')

def place9(request,user,code):
    return msg(request,'мне интересна ваша площадка (заготовка')

def course9(request,user,code):
    return msg(request,'мне интересен ваш курс (заготовка')

def menu(request):
    return render(request,'menu.html')

def xy2t(x1,y1,x2,y2):
  dx = x1 - x2
  dy = y1 - y2
  d2 = dx*dx + dy*dy
  d = sqrt(d2)
  me = 0.04075509311105271
  t = d*40/me
  return t

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

def search(request):
    return render(request,'search.html')

def map112(request,lat,lng):
    return render(request,'map112.html',
        {
        'lat':lat,
        'lng':lng
        }
    )

def map11(request):
    return render(request,'map11.html')

def scan(request):
    xusers = User.objects.all().count()
    xaddr = Location.objects.all().count()
    xkids = Kid.objects.all().count()
    xplaces = Place.objects.all().count()
    xcrs = Course.objects.all().count()
    return render(request,'scan.html',
        {
        'xusers':xusers,
        'xaddr':xaddr,
        'xkids':xkids,
        'xplaces':xplaces,
        'xcrs':xcrs
        }
    )

def choices(user):
    qs = Location.objects.filter(user=user)
    qq = [(x.id,x.name+"("+ x.address +")") for x in qs]
    return qq

def look(request):
    rr = []
    addr_list = choices(request.user)
    if request.method == "POST":
        form = LookForm(request.POST,choices=addr_list)
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

        return render(request,'see.html',
            {'qs':rr}
        )
    else:
        form = LookForm(choices=addr_list)

        return render(request,'look.html',
            {'form':form}
        )

def look2(request):
    addr_list = choices(request.user)
    if request.method == "POST":
        form = Look2Form(request.POST,choices=addr_list)
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
            return render(request,'see2.html',
                {'qs':rr}
            )
    else:
        form = Look2Form(choices=addr_list)

        return render(request,'look2.html',
            {'form':form}
        )

from datetime import timedelta, date

def look3(request):
    addr_list = choices(request.user)
    if request.method == "POST":
        form = Look3Form(request.POST,choices=addr_list)
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

            return render(request,'see3.html',
                {'qs':rr}
            )
    else:
        form = Look3Form(choices=addr_list)

        return render(request,'look3.html',
            {'form':form}
        )

def course3(request,course_id):
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

def place3(request,place_id):
    addr_list = choices(request.user)
    place = Place.objects.get(id=place_id)

    form = PlaceForm(
    initial={
    'code':place.code,
    'name':place.name,
    'location':place.location,
    'letter':place.letter,
    'web':place.web
    },choices=addr_list
    )

    return render(request,'place3.html',
        {'form':form
        }
    )

def kid3(request,kid_id):
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
