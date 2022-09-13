from django.urls import path
from . import views


urlpatterns = [

    path('login',views.login,name = 'login'),
    path('regester',views.regester,name = 'regester'),
    path('cıkıs',views.cıkıs,name = 'cıkıs'),
   
    
    

    
]