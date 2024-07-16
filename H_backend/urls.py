from django.urls import path
from . import views

app_name = 'H_backend'

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('search/', views.search_images, name='search_images'),
    path('analytics/', views.analytics, name='analytics'),
]
