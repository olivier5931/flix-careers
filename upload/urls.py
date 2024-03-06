from django.urls import path
from upload import views

urlpatterns = [
  path('image', views.upload_image, name='upload_image'),
  path('file', views.upload_file, name='upload_file')
]