from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Homepage route
    path('fetch_video_details/', views.fetch_video_details, name='fetch_video_details'),
    path('download_video/', views.download_video, name='download_video'),
]
