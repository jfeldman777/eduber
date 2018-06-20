from django import forms
from django.contrib.auth.models import User
from .models import Profile, Location, Kid, Place, Course, Subject
from django.db import models

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
       self.fields["pref_kid"].label = 'ребенок'
