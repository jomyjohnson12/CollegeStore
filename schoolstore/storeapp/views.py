from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import redirect

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def home(request):
    return render(request,'home.html')

def registration(request):
    if request.method=='POST':
        option=request.POST.get('purpose')
        if option == 'order':
            messages.info(request,'Order Recieved,   We will contact you soon')
        elif option == 'Enquiry':
            messages.info(request,'Enquiry Recieved,   We will contact you soon')
        else:
            messages.info(request,'Return Request Recieved,   We will contact you soon')
    return render(request,'registration.html')


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,"login.html")
    
def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
        
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
     





