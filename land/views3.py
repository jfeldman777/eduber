from django.shortcuts import render
from .models import Location, Profile, Kid, Place, QPage
from .models import Claim, Prop, Course, Chat, Reply, Event, Invite
from .forms2 import LookSForm, UnameForm, FLnameForm
from .forms3 import PrefForm, AgeForm, Age1Form, TimeForm, SubjForm, ReplyForm
from .forms import Date2Form
from math import sqrt
from operator import and_, or_
from functools import reduce
from django.db.models import Q
from django.contrib.auth.models import User
import datetime

def reply(request,chat_id):
    form = None
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            chat = Chat.objects.get(id = reply.chat_id)
            reply.from_starter = (chat.person_from == request.user)
            reply.save()
            return chat2me(request)
        else:
            return msg(request,'bad reply form')
    else:
        form = ReplyForm(initial={'chat':chat_id})
    return render(request,
            'form.html',
            {   'form':form, 'title':'чат: реплика'    }
            )

def chat2user(request,uname):
    user = User.objectd.get(username = uname)
    return chat(request,'user', user.id, user.id)

def chat(request,type,obj_id,holder_id):
    form = None
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            chat = Chat.objects.get(id = reply.chat_id)
            reply.from_starter = (chat.person_from == request.user)
            reply.save()
            return chat2me(request)
        else:
            return msg(request,'bad reply form')
    else:
        chat = Chat(
            person_to = User.objects.get(id = holder_id),
            person_from = request.user,
            subject = type,
            obj_id = obj_id
        )
        chat.save()
        chat_id = chat.id
        form = ReplyForm(initial={'chat':chat_id})
    return render(request,
            'form.html',
            {   'form':form, 'title':'чат: реплика'    }
    )

def chat2me(request):
    qs_from = []
    qs_from_me = Chat.objects.filter(person_from = request.user).order_by('-started')
    for q in qs_from_me:
        try:
            d = Reply.objects.filter(chat_id=q.id).order_by('-written')[0]
            qs_from.append((q,d.written))
        except:
            pass

    qs_to = []
    qs_to_me = Chat.objects.filter(person_to = request.user).order_by('-started')
    for q in qs_to_me:
        try:
            d = Reply.objects.filter(chat_id=q.id).order_by('-written')[0]
            qs_to.append((q,d.written))
        except:
            pass
    return render(request,'chat2me.html',
        {
            'qs_from_me':qs_from,
            'qs_to_me':qs_to
        }
    )

def chat2see(request,chat_id):
    qs = Reply.objects.filter(chat_id = chat_id).order_by('-written')
    return render(request,'chat2see.html',
        {
            'qs':qs,
            'chat_id':chat_id
        }
    )

def search(request):
    profile = request.user.profile
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
        if var == 'prop_rp':
            return look4propRP(request)
        if var == 'prop_nw':
            return look4propNW(request)
        if var == 'course':
            return look4course(request)
        if var == 'kid':
            return look4kid(request)
        if var == 'place':
            return look4place(request)
        if var == 'friends':
            return look4friends(request)
        if var == 'uname':
            return look4uname(request)
        if var == 'flname':
            return look4flname(request)
        if var == 'event':
            return look4event(request)
        return msg(request,'выберите что нибудь')
    else:
        form_age = AgeForm()
        form_time = TimeForm()
        form_subj = SubjForm()
        form_age1 = Age1Form()
        form_uname = UnameForm()
        form_flname = FLnameForm()
        d2form = Date2Form()

    return render(request,'search.html',
        {   'd2form':d2form,
            'form_age':form_age,
            'form_age1':form_age1,
            'form_time':form_time,
            'form_subj':form_subj,
            'form_uname':form_uname,
            'form_flname':form_flname,
            'kid':k_name,
            'addr':a_name}
        )

