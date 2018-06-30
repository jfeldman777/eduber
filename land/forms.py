from django import forms
from django.contrib.auth.models import User
from .models import Profile, Location, Kid, Place, Course, Subject, Reference
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

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['code','name','location','letter','web']

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(PlaceForm, self).__init__(*args, **kwargs)
       self.fields["location"].queryset = Location.objects.filter(user=user)
       self.fields["location"].label = 'адрес'


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code','name','locations','letter','web','level','age',
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields["locations"].queryset = Location.objects.filter(user=user)
        self.fields["locations"].label='адреса'
        self.fields["age"].label='предполагаемый возраст учеников (лет, одно число, в среднем)'


class C2SForm(forms.Form):
    subject = forms.ModelMultipleChoiceField(queryset=
        Subject.objects.all(), widget=forms.CheckboxSelectMultiple
        )

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
    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(KidForm, self).__init__(*args, **kwargs)
       self.fields["locations"] = forms.ModelMultipleChoiceField(
                queryset = Location.objects.filter(user=user),
                widget=forms.CheckboxSelectMultiple,
                label='адреса')


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["name","address","lat","lng"]
        widgets = {'lat': forms.HiddenInput(),
                   'lng': forms.HiddenInput(),
        }

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

class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = ['letter']
        widgets = {'letter':forms.Textarea}
        labels = {'letter':'я думаю что:'}
