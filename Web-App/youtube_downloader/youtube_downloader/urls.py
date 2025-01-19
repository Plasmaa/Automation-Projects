# your_project/urls.py
from django.contrib import admin
from django.urls import path, include  # Include to add app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('download.urls')),  # This will include download app URLs
]
