from django import forms
from django.contrib.auth.models import User
from .models import Profile, Location, Kid, Place, Course, Subject
from django.db import models

class PropForm(forms.Form):
    letter = forms.CharField(widget=forms.Textarea, label='мой комментарий')
    CHOICES = [('B','беби-ситтер'),('R','репетитор'),
                        ('C','консультант по сети')]
    choices = forms.ChoiceField(choices=CHOICES, label='выбрать вариант')
    hide =forms.BooleanField(label='скрыть',required=False)

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
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

class ClaimForm(forms.Form):
    letter = forms.CharField(widget=forms.Textarea, label='мой комментарий')
    CHOICES = [('B','беби-ситтер'),('R','репетитор'),
                    ('C','консультант по сети'),
                ('T','целевая группа'),('D','группа общего развития')]
    choices = forms.ChoiceField(choices=CHOICES, label='выбрать вариант')
    hide =forms.BooleanField(label='скрыть',required=False)

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
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

class UnameForm(forms.Form):
    uname = forms.SlugField()

class GoodForm(forms.Form):
    letter = forms.CharField(label='отзыв',widget=forms.Textarea)

class LookSForm(forms.Form):
    subjects = forms.ModelMultipleChoiceField(label='предметы',
        queryset=
        Subject.objects.all(), widget=forms.CheckboxSelectMultiple
        )

class LookATSForm(forms.Form):
    time_minutes = forms.IntegerField(label='время в минутах')
    #addr = forms.ChoiceField(label='адрес')
    subjects = forms.ModelMultipleChoiceField(label='предметы',
        queryset=
        Subject.objects.all(), widget=forms.CheckboxSelectMultiple
        )
    def __init__(self, *args, **kwargs):
       choices = kwargs.pop('choices')
       super(LookATSForm, self).__init__(*args, **kwargs)
       self.fields["addr"] = forms.ChoiceField(choices=choices,label='адрес')
       self.fields['time_minutes'].initial = 60

class LookATForm(forms.Form):
    time_minutes = forms.IntegerField(label='время в минутах')
    #addr = forms.ChoiceField(label='адрес')
    def __init__(self, *args, **kwargs):
       choices = kwargs.pop('choices')
       super(LookATForm, self).__init__(*args, **kwargs)
       self.fields["addr"] = forms.ChoiceField(choices=choices,label='адрес')
       self.fields['time_minutes'].initial = 60

class LookATSGForm(forms.Form):
    time_minutes = forms.IntegerField(label='время в минутах')
    subjects = forms.ModelMultipleChoiceField(label='предметы',
        queryset=
        Subject.objects.all(), widget=forms.CheckboxSelectMultiple
        )
    age = forms.IntegerField(label='возраст (лет)')
    age_dif = forms.IntegerField(label='различие в возрасте (предельно допустимое, лет)')
    def __init__(self, *args, **kwargs):
       choices = kwargs.pop('choices')
       super(LookATSGForm, self).__init__(*args, **kwargs)
       self.fields["addr"] = forms.ChoiceField(choices=choices,label='адрес')
       self.fields['time_minutes'].initial = 60
       self.fields['age_dif'].initial = 1
       self.fields['age'].initial = 10

class LookATGForm(forms.Form):
    age = forms.IntegerField(label='возраст (лет)')
    age_dif = forms.IntegerField(label='различие в возрасте (предельно допустимое, лет)')
    time_minutes = forms.IntegerField(label='время в минутах')
    #addr = forms.ChoiceField(label='адрес')
    def __init__(self, *args, **kwargs):
       choices = kwargs.pop('choices')
       super(LookATGForm, self).__init__(*args, **kwargs)
       self.fields["addr"] = forms.ChoiceField(choices=choices,label='адрес')
       self.fields['time_minutes'].initial = 60
       self.fields['age_dif'].initial = 1
       self.fields['age'].initial = 10