def look4event(request):
    profile = request.user.profile
    if not profile.pref_addr:
        return msg(request,'укажите адрес')
    location = profile.pref_addr

    if request.method == "POST":
        d2form = Date2Form(request.POST)
        form_time = TimeForm(request.POST)
        if d2form.is_valid() and form_time.is_valid():
            t_min = form_time.cleaned_data['time_minutes']
            d1 = d2form.cleaned_data['date1']
            d2 = d2form.cleaned_data['date2']
            qs = Event.objects.filter(hide = False,
                date_to__date__gte = d1,
                date_from__date__lte = d2).order_by('date_from')
            rr = []
            for q in qs:
                x = q.location
                t = xy2t(x.lat, x.lng, location.lat, location.lng)
                if t <= t_min:
                    rr.append(
                        {'id':q.id,
                        'user':q.user,
                        'code':q.code,
                        'name':q.name,
                        'letter':q.letter,
                        'time':round(t),
                        'lat':x.lat,
                        'lng':x.lng,
                        'date_from':q.date_from,
                        'date_to':q.date_to,
                        }
                    )

            return render(request,'see_event.html',
                {'qs':rr}
            )

        else:
            return msg(request,'bad event')
    return msg(request,'event')

def look4uname(request):
    qs = []
    if request.method == "POST":
        form = UnameForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['uname']
            qs = User.objects.get(username = uname)
    return render(request,'see_uname.html',
        {'qs':[qs]}
    )

def look4flname(request):
    qs = []
    if request.method == "POST":
        form = FLnameForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            qs = User.objects.filter(first_name__icontains = fname,
                last_name__icontains = lname
                ).order_by('last_name','first_name')

    return render(request,'see_uname.html',
        {'qs':qs}
    )

def look4friends(request):
    profile = request.user.profile
    if not profile.pref_addr:
        return msg(request,'укажите адрес')
    kid = profile.pref_kid
    if kid is None:
        kid = Kid.objects.filter(parent = request.user,
                            birth_date = request.user.profile.birth_date)[0]

    location = Location.objects.get(id = profile.pref_addr.id)
    li = kid.interest.split()

    if request.method == "POST":
        form_age = AgeForm(request.POST)
        form_time = TimeForm(request.POST)
        if form_age.is_valid() and form_time.is_valid():

            t_min = form_time.cleaned_data['time_minutes']
            age_dif = form_age.cleaned_data['age_dif']

            b_date = kid.birth_date
            dif = timedelta(days=age_dif*365)

            qs = Kid.objects.filter(
                reduce(or_, [Q(interest__icontains=q) for q in li]),
                birth_date__range=(b_date - dif, b_date + dif)
                ).exclude(pk=kid.id)

            rr = []
            for q in qs:
                qx = Location.objects.filter(kid=q.id)

                for x in qx:
                    t = xy2t(x.lat, x.lng, location.lat, location.lng)
                    if t <= t_min:
                        rr.append(
                            {'id':q.id,
                            'username':q.username,
                            'first_name':q.first_name,
                            'letter':q.letter,
                            'parent':q.parent,
                            'birth_date':q.birth_date,
                            'interest':q.interest,
                            'time':round(t),
                            'lat':x.lat,
                            'lng':x.lng,
                            'myinterest':kid.interest
                            }
                        )

            return render(request,'see_friend.html',
                {'qs':rr}
            )
        else:
            return msg(request,'look4friends bad forms')
    else:
        return msg(request,'friends')

def search_pref(request):
    msg = ''
    profile = request.user.profile##Profile.objects.get(user=request.user)
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

