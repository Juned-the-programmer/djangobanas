from django.urls import path
from banasadmin import views

urlpatterns = [
    path('', views.billadmin, name="billadmin"),
    path('addbill/<pk>', views.addbill, name="addbill"),
    path('addcustomer/', views.addcustomer, name="addcustomer"),
    path('paybill/<pk>', views.paybill, name="paybill"),
    path('paidbilladmin/', views.paidbilladmin, name="paidbilladmin"),
    path('pendingadmin/', views.pendingadmin, name="pendingadmin"),
    path('dailyentryadmin/', views.dailyentryadmin, name="dailyentryadmin")
]
