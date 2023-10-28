from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('organisation/', include('organisation.urls')),
    path('profile/', include('userProfile.urls')),
    path('employees/', include('employees.urls')),
    path('generator/', include('generator.urls')),
]
