from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'organisation'

urlpatterns = [
    path('', views.index, name='index'),
    path('notinorg/', views.notinorg, name='notinorg'),
    path('join/', views.join, name='join'),
    path('leave/', views.leave, name='leave'),
    path('delete/', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    path('remove/<int:user_id>/', views.remove, name='remove'),
    path('generate/', views.generate, name='generate'),
    path('invite/<str:code>/', views.join_with_url, name='join_with_url'),
]
