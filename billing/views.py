from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from banasadmin.models import Customer,Payment,DailyEntry,Bill
from pages.views import *
from django.core.paginator import InvalidPage, Paginator
from pages import decoraters
from banasadmin.models import DailyEntry
import datetime
from datetime import time
from django.contrib import messages

@login_required(login_url='login')
def bill(request):
    return render(request,'billing/bill.html')

@login_required(login_url='login')
def dailyentry(request):
    today = datetime.datetime.now()
    first = today.replace(day=1)
    lastmonth = first - datetime.timedelta(days=31)
    lstmonth = lastmonth.strftime("%Y-%m-%d")
    print(lstmonth)
    if User.is_authenticated:
        user = request.user.username 
        print(user)
    
    dailydata = DailyEntry.objects.filter(date_added__gte=lstmonth).filter(name=user).order_by('-id')

    paginator = Paginator(dailydata, 10 , orphans=0)

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
    if request.method == 'POST':
        name = request.POST['name']
        cooler = request.POST['cooler']

        dailyEntry = DailyEntry(
            name=name,
            cooler=cooler
        )
        h = datetime.datetime.now()
        hour = h.time()
        d = hour.hour
        print(hour)

        if d in range(6,18):
            dailyEntry.save()
        else:
            messages.error(request, 'Now you cannnot do entry on this')
    return render(request,'billing/dailyentry.html',context)

@login_required(login_url='login')
def paidbill(request):
    if User.is_authenticated:
        user = request.user.username 
        print(user)

    billdata = Payment.objects.filter(name=user).order_by('-id')

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
    # payment = request.user.customer.payment_set.all()
    # context={ 'payment': payment }
    return render(request,'billing/paidbill.html',context)

@login_required(login_url='login')
def pendingbill(request):
    if User.is_authenticated:
        user = request.user.username 
        print(user)

    billdata = Bill.objects.filter(name=user,task="pending").order_by('-id')

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
    return render(request,'billing/pendingbill.html',context)