
from django.shortcuts import render
from siparis.models import siparis
# Create your views here.
 
def siparis(request):
    if request.method == 'POST':
        print("siparsişiniz alındı")
        ürünadi= request.POST['ürünadi']
        adet= request.POST['adet']
        fiyat= request.POST['fiyat']
        adres= request.POST['adres']
        from siparis.models import siparis
       
        
        
        x = ürünadi
        y = adet
        z = fiyat
        f = adres
        print(x,y,z,f)
        Urun = siparis(urunadi= x,adet = y,fiyat= z, adres= f)
        Urun.save()

       
        return render(request,'siparis/siparis.html')
        
        
      
    return render(request,'siparis/siparis.html')
   