def obj(request):#показать все объекты
    profile = Profile.objects.get(user=request.user)
    q_adr = Location.objects.filter(user=request.user)
    q_kid = Kid.objects.filter(parent=request.user)
    q_place = Place.objects.filter(user=request.user)
    q_crs = Course.objects.filter(user=request.user)
    q_claim = Claim.objects.filter(user=request.user)
    q_prop = Prop.objects.filter(user=request.user)

    q_qpage = QPage.objects.filter(user=request.user).order_by('code')

    q_events = Event.objects.filter(user=request.user).order_by('code')
    q_invites = Invite.objects.filter(user=request.user).order_by('-status')
    return render(request,'obj.html',
    {
    'profile':profile,
    'q_adr':q_adr,
    'q_kid':q_kid,
    'q_place':q_place,
    'q_crs':q_crs,
    'q_claim':q_claim,
    'q_prop':q_prop,
    'q_events':q_events,
    'q_invites':q_invites,
    'q_qpage':q_qpage

    })

def msg(request,msg):
    return render(request, 'msg.html', {'msg': msg})

def look4propBS(request):
    profile = request.user.profile##Profile.objects.get(user=request.user)
    if not profile.pref_addr:
        return msg(request,'укажите адрес')

    location = Location.objects.get(id = profile.pref_addr.id)

    if request.method == "POST":
        form_time = TimeForm(request.POST)
        if form_time.is_valid():

            t_min = form_time.cleaned_data['time_minutes']

            qs = Prop.objects.filter(choices='B',
                        hide=False
                )

            rr = []
            for q in qs:
                qx = Location.objects.filter(prop=q.id)

                for x in qx:
                    t = xy2t(x.lat, x.lng, location.lat, location.lng)
                    if t <= t_min:
                        u = User.objects.get(id=q.user_id)
                        rr.append(
                            {'id':q.id,
                            'username':u,
                            'first_name':u.first_name,
                            'letter':q.letter,
                            'time':round(t),
                            'lat':x.lat,
                            'lng':x.lng
                            }
                        )

            return render(request,'see_prop.html',
                {'qs':rr}
            )
        else:
            return msg(request,'look4BS bad forms')
    else:
        return msg(request,'ищем беби-ситтера')

def look4propRP(request):
    profile = request.user.profile##Profile.objects.get(user=request.user)
    if not profile.pref_addr:
        return msg(request,'укажите адрес')

    kid = Kid.objects.get(id = profile.pref_kid.id)
    location = Location.objects.get(id = profile.pref_addr.id)
    if request.method == "POST":
        form_time = TimeForm(request.POST)
        form_subj = SubjForm(request.POST)

        if form_time.is_valid() and form_subj.is_valid():
            sbj = form_subj.cleaned_data['subjects']
            t_min = form_time.cleaned_data['time_minutes']

            qs = Prop.objects.filter(subjects__in=sbj,
                hide=False,
                choices='R').distinct()

            rr = []
            for q in qs:
                x = Location.objects.get(claim=q.id)
                t = xy2t(x.lat, x.lng, location.lat, location.lng)
                if t <= t_min:
                    u = User.objects.get(id=q.user_id)
                    rr.append(
                        {'id':q.id,
                        'username':u,
                        'first_name':u.first_name,
                        'letter':q.letter,
                        'time':round(t),
                        'lat':x.lat,
                        'lng':x.lng
                        }
                    )

            return render(request,'see_prop.html',
                {'qs':rr})

        else:
            return msg(request,'не указаны предметы')
    else:
        return msg(request,'ищем репетитора')

def look4propNW(request):
    form_subj = SubjForm(request.POST)
    if not form_subj.is_valid():
        print(form_subj.errors.as_data())
        return msg(request,'укажите хотя бы один предмет')

    sbj = form_subj.cleaned_data['subjects']
    qs = Prop.objects.filter(subjects__in=sbj,hide=False,choices='C').distinct()

    return render(request,'see_prop_nw.html',{'qs':qs})

def look4claimNW(request):
    form_subj = SubjForm(request.POST)
    if not form_subj.is_valid():
        print(form_subj.errors.as_data())
        return msg(request,'укажите хотя бы один предмет')

    sbj = form_subj.cleaned_data['subjects']
    qs = Claim.objects.filter(subjects__in=sbj,hide=False,choices='C').distinct()

    return render(request,'see_claim_nw.html',{'qs':qs})

