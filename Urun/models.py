from django.db import models
class Anasayfa(models.Model):
    Baslik = models.CharField(max_length=50)
    image =  models.CharField(max_length=50)
    text = models.TextField(max_length=50)
    ozellik =models.TextField(max_length=50)
    fiyat =models.CharField(max_length=15)

    Baslik2= models.CharField(max_length=50)
    image2=  models.CharField(max_length=50)
    text2 = models.TextField(max_length=50)
    ozellik2 =models.TextField(max_length=50)
    fiyat2 =models.CharField(max_length=15)

    Baslik3 = models.CharField(max_length=50)
    image3=  models.CharField(max_length=50)
    text3 = models.TextField(max_length=50)
    ozellik3 =models.TextField(max_length=50)
    fiyat3 =models.CharField(max_length=15)

    Baslik4 = models.CharField(max_length=50)
    image4 =  models.CharField(max_length=50)
    text4 = models.TextField(max_length=50)
    ozellik4 =models.TextField(max_length=50)
    fiyat4 =models.CharField(max_length=15)

    Baslik5 = models.CharField(max_length=50)
    image5 =  models.CharField(max_length=50)
    text5 = models.TextField(max_length=50)
    ozellik5 =models.TextField(max_length=50)
    fiyat5 =models.CharField(max_length=15)

    Baslik6= models.CharField(max_length=50)
    image6 =  models.CharField(max_length=50)
    text6 = models.TextField(max_length=50)
    ozellik6 =models.TextField(max_length=50)
    fiyat6 =models.CharField(max_length=15)
    
    
    def get_image_path(self):
        return '/img/' + self.image

    def get_image2_path(self):
        return '/img/' + self.image2
    def get_image3_path(self):
        return '/img/' + self.image3
    def get_image4_path(self):
        return '/img/' + self.image4
    def get_image5_path(self):
        return '/img/' + self.image5
    def get_image6_path(self):
        return '/img/' + self.image6

    
    def get_image_path(self):
        return '/img/' + self.image


class Kadınlar(models.Model):
    Baslik = models.CharField(max_length=50)
    image =  models.CharField(max_length=50)
    text = models.TextField(max_length=50)
    ozellik =models.TextField(max_length=50)
    fiyat =models.CharField(max_length=15)

    Baslik2= models.CharField(max_length=50)
    image2=  models.CharField(max_length=50)
    text2 = models.TextField(max_length=50)
    ozellik2 =models.TextField(max_length=50)
    fiyat2 =models.CharField(max_length=15)

    Baslik3 = models.CharField(max_length=50)
    image3=  models.CharField(max_length=50)
    text3 = models.TextField(max_length=50)
    ozellik3=models.TextField(max_length=50)
    fiyat3 =models.CharField(max_length=15)

    Baslik4 = models.CharField(max_length=50)
    image4 =  models.CharField(max_length=50)
    text4 = models.TextField(max_length=50)
    ozellik4 =models.TextField(max_length=50)
    fiyat4 =models.CharField(max_length=15)

    Baslik5 = models.CharField(max_length=50)
    image5 =  models.CharField(max_length=50)
    text5 = models.TextField(max_length=50)
    ozellik5 =models.TextField(max_length=50)
    fiyat5 =models.CharField(max_length=15)

    Baslik6= models.CharField(max_length=50)
    image6 =  models.CharField(max_length=50)
    text6 = models.TextField(max_length=50)
    ozellik6 =models.TextField(max_length=50)
    fiyat6 =models.CharField(max_length=15)
    
    
    def get_image_path(self):
        return '/img/' + self.image

    def get_image2_path(self):
        return '/img/' + self.image2
    def get_image3_path(self):
        return '/img/' + self.image3
    def get_image4_path(self):
        return '/img/' + self.image4
    def get_image5_path(self):
        return '/img/' + self.image5
    def get_image6_path(self):
        return '/img/' + self.image6

    
class Erkekler(models.Model):

    Baslik = models.CharField(max_length=50, verbose_name = 'Resim Başlığı')
    image =  models.CharField(max_length=50, verbose_name ='Resim adi')
    text = models.TextField(max_length=50, verbose_name = 'Açıklama')
    ozellik =models.TextField(max_length=50, verbose_name = 'özellik')
    fiyat =models.CharField(max_length=50, verbose_name ='Fiyat')

    Baslik2= models.CharField(max_length=50, verbose_name ='Resim Başlığı')
    image2=  models.CharField(max_length=50, verbose_name ='Resim adi')
    text2 = models.TextField(max_length=50, verbose_name ='Açıklama')
    ozellik2 =models.TextField(max_length=50, verbose_name ='özellik')
    fiyat2 =models.CharField(max_length=50, verbose_name ='Fiyat')

    Baslik3 = models.CharField(max_length=50, verbose_name ='Resim Başlığı')
    image3=  models.CharField(max_length=50, verbose_name ='Resim adi')
    text3 = models.TextField(max_length=50, verbose_name ='Açıklama')
    ozellik3 =models.TextField(max_length=50, verbose_name ='özellik')
    fiyat3 =models.CharField(max_length=50, verbose_name ='Fiyat')

    Baslik4 = models.CharField(max_length=50, verbose_name ='Resim Başlığı')
    image4 =  models.CharField(max_length=50, verbose_name ='Resim adi')
    text4 = models.TextField(max_length=50, verbose_name ='Açıklama')
    ozellik4 =models.TextField(max_length=50, verbose_name ='özellik')
    fiyat4 =models.CharField(max_length=50, verbose_name ='Fiyat')

    Baslik5 = models.CharField(max_length=50, verbose_name ='Resim Başlığı')
    image5 =  models.CharField(max_length=50, verbose_name ='Resim adi')
    text5 = models.TextField(max_length=50, verbose_name ='Açıklama')
    ozellik5 =models.TextField(max_length=50, verbose_name ='özellik')
    fiyat5 =models.CharField(max_length=50, verbose_name ='Fiyat')

    Baslik6= models.CharField(max_length=50, verbose_name ='Resim Başlığı')
    image6 =  models.CharField(max_length=50, verbose_name ='Resim adi')
    text6 = models.TextField(max_length=50, verbose_name ='Açıklama')
    ozellik6 =models.TextField(max_length=50, verbose_name ='özellik')
    fiyat6 =models.CharField(max_length=50, verbose_name ='Fiyat')
    
    
    def get_image_path(self):
        return '/img/' + self.image

    def get_image2_path(self):
        return '/img/' + self.image2
    def get_image3_path(self):
        return '/img/' + self.image3
    def get_image4_path(self):
        return '/img/' + self.image4
    def get_image5_path(self):
        return '/img/' + self.image5
    def get_image6_path(self):
        return '/img/' + self.image6




   
