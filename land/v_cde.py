from django.shortcuts import render
from django.utils.translation import gettext as _
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from .models import Profile, Reference, Location, Kid, Place
from .models import Course, Prop, Event, Claim, Invite, QPage, QLine, QOption

from .forms import UserForm, ProfileForm, ReferenceForm, FaceForm, Face2Form
from .forms import KidForm, Face31Form, Face32Form, Face33Form
from .forms import LocationForm, PlaceForm, CourseForm, InviteForm
from .forms import C2SForm, QPageForm, QPageImgForm, QLineForm, QLineImgForm, QOptionForm
from .forms2 import UnameForm, ClaimForm, PropForm, EventForm
from .views3 import msg, obj
from .views import index, viewref

###########################################################################
def opt_cre(request, qline_id):
    qline = QLine.objects.get(id=qline_id)
    qpage = qline.page
    if request.method == "POST":
        form = QOptionForm(request.POST)
        if form.is_valid():
            opt = form.save(commit=False)
            opt.line = qline
            opt.save()
            return qpage_qline(request,qpage.id)
        else:
            return msg(request,'bad form option')
    else:
        form = QOptionForm()
        return render(request,'cre_ed.html',
            {'form':form,
            'title':_('possible answer'),
            'code':_('add')
            }
        )

def opt_ed(request,opt_id):
    opt = QOption.objects.get(id=opt_id)
    if request.method == "POST":
        form = QOptionForm(request.POST,instance=opt)
        if form.is_valid():
            form.save()
            return qpage_qline(request,opt.line.page.id)
        else:
            return msg(request,'bad form opt')
    else:
        form = QOptionForm(instance=opt)
        return render(request,'cre_ed.html',
            {'form':form,
            'title':_('possible answer'),
            'code':_('change')
            }
        )

def opt_del(request,opt_id):
    opt = QOption.objects.get(id=opt_id)
    qline = opt.line
    qpage_id=qline.page.id
    opt.delete()
    return qpage_qline(request,qpage_id)

def qline_img_ed(request,qline_id):
    qline = QLine.objects.get(id = qline_id)
    qpage_id=qline.page.id

    if request.method == 'POST':
        form = QLineImgForm(request.POST, request.FILES)
        if form.is_valid():
            qline.img = form.cleaned_data['img']
            qline.save()
        return qpage_qline(request,qpage_id)
    else:
        form = QLineImgForm(
            initial={'img':qline.img}
                )
        url = None
        if qline.img:
            url = qline.img.url
        return render(request, 'face.html',
            {'form': form,
            'face':url,
            })

def qline_del(request,qline_id):
    qline = QLine.objects.get(id = qline_id)
    qpage_id=qline.page.id
    qline.delete()
    return qpage_qline(request,qpage_id)

def qline_ed(request,qline_id):
    qline = QLine.objects.get(id=qline_id)
    if request.method == "POST":
        form = QLineForm(request.POST,instance=qline)
        if form.is_valid():
            form.save()
            return qpage_qline(request,qline.page.id)
        else:
            return msg(request,'bad form qline')
    else:
        form = QLineForm(instance=qline)
        return render(request,'cre_ed.html',
            {'form':form,
            'title':_('question'),
            'code':_('change')
            }
        )

def qline_cre(request,qpage_id):
    qpage = QPage.objects.get(id=qpage_id)
    if request.method == "POST":
        form = QLineForm(request.POST)
        if form.is_valid():
            qline = form.save(commit=False)
            qline.page = qpage
            qline.save()
            return qpage_qline(request,qpage_id)
        else:
            return msg(request,'bad form qline')
    else:
        form = QLineForm()
        return render(request,'cre_ed.html',
            {'form':form,
            'title':_('question'),
            'code':_('add')
            }
        )

def qpage_qline(request,qpage_id):
    qpage = QPage.objects.get(id=qpage_id)
    qqline = QLine.objects.filter(page=qpage).order_by('line_number')
    qs = []
    for q in qqline:
        x = None
        if q.type == '3':
            x = QOption.objects.filter(line = q)
        qs.append((q,x))

    return render(request,
    'qpage_qline.html',
    {
    'qs':qs,
    'qpage_id':qpage_id
    }
    )

def qpage_cre(request):
    if request.method == "POST":
        form = QPageForm(request.POST)
        if form.is_valid():
            qpage = form.save(commit=False)
            qpage.user = request.user

            qpage.save()
            return obj(request)
        else:
            return msg(request,'bad form qpage')
    else:
        form = QPageForm()
        return render(request,'cre_ed.html',
            {'form':form,
            'title':_('form'),
            'code':_('add')
            }
        )

