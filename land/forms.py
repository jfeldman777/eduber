from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from .models import Profile, Location, Kid, Place, Course
from .models import Subject, Reference, Invite, QPage, QLine, QOption
from django.db import models

class QOptionForm(forms.ModelForm):
    class Meta:
        model = QOption
        exclude = ['line']

class QLineImgForm(forms.ModelForm):
    class Meta:
        model = QLine
        fields = ['img']

class QLineForm(forms.ModelForm):
    class Meta:
        model = QLine
        fields = ['hide','letter','code','type','line_number']

class QPageForm(forms.ModelForm):
    class Meta:
        model = QPage
        fields = ['hide','code', 'name', 'letter']

class QPageImgForm(forms.ModelForm):
    class Meta:
        model = QPage
        fields = ['img']


class InviteForm(forms.ModelForm):
    class Meta:
        model = Invite
        fields = ['status']

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
       self.fields["location"].label = _('address')


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code','name','locations','letter','web','level','age',
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields["locations"].queryset = Location.objects.filter(user=user)
        self.fields["locations"].label=_('addresses')
        self.fields["age"].label=_('approximate students age (years, one number, approximately)')

class Date2Form(forms.Form):
    date1 = forms.DateField(label=_('start (yyyy-mm-dd)'))
    date2 = forms.DateField(label=_('end (yyyy-mm-dd)'))

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
        fields = ['username','first_name','birth_date','locations','letter','interest']
        widgets = {
            'birth_date':forms.SelectDateWidget(years=range(1930,2020))
        }
        labels = {'first_name':_('name'),
                'birth_date':_('date of birth'),
                'letter':_('some words about'),
                'interest':_('interests with commas')
        }

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(KidForm, self).__init__(*args, **kwargs)
       self.fields["locations"] = forms.ModelMultipleChoiceField(
                queryset = Location.objects.filter(user=user),
                widget=forms.CheckboxSelectMultiple,
                label=_('addresses'))


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

class MyletterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['letter']
        labels = {'letter':_('what I think')}

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
        labels = {'letter':_('I think that:')}
