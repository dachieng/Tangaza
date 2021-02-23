from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from products.models import Upload

# Create your views here.

def index(request):
    products = Upload.objects.all()
    return render(request,'index.html', {'products':products})

def register(request):
    if request.method == "POST":
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.info(request, "Sorry Username already exists")
                return redirect('register')
            
            elif User.objects.filter(email = email).exists():
                messages.info(request, "Sorry Email alreaddy in use")
                return redirect('register') 
            else:
                user = User.objects.create_user(first_name = firstname, last_name = lastname, email = email, 
                username = username, password = password)
                user.save()
                return redirect('login')

        else:
            messages.info(request, "passwords dont match")
            return redirect('register')
        
        return redirect('/')
    else:
        return render(request, "register.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "user does not exist")
            return redirect('login')

    
    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def detail(request, album_id):
    upload = Upload.objects.get(pk = album_id)
    user = User.objects.get(pk=upload.user_id)
    return render(request, "details.html", {"upload":upload, "user":user})
