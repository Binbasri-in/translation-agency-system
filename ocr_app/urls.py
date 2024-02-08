from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
      path('', views.upload_file, name='upload_file'),  # URL for the file upload view
    # You can add more URLs for other views here
]
