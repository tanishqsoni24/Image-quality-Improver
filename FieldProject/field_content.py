from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import cv2

def main(request):
    return render(request, 'main.html')

def index(request):
    # return HttpResponse("Index hai bhai")
    return render(request , 'index.html')
    
def results(request):
    if request.method == 'POST' and request.FILES['image']:
        upload = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(request, 'result.html', {'uploaded_file_url': file_url})
    return render(request, 'result.html')