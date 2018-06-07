from django import forms
from django.contrib.auth.models import User
from .models import Profile, Location, Kid, Place, Course, Subject
from django.db import models

class LookForm(forms.Form):
    subjects = forms.ModelMultipleChoiceField(queryset=
        Subject.objects.all(), widget=forms.CheckboxSelectMultiple
        )
