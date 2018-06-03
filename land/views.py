from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.models import User
from .models import Profile
from .forms import UserForm, ProfileForm


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def index(request):
    return render(request,'index.html')

def profile(request):
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user_id=request.user.id)
    if request.method == "POST":
        uform = UserForm(data = request.POST)
        pform = ProfileForm(data = request.POST)
        if uform.is_valid() and pform.is_valid():
            profile.birth_date = pform.cleaned_data['birth_date']
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
            initial={'birth_date':profile.birth_date})
        return render(request,'profile.html',
            {'uform': uform,
             'pform': pform,
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
