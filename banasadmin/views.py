from django.shortcuts import render, redirect
from .models import Bill,Customer,DailyEntry,Payment
from django.contrib import messages
from django.core.paginator import InvalidPage, Paginator
from django.contrib.auth.decorators import login_required
from pages.decoraters import *
from django.contrib.auth.models import User,Group
from django.db.models import Q
from django.db.models import Sum,Min,Max,Avg
# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def billadmin(request):
    billdata = Bill.objects.all().order_by('-id')

    query = request.GET.get('q')
    if query:
        billdata = Bill.objects.filter(
            Q(id__icontains=query) | Q(name__icontains=query) | Q(cooler__icontains=query) | Q(task__icontains=query))

    paginator = Paginator(billdata , 5, orphans=0)

    is_paginated = True if paginator.num_pages > 1 else False
    page = request.GET.get('page') or 1
    try:
        current_page = paginator.page(page)
        # except:
    except InvalidPage as e:
        messages.error(request, str(e))
        current_page = paginator.page(1)

        # context = {
        #     'pending_tasks': pending_tasks,
        # }
    data = Bill.objects.aggregate(Sum('subtotal'))
    pending = Bill.objects.aggregate(Sum('pending_amount'))
    print(data['subtotal__sum'])
    c = data['subtotal__sum']
    b = pending['pending_amount__sum']
    # c = result['subtotal__sum']
    # print(c)
    context = {
        'current_page': current_page,
        'is_paginated': is_paginated,
        'paginator': paginator,
        'c' : c ,
        'b' : b
        # 'myfilter' : myfilter
    }
    return render(request, 'banasadmin/billadmin.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def dailyentryadmin(request):
    if request.method == 'POST':
        name = request.POST['name']
        cooler = request.POST['cooler']

        dailyEntry = DailyEntry(
            name=name,
            cooler=cooler
        )
        dailyEntry.save()

    data = Customer.objects.all()
    print(data)
    context = {
        'data':data
    }
    return render(request, 'banasadmin/dailyentryadmin.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def addcustomer(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_no = request.POST['phoneno']
        route = request.POST['route']
        password = request.POST['pwd']
        password1 = request.POST['pwd1']

        if Customer.objects.filter(name=name).exists():
            messages.error(request, 'name already exists')
            return redirect('billadmin')
        else:
            AddBill = Bill(
                name=name,
                cooler=0,
                rate=0,
                amount=0,
                pending_amount=0,
                subtotal=0
            )
            AddCustomer = Customer( 
                name=name,
                phone_no=phone_no,
                route=route,
                pwd = password,
                pwd1 = password1
            )
            # response = sendPostRequest(URL, 'BTAYN8KJCTSCCDIYW0CVXIUCC0F8XLSQ', '4K7G9XIOQIPNSTBF', 'stage', phone_no , 'banas water', 'THANKS FOR REGISTRATION IN THIS WEBSITE BANAS WATER' )
            user = User.objects.create_user(username=name,password=password)
            user.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            AddBill.save()
            AddCustomer.save()
            return redirect('billadmin')
    return render(request, 'banasadmin/addcustomer.html')


def get_bill_object(id):
    try:
        return Bill.objects.get(pk=id)
    except Bill.DoesNotExist:
        return False

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def paybill(request,pk):
    if request.method == 'POST':
        name = request.POST['name']
        print(name)
        amount = request.POST['amount']
        a=int(amount)
        print(type(a))
        print(a)
        paidamount = request.POST['paidamount']  
        b=int(paidamount)
        print(type(b))
        print(b)
        
        c=a-b
        print(type(c))
        print(c)

        customer = Customer.objects.filter(name = name).get()
        phone = customer.phone_no
        print(phone)

        BILL = Bill.objects.get(pk=pk)
        # BILL.name = name
        # BILL.amount = amount
        # # BILL.subtotal = subtotal
        # # BILL.rate=0
        # # BILL.pending_amount
        # # BILL.cooler = 0
        # print(BILL.pending_amount)
        # print(BILL.subtotal)
        # print(paidamount)
        BILL.pending_amount = c
        BILL.amount=0
        BILL.subtotal=c
        if BILL.pending_amount <= 50:
            BILL.pending_amount=0
            BILL.task="paid"
        paidbill = Payment(
            name = name,
            amount = amount,
            pay = paidamount,
            pending = BILL.pending_amount
        )
        # response = sendPostRequest(URL, 'U8YZP19ED1QO5X23W0WQAS7TLW31KRMM', 'YHOFLS7O140FA1CL', 'prod', phone , 'banas water', 'DEAR '+name+' YOUR TOTAL AMOUNT OF BILL IS '+amount+' FROM THAT YOU HAVE PAID '+paidamount+' YOUR TOTAL PENDING AMOUNT IS THANKS FROM WITH ME..' )
        # account_sid = 'AC456e86e5e5b54f793c12db6ee162de70'
        # auth_token = '6654606e64429cddd07aa2b0d8525d84'
        # client = Client(account_sid, auth_token)
        # message = client.messages \
        #         .create(
        #              body='DEAR '+name+' YOUR TOTAL AMOUNT OF BILL IS '+amount+' FROM THAT YOU HAVE PAID '+paidamount+' YOUR TOTAL PENDING AMOUNT IS THANKS FROM WITH ME..',
        #              from_='+12057367667',
        #              to='+91'+phone
        #          )
        paidbill.save()
        BILL.save()
        messages.success(request,'Paid successsfully')
        return redirect('billadmin')

    editdata = Bill.objects.get(pk=pk)
    context = {
        'editdata':editdata
    }

    return render(request, 'banasadmin/paybill.html',context)
    
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def addbill(request,pk):
    if User.is_authenticated:
        user = request.user.username 
        print(user)
    if request.method == 'POST':
        name = request.POST['name']
        cooler = request.POST['cooler']
        rate = request.POST['rate']
        amount = request.POST['amount']
        pending_amount = request.POST['pending']
        subtotal = request.POST['subtotal']
        task = "pending"

        createbill = Bill.objects.get(pk=pk)

        createbill.name = name
        createbill.cooler=cooler
        createbill.rate=rate   
        createbill.amount=amount
        createbill.pending_amount=pending_amount
        createbill.subtotal=subtotal
        createbill.task=task        

        # createbill = Bill(
        #     name = name,
        #     cooler = cooler,
        #     rate = rate,
        #     amount = amount,
        #     pending_amount = pending_amount,
        #     subtotal = subtotal,
        #     task = task
        # )
        
        
        if Customer.objects.filter(name = name).exists():
            #pendingamount = Bill.objects.get(pending_amount)
            createbill.amount = int(createbill.cooler) * int(createbill.rate)
            createbill.subtotal = int(createbill.amount) + int(createbill.pending_amount)
            print(createbill.subtotal)
            createbill.save()
            return redirect('billadmin')
        else:
            return redirect('billadmin')
            messages.error(request,'Customer Doesnot Exists')

    getbilldata = Bill.objects.get(pk=pk)
    context = {
        'getbilldata':getbilldata
    }
    return render(request, 'banasadmin/addbill.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def paidbilladmin(request):
    billdata = Payment.objects.all().order_by('-id')

    paginator = Paginator(billdata, 5, orphans=0)

    is_paginated = True if paginator.num_pages > 1 else False
    page = request.GET.get('page') or 1
    try:
        current_page = paginator.page(page)
        # except:
    except InvalidPage as e:
        messages.error(request, str(e))
        current_page = paginator.page(1)

        # context = {
        #     'pending_tasks': pending_tasks,
        # }
    context = {
        'current_page': current_page,
        'is_paginated': is_paginated,
        'paginator': paginator
    }
    return render(request,'banasadmin/paidbilladmin.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def pendingadmin(request):
    billdata = Bill.objects.filter(task="pending").order_by('-id')

    paginator = Paginator(billdata, 5, orphans=0)

    is_paginated = True if paginator.num_pages > 1 else False
    page = request.GET.get('page') or 1
    try:
        current_page = paginator.page(page)
        # except:
    except InvalidPage as e:
        messages.error(request, str(e))
        current_page = paginator.page(1)

        # context = {
        #     'pending_tasks': pending_tasks,
        # }
    context = {
        'current_page': current_page,
        'is_paginated': is_paginated,
        'paginator': paginator
    }
    return render(request,'banasadmin/pendingadmin.html',context)