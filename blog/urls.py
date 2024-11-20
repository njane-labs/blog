from django.urls import path, include
from . import views
from .views import CustomLoginView, CustomLogoutView, register_view

urlpatterns = [

    path('', views.blog, name='blog'),
    path('allposts/', views.allposts, name='allposts'),
    path('contact/', views.contact, name='contact'),
    path('getstarted/', register_view, name='getstarted'),
    # path('login/', views.login, name='login'),
    path('newblog/', views.newblog, name='newblog'),
    path('about/', views.about, name='about'),
    path('lifestyle/', views.lifestyle, name='lifestyle'),
    path('tech/', views.tech, name='tech'),
    path('travel/', views.travel, name='travel'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('allposts/', views.allposts, name='allposts'),
    path('create/', views.createview, name='create'),
    path('<int:pk>/', views.detailview, name='detail'),
    path('<int:pk>/edit/', views.UpdateView.as_view(),name='update'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    path('tinymce/', include('tinymce.urls')),
    path('register/', views.admin_register_user, name='admin_register_user'),
    path('users/', views.user_list, name='user_list'),
    path('users/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    

]