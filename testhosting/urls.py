# your_project_name/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world),
    # Add other app URLs here if you have them, e.g.:
    # path('', include('myapp.urls')),
]

# IMPORTANT: THIS IS FOR DEVELOPMENT ONLY! DO NOT USE IN PRODUCTION!
if settings.DEBUG:
    # This line tells the development server to serve static files
    # from your apps' 'static/' folders and STATICFILES_DIRS.
    urlpatterns += static(settings.STATIC_URL)

    # If you also have user-uploaded media files and a MEDIA_URL defined,
    # you would add a similar line for media:
    # from django.conf.urls.static import static as media_static # alias to avoid conflict
    # urlpatterns += media_static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)