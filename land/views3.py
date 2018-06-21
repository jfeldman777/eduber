from django.shortcuts import render
from .models import Location, Profile, Kid, Place, Claim, Prop, Course
from .forms2 import LookSForm
from .forms3 import PrefForm, AgeForm, TimeForm, SubjForm
from math import sqrt

def search(request):
    profile = Profile.objects.get(user=request.user)
    k_name = None
    a_name = None
    if profile.pref_kid:
        k_name = profile.pref_kid.first_name
    if profile.pref_addr:
        a_name = profile.pref_addr.name

    if request.method == "POST":
        var = request.POST['look_var']
        if var == 'claim_bs':
            return look4claimBS(request)
        if var == 'claim_rp':
            return look4claimRP(request)
        if var == 'claim_nw':
            return look4claimNW(request)
        if var == 'claim_gt':
            return look4claimGT(request)
        if var == 'claim_gd':
            return look4claimGD(request)
        if var == 'prop_bs':
            return look4propBS(request)
        if var == 'prop_bs':
            return look4propRP(request)
        if var == 'prop_nw':
            return look4propNW(request)
        if var == 'course':
            return look4course(request)
        if var == 'kid':
            return look4kid(request)
        if var == 'place':
            return look4place(request)
        return msg(request,'выберите что нибудь')
    else:
        form_age = AgeForm()
        form_time = TimeForm()
        form_subj = SubjForm()

    return render(request,'search.html',
        {   'form_age':form_age,
            'form_time':form_time,
            'form_subj':form_subj,
            'kid':k_name,'addr':a_name}
        )

