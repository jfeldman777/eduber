from django import forms
from django.contrib.auth.models import User
from .models import Profile, Location, Kid, Place, Course, Subject
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
       choices = kwargs.pop('choices')
       super(PlaceForm, self).__init__(*args, **kwargs)
       self.fields["location"] = forms.ChoiceField(choices=choices,label='адрес')


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code','name','locations','letter','web','level','age',
        ]

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       initial = kwargs.pop('initial')
       course_id = kwargs.pop('course_id')
       super(CourseForm, self).__init__(*args, **kwargs)
       self.fields["locations"] = forms.ModelMultipleChoiceField(
                queryset = Location.objects.filter(user=user),
                widget=forms.CheckboxSelectMultiple,
                label='адреса')
       if initial:
            self.fields['code'].initial = initial['code']
            self.fields['name'].initial = initial['name']
            self.fields['letter'].initial = initial['letter']
            self.fields['web'].initial = initial['web']
            self.fields['level'].initial = initial['level']
            self.fields['age'].initial = initial['age']
            if course_id:
                self.fields['locations'].initial = Location.objects.filter(course=course_id)

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
       initial = kwargs.pop('initial')
       kid_id = kwargs.pop('kid_id')
       super(KidForm, self).__init__(*args, **kwargs)
       self.fields["locations"] = forms.ModelMultipleChoiceField(
                queryset = Location.objects.filter(user=user),
                widget=forms.CheckboxSelectMultiple,
                label='адреса')
       if initial:
            self.fields['username'].initial = initial['username']
            self.fields['first_name'].initial = initial['first_name']
            self.fields['birth_date'].initial = initial['birth_date']
            self.fields['letter'].initial = initial['letter']
            if kid_id:
                self.fields['locations'].initial = Location.objects.filter(kid=kid_id)


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

class ReferenceForm(forms.Form):
    uname_to = forms.CharField(label='username друга',max_length=20)
    email = forms.CharField(label='email друга')
    letter = forms.CharField(label='Мои рекомендации',widget=forms.Textarea)
