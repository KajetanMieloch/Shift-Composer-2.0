from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'organisation'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('join/', views.join, name='join'),
]
