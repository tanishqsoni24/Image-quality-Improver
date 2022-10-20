from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from PIL import Image
import glob



def index(request):
    return render(request , 'index.html')

def results(request):
    if request.method == 'POST' and request.FILES['image']:
        upload = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        input_ = {'uploaded':upload}
        
        # Import the Images module from pillow
        
        # Open the image by specifying the image path.
        for filename in glob.glob(file_url):
            image_path = filename
            image_file = Image.open(image_path)
            edited_file = image_file.save(image_file.name, image_file)
            edited_file_url = image_file.url(edited_file)
            
            # the default
            image_file.save("image_name.jpg", quality=95)
            print(file_url,edited_file_url)
        return render(request, 'result.html', {'uploaded_file_url': file_url,#'edited_file_url':edited_file_url
        })

    return render(request, 'result.html')
