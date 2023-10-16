from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('',views.index, name='index'),
    path('delete/<int:employee_id>/', views.delete, name='delete'),
    path('details/<int:employee_id>/', views.details, name='details'),
]
