from django.db import models

class siparis(models.Model):
    
    urunadi= models.CharField(max_length=50)
    adet=  models.CharField(max_length=50)
    fiyat= models.TextField(max_length=50)
    adres=models.TextField(max_length=50)
  