def look4claimBS(request):
    profile = request.user.profile##Profile.objects.get(user=request.user)
    if not profile.pref_addr:
        return msg(request,'укажите адрес')

    location = Location.objects.get(id = profile.pref_addr.id)
    if request.method == "POST":
        form = TimeForm(request.POST)
        if form.is_valid():
            t_min = form.cleaned_data['time_minutes']
            qs = Claim.objects.filter(choices='B',hide=False)
            rr = []
            for q in qs:
                #try:
                    x = Location.objects.get(claim=q.id)
                    if x:
                        t = xy2t(x.lat, x.lng, location.lat, location.lng)
                        if t <= t_min:
                            kid = Kid.objects.get(id=q.kid_id)
                            rr.append(
                                {'id':q.id,
                                'kid_id':kid.id,
                                'name':kid.first_name,
                                'letter':q.letter,
                                'user':q.user,
                                'time':round(t),
                                'lat':x.lat,
                                'lng':x.lng,
                                }
                            )
                #except:
                #    return msg(request,'look4claimBS exception')
            return render(request,'see_claim.html',
                {'qs':rr}
            )
    else:
        return msg(request,'ищем заявку на беби-ситтера?')

def look4claimRP(request):
    rr = []
    profile = request.user.profile##Profile.objects.get(user=request.user)
    if not profile.pref_addr:
        return msg(request,'укажите адрес')

    if not profile.pref_kid:
        return msg(request,'укажите своего ребенка')

    location = Location.objects.get(pk=profile.pref_addr.id)

    form_age = AgeForm(request.POST)
    form_age1 = Age1Form(request.POST)
    form_time = TimeForm(request.POST)
    form_subj = SubjForm(request.POST)

    if form_age.is_valid() and form_age1.is_valid() and form_time.is_valid() and form_subj.is_valid():
        sbj = form_subj.cleaned_data['subjects']
        t_min = form_time.cleaned_data['time_minutes']
        age_dif = form_age.cleaned_data['age_dif']
        age = form_age1.cleaned_data['age']

        dif = timedelta(days=age_dif*365)
        now = date.today()
        back = timedelta(days=age*365)

        qs = Claim.objects.filter(subjects__in=sbj,choices='R',hide=False)

        rr = []
        for q in qs:
            kid = Kid.objects.get(id = q.kid_id)
            if  (now - back - dif) <= kid.birth_date <= (now - back + dif):
                x = Location.objects.get(claim=q.id)
                t = xy2t(x.lat, x.lng, location.lat, location.lng)
                if t <= t_min:
                    rr.append(
                        {'id':q.id,
                        'user':q.user,
                        'name':kid.first_name,
                        'letter':q.letter,
                        'kid_id':kid.id,
                        'time':round(t),
                        'lat':x.lat,
                        'lng':x.lng
                        }
                    )


        return render(request,'see_claim.html',
            {'qs':rr}
        )
    else:
        return msg(request,'не указаны предметы')
#################################################

