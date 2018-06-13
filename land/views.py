from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from .models import Profile, Reference, Location, Kid, Place, Course
from .forms import UserForm, ProfileForm, ReferenceForm, FaceForm, Face2Form
from .forms import KidForm, Face31Form, Face32Form, Face33Form
from .forms import LocationForm, PlaceForm, CourseForm
from .forms import C2SForm
from .forms2 import UnameForm
from .views2 import choices
from .views1 import obj

def msg(request,msg):
    return render(request, 'msg.html', {'msg': msg})

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
        })

def viewref(request,uname):
    user = User.objects.get(username = uname)
    qs = Reference.objects.filter(person_to = user)
    return render(request,'viewref.html',{
        'qs':qs
    })

def grant(request,role,uname):
    user = User.objects.get(username = uname)
    profile = Profile.objects.get(user = user)
    if role == 1:
        profile.has_parent = True
    elif role == 2:
        profile.has_producer = True
    elif role == 3:
        profile.has_teacher = True

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

    profile.save()
    return index(request)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def index(request):
    profile = None
    user = request.user
    xuser = User.objects.get(username = 'jacobfeldman')
    comment = 'none'
    comment_all = 'none'
    try:
        profile = Profile.objects.get(user = user)
        comment = profile.adm_comment
        comment_all = Profile.objects.get(user = xuser).adm_comment
    except:
        pass
    return render(request,'index.html',
        {'adm':comment,
         'adm_all':comment_all,
         'profile':profile
        }
        )

def q(request):
    qs1 = Profile.objects.filter(ask_parent=True, has_parent=False)
    qs2 = Profile.objects.filter(ask_producer=True, has_producer=False)
    qs3 = Profile.objects.filter(ask_teacher=True, has_teacher=False)

    return render(request,'q.html',
        {'qs1':qs1,
        'qs2':qs2,
        'qs3':qs3,
        }
    )

##########################################################
def del_kid(request,kid_id):
    kid = Kid.objects.get(id=kid_id)
    kid.delete()
    return obj(request)

def del_place(request,place_id):
    place = Place.objects.get(id=place_id)
    place.delete()
    return obj(request)

