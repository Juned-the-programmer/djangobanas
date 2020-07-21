from django.urls import path
from . import views

urlpatterns = [
    path('bill/',views.bill,name="bill"),
    path('dailyentry/',views.dailyentry,name="dailyentry"),
    path('paidbill/',views.paidbill,name="paidbill"),
    path('pendingbill/',views.pendingbill,name="pendingbill")
]
