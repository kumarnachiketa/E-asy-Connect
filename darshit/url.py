from django.contrib import admin
from django.urls import path
from . import views

app_name = 'darshit'

urlpatterns = [
    path('blog', views.blog, name='blog'),
    path('blogdetail', views.blogdetail, name='blogdetail'),
    path('contact', views.contact, name='contact'),
    path('index', views.index, name='index'),
    path('projectdetail', views.projectdetail, name='projectdetail'),
]