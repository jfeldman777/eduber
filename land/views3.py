from django.shortcuts import render
from .models import Location, Profile, Kid, Place, Claim, Prop, Course
from .forms2 import LookSForm

def xy2t(x1,y1,x2,y2):
  dx = x1 - x2
  dy = y1 - y2
  d2 = dx*dx + dy*dy
  d = sqrt(d2)
  me = 0.04075509311105271
  t = d*40/me
  return t

def choices(user):
    qs = Location.objects.filter(user=user)
    qq = [(x.id,x.name+"("+ x.address +")") for x in qs]
    return qq

def obj(request):#показать все объекты
    profile = Profile.objects.get(user=request.user)
    q_adr = Location.objects.filter(user=request.user)
    q_kid = Kid.objects.filter(parent=request.user)
    q_place = Place.objects.filter(user=request.user)
    q_crs = Course.objects.filter(user=request.user)
    q_claim = Claim.objects.filter(user=request.user)
    q_prop = Prop.objects.filter(user=request.user)
    return render(request,'obj.html',
    {
    'profile':profile,
    'q_adr':q_adr,
    'q_kid':q_kid,
    'q_place':q_place,
    'q_crs':q_crs,
    'q_claim':q_claim,
    'q_prop':q_prop
    })


def msg(request,msg):
    return render(request, 'msg.html', {'msg': msg})

def chat2me(request):
    return render(request,'chat2me.html')

def kid2chat(request,kid_id):
    return msg(request,'мне интересен ваш ребенок (заготовка)')

def place2chat(request,place_id):
    return msg(request,'мне интересна ваша площадка (заготовка')

def course2chat(request,course_id):
    return msg(request,'мне интересен ваш курс (заготовка')

def menu(request):
    return render(request,'menu.html')

def search(request):
    return render(request,'search.html')

def map112(request,lat,lng):
    return render(request,'map112.html',
        {
        'lat':lat,
        'lng':lng
        }
    )

def map11(request):
    return render(request,'map11.html')

def look4propBS(request):
    return render(request,'look.html')
    #return obj(request)

def look4propRP(request):
    return obj(request)

def look4propNW(request):
    return obj(request)

def look4claimBS(request):
    return obj(request)

def look4claimRP(request):
    return obj(request)

def look4claimNW(request):
    form = LookSForm()
    return render(request,'look4claim.html',
    {'form':form }
    )

def look4claimGT(request):
    return obj(request)

def look4claimGD(request):
    return obj(request)
