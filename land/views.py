from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.models import User
from .models import Profile, Reference
from .forms import UserForm, ProfileForm, ReferenceForm

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
    return render(request,'viewref.html',{})

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
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user_id=request.user.id)
    if request.method == "POST":
        uform = UserForm(data = request.POST)
        pform = ProfileForm(data = request.POST)
        if uform.is_valid() and pform.is_valid():
            profile.birth_date = pform.cleaned_data['birth_date']
            profile.phone = pform.cleaned_data['phone']

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
            'phone':profile.phone
            })
        return render(request,'profile.html',
            {'uform': uform,
             'pform': pform,
            })

def xin(request):
    return render(request,'in.html')

def about(request):
    return render(request,'about.html')

def demo1(request):
    return render(request,'demo/demo1.html')

def demo2(request):
    return render(request,'demo/demo2.html')

def demo3(request):
    return render(request,'demo/demo3.html')
