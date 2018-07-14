from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from .models import Profile, Reference, Location, Kid, Place, Course, Prop
from .forms import UserForm, ProfileForm, ReferenceForm, FaceForm, Face2Form
from .forms import KidForm, Face31Form, Face32Form, Face33Form
from .forms import LocationForm, PlaceForm, CourseForm
from .forms import C2SForm
from .forms2 import UnameForm
from .views3 import obj
from .views3 import msg

def viewcab(request,uname):
    user = User.objects.get(username = uname)
    profile = Profile.objects.get(user = user)
    uform = UserForm(initial={
    'first_name':user.first_name,
    'last_name':user.last_name,
    'email':user.email})
    pform = ProfileForm(
        initial={
        'birth_date':profile.birth_date,
        'phone':profile.phone
        })

    url = None
    if profile.face:
        url = profile.face.url

    return render(request,'viewcab.html',
        {'uform': uform,
         'pform': pform,
         'face':url,
         'uname':uname
        })

def viewref(request,uname):
    user = User.objects.get(username = uname)
    qs = Reference.objects.filter(person_to = user).order_by('-written')
    return render(request,'viewref.html',{
        'qs':qs,
        'uname':uname
    })

def grant(request,role,uname):
    user = User.objects.get(username = uname)
    profile = user.profile ##Profile.objects.get(user = user)
    if role == 1:
        profile.has_parent = True
    elif role == 2:
        profile.has_producer = True
    elif role == 3:
        profile.has_teacher = True
    elif role == 4:
        profile.has_justme = True
        kid = Kid(
            parent = request.user,
            username = 'me',
            first_name = request.user.first_name,
            birth_date = request.user.profile.birth_date,
            face = request.user.profile.face
                    )
        kid.save()
    profile.save()
    return index(request)

def ask(request,role):
    profile = Profile.objects.get(user = request.user)
    if role == 1:
        profile.ask_parent = True
    elif role == 2:
        profile.ask_producer = True
    elif role == 3:
        profile.ask_teacher = True
    elif role == 4:
        profile.ask_justme = True

    profile.save()
    return index(request)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def index(request):
    profile = None
    comment_all = None
    iamwatched = None

    xuser = User.objects.get(username = 'jacobfeldman')
    comment = 'none'
    comment_all = 'none'

    if request.user.is_authenticated:
        profile = request.user.profile
        comment_all = xuser.profile.adm_comment
        iamwatched = Profile.objects.filter(friends__in = [request.user.id]).exclude(user__in = profile.friends.all())

    return render(request,'index.html',
        {
         'adm_all':comment_all,
         'profile':profile,
         'iamwatched':iamwatched
        }
        )

def q(request):
    qs1 = Profile.objects.filter(ask_parent=True, has_parent=False)
    qs2 = Profile.objects.filter(ask_producer=True, has_producer=False)
    qs3 = Profile.objects.filter(ask_teacher=True, has_teacher=False)
    qs4 = Profile.objects.filter(ask_justme=True, has_justme=False)

    return render(request,'q.html',
        {'qs1':qs1,
        'qs2':qs2,
        'qs3':qs3,
        'qs4':qs4
        }
    )

##########################################################
def face31(request,place_id):
    place = Place.objects.get(id=place_id)
    if request.method == 'POST':
        form = Face31Form(request.POST, request.FILES)
        if form.is_valid():
            place.face1 = form.cleaned_data['face1']
            place.save()
        return obj(request)
    else:
        form = Face31Form(
            initial={'face1':place.face1}
                )
        url = None
        if place.face1:
            url = place.face1.url
        return render(request, 'face3.html',
            {'form': form,
            'face':url,
            })

def face32(request,place_id):
    place = Place.objects.get(id=place_id)
    if request.method == 'POST':
        form = Face32Form(request.POST, request.FILES)
        if form.is_valid():
            place.face2 = form.cleaned_data['face2']
            place.save()
        return obj(request)

    else:
        form = Face32Form(
            initial={'face2':place.face2}
                )
        url = None
        if place.face2:
            url = place.face2.url
        return render(request, 'face3.html',
            {'form': form,
            'face':url,
            })

def face33(request,place_id):
    place = Place.objects.get(id=place_id)
    if request.method == 'POST':
        form = Face32Form(request.POST, request.FILES)
        if form.is_valid():
            place.face3 = form.cleaned_data['face3']
            place.save()
        return obj(request)

    else:
        form = Face33Form(
            initial={'face3':place.face3}
                )
        url = None
        if place.face3:
            url = place.face3.url
        return render(request, 'face3.html',
            {'form': form,
            'face':url,
            })

def face2(request):
    profile = request.user.profile##Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = Face2Form(request.POST, request.FILES)
        if form.is_valid():
            profile.face = form.cleaned_data['face']
            profile.save()
        return index(request)

    else:
        form = Face2Form(
            initial={'face':profile.face}
                )
        url = None
        if profile.face:
            url = profile.face.url
        return render(request, 'face2.html',
            {'form': form,
            'face':url,
            })

def face(request,kid_id):
    kid = Kid.objects.get(id=kid_id)
    if request.method == 'POST':
        form = FaceForm(request.POST, request.FILES)
        if form.is_valid():
            kid.face = form.cleaned_data['face']
            kid.save()
        return obj(request)

    else:
        form = FaceForm(
            initial={'face':kid.face}
                )
        url = None
        if kid.face:
            url = kid.face.url
        return render(request, 'face.html',
            {'form': form,
            'face':url,
            })
###########################################################################
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


def map20(request,location_id):
    location = Location.objects.get(id=location_id)
    return render(request,'map112.html',
        {
            'lat':str(location.lat).replace( ',' , '.'),
            'lng':str(location.lng).replace(',' , '.')
        }
    )

############################################################
def xin(request):
    return render(request,'in.html')

def about(request):
    return render(request,'about.html')

def demo1(request):
    return render(request,'demo1.html')

def demo2(request):
    return render(request,'demo2.html')

def demo3(request):
    return render(request,'demo3.html')
