# your_project_name/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.conf.urls.static import static as django_static 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world),
    # Add other app URLs here if you have them, e.g.:
    # path('', include('myapp.urls')),
]

# IMPORTANT: THIS IS FOR DEVELOPMENT ONLY! DO NOT USE IN PRODUCTION!
urlpatterns += django_static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += django_static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)