def qpage_img_ed(request,qpage_id):
    qpage = QPage.objects.get(id=qpage_id)
    if request.method == 'POST':
        form = QPageImgForm(request.POST, request.FILES)
        if form.is_valid():
            qpage.img = form.cleaned_data['img']
            qpage.save()
        return obj(request)
    else:
        form = QPageImgForm(
            initial={'img':qpage.img}
                )
        url = None
        if qpage.img:
            url = qpage.img.url
        return render(request, 'face.html',
            {'form': form,
            'face':url,
            })

def qpage_ed(request,qpage_id):
    qpage = QPage.objects.get(id=qpage_id)
    if request.method == "POST":
        form = QPageForm(request.POST,instance=qpage)
        if form.is_valid():
            qpage.save()
            return obj(request)
        else:
            print(form.errors.as_data())
            return msg(request,'bad form')
    else:
        form = QPageForm(instance=qpage
        )
        return render(request,'cre_ed.html',
            {'form':form,
            'title':_('edit form'),
            'code':qpage.code
            }
        )

def qpage_del(request,qpage_id):
    qpage = QPage.objects.get(id = qpage_id)
    qpage.delete()
    return obj(request)

def invite_del(request,invite_id):
    invite = Invite.objects.get(id=invite_id)
    invite.delete()
    return obj(request)

def invite_ed(request,invite_id):
    msg = ''
    invite = Invite.objects.get(id=invite_id)
    if request.method == "POST":
        form = InviteForm(request.POST,instance=invite)
        if form.is_valid():
            form.save()
            msg = _('data saved')
        else:
            print(form.errors.as_data())
            return msg(request,'bad form')
    else:
        form = InviteForm(instance=invite)

    return render(request,'invite_ed.html',
        {'form':form,'msg':msg}
        )

def invite_cre(request,event_id):
    if request.method == "POST":
        form = InviteForm(request.POST)
        if form.is_valid():
            invite = form.save(commit=False)
            invite.user = request.user
            invite.event = Event.objects.get(id=event_id)
            invite.save()
            return obj(request)
        else:
            return msg(request,'bad form invite')
    else:
        form = InviteForm()
        return render(request,'cre_ed.html',
            {'form':form,
            'title':_('invitation'),
            'code':_('add')
            }
        )

def cp2s(request,prop_id):
    prop = Prop.objects.get(id=prop_id)
    if request.method == "POST":
        form = C2SForm(request.POST)
        if form.is_valid():
            prop.subjects.set(form.cleaned_data['subject'])
            prop.save()
            return obj(request)
    else:
        form = C2SForm(
        initial={
        'subject':list(prop.subjects.all())
        }
        )
        return render(request,'c2s.html',
            {'form':form,
             'sb':list(prop.subjects.all())
            }
        )

