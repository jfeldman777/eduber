from django import forms
from django.contrib.auth.models import User
from .models import Profile, Location, Kid, Place, Course, Subject, Reply
from django.db import models

class AdmForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['adm_comment']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['chat','letter']
        widgets = {'chat': forms.HiddenInput()}

class PrefForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['pref_kid','pref_addr']

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(PrefForm, self).__init__(*args, **kwargs)
       self.fields["pref_addr"].queryset = Location.objects.filter(user=user)
       self.fields["pref_addr"].label = 'адрес'
       self.fields["pref_kid"].queryset = Kid.objects.filter(parent=user)
       self.fields["pref_kid"].label = 'ученик/ребенок'

class TimeForm(forms.Form):
    time_minutes = forms.IntegerField(label='время в минутах')
    def __init__(self, *args, **kwargs):
       super(TimeForm, self).__init__(*args, **kwargs)
       self.fields['time_minutes'].initial = 60

class AgeForm(forms.Form):
    age_dif = forms.IntegerField(label='различие в возрасте (предельно допустимое, лет)')
    def __init__(self, *args, **kwargs):
       super(AgeForm, self).__init__(*args, **kwargs)
       self.fields['age_dif'].initial = 1

class Age1Form(forms.Form):
    age = forms.IntegerField(label='возраст (лет)')
    def __init__(self, *args, **kwargs):
       super(Age1Form, self).__init__(*args, **kwargs)
       self.fields['age'].initial = 10

class SubjForm(forms.Form):
    subjects = forms.ModelMultipleChoiceField(label='предметы',
        queryset=Subject.objects.all(), widget=forms.CheckboxSelectMultiple
        )
