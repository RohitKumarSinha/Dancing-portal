from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('index/', views.index, name='index'),
    path('view/', views.view, name='view'),

]
