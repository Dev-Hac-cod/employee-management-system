from turtle import home
from django import views
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('',views.home , name="home"),
    path('signup', views.signup , name="signup"),
    path('signin', views.signin, name="signin"),
]
