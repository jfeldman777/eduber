from django import forms
from django.contrib.auth.models import User
from .models import Profile, Location, Kid, Place, Course, Subject
from django.db import models

class PropForm(forms.Form):
    CHOICES = [('B','беби-ситтер'),('R','репетитор')]
    choices = forms.ChoiceField(choices=CHOICES)

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       initial = kwargs.pop('initial')
       prop_id = kwargs.pop('prop_id')

       super(PropForm, self).__init__(*args, **kwargs)
       self.fields["locations"] = forms.ModelMultipleChoiceField(
                       queryset = Location.objects.filter(user=user),
                       widget=forms.CheckboxSelectMultiple,
                       label='адреса')

       self.fields['subjects'] = forms.ModelMultipleChoiceField(queryset=
               Subject.objects.all(), widget=forms.CheckboxSelectMultiple,
               label='предметы'
               )

       if initial:
           self.fields['choices'].initial = initial['choices']
           if prop_id:
                self.fields['locations'].initial = Location.objects.filter(claim=prop_id)
                self.fields['subjects'].initial = Subject.objects.filter(claim=prop_id)

class ClaimForm(forms.Form):
    CHOICES = [('B','беби-ситтер'),('R','репетитор'),
                ('T','целевая группа'),('D','группа общего развития')]
    choices = forms.ChoiceField(choices=CHOICES)

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       initial = kwargs.pop('initial')
       claim_id = kwargs.pop('claim_id')

       super(ClaimForm, self).__init__(*args, **kwargs)
       self.fields["kids"] = forms.ModelMultipleChoiceField(
                       queryset = Kid.objects.filter(parent=user),
                       widget=forms.CheckboxSelectMultiple,
                       label='адреса')

       self.fields["locations"] = forms.ModelMultipleChoiceField(
                       queryset = Location.objects.filter(user=user),
                       widget=forms.CheckboxSelectMultiple,
                       label='адреса')

       self.fields['subjects'] = forms.ModelMultipleChoiceField(queryset=
               Subject.objects.all(), widget=forms.CheckboxSelectMultiple,
               label='предметы'
               )

       if initial:
           self.fields['choices'].initial = initial['choices']
           if claim_id:
                self.fields['locations'].initial = Location.objects.filter(claim=claim_id)
                self.fields['kids'].initial = Kid.objects.filter(claim=claim_id)
                self.fields['subjects'].initial = Subject.objects.filter(claim=claim_id)


class UnameForm(forms.Form):
    uname = forms.SlugField()

class GoodForm(forms.Form):
    letter = forms.CharField(label='отзыв',widget=forms.Textarea)

class LookForm(forms.Form):
    time_minutes = forms.IntegerField(label='время в минутах')
    #addr = forms.ChoiceField(label='адрес')
    subjects = forms.ModelMultipleChoiceField(label='предметы',
        queryset=
        Subject.objects.all(), widget=forms.CheckboxSelectMultiple
        )
    def __init__(self, *args, **kwargs):
       choices = kwargs.pop('choices')
       super(LookForm, self).__init__(*args, **kwargs)
       self.fields["addr"] = forms.ChoiceField(choices=choices,label='адрес')
       self.fields['time_minutes'].initial = 60

class Look2Form(forms.Form):
    time_minutes = forms.IntegerField(label='время в минутах')
    #addr = forms.ChoiceField(label='адрес')
    def __init__(self, *args, **kwargs):
       choices = kwargs.pop('choices')
       super(Look2Form, self).__init__(*args, **kwargs)
       self.fields["addr"] = forms.ChoiceField(choices=choices,label='адрес')
       self.fields['time_minutes'].initial = 60

class Look3Form(forms.Form):
    age = forms.IntegerField(label='возраст (лет)')
    age_dif = forms.IntegerField(label='различие в возрасте (предельно допустимое, лет)')
    time_minutes = forms.IntegerField(label='время в минутах')
    #addr = forms.ChoiceField(label='адрес')
    def __init__(self, *args, **kwargs):
       choices = kwargs.pop('choices')
       super(Look3Form, self).__init__(*args, **kwargs)
       self.fields["addr"] = forms.ChoiceField(choices=choices,label='адрес')
       self.fields['time_minutes'].initial = 60
       self.fields['age_dif'].initial = 1
       self.fields['age'].initial = 10
