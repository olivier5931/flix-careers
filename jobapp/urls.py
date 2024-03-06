from django.urls import path
from jobapp import views

from jobapp.views import job_detail, job_list

urlpatterns = [
  path('', views.job_list, name='jobs_home'),
  path('job/<int:id>', views.job_detail, name='jobs_detail'),
]