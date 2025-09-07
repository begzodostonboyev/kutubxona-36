from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.urls import path

# Create your views here.

def home_view(request):
    return render(request, 'home.html')


def mualliflar_view(request):
    mualliflar = Muallif.objects.all()
    context={
        'mualliflar': mualliflar,
    }
    return render(request, 'mualliflar.html',context)

def tanlangan_muallif_view(request, muallif_id):
    t_muallif = Muallif.objects.get(id=muallif_id)
    context = {
        't_muallif': t_muallif,
    }
    return render(request,'muallif_malumoti.html',context)

def kitoblar_view(request):
    kitoblar = Kitob.objects.all()
    context = {
        'kitoblar': kitoblar,
    }
    return render(request,'3topshiriq.html',context)

