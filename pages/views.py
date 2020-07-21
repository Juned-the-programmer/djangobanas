from django.shortcuts import render, HttpResponse, redirect
from banasadmin.models import *
from django.contrib import messages
from django.contrib.auth.models import auth,User,Group
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request, 'pages/index.html')

@login_required(login_url='login')
def about(request):
    return render(request, 'pages/about.html')


def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['pwd']
        password1 = request.POST['pwd1']
        phoneno = request.POST['phoneno']
        route = request.POST['route']

        if password==password1:
            user = User.objects.create_user(username=username,password=password)
            user.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)

            AddBill = Bill(
                name=username,
                cooler=0,
                rate=0,
                amount=0,
                pending_amount=0,
                subtotal=0
            )
            AddCustomer = Customer( 
                name=username,
                phone_no=phoneno,
                route=route,
                pwd = password,
                pwd1 = password1
            )
            AddBill.save()
            AddCustomer.save()
            return redirect('login')

    return render(request,'pages/signup.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        pwd = request.POST['password']

        user = auth.authenticate(username=username,password=pwd)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Enter Correct Username or Password')
            return redirect('login')

    return render(request,'pages/login.html')
        # if User.is_authenticated:

        # user = auth.authenticate(name=name,pwd=pwd)
        # if user is not None:
        #     auth.login(request,user)
        #     return redirect('/')
        # username = Customer.objects.get(name=name)
        # password = Customer.objects.get(pwd=pwd)
        
        # if name == username & pwd == password:
        #     messages.success(request, 'you are successfully logged')
        #     return redirect('/')
        # else:
        #     messages.error(request, 'Enter correct usernameor password')
        #     return redirect('login')

def logout(request):
    auth.logout(request)
    # return HttpResponse('LOGEDOUT SUCCESSFULLY')
    # return redirect('/')
    return render(request,'pages/index.html')