def look4claimGT(request):
    rr = []
    profile = request.user.profile##Profile.objects.get(user=request.user)
    if not profile.pref_kid:
        return msg(request,'укажите своего ребенка')

    if not profile.pref_addr:
        return msg(request,'укажите адрес')

    location = Location.objects.get(pk=profile.pref_addr.id)

    form_age = AgeForm(request.POST)
    form_age1 = Age1Form(request.POST)
    form_time = TimeForm(request.POST)
    form_subj = SubjForm(request.POST)

    if form_age.is_valid() and form_age1.is_valid() and form_time.is_valid() and form_subj.is_valid():
        sbj = form_subj.cleaned_data['subjects']
        t_min = form_time.cleaned_data['time_minutes']
        age_dif = form_age.cleaned_data['age_dif']
        age = form_age1.cleaned_data['age']

        dif = timedelta(days=age_dif*365)
        now = date.today()
        back = timedelta(days=age*365)

        qs = Claim.objects.filter(subjects__in=sbj,choices='T',hide=False)

        rr = []
        for q in qs:
            kid = Kid.objects.get(id = q.kid_id)
            if  (now - back - dif) <= kid.birth_date <= (now - back + dif):
                x = Location.objects.get(claim=q.id)
                t = xy2t(x.lat, x.lng, location.lat, location.lng)
                if t <= t_min:
                    rr.append(
                        {'id':q.id,
                        'user':q.user,
                        'name':kid.first_name,
                        'letter':q.letter,
                        'kid_id':kid.id,
                        'time':round(t),
                        'lat':x.lat,
                        'lng':x.lng
                        }
                    )

        return render(request,'see_course.html',
            {'qs':rr}
        )
    else:
        return msg(request,'look4claimGT bad forms')
###########################################################

def look4claimGD(request):
    profile = request.user.profile
    if not profile.pref_addr:
        return msg(request,'укажите адрес')

    location = Location.objects.get(id = profile.pref_addr.id)

    if request.method == "POST":
        form_age = AgeForm(request.POST)
        form_age1 = Age1Form(request.POST)
        form_time = TimeForm(request.POST)
        if form_age.is_valid() and form_time.is_valid() and form_age1.is_valid():

            t_min = form_time.cleaned_data['time_minutes']
            age_dif = form_age.cleaned_data['age_dif']
            age = form_age1.cleaned_data['age']

            dif = timedelta(days=age_dif*365)
            now = date.today()
            back = timedelta(days=age*365)

            qs = Claim.objects.filter(choices='D',hide=False)

            rr = []
            for q in qs:
                kid = Kid.objects.get(id = q.kid_id)
                if  (now - back - dif) <= kid.birth_date <= (now - back + dif):
                    x = Location.objects.get(claim=q.id)
                    t = xy2t(x.lat, x.lng, location.lat, location.lng)
                    if t <= t_min:
                        rr.append(
                            {'id':q.id,
                            'user':q.user,
                            'name':kid.first_name,
                            'letter':q.letter,
                            'kid_id':kid.id,
                            'time':round(t),
                            'lat':x.lat,
                            'lng':x.lng
                            }
                        )

            return render(request,'see_claim.html',
                {'qs':rr}
            )
        else:
            return msg(request,'look4claimGD bad forms')
    else:
        return msg(request,'ищем группу общего развития')

def look4course(request):
    rr = []
    profile = request.user.profile
    if not profile.pref_addr:
        return msg(request,'укажите адрес')

    if not profile.pref_kid:
        return msg(request,'укажите своего ребенка')

    location = Location.objects.get(pk=profile.pref_addr.id)
    kid = Kid.objects.get(pk=profile.pref_kid.id )

    form_age = AgeForm(request.POST)
    form_time = TimeForm(request.POST)
    form_subj = SubjForm(request.POST)

    if form_age.is_valid() and form_time.is_valid() and form_subj.is_valid():
        sbj = form_subj.cleaned_data['subjects']
        t_min = form_time.cleaned_data['time_minutes']
        dif = form_age.cleaned_data['age_dif']

        b_date = kid.birth_date.year
        b_now = datetime.datetime.now().year
        b_age = b_now - b_date

        qs = Course.objects.filter(subject__in=sbj,
                    age__range=(b_age - dif, b_age + dif)).distinct()

        for q in qs:
            qx = Location.objects.filter(course=q.id)
            for x in qx:
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
                        'lng':x.lng
                        }
                    )

        return render(request,'see_course.html',
            {'qs':rr}
        )
    else:
        return msg(request,'надо выбрать хотя бы один предмет')

def look4place(request):
    profile = request.user.profile##Profile.objects.get(user=request.user)
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
    profile = request.user.profile##Profile.objects.get(user=request.user)
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
                    if t <= t_min:
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
