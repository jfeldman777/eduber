from django import forms
from django.contrib.auth.models import User
from .models import Profile, Location, Kid, Place, Course, Subject
from django.db import models

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
       choices = kwargs.pop('my_choices')
       super(LookForm, self).__init__(*args, **kwargs)
       self.fields["addr"] = forms.ChoiceField(choices=choices,label='адрес')
       self.fields['time_minutes'].initial = 60

class Look2Form(forms.Form):
    time_minutes = forms.IntegerField(label='время в минутах')
    #addr = forms.ChoiceField(label='адрес')
    def __init__(self, *args, **kwargs):
       choices = kwargs.pop('my_choices')
       super(Look2Form, self).__init__(*args, **kwargs)
       self.fields["addr"] = forms.ChoiceField(choices=choices,label='адрес')
       self.fields['time_minutes'].initial = 60

class Look3Form(forms.Form):
    age = forms.IntegerField(label='возраст (лет)')
    age_dif = forms.IntegerField(label='различие в возрасте (предельно допустимое, лет)')
    time_minutes = forms.IntegerField(label='время в минутах')
    #addr = forms.ChoiceField(label='адрес')
    def __init__(self, *args, **kwargs):
       choices = kwargs.pop('my_choices')
       super(Look3Form, self).__init__(*args, **kwargs)
       self.fields["addr"] = forms.ChoiceField(choices=choices,label='адрес')
       self.fields['time_minutes'].initial = 60
       self.fields['age_dif'].initial = 1
       self.fields['age'].initial = 10

class Kid2Form(forms.ModelForm):
    class Meta:
        model = Kid
        fields = ['username','first_name','birth_date','locations','letter']
