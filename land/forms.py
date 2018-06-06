from django import forms
from django.contrib.auth.models import User
from .models import Profile, Location, Kid, Place, Course
from django.db import models

class Face31Form(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['face1']

class Face32Form(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['face2']

class Face33Form(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['face3']

class Place2Form(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name','location','letter']

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['code','name','location','letter']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code','name','locations','letter','web','level','age']

class Course2Form(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name','locations','letter','web','level','age']

class Face2Form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['face']

class FaceForm(forms.ModelForm):
    class Meta:
        model = Kid
        fields = ['face']

class KidForm(forms.ModelForm):
    class Meta:
        model = Kid
        fields = ['username','first_name','birth_date','locations','letter']
        widgets = {
            'birth_date':forms.SelectDateWidget(years=range(2000,2020))
        }

class Kid2Form(forms.ModelForm):
    class Meta:
        model = Kid
        fields = ['first_name','birth_date','locations','letter']
        widgets = {
            'birth_date':forms.SelectDateWidget(years=range(2000,2020))
        }

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["name","address","lat","lng"]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["birth_date","phone","web"]
        widgets = {
            'birth_date':forms.SelectDateWidget(years=range(1920,2019))
        }

class EdAddrForm(forms.Form):
    address = forms.CharField(label='адрес', max_length=50)

class ReferenceForm(forms.Form):
    uname_to = forms.CharField(label='username друга',max_length=20)
    email = forms.CharField(label='email друга',max_length=20)
    letter = forms.CharField(label='Мои рекомендации',widget=forms.Textarea)
