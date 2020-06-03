from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('',views.index,name="home"),
    path('about/',views.about,name="about"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout")
]