def search_pref(request):
    msg = ''
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = PrefForm(request.POST,instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            msg = '(данные сохранены)'
        else:
            print(form.errors.as_data())
            return msg(request,'bad form')
    else:
        form = PrefForm(instance=profile, user=request.user)

    return render(request,'search_pref.html',
        {'form':form,'msg':msg}
        )

def xy2t(x1,y1,x2,y2):
    dx = x1 - x2
    dy = y1 - y2
    d2 = dx*dx + dy*dy
    d = sqrt(d2)
    me = 0.04075509311105271
    t = d*40/me
    return t

def choices(user):
    qs = Location.objects.filter(user=user)
    qq = [(x.id,x.name+"("+ x.address +")") for x in qs]
    return qq

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


def msg(request,msg):
    return render(request, 'msg.html', {'msg': msg})

def chat2me(request):
    return render(request,'chat2me.html')

def kid2chat(request,kid_id):
    return msg(request,'мне интересен ваш ребенок (заготовка)')

def place2chat(request,place_id):
    return msg(request,'мне интересна ваша площадка (заготовка')

def course2chat(request,course_id):
    return msg(request,'мне интересен ваш курс (заготовка')

def menu(request):
    return render(request,'menu.html')

def map112(request,lat,lng):
    return render(request,'map112.html',
        {
        'lat':lat,
        'lng':lng
        }
    )

def map11(request):
    return render(request,'map11.html')

def look4propBS(request):
    form_age = AgeForm(request.POST,user=request.user)
    form_time = TimeForm(request.POST)

    if not form_time.is_valid():
        print(form_time.errors.as_data())
        return msg(request,'bad time_form')

    if not form_age.is_valid():
        print(form_age.errors.as_data())
        return msg(request,'bad age_form')

    return render(request,'see.html')


def look4propRP(request):
    form_age = AgeForm(request.POST,user=request.user)
    form_time = TimeForm(request.POST)
    form_subj = SubjForm(request.POST)

    if not form_time.is_valid():
        print(form_time.errors.as_data())
        return msg(request,'bad time_form')

    if not form_subj.is_valid():
        print(form_subj.errors.as_data())
        return msg(request,'bad subj_form')

    if not form_age.is_valid():
        print(form_age.errors.as_data())
        return msg(request,'bad age_form')

    return obj(request)

def look4propNW(request):
    form_subj = SubjForm(request.POST)
    if not form_subj.is_valid():
        print(form_subj.errors.as_data())
        return msg(request,'bad subj_form')

    sbj = form_subj.cleaned_data['subjects']
    qs = Prop.objects.filter(subjects__in=sbj,hide=False,choices='C').distinct()

    return render(request,'see_prop_nw.html',{'qs':qs})

def look4claimNW(request):
    form_subj = SubjForm(request.POST)
    if not form_subj.is_valid():
        print(form_subj.errors.as_data())
        return msg(request,'bad subj_form')

    sbj = form_subj.cleaned_data['subjects']
    qs = Claim.objects.filter(subjects__in=sbj,hide=False,choices='C').distinct()

    return render(request,'see_claim_nw.html',{'qs':qs})

def look4claimBS(request):
    form_age = AgeForm(request.POST,user=request.user)
    form_time = TimeForm(request.POST)
    form_subj = SubjForm(request.POST)

    if not form_time.is_valid():
        print(form_time.errors.as_data())
        return msg(request,'bad time_form')

    if not form_subj.is_valid():
        print(form_subj.errors.as_data())
        return msg(request,'bad subj_form')

    if not form_age.is_valid():
        print(form_age.errors.as_data())
        return msg(request,'bad age_form')

    return obj(request)

def look4claimRP(request):
    form_age = AgeForm(request.POST,user=request.user)
    form_time = TimeForm(request.POST)
    form_subj = SubjForm(request.POST)

    if not form_time.is_valid():
        print(form_time.errors.as_data())
        return msg(request,'bad time_form')

    if not form_subj.is_valid():
        print(form_subj.errors.as_data())
        return msg(request,'bad subj_form')

    if not form_age.is_valid():
        print(form_age.errors.as_data())
        return msg(request,'bad age_form')

    return obj(request)

def look4claimGT(request):
    form_age = AgeForm(request.POST,user=request.user)
    form_time = TimeForm(request.POST)
    form_subj = SubjForm(request.POST)

    if not form_time.is_valid():
        print(form_time.errors.as_data())
        return msg(request,'bad time_form')

    if not form_subj.is_valid():
        print(form_subj.errors.as_data())
        return msg(request,'bad subj_form')

    if not form_age.is_valid():
        print(form_age.errors.as_data())
        return msg(request,'bad age_form')

    return obj(request)

def look4claimGD(request):
    form_age = AgeForm(request.POST)
    form_time = TimeForm(request.POST)
    form_subj = SubjForm(request.POST)

    if not form_time.is_valid():
        print(form_time.errors.as_data())
        return msg(request,'bad time_form')

    if not form_subj.is_valid():
        print(form_subj.errors.as_data())
        return msg(request,'bad subj_form')

    if not form_age.is_valid():
        print(form_age.errors.as_data())
        return msg(request,'bad age_form')

    return obj(request)

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
    profile = Profile.objects.get(user=request.user)
    if not profile.pref_addr:
        return msg(request,'укажите адрес')

    location = Location.objects.get(id = profile.pref_addr.id)
    if request.method == "POST":
        form = TimeForm(request.POST)
        if form.is_valid():
            t_min = form.cleaned_data['time_minutes']
            qs = Place.objects.all()
            rr = []
            for q in qs:
                try:
                    x = Location.objects.get(place=q.id)
                    if x:
                        t = xy2t(x.lat, x.lng, location.lat, location.lng)
                        if t <= t_min:
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
                    return msg(request,'look4place exception')
            return render(request,'see_place.html',
                {'qs':rr}
            )
    else:
        return msg(request,'ищем площадку?')

from datetime import timedelta, date

def look4kid(request):
    profile = Profile.objects.get(user=request.user)
    if not profile.pref_kid:
        return msg(request,'укажите своего ребенка')

    if not profile.pref_addr:
        return msg(request,'укажите адрес')

    kid = Kid.objects.get(id = profile.pref_kid.id)
    location = Location.objects.get(id = profile.pref_addr.id)

    if request.method == "POST":
        form_age = AgeForm(request.POST)
        form_time = TimeForm(request.POST)
        if form_age.is_valid() and form_time.is_valid():

            t_min = form_time.cleaned_data['time_minutes']
            age_dif = form_age.cleaned_data['age_dif']

            b_date = kid.birth_date

            dif = timedelta(days=age_dif*365)

            qs = Kid.objects.filter(
                birth_date__range=(b_date - dif, b_date + dif)
                )

            rr = []
            for q in qs:
                qx = Location.objects.filter(kid=q.id)

                for x in qx:
                    t = xy2t(x.lat, x.lng, location.lat, location.lng)
                    if True or t <= t_min:
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
            return msg(request,'look4kid bad forms')
    else:
        return msg(request,'ищем ребенка')
