from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.utils.text import slugify

from django.contrib.auth.models import User
from .models import Profile, Reference, Location, Kid
from .forms import UserForm, ProfileForm, ReferenceForm
from .forms import KidForm, Kid2Form, LocationForm, EdAddrForm

def msg(request,msg):
    return render(request, 'msg.html', {'msg': msg})

def viewcab(request,uname):
    user = User.objects.get(username = uname)
    profile = Profile.objects.get(user = user)
    uform = UserForm(initial={
    'first_name':user.first_name,
    'last_name':user.last_name,
    'email':user.email})
    pform = ProfileForm(
        initial={
        'birth_date':profile.birth_date,
        'phone':profile.phone
        })
    return render(request,'viewcab.html',
        {'uform': uform,
         'pform': pform,
        })

def viewref(request,uname):
    user = User.objects.get(username = uname)
    qs = Reference.objects.filter(person_to = user)
    return render(request,'viewref.html',{
        'qs':qs
    })

def grant(request,role,uname):
    user = User.objects.get(username = uname)
    profile = Profile.objects.get(user = user)
    if role == 1:
        profile.has_parent = True
    elif role == 2:
        profile.has_producer = True
    elif role == 3:
        profile.has_teacher = True

    profile.save()
    return index(request)

def ask(request,role):
    profile = Profile.objects.get(user = request.user)
    if role == 1:
        profile.ask_parent = True
    elif role == 2:
        profile.ask_producer = True
    elif role == 3:
        profile.ask_teacher = True

    profile.save()
    return index(request)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def index(request):
    profile = None
    user = request.user
    xuser = User.objects.get(username = 'jacobfeldman')
    comment = 'none'
    comment_all = 'none'
    try:
        profile = Profile.objects.get(user = user)
        comment = profile.adm_comment
        comment_all = Profile.objects.get(user = xuser).adm_comment
    except:
        pass
    return render(request,'index.html',
        {'adm':comment,
         'adm_all':comment_all,
         'profile':profile
        }
        )

def q(request):
    qs1 = Profile.objects.filter(ask_parent=True, has_parent=False)
    qs2 = Profile.objects.filter(ask_producer=True, has_producer=False)
    qs3 = Profile.objects.filter(ask_teacher=True, has_teacher=False)

    return render(request,'q.html',
        {'qs1':qs1,
        'qs2':qs2,
        'qs3':qs3,
        }
    )

def ed_kid(request,name):
    kid = Kid.objects.get(parent=request.user,username=name)
    if request.method == "POST":
        form = KidForm(request.POST)
        if form.is_valid():

            kid.first_name = form.cleaned_data['first_name']
            kid.birth_date = form.cleaned_data['birth_date']
            kid.locations = form.cleaned_data['locations']
            kid.letter = form.cleaned_data['letter']
            kid.save()
            return obj(request)
    else:
        form = Kid2Form(
        initial={
        'first_name':kid.first_name,
        'birth_date':kid.birth_date,
        'locations':kid.locations,
        'letter':kid.letter
        }
        )
        return render(request,'kid2.html',
            {'form':form,
             'username':kid.username,
            }
        )

def del_kid(request,name):
    kid = Kid.objects.get(parent=request.user,username=name)
    kid.delete()
    return obj(request)

def face(request,name):
    return obj(request)

def kid(request):
    if request.method == "POST":
        form = KidForm(request.POST)
        if form.is_valid():
            kid = Kid()
            kid.parent = request.user
            kid.username = slugify(form.cleaned_data['username'])
            n = Kid.objects.filter(parent=request.user,username=kid.username).count()
            if n > 0:
                return msg(request,'username занят, сохранить не удалось')
            kid.first_name = form.cleaned_data['first_name']
            kid.birth_date = form.cleaned_data['birth_date']
            kid.locations = form.cleaned_data['locations']
            kid.letter = form.cleaned_data['letter']
            kid.save()
            return obj(request)
    else:
        form = KidForm()
        return render(request,'kid.html',
            {'form':form}
        )

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

def ed_addr(request,name):
    location = Location.objects.get(user=request.user,name=name)
    if request.method == 'POST':
        form = EdAddrForm(data = request.POST)
        if form.is_valid():
            location.address = form.cleaned_data['address']
            location.save()
        return obj(request)
    else:
        form = EdAddrForm(initial={'address':location.address})
        return render(request,'ed_addr.html',
            {'form':form}
        )

def del_addr(request,name):
    location = Location.objects.get(user=request.user,name=name)
    location.delete()
    return obj(request)

def map2(request,name):
    location = Location.objects.get(user=request.user,name=name)
    if request.method == 'POST':
        form = LocationForm(data = request.POST)
        if form.is_valid():
            location.lat = form.cleaned_data['lat']
            location.lng = form.cleaned_data['lng']
            location.save()
        return obj(request)
    else:
        return render(request,'map2.html',
            {
                'lat':location.lat,
                'lng':location.lng,
                'slug':name
            }
        )

def map(request):
    if request.method == 'POST':
        form = LocationForm(data = request.POST)
        if form.is_valid():
            location = Location()
            location.user = request.user
            location.name = slugify(form.cleaned_data['name'])
            location.address = form.cleaned_data['address']
            location.lat = form.cleaned_data['lat']
            location.lng = form.cleaned_data['lng']

            n = Location.objects.filter(user=request.user,name=location.name).count()
            if n>0:
                return msg(request,'Имя занято, сохранить невозможно')

            location.save()
        return obj(request)
    else:
        return render(request,'map.html')

def obj(request):
    profile = Profile.objects.get(user=request.user)
    q_adr = Location.objects.filter(user=request.user)
    q_kid = Kid.objects.filter(parent=request.user)
    return render(request,'obj.html',
    {
    'profile':profile,
    'q_adr':q_adr,
    'q_kid':q_kid
    })

def xin(request):
    return render(request,'in.html')

def about(request):
    return render(request,'about.html')

def demo1(request):
    return render(request,'demo1.html')

def demo2(request):
    return render(request,'demo2.html')

def demo3(request):
    return render(request,'demo3.html')
