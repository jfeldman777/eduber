from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .views3 import msg
from .models import Location, Kid, Place, Subject, Profile
from .forms3 import AdmForm

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

    return render(request,'adm.html',{'form':form})


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
