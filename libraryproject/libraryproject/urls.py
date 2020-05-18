from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from libraryapp.models import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('libraryapp.urls')),
]
