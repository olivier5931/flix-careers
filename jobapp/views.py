from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse

from jobapp.models import JobPost

# job_title = [
#   "First Job",
#   "Second Job",
#   "Third Job"
# ]
# job_description = [
#   "First Job Description",
#   "Second Job Description",
#   "Third Job Description"
# ]

# class TempClass:
#   x = 5

# def hello(request):
#   list = ["alpha", "beta"]
#   temp = TempClass()
#   is_authenticated = False
#   context={"name":"Django", "age":10, "first_list":list, "temp_object":temp, "is_authenticated":is_authenticated}
#   return render(request, "jobapp/hello.html", context)

def job_list(request):
  # list_of_jobs = "<ul>"
  # for j in job_title:
  #   job_id = job_title.index(j)
  #   detail_url = reverse('jobs_detail', args=(job_id,)) #don't forget comma at the end of args
  #   list_of_jobs += f"<li><a href='{detail_url}'>{j}</a></li>"
  # list_of_jobs += "</ul>"
  # return HttpResponse(list_of_jobs)
  jobs = JobPost.objects.all()
  context={"jobs":jobs}
  return render(request, "jobapp/index.html", context)

def job_detail(request, id):
  print(type(id))
  try:
    if id == 0:
      return redirect(reverse('jobs_home'))
    job = JobPost.objects.get(id=id)
    context={"job":job}
    return render(request, "jobapp/job_detail.html", context)
  except:
    return HttpResponseNotFound("No Job Found")