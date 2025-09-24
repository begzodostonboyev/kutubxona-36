from re import search

from django.db.models.deletion import get_candidate_relations_to_delete
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.utils.http import escape_leading_slashes

from .models import *
from django.urls import path

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def talabalar_view(request):
    if request.method == 'POST':
#   data = request.POST
#   ism = data.get('ism')
#   guruh = data.get('guruh')
#   kurs = data.get('kurs')
#   kitob_soni = data.get('kitob_soni')
#   Talaba.objects.create(
#       ism=ism,
#       guruh=guruh,
#       kurs=kurs,
#       kitob_soni=kitob_soni,
#   )
        Talaba.objects.create(
            ism=request.POST.get('ism'),
            guruh=request.POST.get('guruh'),
            kurs=request.POST.get('kurs'),
            kitobi_soni=request.POST.get('kitobi_soni') if request.POST.get('kitobi_soni') else 0
        )

        return redirect('/talabalar/')

    talabalar = Talaba.objects.all()
    search = request.GET.get('search')
    if search:
        talabalar = talabalar.filter(ism__contains=search)



    context= {
        'talabalar': talabalar,
        'search': search,

    }
    return render(request, 'talabalar.html', context)

def student_deteils_view(request, pk):
    talaba = Talaba.objects.get(id=pk)
    context= {
        'talaba': talaba
    }
    return render(request, 'talaba_deteils.html', context)

def talaba_delete_view(request, pk):
    talaba = get_object_or_404(Talaba, pk=pk)
    talaba.delete()
    return redirect('/talabalar/')

def talaba_update_view(request, pk):
    talaba =get_object_or_404(Talaba, id=pk)
    if request.method == "POST":
        talaba.ism = request.POST.get('ism')
        talaba.guruh = request.POST.get('guruh')
        talaba.kurs = request.POST.get('kurs')
        talaba.kitobi_soni = request.POST.get('kitob_soni')
        talaba.save()
        return redirect('talabalar')
    context={
        'talaba': talaba
    }
    return render(request, 'talaba_update.html', context)
def mualliflar_view(request):
    mualliflar = Muallif.objects.all()
    context = {
        'mualliflar' : mualliflar
    }
    return render(request, 'mualliflar.html', context)



def tanlangan_muallif_view(request, muallif_id):
    muallif = Muallif.objects.get(id=muallif_id)
    context={
        'muallif': muallif
    }
    return render(request,'tanlangan_mualliflar.html', context)

def muallif_delete_view(request, muallif_id):
    muallif = get_object_or_404(Muallif, id=muallif_id)
    return redirect('/mualliflar/')

def kitoblar_view(request ):
    if request.method == 'POST':
        Kitob.objects.crete(
            nom=request.POST.get('nom'),
            janr=request.POST.get('janr'),
            sahifa=request.POST.get('sahifa'),
            muallif=get_object_or_404(Muallif, id=request.POST.get('muallif_id'))
        )
        return redirect("/kitoblar/")

    kitoblar = Kitob.objects.all()
    search= request.GET.get('search')
    if search:
        kitoblar = kitoblar.filter(
            Q(nom__contains=search)|
            Q(muallif__ism__contains=search)
        )
    context = {
        'kitoblar': kitoblar,
        'search': search
    }
    return render(request, 'kitoblar.html', context)

def kitob_deteils_view(request, kitob_id):
    kitob = Kitob.objects.get(id=kitob_id)
    context = {
            'kitob': kitob
    }
    return render(request, 'kitob_deteils.html', context)

def kitob_delete_confirm_view(request,kitob_id):
    kitob = get_object_or_404(Kitob, id=kitob_id)
    context={
        'kitob': kitob
    }
    return render(request, 'kitob_delete_confirm.html', context)

def kitob_delete_view(request, kitob_id):
    kitob = get_object_or_404(Kitob, id = kitob_id)
    kitob.delete()
    return redirect('/kitoblar/')

