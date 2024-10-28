from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('allposts/', views.allposts, name='allposts'),
    path('contact/', views.contact, name='contact'),
    path('getstarted/', views.getstarted, name='getstarted'),
    path('login/', views.login, name='login'),
    path('newblog/', views.newblog, name='newblog'),
    path('about/', views.about, name='about'),
    path('lifestyle/', views.lifestyle, name='lifestyle'),
    path('tech/', views.tech, name='tech'),
    path('travel/', views.travel, name='travel'),
]
