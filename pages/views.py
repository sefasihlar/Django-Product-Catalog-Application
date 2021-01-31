from django.shortcuts import render
from django.http import HttpResponse
from Urun.models import Anasayfa
from Urun.models import Kadınlar
from Urun.models import Erkekler



# Create your views here.
def index(request):
    Urunler = Anasayfa.objects.all()
    bilgiler = {
        'Urunler':Urunler
    }
    
   
    
    return render(request,'pages/index.html',bilgiler)

def about(request):
    Urunler = Kadınlar.objects.all()
    bilgiler = {
        'Urunler':Urunler
    }
   
    return render(request,'pages/about.html',bilgiler)
def kadinlar(request):
    Urunler = Erkekler.objects.all()
    bilgiler = {
        'Urunler':Urunler
    }
    
    
    return render(request,'pages/kadinlar.html',bilgiler)