def del_course(request,course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return obj(request)
#####################################################################
def ed_place(request,place_id):
    addr_list = choices(request.user)
    place = Place.objects.get(id=place_id)
    if request.method == "POST":
        form = PlaceForm(request.POST,choices=addr_list)
        if form.is_valid():
            place.code = form.cleaned_data['code']
            place.name = form.cleaned_data['name']
            place.location = form.cleaned_data['location']
            place.letter = form.cleaned_data['letter']
            place.web = form.cleaned_data['web']
            place.save()
            return obj(request)
    else:
        form = PlaceForm(
        initial={
        'code':place.code,
        'name':place.name,
        'location':place.location,
        'letter':place.letter,
        'web':place.web
        },choices=addr_list
        )
        return render(request,'place2.html',
            {'form':form}
        )



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
    profile = Profile.objects.get(user=request.user)
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
def ed_kid(request,kid_id):
    kid = Kid.objects.get(id=kid_id)
    if request.method == "POST":
        form = KidForm(request.POST,user=request.user,kid_id=kid_id,initial=None)
        if form.is_valid():
            kid.username = form.cleaned_data['username']
            kid.first_name = form.cleaned_data['first_name']
            kid.birth_date = form.cleaned_data['birth_date']
            kid.letter = form.cleaned_data['letter']
            kid.locations.set(form.cleaned_data['locations'])
            kid.save()
            return obj(request)
        else:
            print(form.errors.as_data())
            return msg(request,'bad form')
    else:
        form = KidForm(
        initial={
        'username':kid.username,
        'first_name':kid.first_name,
        'birth_date':kid.birth_date,
        'locations':kid.locations,
        'letter':kid.letter
        },user=request.user,kid_id=kid_id
        )
        return render(request,'kid2.html',
            {'form':form,
             'username':kid.username,
            }
        )

def kid(request):
    if request.method == "POST":
        form = KidForm(request.POST,
            user=request.user,initial=None,kid_id=None)
        if form.is_valid():
            kid = Kid()
            kid.parent = request.user
            kid.username = form.cleaned_data['username']
            kid.first_name = form.cleaned_data['first_name']
            kid.birth_date = form.cleaned_data['birth_date']
            kid.letter = form.cleaned_data['letter']
            kid.save()
            kid.locations.set(form.cleaned_data['locations'])
            kid.save()
            return obj(request)
        else:
            print(form.errors.as_data())
            return msg(request,'bad form')
    else:
        form = KidForm(
            user=request.user,initial=None,kid_id=None)
        return render(request,'kid.html',
            {'form':form}
        )

def place(request):
    addr_list = choices(request.user)
    if request.method == "POST":
        form = PlaceForm(request.POST,choices=addr_list)
        if form.is_valid():
            place = Place()
            place.user = request.user
            place.code = form.cleaned_data['code']
            place.name = form.cleaned_data['name']
            place.location = form.cleaned_data['location']
            place.letter = form.cleaned_data['letter']
            place.web = form.cleaned_data['web']
            place.save()
            return obj(request)
    else:
        form = PlaceForm(choices=addr_list)
        return render(request,'place.html',
            {'form':form}
        )
#####################################################################
def course(request):
    if request.method == "POST":
        form = CourseForm(request.POST,user=request.user,initial=None,course_id=None)
        if form.is_valid():
            course = Course()
            course.user = request.user
            course.code = form.cleaned_data['code']
            course.name = form.cleaned_data['name']

            course.letter = form.cleaned_data['letter']
            course.web = form.cleaned_data['web']
            course.level = form.cleaned_data['level']
            course.age = form.cleaned_data['age']
            course.save()
            course.locations.set(form.cleaned_data['locations'])
            course.save()
            return obj(request)
        else:
            print(form.errors.as_data())
            return msg(request,'bad form')
    else:
        form = CourseForm(user=request.user,initial=None,course_id=None)
        return render(request,'course.html',
            {'form':form}
        )
def ed_course(request,course_id):
    course = Course.objects.get(id=course_id)
    print(course)
    if request.method == "POST":
        form = CourseForm(request.POST,
            user=request.user,initial=None,course_id=None)
        if form.is_valid():
            course.code = form.cleaned_data['code']
            course.name = form.cleaned_data['name']
            course.letter = form.cleaned_data['letter']
            course.web = form.cleaned_data['web']
            course.level = form.cleaned_data['level']
            course.age = form.cleaned_data['age']
            course.locations.set(form.cleaned_data['locations'])
            course.save()
            return obj(request)
        else:
            print(form.errors.as_data())
            return msg(request,'bad form')
    else:
        form = CourseForm(
            course_id=course_id,
            user=request.user,
            initial={
                'code':course.code,
                'name':course.name,
                'locations':course.locations,
                'letter':course.letter,
                'web':course.web,
                'level':course.level,
                'age':course.age
                }
            )
    return render(request,'course2.html',
        {
        'form':form,
        'code':course.code
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
             'code':course.code,
             'sb':list(course.subject.all())
            }
        )
###############################################################################
def del_addr(request,location_id):
    location = Location.objects.get(id=location_id)
    location.delete()
    return obj(request)

def map2(request,location_id):
    location = Location.objects.get(id=location_id)
    if request.method == 'POST':
        form = LocationForm(data = request.POST)
        if form.is_valid():
            location.name = form.cleaned_data['name']
            location.address = form.cleaned_data['address']
            location.lat = form.cleaned_data['lat']
            location.lng = form.cleaned_data['lng']
            location.save()
            return obj(request)
        else:
            return msg(request,'bad form map2')
    else:
        return render(request,'map.html',
            {
                'name':location.name,
                'address':location.address,
                'lat':location.lat,
                'lng':location.lng,
            }
        )

def map(request):
    if request.method == 'POST':
        form = LocationForm(data = request.POST)
        if form.is_valid():
            location = Location()
            location.user = request.user
            location.name = form.cleaned_data['name']
            location.address = form.cleaned_data['address']
            location.lat = form.cleaned_data['lat']
            location.lng = form.cleaned_data['lng']
            location.save()
        return obj(request)
    else:
        return render(request,'map.html',
            {
                'lat':59.93863,
                'lng':30.31413,
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
