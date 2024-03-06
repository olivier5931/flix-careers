from django.shortcuts import render

from upload.forms import UploadFileForm, UploadForm

def upload_image(request):
  if request.method == 'POST':
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid:
      form.save()
      saved_object = form.instance
      return render(request, 'upload/add_image.html',{'form':form, 'saved_object':saved_object})
  else:
    form = UploadForm()
  return render(request, 'upload/add_image.html',{'form':form})

def upload_file(request):
  if request.method == 'POST':
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      saved_object = form.instance
      return render(request, 'upload/add_file.html',{'form':form, 'saved_object':saved_object})
  else:
    form = UploadFileForm()
  return render(request, 'upload/add_file.html',{'form':form})
