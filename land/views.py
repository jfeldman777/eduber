from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')

def map(request):
    return render(request,'map.html')

def gps(request):
    return render(request,'gps.html')
