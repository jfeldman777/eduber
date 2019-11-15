from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from .models import Profile, Location, Kid, Place, Course, Subject, Prop, Claim, Event, QPage
from django.db import models

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['user']

        labels = {'code':_('code'),
                'name':_('name'),
                'letter':_('some words about'),
                'date_from':_('starting time/date (dd.mm.yyyy hh:mm)'),
                'date_to':_('ending time/date (dd.mm.yyyy hh:mm)')
        }

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(EventForm, self).__init__(*args, **kwargs)

       self.fields['location'].queryset = Location.objects.filter(user=user)
       self.fields['page1'].queryset = QPage.objects.filter(user=user,hide=False)

class PropForm(forms.ModelForm):
    class Meta:
        model = Prop
        fields = ['hide','choices','location','letter']

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(PropForm, self).__init__(*args, **kwargs)

       self.fields['location'].queryset = Location.objects.filter(user=user)

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['hide','choices','kid','location','letter','subjects']

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(ClaimForm, self).__init__(*args, **kwargs)

       self.fields['kid'].queryset = Kid.objects.filter(parent=user)
       self.fields['location'].queryset = Location.objects.filter(user=user)
       self.fields['subjects'].queryset = Subject.objects.all()

class UnameForm(forms.Form):
    uname = forms.SlugField(required=False)

class FLnameForm(forms.Form):
    first_name = forms.CharField(required=False,label=_('first name'))
    last_name = forms.CharField(required=False,label=_('last name'))

class GoodForm(forms.Form):
    letter = forms.CharField(label='отзыв',widget=forms.Textarea)

class LookSForm(forms.Form):
    subjects = forms.ModelMultipleChoiceField(label=_('subjects'),
        queryset=
        Subject.objects.all(), widget=forms.CheckboxSelectMultiple
        )
