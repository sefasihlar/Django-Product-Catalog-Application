from django.shortcuts import render,redirect
# Create your views here.
from django.contrib.auth.models import User
from django.contrib import auth
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            print('kullanıcı adı yada parola yanlış')
            return redirect('login')

    else: 

        return render(request,'user/login.html')
def regester(request):
   
    if request.method == 'POST':
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        if password == repassword:
            if User.objects.filter(username = username).exists():
                print('bu kullanıcı adı daha önce alınmış')
                return redirect('regester')
            else:
                if User.objects.filter(email = email).exists():
                    print('bu email adı daha önce alınmış')
                    return redirect('regester')
                else:
                    user =  User.objects.create_user(username=username,password=password,email=email)
                    user.save()
                    return redirect('login')
                    print('kullanıcı oluşturuldu')

        else:
            print('parolalar esleşmıyor')
            return redirect('regester')
       
        

        
    else:
        return render(request,'user/regester.html' )

def cıkıs(request):
    return render(request,'user/cıkıs.html')
