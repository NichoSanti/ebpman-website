from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact-page', views.contact, name='contact-page'),
]