def c2s(request,course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = C2SForm(request.POST)
        if form.is_valid():
            course.subject.set(form.cleaned_data['subject'])
            course.save()
            return obj(request)
    else:
        form = C2SForm(
        initial={
        'subject':list(course.subject.all())
        }
        )
        return render(request,'c2s.html',
            {'form':form,
             'sb':list(course.subject.all())
            }
        )
###############################################################################
def del_addr(request,location_id):
    location = Location.objects.get(id=location_id)
    location.delete()
    return obj(request)

def kid_del(request,kid_id):
    kid = Kid.objects.get(id=kid_id)
    kid.delete()
    return obj(request)

def place_del(request,place_id):
    place = Place.objects.get(id=place_id)
    place.delete()
    return obj(request)

def course_del(request,course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return obj(request)

def event_del(request,event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    return obj(request)

def event_ed(request,event_id):
    event = Event.objects.get(id=event_id)
    if request.method == "POST":
        form = EventForm(request.POST,instance=event,user=request.user)
        if form.is_valid():
            event.save()
            return obj(request)
        else:
            print(form.errors.as_data())
            return msg(request,'bad form')
    else:
        form = EventForm(instance=event
        ,user=request.user
        )
        return render(request,'cre_ed.html',
            {'form':form,
            'title':_('edit event'),
            'code':event.code
            }
        )

#####################################################################
def place_ed(request,place_id):
    place = Place.objects.get(id=place_id)
    if request.method == "POST":
        form = PlaceForm(request.POST,instance=place,user=request.user)
        if form.is_valid():
            place.save()
            return obj(request)
        else:
            print(form.errors.as_data())
            return msg(request,'bad form')
    else:
        form = PlaceForm(instance=place
        ,user=request.user
        )
        return render(request,'cre_ed.html',
            {'form':form,
            'title':_('edit place'),
            'code':place.code
            }
        )
################################################################################
def kid_ed(request,kid_id):
    kid = Kid.objects.get(id=kid_id)
    if request.method == "POST":
        form = KidForm(request.POST,user=request.user,instance=kid)
        if form.is_valid():
            form.save()
            return obj(request)
        else:
            print(form.errors.as_data())
            return msg(request,_('make sure to input address (first create address)'))
    else:
        form = KidForm(instance=kid
            ,user=request.user
        )
        return render(request,'cre_ed.html',
            {'form':form,
            'title':_('student/amateur/kid'),
             'code':_('specify information'),
            }
        )

def kid_cre(request):
    if request.method == "POST":
        form = KidForm(request.POST,
            user=request.user)
        if form.is_valid():
            kid = form.save(commit=False)
            kid.parent = request.user
            kid.save()
            return obj(request)
        else:
            return msg(request,_('you did not input address (first create address)'))
    else:
        form = KidForm(
            user=request.user)
        return render(request,'cre_ed.html',
            {'form':form,
            'title':_('student/kid'),
            'code':_('add')
            }
        )

def event_cre(request):
    if request.method == "POST":
        form = EventForm(request.POST,user=request.user)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return obj(request)
    else:
        form = EventForm(user=request.user)
        return render(request,'form.html',
            {'form':form,
            'title':_('event'),
            'code':_('add')}
        )

def place_cre(request):
    if request.method == "POST":
        form = PlaceForm(request.POST,user=request.user)
        if form.is_valid():
            place = form.save(commit=False)
            place.user = request.user
            place.save()
            return obj(request)
    else:
        form = PlaceForm(user=request.user)
        return render(request,'cre_ed.html',
            {'form':form,
            'title':_('place'),
            'code':_('add')}
        )
#####################################################################
def course_cre(request):
    if request.method == "POST":
        form = CourseForm(request.POST,user=request.user)
        if form.is_valid():
            course = form.save(commit=False)
            course.user = request.user
            course.save()
            return obj(request)
        else:
            print(form.errors.as_data())
            return msg(request,'bad form')
    else:
        form = CourseForm(user=request.user)
        return render(request,'cre_ed.html',
            {'form':form,
            'title':_('course'),
            'code':_('add')}
        )


def course_ed(request,course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = CourseForm(request.POST,instance=course,
            user=request.user)
        if form.is_valid():
            form.save()
            return obj(request)
        else:
            print(form.errors.as_data())
            return msg(request,'bad form')
    else:
        form = CourseForm(
            instance=course,
            user=request.user,
            )
    return render(request,'cre_ed.html',
        {
        'form':form,
        'title':_('course'),
        'code':_('specify information')
        }
    )
#############################

def prop_ed(request,prop_id):
    prop = Prop.objects.get(id=prop_id)
    if request.method == "POST":
        form = PropForm(request.POST, user=request.user, instance=prop)
        if form.is_valid():
            form.save()
            return obj(request)
        else:
            print(form.errors.as_data())
            return msg(request,'bad form')
    else:
        form = PropForm(user=request.user,instance=prop)
        return render(request,
            'prop_cre.html',
            {
            'form':form,
            'title':_('offer (I am offering)'),
            'code':_('specify information')
            })

def claim_ed(request,claim_id):
    claim = Claim.objects.get(id=claim_id)
    if request.method == "POST":
        form = ClaimForm(request.POST, user=request.user,instance=claim)
        if form.is_valid():
            form.save()
            return obj(request)
        else:
            print(form.errors.as_data())
            return msg(request,'bad form')
    else:
        form = ClaimForm(user=request.user,instance=claim)
        return render(request,
            'cre_ed.html',
            {
            'form':form,
            'title':_('request (I am searching)'),
            'code':_('specify information')
            })
def prop_del(request,prop_id):
    prop = Prop.objects.get(id=prop_id)
    prop.delete()
    return obj(request)

def claim_del(request,claim_id):
    claim = Claim.objects.get(id=claim_id)
    claim.delete()
    return obj(request)

def prop_cre(request):
    if request.method == "POST":
        form = PropForm(request.POST, user=request.user)
        if form.is_valid():
            prop = form.save(commit=False)
            prop.user = request.user
            prop.save()
            return obj(request)
        else:
            print(form.errors.as_data())
            return msg(request,'bad form')
    else:
        form = PropForm(user=request.user)
        return render(request,
            'cre_ed.html',
            {
            'form':form,
            'title':_('offer (I am offering)'),
            'code':_('create')
            })

def claim_cre(request):
    if request.method == "POST":
        form = ClaimForm(request.POST, user=request.user)
        if form.is_valid():
            claim = form.save(commit=False)
            claim.user = request.user
            claim.save()
            return obj(request)
        else:
            print(form.errors.as_data())
            return msg(request,'bad form')
    else:
        form = ClaimForm(user=request.user)
        return render(request,
            'cre_ed.html',
            {
            'form':form,
            'title':_('request (I am searching)'),
            'code':_('specify information')
            })
